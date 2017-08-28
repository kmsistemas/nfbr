from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _


class TbusuarioManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, usuario_contabil, usuario_suporte_sistema, password, **extra_fields):
        """
        Creates and saves a User with the given email, usuario_contabil, usuario_suporte_sistema and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not usuario_contabil:
            raise ValueError(_('Users must have an usuario_contabil'))
        if not usuario_suporte_sistema:
            raise ValueError(_('Users must have an usuario_suporte_sistema'))
        email = self.normalize_email(email)
        user = self.model(email=email, usuario_contabil=usuario_contabil, usuario_suporte_sistema=usuario_suporte_sistema, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, usuario_contabil, usuario_suporte_sistema, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, usuario_contabil, usuario_suporte_sistema and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, usuario_contabil, usuario_suporte_sistema, password, **extra_fields)

    def create_superuser(self, email, usuario_contabil, usuario_suporte_sistema, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, usuario_contabil, usuario_suporte_sistema and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self._create_user(email, usuario_contabil, usuario_suporte_sistema, password, **extra_fields)

        # user = self.create_user(
        #     email,
        #     first_name=first_name,
        #     password=password,
        # )
        # user.is_staff = True
        # user.is_admin = True
        # user.save(using=self._db)
        # return user


class TbcontribuinteManager(models.Manager):
    def all(self, user):
        if user.is_superuser:
            return super().all()
        return super().get_queryset().filter(tbusuariocontribuinte__id_usuario=user)


class ModelPerUserManager(models.Manager):
    def all(self, user):
        filtro = Q(id_contribuinte=user.id_contribuinte)
        if not user.is_superuser:
            filtro &= Q(id_contribuinte__tbusuariocontribuinte__id_usuario=user)

        return super().get_queryset().filter(filtro)

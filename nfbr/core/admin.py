from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext, ugettext_lazy as _
from nfbr.core.forms import UserCreationForm, UserChangeForm
from nfbr.core.models import Tbusuario


# @admin.register(Tbncm)
# class TbncmAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Tbproduto)
# class TbprodutoAdmin(admin.ModelAdmin):
#     pass


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('nome',)}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser',
                                       # 'groups', 'user_permissions')}),
                                       )}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'password1', 'password2')}
        ),
    )
    list_display = ('email', 'nome', 'is_staff')
    # list_filter = ('is_staff', 'is_superuser', 'groups')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('email', 'nome')
    ordering = ('email',)
    # filter_horizontal = ('groups', 'user_permissions',)


# Now register the new UserAdmin...
admin.site.register(Tbusuario, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)

from django.contrib.auth.models import Permission
admin.site.register(Permission)

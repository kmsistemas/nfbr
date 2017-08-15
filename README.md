# NFbr web KM Sistemas

Sistema de emissão de NFCe.

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.6
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone https://github.com/KmSistemas/nfbr.git
cd nfbr
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```


## Útil

```console
# Visualizar logs do heroku
heroku logs -t
```

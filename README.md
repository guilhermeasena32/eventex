# Eventex
Sistema de Eventos enconmendado pela Morena

[![Build Status](https://travis-ci.org/guilhermeasena32/eventex.svg?branch=master)](https://travis-ci.org/guilhermeasena32/eventex)

## Como desenvolver?
1. Clone o repositório
2. Crie um virtualenv com o Python 3.6
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.
```console
git clone https://github.com/guilhermeasena32/eventex.git
cd wttd
python3 -m venv .wttd
source .wttd/bin/activate
pip3 install -r requirements.txt
cp contrib/env-sample .env
python3 manage.py test
```

## Como fazer o deploy?
1. Crie um instância no heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroku master --force
```
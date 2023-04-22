import os
import sys

aplicacao_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'aplicacao')
sys.path.append(aplicacao_path)

import pytest
from aplicacao import app as _app

@pytest.fixture(scope='module')
def app():
    _app.config['TESTING'] = True
    _app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # cria um banco de dados somente na memória para os testes
    return _app

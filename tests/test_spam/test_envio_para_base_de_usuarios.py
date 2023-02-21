from unittest.mock import Mock

import pytest

from spam.enviador_de_email import Enviador
from spam.main import EnviadorDeSpam
from spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Javan', email='olajava11@gmail.com'),
            Usuario(nome='Renzo', email='olajava11@gmail.com')
        ],
        [
            Usuario(nome='Javan', email='olajava11@gmail.com')
        ]
    ]

)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'olajava11@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count





    def test_parametros_de_spam(sessao):
        usuario = Usuario(nome='Javan', email='olajava11@gmail.com')
        sessao.salvar(usuario)
        enviador = Mock()
        enviador_de_spam = EnviadorDeSpam(sessao, enviador)
        enviador_de_spam.enviar_emails(
            'renjava11@gmail.com',
            'Curso Python Pro',
            'Confira os módulos fantásticos'
        )
        enviador.enviar.assert_called_once_with(
            'renjava11@gmail.com',
            'olajava11@gmail.com'
            'Curso Python Pro',
            'Confira os módulos fantásticos'
        )
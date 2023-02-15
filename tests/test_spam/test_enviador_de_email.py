import pytest

from spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'olajava11@gmail.com']
)
def test_rementente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'olajava11@gmail.com'
        'Curso Python Pro.'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'olajava']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'olajava11@gmail.com'
            'Curso Python Pro.'
        )

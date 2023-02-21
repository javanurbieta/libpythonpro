from spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Javan', email='olajava11@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)







def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Javan', email='olajava11@gmail.com'),
        Usuario(nome='Renzo', email='renjava11@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listarr()


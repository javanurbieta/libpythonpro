class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remetente, assunto, corpo):
        for usuario in self.sessao.listarr():
            self.enviador.enviar(
                remetente,
                usuario.email,
                assunto

            )

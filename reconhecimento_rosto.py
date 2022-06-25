class Reconhecimento:

    def __init__(self,texto):
        self.texto = texto

    def reconhecimento_facial(self):
        # Quando receber à palavra Foto chamar o script reconhecimento facial
        if self.texto.capitalize() == 'Foto':
            import reconhecimentofacial # MELHORAR




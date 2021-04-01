class Pessoa:
    def __init__(self, email: str, nome: str, sobrenome: str, residencia: str,
    formacao: str, habilidades: str, experiencia: list):
        self.email = email
        self.nome = nome
        self.sobrenome = sobrenome
        self.residencia = residencia
        self.formacao = formacao
        self.experiencia = experiencia

    def adicionar_experiencia(self, experiencia: str):
        self.experiencia.append(experiencia)

    def __str__(self):
        return f"Email: {self.email}, Nome: {self.nome}, Sobrenome: {self.sobrenome}, Residência: {self.residencia}, " +  f"Formação: {self.formacao}, Experiência: {self.experiencia}."
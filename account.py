import getpass

class Account():

    def info_Account(self, ):
        self.account = ()

        # name = str(input("Digite seu e-mail: "))
        # password = str(input("Digite sua senha: "))
        # subject = str(input("Digite o assunto do e-mail: "))
        # destinatario = str(input("Digite o destinatario: "))
        # mensagem = str(input("Digite a mensagem: "))

        name = "warleyzee@gmail.com"
        # password = getpass.getpass(prompt="Please Enter your password")
        password = "w@@##2492"
        subject = "E-mail com anexo"
        destinatario = "warleyzee@hotmail.com"
        mensagem = "Voce tem uma email com anexo"

        self.account = name, password, subject, destinatario, mensagem

        return self.account

# test = Account()
# print(test.info_Account())
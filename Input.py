class Input:
  @staticmethod
  def ler_nome():
      while True:
          nome = input("Digite o nome: ")
          if nome:
              return nome
          else:
            print("Nome inválido. Digite novamente.")
  @staticmethod
  def ler_idade():
      while True:
            idade = input("Digite a idade: ")
            if idade:
                return idade
            else:
              print("idade inválida. Digite novamente.")
  @staticmethod
  def ler_cpf():
      while True:
            cpf = input("Digite o CPF: ")
            if cpf:
                return cpf
            else:
              print("CPF inválido. Digite novamente.")
  @staticmethod
  def ler_email():
      while True:
            email = input("Digite o email: ")
            if email:
                return email
            else:
              print("email inválido. Digite novamente.")

    
  #metodo generico
  @staticmethod
  def ler_string(mensagem):
      string = input(mensagem)
      return string

  @staticmethod
  def ler_inteiro(mensagem):
      idade = input(mensagem)
      return idade

  
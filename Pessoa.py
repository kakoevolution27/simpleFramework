import uuid

class Pessoa:
  def __init__(self, nome, idade, cpf, data_nascimento, email):
      self.id = str(uuid.uuid4())
      self.nome = nome
      self.idade = idade
      self.cpf = cpf
      self.data_nascimento = data_nascimento
      self.email = email

      #cria uma lista de tuplas com os atributos (chave, valor) 
      self._atributos = list(self.__dict__.items())

  def __iter__(self):
    self._index = 0
    return self

  def __next__(self):
      if self._index < len(self._atributos):
        resultado = self._atributos[self._index]
        self._index += 1
        return resultado
      else: 
        raise StopIteration



    



       
         
      

   
      
      
        

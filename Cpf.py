
import re


class Cpf:
   def __init__(self, numero):
      regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'

      if bool(re.match(regex, numero)):
         self.numero_cpf = numero
      else:
         self.numero_cpf = None
         raise ValueError('O CPF está inválido!')
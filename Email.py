import re


class Email:
    def __init__(self, valor):
      regex =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
      if bool(re.match(regex, valor)):
         self.email = valor
      else:
         self.email = None
         raise ValueError('O Email está Invalido')
from datetime import datetime


class Data:
    def __init__(self, valor):
        self.data = datetime.strptime(valor, '%Y-%m-%d')

    def __str__(self):
        return self.data.strftime('%Y-%m-%d')

    @property
    def ano(self):
        return self.data.year
    
    @property
    def dia(self):
        return self.data.day
    
    @property
    def mes(self):
       return self.data.month
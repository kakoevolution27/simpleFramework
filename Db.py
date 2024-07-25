import mysql.connector

class Db():
    def __init__(self, user, password, host, database, table):
        self.config = {
            'user': user,
            'password': password,
            'host': host,
            'database': database,
        }
        self.tabela = table
        self.conn = None
        self.cursor = None

    def abrir_conexao(self):
        if not self.conn:
            try:
                self.conn = mysql.connector.connect(**self.config)
            except mysql.connector.Error as err:
                return f'Nao foi possivel abrir conexão! Erro: {err}'
        else: 
            return 'Conexão ja esta aberta'
    
    def abrir_cursor(self):
        if self.conn and not self.cursor:
            try:
                self.cursor = self.conn.cursor()
                return 'Cursor criado com sucesso!'
            except mysql.connector.Error as err:
                return f'Não foi possível criar o cursor! Erro: {err}'
        elif not self.conn:
            return 'Conexão não está aberta'
        else:
            return 'Cursor já está criado'
                
    def registrar(self, dados: dict):
        #separa as colunas e valores
        colunas = ','.join(dados.keys())
        valores = ','.join(['%s'] * len(dados))

        query = f'INSERT INTO {self.tabela} ({colunas}) VALUES ({valores})'

        try:
            self.cursor.execute(query, tuple(dados.values))
            self.conn.commit()
            return('Resgistro inserido no banco de dados com sucesso!')
        except mysql.connector.Error as err:
            self.conn.rollback()
            return f'Erro ao inserir registro no banco de dados! Erro: {err}'
    
    def ler(self, id:int=0):
        query_padrao = f"SELECT * FROM {self.tabela}"
        query_com_id = f"SELECT * FROM {self.tabela} WHERE id = %s"

        try:
            if id != 0:
                self.cursor.execute(query_com_id, (id,))
                registros = self.cursor.fetchone()
                if registros:
                    return registros
                else:
                    return f'Nenhum registro encontrado com id = {id}'
            else:
                self.cursor.execute(query_padrao)
                registros = self.cursor.fetchall()

                if registros:
                    return registros
                else:
                    return 'Nenhum registro encontrado'
        except mysql.connector.Error as err:
            return f'Não foi possível recuperar os registros. Erro: {err}'

    def deletar(self, id):
        query = f"DELETE FROM {self.tabela} WHERE = %s"
        try: 
            self.cursor.execute(query, (id,))
            self.conn.commit()
            return 'Registro deletado com sucesso'
        except mysql.connector.Error as err:
            self.conn.rollback()
            return f'Não foi possível deletar o registro! Erro: {err}'
        
    def atualizar(self, id, dados:dict):
        clausula_Set = ','.join([f'{coluna} = %s' for coluna in dados.keys()])
        query = f"UPDATE {self.tabela} SET {clausula_Set} WHERE id = %s"
        
        try: 
            valores = list(dados.values())
            valores.append(id)

            self.cursor.execute(query, valores)
            self.conn.commit()
            return f'Registro {id} atualizado com sucesso'
        except mysql.connector.Error as err:
            self.conn.rollback()
            return f'erro ao atualizar registro {id}! Erro: {err}'

    def fechar_cursor(self):
        if self.cursor:
            self.cursor.close()
            self.cursor = None
            return 'Cursor fechado com sucesso'
        else:
            return 'O cursor já está fechado'
    
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            return 'Conexão fechada com sucesso'
        else:
            return 'A conexão já está fechada'


        
    
    








        










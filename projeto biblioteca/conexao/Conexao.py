import pyodbc

class conexao:
    @staticmethod
    def get_connection():
        #configuraçoes (endereço aonde os dados moram e a chave pra entrar na casa )
        conn_string = (
            "Driver={SQL Server};"
            "Server=(local);"      #nome do pc \sqlexpress
            "Database=bancoPython;"    #nome doo banco 
            "UID=;"         #usa login do windows
            "PWD=;"         #evita erro de ssl
        )
        try:
            conn = pyodbc.connect(conn_string)
            print("Conexao bem sucedida")
            return conn
        except Exception as e:
            raise RuntimeError(f"Erro na conexão com o banco: {e}")
        


conexao.get_connection()
import sqlite3
from Ativos import ativos_dicionario, vulnerabilidades_dicionario, TipoAtivos, TipoSeveridade, TipoStatus



DB_NAME = "sistema_seguranca.db"



def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn




def inicializar_banco():
                        #Cria as tabelas se elas não existirem no início do programa

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ativos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            descricao TEXT,
            responsavel TEXT,
            setor TEXT,
            localizacao TEXT,
            tipo INTEGER
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vulnerabilidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ativo_id INTEGER,
            vulnerabilidade TEXT,
            risco TEXT,
            categoria TEXT,
            severidade INTEGER,
            status INTEGER,
            FOREIGN KEY (ativo_id) REFERENCES ativos (id) ON DELETE CASCADE
        )
    ''')


    conn.commit()
    conn.close()





def salvar_ativos():
                        #Le o  dicionário de ativos e sincroniza com o banco de dados
    conn = conectar()
    cursor = conn.cursor()

    
                        #Limpa a tabela para reinscrever o dicionário atualizado
    cursor.execute("DELETE FROM ativos")
    

    for k, v in ativos_dicionario.items():
        cursor.execute('''
            INSERT INTO ativos (id, nome, descricao, responsavel, setor, localizacao, tipo)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (k, v["Nome"], v["Descrição"], v["Responsável"], v["Setor"], v["Localização"], v["Tipo"].value))
        

    conn.commit()
    conn.close()





def carregar_ativos():
                    #Busca do banco e monta o dicionário
    conn = conectar()
    cursor = conn.cursor()
    ativos_final = {}

    try:
        cursor.execute("SELECT id, nome, descricao, responsavel, setor, localizacao, tipo FROM ativos")
        for linha in cursor.fetchall():
            ativos_final[linha[0]] = {
                "Nome": linha[1],
                "Descrição": linha[2],
                "Responsável": linha[3],
                "Setor": linha[4],
                "Localização": linha[5],
                "Tipo": TipoAtivos(linha[6])
            }

    except sqlite3.OperationalError:
        pass
    conn.close()
    return ativos_final




def salvar_vulnerabilidade():
                            #Le o dicionário de vulnerabilidades e sincroniza com o banco
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM vulnerabilidades")
    

    for ativo_id, lista_vulns in vulnerabilidades_dicionario.items():
        for v in lista_vulns:
            cursor.execute('''
                INSERT INTO vulnerabilidades (ativo_id, vulnerabilidade, risco, categoria, severidade, status)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (ativo_id, v["Vulnerabilidade"], v["Risco"], v["Categoria"], v["Severidade"].value, v["Status"].value))
            

    conn.commit()
    conn.close()




def carregar_vulnerabilidade():
                            #Busca do banco e remonta a estrutura de listas dentro do dicionário
    conn = conectar()
    cursor = conn.cursor()
    vulnerabilidade_final = {}

    try:
        cursor.execute("SELECT ativo_id, vulnerabilidade, risco, categoria, severidade, status FROM vulnerabilidades")
        for linha in cursor.fetchall():
            ativo_id = linha[0]
            if ativo_id not in vulnerabilidade_final:
                vulnerabilidade_final[ativo_id] = []
                
            vulnerabilidade_final[ativo_id].append({
                "Vulnerabilidade": linha[1],
                "Risco": linha[2],
                "Categoria": linha[3],
                "Severidade": TipoSeveridade(linha[4]),
                "Status": TipoStatus(linha[5])
            })

    except sqlite3.OperationalError:
        pass
    conn.close()
    return vulnerabilidade_final
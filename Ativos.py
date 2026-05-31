from enum import Enum

class TipoAtivos(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    APLICACAO_WEB = 4
    ESTACAO_TRABALHO = 5
    IMPRESSORA_REDE = 6
    BANCO_DE_DADOS = 7
    SOFTWARE = 8
    OUTRO = 9

class TipoSeveridade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4

class TipoStatus(Enum):
    ABERTA = 1
    EM_TRATAMENTO = 2
    CORRIGIDA = 3

# Dicionários globais iniciam vazios e serão populados pelo banco de dados
ativos_dicionario = {}
vulnerabilidades_dicionario = {}
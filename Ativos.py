from enum import Enum

class TipoAtivos(Enum):         #Classe com herança do Enum para definir o tipo dos ativos
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    APLICACAO_WEB = 4
    ESTACAO_TRABALHO = 5
    IMPRESSORA_REDE = 6
    BANCO_DE_DADOS = 7
    SOFTWARE = 8
    OUTRO = 9



ativos = {                      #Informações dos ativos
    1: {"Nome": "Notebook-DELLI15",
        "Descrição": "Notebook Dell Inspiron 15 utilizado pelo gerente de TI.",
        "Responsável": "Raul Santos",
        "Setor": "Gerente de TI",
        "Localização": "Bloco C - C202",
        "Tipo": TipoAtivos.NOTEBOOK
        },

    2: {"Nome": "Servidor-01",
        "Descrição": "Servidor principal para centralização, armazenamento e gerenciamento dos principais dados.",
        "Responsável": "Luisa Almeida",
        "Setor": "Gerente de Infraestrutura",
        "Localização": "Bloco B - B103",
        "Tipo": TipoAtivos.SERVIDOR
        },

    3: {"Nome": "Roteador-A57",
        "Descrição": "Roteador principal que é responsável pela entrega da rede aos roteadores que propagam a rede.",
        "Responsável": "Eduardo Barbosa",
        "Setor": "Administrador de Redes",
        "Localização": "Bloco A - A101",
        "Tipo": TipoAtivos.ROTEADOR
        },

    4: {"Nome": "Aplicação Web",
        "Descrição": "Aplicação Web da empresa.",
        "Responsável": "Maria Eduarda da Silva",
        "Setor": "Gerente de Projeto",
        "Localização": "Bloco C - C306",
        "Tipo": TipoAtivos.APLICACAO_WEB
        }
}

class TipoSeveridade(Enum):      #Classe com herança do Enum para definir a severidade das vulnerabilidades dos ativos
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4

class TipoStatus(Enum):         #Classe com herança do Enum para definir o status das vulnerabilidades dos ativos
    ABERTA = 1
    EM_TRATAMENTO = 2
    CORRIGIDA = 3
    RISCO_ACEITO = 4






vulnerabilidades = {             #Vulnerabilidades dos ativos
    1: [{"Vulnerabilidade": "Disco sem criptografia",
        "Risco": "Vazamento de dados em caso de roubo.",
        "Categoria": "Configuração",
        "Severidade": TipoSeveridade.ALTA,
        "Status": TipoStatus.CORRIGIDA
         },

        {"Vulnerabilidade": "Sem antivírus ativo",
        "Risco": "Suscetível a malwares.",
        "Categoria": "Software",
        "Severidade": TipoSeveridade.MEDIA,
        "Status": TipoStatus.RISCO_ACEITO
         },

        {"Vulnerabilidade": "Senha de login fraca",
        "Risco": "Acesso não autorizado fácil.",
        "Categoria": "Autenticação",
        "Severidade": TipoSeveridade.ALTA,
        "Status": TipoStatus.ABERTA
         }],


    2: [{"Vulnerabilidade": "Portas desnecessárias abertas",
        "Risco": "Superfície de ataque ampliada.",
        "Categoria": "Configuração",
        "Severidade": TipoSeveridade.CRITICA,
        "Status": TipoStatus.EM_TRATAMENTO
          },

        {"Vulnerabilidade": "SO desatualizado",
        "Risco": "Exploração de Vulnerabilidades e Exposições Comuns (CVE's) conhecidas.",
        "Categoria": "Atualização",
        "Severidade": TipoSeveridade.ALTA,
        "Status": TipoStatus.ABERTA
         },

        {"Vulnerabilidade": "Acesso root via Secure Shell (SSH) habilitado",
        "Risco": "Comprometimento total do servidor.",
        "Categoria": "Permissão",
        "Severidade": TipoSeveridade.CRITICA,
        "Status": TipoStatus.CORRIGIDA
         }],


    3: [{"Vulnerabilidade": "Senha padrão de fábrica",
        "Risco": "Controle total da rede por invasor.",
        "Categoria": "Autenticação",
        "Severidade": TipoSeveridade.CRITICA,
        "Status": TipoStatus.CORRIGIDA
         },

        {"Vulnerabilidade": "Firmware desatualizado",
        "Risco": "Exploração de Vulnerabilidades e Exposições Comuns (CVE's) conhecidas.",
        "Categoria": "Atualização",
        "Severidade": TipoSeveridade.ALTA,
        "Status": TipoStatus.ABERTA
        },

        {"Vulnerabilidade": "Wi-Fi Protected Setup (WPS) ativado",
        "Risco": "Ataque de força bruta ao PIN.",
        "Categoria": "Configuração",
        "Severidade": TipoSeveridade.MEDIA,
        "Status": TipoStatus.EM_TRATAMENTO
         }],


    4: [{"Vulnerabilidade": "Sem HTTPS",
        "Risco": "Intercepção de dados em trânsito.",
        "Categoria": "Configuração",
        "Severidade": TipoSeveridade.ALTA,
        "Status": TipoStatus.EM_TRATAMENTO
         },

        {"Vulnerabilidade": "Formulário suscetível a SQL Injection",
        "Risco": "Acesso ao banco de dados inteiro.",
        "Categoria": "Código",
        "Severidade": TipoSeveridade.CRITICA,
        "Status": TipoStatus.ABERTA
         },

        {"Vulnerabilidade": "Sessão sem timeout",
        "Risco": "Sequestro de sessão ativa.",
        "Categoria": "Autenticação",
        "Severidade": TipoSeveridade.MEDIA,
        "Status": TipoStatus.CORRIGIDA
        }]
    }
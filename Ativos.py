from enum import Enum

class TipoAtivos(Enum):         #Classe com herança do Enum para definir o tipo dos ativos
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    APLICACAO_WEB = 4


ativos = {                      #Informações dos ativos
    1: {"nome": "Notebook-DELLI15",
        "descricao": "Notebook Dell Inspiron 15 utilizado pelo gerente de TI.",
        "responsavel": "Raul Santos",
        "setor": "Gerente de TI",
        "localizacao": "Bloco C - C202",
        "tipo": TipoAtivos.NOTEBOOK
        },

    2: {"nome": "Servidor-01",
        "descricao": "Servido principal para centralização, armazenamento e gerenciamentos dos principais dados.",
        "responsavel": "Luisa Almeida",
        "setor": "Gerente de Infraestrutura",
        "localizacao": "Bloco B - B103",
        "tipo": TipoAtivos.SERVIDOR
        },

    3: {"nome": "Roteador-A57",
        "descricao": "Roteador principal que é responsável pela entrega da rede aos roteadores que propagam a rede.",
        "responsavel": "Eduardo Barbosa",
        "setor": "Administrador de Redes",
        "localizacao": "Bloco A - A101",
        "tipo": TipoAtivos.ROTEADOR
        },

    4: {"nome": "Aplicação Web",
        "descricao": "Aplicação Web da empresa.",
        "responsavel": "Maria Eduarda da Silva",
        "setor": "Gerente de Projeto",
        "localizacao": "Bloco C - C306",
        "tipo": TipoAtivos.APLICACAO_WEB
        }
}

class Severidade(Enum):      #Classe com herança do Enum para definir a severidade das vulnerabilidades dos ativos
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4





vulnerabilidades = {             #Vulnerabilidades dos ativos
    1: [{"vulnerabilidade": "Disco sem ciptografia",
        "risco": "Vazamento de dados em caso de roubo.",
        "categoria": "Configuração",
        "severidade": Severidade.ALTA,
        "status": "Resolvido"
         },

        {"vulnerabilidade": "Sem ativírus ativo",
        "risco": "Suscetível a malwares.",
        "categoria": "Software",
        "severidade": Severidade.MEDIA,
        "status": "Não Resolvido"
         },

        {"vulnerabilidade": "Senha de login fraca",
        "risco": "Acesso não autorizado fácil.",
        "categoria": "Autenticação",
        "severidade": Severidade.ALTA,
        "status": "Não Resolvido"
         }],


    2: [{"vulnerabilidade": "Portas desnecessárias abertas",
        "risco": "Superfície de ataque ampliada.",
        "categoria": "Configuração",
        "severidade": Severidade.CRITICA,
        "status": "Resolvendo"
          },

        {"vulnerabilidade": "SO desatualizado",
        "risco": "Exploração de Vulnerabilidades e Exposições Comuns (CVE's) conhecidas.",
        "categoria": "Atualização",
        "severidade": Severidade.ALTA,
        "status": "Resolvido"
         },

        {"vulnerabilidade": "Acesso root via Secure Shell (SSH) habilitado",
        "risco": "Comprometimento total do servidor.",
        "categoria": "Permissão",
        "severidade": Severidade.CRITICA,
        "status": "Não Resolvido"
         }],


    3: [{"vulnerabilidade": "Senha padrão de fábrica",
        "risco": "Conrole total da rede por invasor.",
        "categoria": "Autenticação",
        "severidade": Severidade.CRITICA,
        "status": "Resolvido"
         },

        {"vulnerabilidade": "Firmware desatualizado",
        "risco": "Exploração de Vulnerabilidades e Exposições Comuns (CVE's) conhecidas.",
        "categoria": "Atualização",
        "severidade": Severidade.ALTA,
        "status": "Não Resolvido"
        },

        {"vulnerabilidade": "Wi-Fi Protected Setup (WPS) ativado",
        "risco": "Ataque de força bruta ao PIN.",
        "categoria": "Configuração",
        "severidade": Severidade.MEDIA,
        "status": "Não Resolvido"
         }],


    4: [{"vulnerabilidade": "Sem  HTTPS",
        "risco": "Intercepção de dados em trânsito.",
        "categoria": "Configuração",
        "severidade": Severidade.ALTA,
        "status": "Resolvendo"
         },

        {"vulnerabilidade": "Formulário suscetível a SQL Injection",
        "risco": "Acesso ao banco de dados inteiro.",
        "categoria": "Código",
        "severidade": Severidade.CRITICA,
        "status": "Não Resolvido"
         },

        {"vulnerabilidade": "Sessão sem timeout",
        "risco": "Sequestro de sessão ativa.",
        "categoria": "Autenticação",
        "severidade": Severidade.MEDIA,
        "status": "Resolvido"
        }]
    }
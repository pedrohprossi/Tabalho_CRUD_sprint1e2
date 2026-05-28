import json
from Ativos import ativos, vulnerabilidades, TipoAtivos, TipoSeveridade, TipoStatus


def salvar_ativos():  # Salva os ativos em JSON
    ativos_temporario = {}
    ativos_copia = {}


    for k, v in ativos.items():  # Transformar Enum em string para o JSON ler
        ativos_copia = v.copy()
        ativos_copia["Tipo"] = ativos_copia["Tipo"].value
        ativos_temporario[k] = ativos_copia


    with open("ativos.json", "w", encoding="utf-8") as f:
        json.dump(ativos_temporario, f, indent=4, ensure_ascii=False)




def carregar_ativos():  # Le os ativo do arquivo JSON
    ativos_final = {}
    ativos_copia = {}


    try:  # Tratamento de erro e criar / escrever no arquivo
        with open("ativos.json", "r", encoding="utf-8") as f:
            ativos_json = json.load(f)
    except FileNotFoundError:
        return {}


    for k, v in ativos_json.items():  # Transforma string de volta em Enum pro python
        ativos_copia = v.copy()
        ativos_copia["Tipo"] = TipoAtivos(v["Tipo"])
        ativos_final[int(k)] = ativos_copia

    return ativos_final  # Retorna os ativos em Enum




def salvar_vulnerabilidade():  #Salva as vulnerabilidades em JSON
    vulnerabilidade_temporaria = {}
    vulnerabilidade_copia = {}


    for k, lista in vulnerabilidades.items():       # Transformar Enum em string para o JSON ler
        lista_conv_enum = []
        for vuln in lista:
            vulnerabilidade_copia = vuln.copy()
            vulnerabilidade_copia["Severidade"] = vulnerabilidade_copia["Severidade"].value
            vulnerabilidade_copia["Status"] = vulnerabilidade_copia["Status"].value
            lista_conv_enum.append(vulnerabilidade_copia)
        vulnerabilidade_temporaria[k] = lista_conv_enum


    with open("vulnerabilidades.json", "w", encoding="utf-8") as f:
        json.dump(vulnerabilidade_temporaria, f, indent=4, ensure_ascii=False)




def carregar_vulnerabilidade():       #Le as vulnerabilidades do arquivo JSON
    vulnerabilidade_final = {}
    vulnerabilidade_copia = {}


    try:  # Tratamento de erro e criar / escrever no arquivo
        with open("vulnerabilidades.json", "r", encoding="utf-8") as f:
            vulnerabilidades_json = json.load(f)
    except FileNotFoundError:
        return {}

    for k, lista in vulnerabilidades_json.items():  # Transformar Enum em string para o JSON ler
        lista_conv_enum = []
        for vuln in lista:
            vulnerabilidade_copia = vuln.copy()
            vulnerabilidade_copia["Severidade"] =TipoSeveridade(vulnerabilidade_copia["Severidade"])
            vulnerabilidade_copia["Status"] = TipoStatus(vulnerabilidade_copia["Status"])
            lista_conv_enum.append(vulnerabilidade_copia)
        vulnerabilidade_final[int(k)] = lista_conv_enum

    return vulnerabilidade_final     # Retorna as vulnerabilidades em Enum
import json
from datetime import datetime
from util import calcular_distancia, carregar_dados, salvar_dados

PONTO_CENTRAL = (-23.5505, -46.6333)  # Exemplo: São Paulo (fixo)
ARQUIVO = "data/relatos.json"

def cadastrar_relator():
    print("\n--- Cadastro de Relator ---")
    nome = input("Nome completo: ")
    doc = input("Documento (CPF/RG): ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    local = input("Localização (cidade ou referência): ")

    relator = {
        "nome": nome,
        "documento": doc,
        "email": email,
        "telefone": telefone,
        "localizacao": local
    }

    dados = carregar_dados(ARQUIVO)
    dados["relatores"].append(relator)
    salvar_dados(ARQUIVO, dados)
    print("Relator cadastrado com sucesso!")

def cadastrar_relato():
    print("\n--- Cadastro de Relato ---")
    tipo = input("Tipo da catástrofe: ")
    descricao = input("Descrição: ")
    data = input("Data (AAAA-MM-DD): ")
    hora = input("Hora (HH:MM): ")
    lat = float(input("Latitude: "))
    lon = float(input("Longitude: "))

    distancia = calcular_distancia(PONTO_CENTRAL, (lat, lon))
    if distancia > 10:
        print("Local fora do raio de 10 km. Relato não registrado.")
        return

    relato = {
        "tipo": tipo,
        "descricao": descricao,
        "data": data,
        "hora": hora,
        "localizacao": {"lat": lat, "lon": lon}
    }

    dados = carregar_dados(ARQUIVO)
    dados["relatos"].append(relato)
    salvar_dados(ARQUIVO, dados)
    print("Relato cadastrado com sucesso!")

def listar_relatos():
    dados = carregar_dados(ARQUIVO)
    for i, relato in enumerate(dados["relatos"], 1):
        print(f"\nRelato #{i}")
        print(f"Tipo: {relato['tipo']}")
        print(f"Descrição: {relato['descricao']}")
        print(f"Data: {relato['data']} Hora: {relato['hora']}")
        print(f"Localização: {relato['localizacao']}")

def buscar_relatos():
    tipo_filtro = input("Filtrar por tipo (deixe em branco para ignorar): ")
    data_ini = input("Data inicial (AAAA-MM-DD): ")
    data_fim = input("Data final (AAAA-MM-DD): ")

    dados = carregar_dados(ARQUIVO)
    resultados = []

    for r in dados["relatos"]:
        if tipo_filtro and tipo_filtro.lower() not in r["tipo"].lower():
            continue
        if not (data_ini <= r["data"] <= data_fim):
            continue
        resultados.append(r)

    if not resultados:
        print("Nenhum relato encontrado.")
    else:
        for r in resultados:
            print(f"\n{r['tipo']} em {r['data']} às {r['hora']}: {r['descricao']}")

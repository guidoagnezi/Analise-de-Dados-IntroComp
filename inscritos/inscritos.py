import pandas as pd
from rapidfuzz import process, fuzz

# =========================FUNÇÕES DE ANÁLISE UNIVARIÁVEIS:========================= 

def relacao_de_turno(df: pd.DataFrame):
    #Retorna a relação de inscritos nos turnos (morning ou afternoon)
    return df['turno'].value_counts()

def relacao_sabem_programar(df: pd.DataFrame):
    # Retorna o número de inscritos que sabe programar
    return df['sabe programar'].value_counts().get(True)

def relacao_tem_computador(df: pd.DataFrame):
    # Retorna o número de inscritos com acesso a um computador
    return df['sabe programar'].value_counts().get(True)

def relacao_tem_internet(df: pd.DataFrame):
    # Retorna o número de inscritos com acesso a internet
    return df['tem internet'].value_counts().get(True)

def relacao_como_soube_do_introcomp(df: pd.DataFrame):
    mapeamento = {
        'Amigos': 'Amigos',
        'Família': 'Família',
        'Whatsapp': 'Whatsapp',
        'Facebook': 'Facebook',
        'Instagram': 'Instagram',
        'Professor': 'Professor' 
    }
    
    return df['como soube do Introcomp'].map(mapeamento).fillna('Outros').value_counts()

def relacao_genero(df: pd.DataFrame):
    # Retorna a relação de homens e mulheres
    return df['genero'].value_counts()

def relacao_bairro(df: pd.DataFrame):
    # Retorna a relação de bairros com mais inscritos
    return df['bairro'].value_counts()

def relacao_cidade(df: pd.DataFrame):
    # Retorna a relação de cidades com mais inscritos
    return df['cidade'].value_counts()

def relacao_escolaridade(df: pd.DataFrame):
    # Retorna a relação de série com mais inscritos
    return df['escolaridade'].value_counts()

def relacao_cidade_escola(df: pd.DataFrame):
    # Retorna a relação de cidades das escolas com mais inscritos
    return df['cidade escola'].value_counts()

def relacao_escola(df: pd.DataFrame):
    # Retorna a relação das escolas com mais inscritos
    return df['escola'].value_counts()

def relacao_escola_agrupada(df: pd.DataFrame, limite_similaridade=70):
    # Retorna a relação das escolas com mais inscritos
    # A função agrupa entradas com nome parecido evitando elementos diferentes na série, mas que representam a mesma escola
    escolas_originais = df['escola'].dropna().unique()
    grupos = {}

    for escola in escolas_originais:
        escola_base = escola.strip().lower()

        # Só tenta comparar se já houver grupos existentes
        if grupos:
            resultado = process.extractOne(escola_base, list(grupos.keys()), scorer=fuzz.token_sort_ratio)
        else:
            resultado = None

        if resultado and resultado[1] >= limite_similaridade:
            correspondencia = resultado[0]
            grupos[correspondencia].append(escola)
        else:
            grupos[escola_base] = [escola]

    # Criar o mapeamento de nomes originais para o nome base do grupo
    mapeamento = {}
    for base, nomes in grupos.items():
        for nome in nomes:
            mapeamento[nome] = base

    serie_normalizada = df['escola'].map(mapeamento)
    return serie_normalizada.value_counts()

def relacao_tipo_escola(df: pd.DataFrame):
    # Retorna a relação do tipo das escolas com mais inscritos
    return df['tipo escola'].value_counts()

# =========================FUNÇÕES DE ANÁLISE MULTIVARIÁVEIS:=========================

def relacao_sabem_programar_e_possuem_internet(df: pd.DataFrame):
    # Retorna a relação dos inscritos que possuem tanto internet quanto computador
    return pd.crosstab(df['tem computador'], df['tem internet'])
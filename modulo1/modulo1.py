import pandas as pd
from rapidfuzz import process, fuzz
import unidecode

def normalizar_nome(nome):
    return unidecode.unidecode(str(nome).strip().lower())

def associar_nome_mais_proximo(nome, nomes_referencia, threshold=62):
    resultado = process.extractOne(nome, nomes_referencia, scorer=fuzz.token_sort_ratio)
    if resultado and resultado[1] >= threshold:
        print("Guido!")
        return resultado[0]
    return nome

def concatena_mat_vesp(dfm: pd.DataFrame, dfv: pd.DataFrame) -> pd.DataFrame:

    dfm.columns = dfm.columns.str.strip().str.lower()
    dfv.columns = dfv.columns.str.strip().str.lower()
    dfm['name'] = dfm['name'].str.lower()
    dfv['name'] = dfv['name'].str.lower()

    df_completo = pd.concat([dfm, dfv], ignore_index=True)

    return df_completo

def relacao_aprovados(df: pd.DataFrame):
    return df['resultado'].value_counts()

def merge_df_notas_informacoes(df_notas, df_informacoes):
    df_notas['name_normalized'] = df_notas['name'].str.strip().str.lower()
    df_informacoes['name_normalized'] = df_informacoes['name'].str.strip().str.lower()


    nomes_info = df_informacoes['name_normalized'].tolist()
    mapeamento = {
        nome: process.extractOne(nome, nomes_info, scorer=fuzz.token_sort_ratio)[0]
        for nome in df_notas['name_normalized'].unique()
    }


    df_notas['name_normalized'] = df_notas['name_normalized'].map(mapeamento)


    df_merge = pd.merge(
        df_notas,
        df_informacoes,
        left_on='name_normalized',
        right_on='name_normalized',
        how='left'
    )

    return df_merge

def relacao_aprovados_por_cidade(df_relacao : pd.DataFrame):

    return df_relacao.groupby(['cidade', 'resultado']).size().unstack(fill_value=0)
    
def formatacao_notas(df : pd.DataFrame):
    df = df.applymap(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)
    df['nota final'] = pd.to_numeric(df['nota final'], errors='coerce')
    df['notas workings'] = pd.to_numeric(df['notas workings'], errors='coerce')
    df['notas prova'] = pd.to_numeric(df['notas prova'], errors='coerce')
    return df

def relacao_media_final_por_cidade(df_relacao : pd.DataFrame):
    
    return df_relacao.groupby('cidade')['nota final'].mean().sort_values(ascending=False)

def relacao_notas_working_por_cidade(df : pd.DataFrame):

    return df.groupby('cidade')['notas workings'].mean().sort_values(ascending=False)

def relacao_notas_prova_por_cidade(df : pd.DataFrame):

    return df.groupby('cidade')['notas prova'].mean().sort_values(ascending=False)

def relacao_menor_media_working(df : pd.DataFrame):

    for col in df.columns[3:56]:
        df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')

    colunas_w1 = df.columns[3:8]
    colunas_w2 = df.columns[11:16]
    colunas_w3 = df.columns[19:24]
    colunas_w4 = df.columns[27:32]
    colunas_w5 = df.columns[35:40]
    colunas_w6 = df.columns[43:48]
    colunas_w7 = df.columns[51:56]

    df['w1_soma'] = df[colunas_w1].sum(axis=1, skipna=True)
    df['w2_soma'] = df[colunas_w2].sum(axis=1, skipna=True)
    df['w3_soma'] = df[colunas_w3].sum(axis=1, skipna=True)
    df['w4_soma'] = df[colunas_w4].sum(axis=1, skipna=True)
    df['w5_soma'] = df[colunas_w5].sum(axis=1, skipna=True)
    df['w6_soma'] = df[colunas_w6].sum(axis=1, skipna=True)
    df['w7_soma'] = df[colunas_w7].sum(axis=1, skipna=True)

    w1 = df['w1_soma'].mean()
    w2 = df['w2_soma'].mean()
    w3 = df['w3_soma'].mean()
    w4 = df['w4_soma'].mean()
    w5 = df['w5_soma'].mean()
    w6 = df['w6_soma'].mean()
    w7 = df['w7_soma'].mean()

    medias = [
        w1,
        w2,
        w3,
        w4,
        w5,
        w6,
        w7 
    ]

    for m in medias:
        print(m)

    return medias

pd.set_option('display.max_rows', None)
df_notas_m = pd.read_csv('dados/notas_m_m1.csv', header=2)
df_notas_v = pd.read_csv('dados/notas_v_m1.csv', header=2)
df_info_m = pd.read_csv('dados/info_matutino_m1.csv')
df_info_v = pd.read_csv('dados/info_vespertino_m1.csv')

df_info = concatena_mat_vesp(df_info_m, df_info_v)
df_notas = concatena_mat_vesp(df_notas_m, df_notas_v)

df_info.to_csv("info.csv", index=False)
df_notas.to_csv("notas.csv", index=False)

df_relacao = merge_df_notas_informacoes(df_notas, df_info)
df_relacao = formatacao_notas(df_relacao)
print(df_relacao)

print(relacao_aprovados_por_cidade(df_relacao))
print(relacao_media_final_por_cidade(df_relacao))
print(relacao_notas_working_por_cidade(df_relacao))
print(relacao_notas_prova_por_cidade(df_relacao))

df_notas = formatacao_notas(df_notas)
relacao_menor_media_working(df_notas)
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

def relacao_aprovados_por_cidade(df_notas: pd.DataFrame, df_informacoes):
    return pd.merge(df_notas, df_informacoes, on="name", how="left").groupby(['cidade', 'resultado']).size().unstack(fill_value=0)

pd.set_option('display.max_rows', None)
df_notas_m = pd.read_csv('dados/notas_m_m1.csv', header=2)
df_notas_v = pd.read_csv('dados/notas_v_m1.csv', header=2)
df_info_m = pd.read_csv('dados/info_matutino_m1.csv')
df_info_v = pd.read_csv('dados/info_vespertino_m1.csv')

df_info = concatena_mat_vesp(df_info_m, df_info_v)
df_notas = concatena_mat_vesp(df_notas_m, df_notas_v)

df_info.to_csv("info.csv", index=False)
df_notas.to_csv("notas.csv", index=False)

print(relacao_aprovados_por_cidade(df_notas, df_info))

print(df_notas)
print(df_info)
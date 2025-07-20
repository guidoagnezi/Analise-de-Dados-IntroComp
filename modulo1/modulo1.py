import pandas as pd
from rapidfuzz import process, fuzz

def concatena_mat_vesp(dfm: pd.DataFrame, dfv : pd.DataFrame):
    dfm.columns = dfm.columns.str.strip().str.lower()
    dfv.columns = dfv.columns.str.strip().str.lower()
    dfm['turno'] = 'matutino'
    dfv['turno'] = 'vespertino'

    df_completo = pd.concat([dfm, dfv], ignore_index=True)
    return df_completo

def relacao_aprovados(df: pd.DataFrame):
    return df['resultado'].value_counts()

def relacao_aprovados_por_cidade(df_notas: pd.DataFrame, df_informacoes):
    return pd.merge(df_notas, df_informacoes, on="name", how="left").groupby(['cidade', 'resultado']).size().unstack(fill_value=0)

pd.set_option('display.max_rows', None)
df_notas_m = pd.read_csv('dados/notas_matutino_m1.csv', header=2)
df_notas_v = pd.read_csv('dados/notas_vespertino_m1.csv', header=2)
df_info_m = pd.read_csv('dados/info_matutino_m1.csv')
df_info_v = pd.read_csv('dados/info_vespertino_m1.csv')

df_info = concatena_mat_vesp(df_info_m, df_info_v)
df_notas = concatena_mat_vesp(df_notas_m, df_notas_v)

df_info.to_csv("info.csv", index=False)
df_notas.to_csv("notas.csv", index=False)

print(relacao_aprovados_por_cidade(df_notas, df_info))

print(df_info)
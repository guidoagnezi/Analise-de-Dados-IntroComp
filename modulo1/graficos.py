import matplotlib.pyplot as plt
import modulo1 as m1
import pandas as pd

def plot_media_final_por_cidade(df_relacao: pd.DataFrame):
    medias = m1.relacao_media_final_por_cidade(df_relacao)
    
    plt.figure(figsize=(10, 6))
    plt.barh(medias.index, medias.values, color='teal')
    plt.xlabel('Média Final')
    plt.title('Média Final por Cidade')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_notas_working_por_cidade(df: pd.DataFrame):
    medias = m1.relacao_notas_working_por_cidade(df)

    plt.figure(figsize=(10, 6))
    plt.barh(medias.index, medias.values, color='slateblue')
    plt.xlabel('Média Working')
    plt.title('Notas Working por Cidade')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_notas_prova_por_cidade(df: pd.DataFrame):
    medias = m1.relacao_notas_prova_por_cidade(df)

    plt.figure(figsize=(10, 6))
    plt.barh(medias.index, medias.values, color='darkorange')
    plt.xlabel('Média Prova')
    plt.title('Notas da Prova por Cidade')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_menor_media_workings(df: pd.DataFrame):
    medias = m1.relacao_menor_media_working(df)
    workings = [f'W{i}' for i in range(1, 8)]

    plt.figure(figsize=(8, 5))
    plt.bar(workings, medias, color='steelblue')
    plt.ylabel('Média Geral')
    plt.title('Média Geral por Working (W1 a W7)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

plot_media_final_por_cidade(m1.df_relacao)
plot_notas_prova_por_cidade(m1.df_relacao)
plot_notas_working_por_cidade(m1.df_relacao)
plot_menor_media_workings(m1.df_notas)
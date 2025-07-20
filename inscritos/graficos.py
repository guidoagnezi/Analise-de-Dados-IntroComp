import matplotlib.pyplot as plt
import pandas as pd

def plot_bar_from_series(s: pd.Series, title, xlabel, ylabel, color_list, figsize=(8, 5)):
    fig, ax = plt.subplots(figsize=figsize)
    colors = color_list or plt.cm.tab10.colors  # usa uma paleta padrão se não for passado
    ax.bar(s.index, s.values, color=colors[:len(s)])  # aplica uma cor por barra
    if title: ax.set_title(title)
    if xlabel: ax.set_xlabel(xlabel)
    if ylabel: ax.set_ylabel(ylabel)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_pie_from_series(s: pd.Series, title, figsize=(8, 8), autopct: str = '%1.1f%%', startangle: int = 90, shadow: bool = True, colors=None, explode=None):
    fig, ax = plt.subplots(figsize=figsize)
    wedges, texts, autotexts = ax.pie(s.values, labels=None, autopct=autopct,
           startangle=startangle, shadow=False,
           colors=colors, explode=explode)
    
    # Adiciona legenda com os rótulos e cores
    ax.legend(wedges, s.index, title="Categorias", loc="center left", bbox_to_anchor=(1, 0.5))
    
    ax.axis('equal')  # garante forma circular :contentReference[oaicite:3]{index=3}
    if title: ax.set_title(title)
    plt.tight_layout()
    plt.show()

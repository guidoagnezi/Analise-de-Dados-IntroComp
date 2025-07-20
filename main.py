import pandas as pd
from inscritos.inscritos import *
from inscritos.graficos import *

# Mostra todos os elementos das Series (sem truncar)
pd.set_option('display.max_rows', None)
df = pd.read_csv('dados/inscritos_2024.csv')

gen_serie = relacao_genero(df)
#plot_bar_from_series(gen_serie, 'Relação de gênero', 'Gênero', 'Número de inscritos', None)

como_soube_serie = relacao_como_soube_do_introcomp(df)
#plot_pie_from_series(como_soube_serie, 'Relação do meio de descoberta do projeto')
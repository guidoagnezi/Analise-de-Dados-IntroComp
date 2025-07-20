import pandas as pd
from inscritos.inscritos import *

# Mostra todos os elementos das Series (sem truncar)
pd.set_option('display.max_rows', None)
df = pd.read_csv('dados/inscritos_2024.csv')

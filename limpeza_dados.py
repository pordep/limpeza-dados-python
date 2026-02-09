import pandas as pd
import numpy as np

data = {
    'cliente_id': [101, 102, 103, 104, 105],
    'valor': ['R$ 500,00', '1.200,50', 'nan', 'R$ 1.000.000,00', '350'],
    'data_pagamento': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-05', '2024-01-02'],
    'pais': ['brasil', 'BRASIL', 'brazil', 'BR', 'Brasil']
}
df = pd.DataFrame(data)


df['pais'] = 'BR'
df['valor'] = df['valor'].str.replace('R\$ ', '', regex = True)
df['valor'] = df['valor'].str.replace('.', '', regex = False)
df['valor'] = df['valor'].str.replace(',', '.', regex = False)

df['valor'] = pd.to_numeric(df['valor'], errors = 'coerce')
mediana = df['valor'].median()

df['valor'] = df['valor'].fillna(mediana)
df['status'] = df['valor'].apply(lambda x: 'VERIFICAR' if x > 50000 else 'OK')

# Exportando para Excel
df.to_excel('limpeza_dados.xlsx', index=False, sheet_name='transacoes')
print(df)

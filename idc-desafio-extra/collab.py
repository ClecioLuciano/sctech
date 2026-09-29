import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('superstore.csv', encoding='latin1')

print(df.head())

print(df.info())

print(df.describe())

print(df.dtypes)

## 2. Tratamento e preparação dos dados

print("Valores nulos por coluna:")
print(df.isnull().sum())

duplicateRows = df[df.duplicated()]
print("\nNúmero de linhas duplicadas: " + str(len(duplicateRows)))

# Removendo as linhas duplicadas
print(len(df))
df.drop_duplicates(keep='last', inplace=True)
print(len(df))

# Removendo os valores nulos
df.dropna(subset=['Profit'], inplace=True)
print(df)

### Convertendo tipos de dados

# Certificando-se de que as colunas de data são do tipo datetime antes de formatar

# Converter colunas de data
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y') # Usando o nome original da coluna
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y') # Usando o nome original da coluna

print("\nPrimeiras 5 linhas com datas antes de serem formatadas (como datetime):")
print(df[['Order Date', 'Ship Date']].head()) # Usando o nome original da coluna

# Convertendo as colunas de data para o formato de string dd/mm/aaaa
df['Order Date'] = df['Order Date'].dt.strftime('%d/%m/%Y')
df['Ship Date'] = df['Ship Date'].dt.strftime('%d/%m/%Y')

# Verificando os tipos de dados após a conversão para string
print("\nPrimeiras 5 linhas com datas formatadas:")
print(df[['Order Date', 'Ship Date']].head()) # Usando o nome original da coluna

### Organização e padronização das colunas

# Padronizando os nomes das colunas: convertendo para minúsculas e substituindo espaços por underscores
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Exibindo os novos nomes das colunas para verificar
print("Novos nomes das colunas:")
print(df.columns)

### Visualizando Nomes de Colunas em Português

# Mapeamento dos nomes das colunas em inglês para português
column_name_mapping = {
    'row_id': 'codigo_linha',
    'order_id': 'codigo_pedido',
    'order_date': 'data_pedido',
    'ship_date': 'data_envio',
    'ship_mode': 'modo_envio',
    'customer_id': 'codigo_cliente',
    'customer_name': 'nome_cliente',
    'segment': 'segmento',
    'country': 'pais',
    'city': 'cidade',
    'state': 'estado',
    'postal_code': 'codigo_postal',
    'region': 'regiao',
    'product_id': 'codigo_produto',
    'category': 'categoria',
    'sub-category': 'sub_categoria',
    'product_name': 'nome_produto',
    'sales': 'vendas',
    'quantity': 'quantidade',
    'discount': 'desconto',
    'profit': 'lucro'
}

# Exibindo as primeiras linhas do DataFrame com os nomes das colunas traduzidos para visualização
df_translated_columns = df.rename(columns=column_name_mapping)
sns.displot(df_translated_columns.head())

# Com os nomes das colunas padronizados, o DataFrame está mais fácil de manipular.
#  Agora podemos prosseguir com outras análises ou transformações.

### Identificação e Tratamento de Outliers


# Garantir que os nomes das colunas estejam padronizados antes de prosseguir
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Identificação de Outliers com Box Plots para as colunas numéricas

# Colunas numéricas para análise de outliers
numeric_cols = ['sales', 'quantity', 'discount', 'profit']

plt.figure(figsize=(15, 10))
for i, col in enumerate(numeric_cols):
    plt.subplot(2, 2, i + 1) # Cria uma grade de 2x2 para os gráficos
    sns.boxplot(y=df[col])
    plt.title(f'Box Plot de {col.capitalize()}')
    plt.ylabel('') # Remove o rótulo do eixo y para evitar redundância
plt.tight_layout()
plt.show()

## 3. Análise exploratória

### Aplicação de filtros, ordenações e agrupamentos (GroupBy)


df_grouped_category = df.groupby('category')[['sales', 'profit']].mean().reset_index()
df_grouped_category.columns = ['categoria', 'media_vendas', 'media_lucro']
df_grouped_category.sort_values(by='media_lucro', ascending=False, inplace=True)

# Adição do filtro: mostrar apenas categorias com lucro médio positivo
df_grouped_category = df_grouped_category[df_grouped_category['media_lucro'] > 0]

sns.displot(df_grouped_category)

### Análise das variáveis relevantes do dataset

#### Análise por Segmento de Cliente


# Contagem de ocorrências por segmento
print("Contagem de clientes por segmento:\n")
sns.displot(df['segment'].value_counts())

# Agrupamento por segmento para calcular a média de vendas e lucro
df_grouped_segment = df.groupby('segment')[['sales', 'profit']].mean().reset_index()
df_grouped_segment.columns = ['segmento', 'media_vendas', 'media_lucro']
df_grouped_segment.sort_values(by='media_lucro', ascending=False, inplace=True)

print("\nMédia de Vendas e Lucro por Segmento:\n")
sns.displot(df_grouped_segment)

#### Visualização por Segmento de Cliente

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.barplot(x='segmento', y='media_vendas', data=df_grouped_segment, palette='viridis', hue='segmento', legend=False)
plt.title('Média de Vendas por Segmento de Cliente')
plt.xlabel('Segmento')
plt.ylabel('Média de Vendas')
plt.xticks(rotation=45, ha='right')

plt.subplot(1, 2, 2)
sns.barplot(x='segmento', y='media_lucro', data=df_grouped_segment, palette='plasma', hue='segmento', legend=False)
plt.title('Média de Lucro por Segmento de Cliente')
plt.xlabel('Segmento')
plt.ylabel('Média de Lucro')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

### Análise por Região Geográfica

# Contagem de ocorrências por região
print("Contagem de vendas por região:\n")
sns.displot(df['region'].value_counts())

# Agrupamento por região para calcular a média de vendas e lucro
df_grouped_region = df.groupby('region')[['sales', 'profit']].mean().reset_index()
df_grouped_region.columns = ['regiao', 'media_vendas', 'media_lucro']
df_grouped_region.sort_values(by='media_lucro', ascending=False, inplace=True)

print("\nMédia de Vendas e Lucro por Região:\n")
sns.displot(df_grouped_region)

#### Visualização por Região Geográfica

plt.figure(figsize=(14, 6))

# Número de regiões
n = len(df_grouped_region)

# Gerar paletas com n cores distintas
cores_vendas = plt.cm.viridis(np.linspace(0, 1, n))
cores_lucro = plt.cm.plasma(np.linspace(0, 1, n))

# Gráfico de pizza para média de vendas por região
plt.subplot(1, 2, 1)
plt.pie(df_grouped_region['media_vendas'],
        labels=df_grouped_region['regiao'],
        autopct='%1.1f%%',
        colors=cores_vendas)
plt.title('Média de Vendas por Região Geográfica')

# Gráfico de pizza para média de lucro por região
plt.subplot(1, 2, 2)
plt.pie(df_grouped_region['media_lucro'],
        labels=df_grouped_region['regiao'],
        autopct='%1.1f%%',
        colors=cores_lucro)
plt.title('Média de Lucro por Região Geográfica')

plt.tight_layout()
plt.show()

### Investigação de relações entre variáveis: Desconto vs Lucro

plt.figure(figsize=(10, 6))
sns.scatterplot(x='discount', y='profit', data=df, alpha=0.6)
plt.title('Relação entre Desconto e Lucro')
plt.xlabel('Desconto')
plt.ylabel('Lucro')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
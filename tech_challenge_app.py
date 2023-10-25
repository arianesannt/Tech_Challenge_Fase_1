# bibliotecas

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.float_format = '{:,.2f}'.format
import streamlit as st

st.write('# Tech Challenge Vinhos')

#Criando o layout da aplicação
tab0, tab1, tab2 = st.tabs(["Limpeza", "Análise inicial", "Estudo"])

with tab0:
    st.write('### Limpeza')

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    # Subindo e tratando os dados
    exportacao = pd.read_csv('ExpVinho.csv', sep=';')
    exportacao_visualizador = pd.DataFrame(exportacao)

    # excluindo a coluna 'Id', porque não é uma informação útil para a análise
    exportacao = exportacao.drop('Id', axis=1)

    # o problema de negócio pede que sejam analisados os últimos 15 anos
    # como cada coluna representa um valor de quantidade e de valor monetario por ano, será conservado somente as últimas 30 colunas
    colunas = exportacao.columns[-30:]
    colunas = colunas.insert(0, 'País')
    exportacao = exportacao[colunas]
    exportacao['País'].iloc[2] = 'Alemanha'
    
    # retirando dos dataframe os países que não compraram vinho com o brasil
    exportacao['total'] = exportacao.sum(numeric_only=True, axis=1)
    paises_comercio_zero = exportacao[exportacao['total'] == 0]
    exportacao = exportacao.drop(paises_comercio_zero.index, axis=0)
    exportacao = exportacao.drop('total', axis=1)
    st.dataframe(exportacao, use_container_width=True)
    """
    st.code(codigo_python, language='python')

    # Subindo e tratando os dados
    exportacao = pd.read_csv('ExpVinho.csv', sep=';')
    exportacao_visualizador = pd.DataFrame(exportacao)

    # excluindo a coluna 'Id', porque não é uma informação útil para a análise
    exportacao = exportacao.drop('Id', axis=1)

    # o problema de negócio pede que sejam analisados os últimos 15 anos
    # como cada coluna representa um valor de quantidade e de valor monetario por ano, será conservado somente as últimas 30 colunas
    colunas = exportacao.columns[-30:]
    colunas = colunas.insert(0, 'País')
    exportacao = exportacao[colunas]
    exportacao['País'].iloc[2] = 'Alemanha'

    # retirando dos dataframe os países que não compraram vinho com o brasil
    exportacao['total'] = exportacao.sum(numeric_only=True, axis=1)
    paises_comercio_zero = exportacao[exportacao['total'] == 0]
    exportacao = exportacao.drop(paises_comercio_zero.index, axis=0)
    exportacao = exportacao.drop('total', axis=1)

    st.dataframe(exportacao, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    # Separando os valores das variáveis 'quantidade' e 'valor' que hoje estão representadas no dataframe como ANO e ANO.1 respectivamente
    quantidadel = []
    valoruss = []
    for item in exportacao.columns:
        if item == 'País':
            quantidadel.append(item)
            valoruss.append(item)
        elif len(item) == 4:
            quantidadel.append(item)
        else:
            valoruss.append(item)
    # criando dataframes separados para quantidade e valor
    quantidade_l = exportacao[quantidadel]
    quantidade_l = quantidade_l.set_index('País')
    valor_uss = exportacao[valoruss]
    valor_uss = valor_uss.set_index('País')
    """
    st.code(codigo_python, language='python')

    # Separando os valores das variáveis 'quantidade' e 'valor' que hoje estão representadas no dataframe como ANO e ANO.1 respectivamente
    quantidadel = []
    valoruss = []
    for item in exportacao.columns:
        if item == 'País':
            quantidadel.append(item)
            valoruss.append(item)
        elif len(item) == 4:
            quantidadel.append(item)
        else:
            valoruss.append(item)
    # criando dataframes separados para quantidade e valor
    quantidade_l = exportacao[quantidadel]
    quantidade_l = quantidade_l.set_index('País')
    valor_uss = exportacao[valoruss]
    valor_uss = valor_uss.set_index('País')

    st.dataframe(quantidade_l, use_container_width=True)
    st.dataframe(valor_uss, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    # retirando o '.1' do valor da coluna para que futuramente seja possível juntar as tabelas
    colunas = valor_uss.columns.str[:-2]
    valor_uss.columns = colunas
    valor_uss.head(2)
    """
    st.code(codigo_python, language='python')

    # retirando o '.1' do valor da coluna para que futuramente seja possível juntar as tabelas
    colunas = valor_uss.columns.str[:-2]
    valor_uss.columns = colunas
    valor_uss.head(2)

    st.dataframe(valor_uss, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    # fazendo o melt e criando um dataframe único com informações de quantidade e valor
    valor_uss2 = valor_uss.reset_index('País')
    quantidade_l2 = quantidade_l.reset_index('País')

    quantidade_l2 = quantidade_l2.melt(id_vars=['País'], value_vars=quantidade_l.columns)
    valor_uss2 = valor_uss2.melt(id_vars=['País'], value_vars=valor_uss.columns)

    # renomeando as colunas para a correta identificação das variáveis
    quantidade_l2.columns = ['pais_destino', 'ano', 'quantidade_l']
    valor_uss2.columns = ['pais_destino', 'ano', 'valor_uss']
    """
    st.code(codigo_python, language='python')

    # fazendo o melt e criando um dataframe único com informações de quantidade e valor
    valor_uss2 = valor_uss.reset_index('País')
    quantidade_l2 = quantidade_l.reset_index('País')
    quantidade_l2 = quantidade_l2.melt(id_vars=['País'], value_vars=quantidade_l.columns)
    valor_uss2 = valor_uss2.melt(id_vars=['País'], value_vars=valor_uss.columns)

    # renomeando as colunas para a correta identificação das variáveis
    quantidade_l2.columns = ['pais_destino', 'ano', 'quantidade_l']
    valor_uss2.columns = ['pais_destino', 'ano', 'valor_uss']

    st.dataframe(quantidade_l2, use_container_width=True)
    st.dataframe(valor_uss2, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    # fazendo o .join() entre as duas tabelas para tranasformá-la em uma só
    exportacao_long = quantidade_l2.join(valor_uss2['valor_uss'])
    exportacao_long.head(2)
    """
    st.code(codigo_python, language='python')

    # fazendo o .join() entre as duas tabelas para tranasformá-la em uma só
    exportacao_long = quantidade_l2.join(valor_uss2['valor_uss'])
    
    st.dataframe(exportacao_long, use_container_width=True)
    st.dataframe(exportacao_long.describe(), use_container_width=True)
    
with tab1:
    st.write('### Análises iniciais')

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    exportacao_long_por_pais = exportacao_long.groupby(by='pais_destino').sum(numeric_only=True)
    exportacao_long_por_pais = exportacao_long_por_pais.sort_values(by='valor_uss', ascending=False)
    exportacao_long_por_pais.sum()
    """
    st.code(codigo_python, language='python')

    exportacao_long_por_pais = exportacao_long.groupby(by='pais_destino').sum(numeric_only=True)
    exportacao_long_por_pais = exportacao_long_por_pais.sort_values(by='valor_uss', ascending=False)

    st.dataframe(exportacao_long_por_pais.sum(), use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    exportacao_long_por_pais_top10 = exportacao_long_por_pais.head(10)
    exportacao_long_por_pais_top10 = exportacao_long_por_pais_top10.reset_index('pais_destino')
    exportacao_long_por_pais_top10.head()
    """
    st.code(codigo_python, language='python')

    exportacao_long_por_pais_top10 = exportacao_long_por_pais.head(10)
    exportacao_long_por_pais_top10 = exportacao_long_por_pais_top10.reset_index('pais_destino')

    st.dataframe(exportacao_long_por_pais_top10, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    df_aux = pd.read_excel('codigo_iso-alpha_top10_paises_importadores_vinho.xlsx')
    df_aux.head
    """
    st.code(codigo_python, language='python')

    df_aux = pd.read_csv('codigo_iso-alpha_top10_paises_importadores_vinho.csv', sep=';', encoding='latin1')

    st.dataframe(df_aux, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    # fazendo o .join() entre as duas tabelas para tranasformá-la em uma só
    exportacao_long_por_pais_top10 = exportacao_long_por_pais_top10.join(df_aux[['cod_num', 'iso_alpha']])
    exportacao_long_por_pais_top10.head()
    """
    st.code(codigo_python, language='python')

    # fazendo o .join() entre as duas tabelas para tranasformá-la em uma só
    exportacao_long_por_pais_top10 = exportacao_long_por_pais_top10.join(df_aux[['cod_num', 'iso_alpha']])
    exportacao_long_por_pais_top10.head()

    st.dataframe(exportacao_long_por_pais_top10, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    exportacao_long_por_pais_top10['pais_origem'] = 'Brasil'
    exportacao_long_por_pais_top10.head()
    """
    st.code(codigo_python, language='python')

    exportacao_long_por_pais_top10['pais_origem'] = 'Brasil'

    st.dataframe(exportacao_long_por_pais_top10, use_container_width=True)

    st.write('_________________________________________________________')

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    exportacao_long_por_pais['dolar_por_litro'] = exportacao_long_por_pais['valor_uss'] / exportacao_long_por_pais['quantidade_l']
    exportacao_long_por_pais.head()
    """
    st.code(codigo_python, language='python')

    # fazendo o .join() entre as duas tabelas para tranasformá-la em uma só
    exportacao_long_por_pais['dolar_por_litro'] = exportacao_long_por_pais['valor_uss'] / exportacao_long_por_pais['quantidade_l']
    exportacao_long_por_pais.head(10)

    st.dataframe(exportacao_long_por_pais, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    # incluindo a coluna total nos dataframe
    quantidade_l["Total_quantidade"] = quantidade_l.sum(axis=1)
    valor_uss["Total_valor"] = valor_uss.sum(axis=1)
    """
    st.code(codigo_python, language='python')

    # incluindo a coluna total nos dataframe
    quantidade_l["Total_quantidade"] = quantidade_l.sum(axis=1)
    valor_uss["Total_valor"] = valor_uss.sum(axis=1)

    st.dataframe(quantidade_l, use_container_width=True)
    st.dataframe(valor_uss, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    # criando dataframe com paises que não compraram vinho do brasil
    paises_comercio_zero = valor_uss[valor_uss['Total_valor'] == 0]
    paises_comercio_zero
    """
    st.code(codigo_python, language='python')

    # incluindo a coluna total nos dataframe
    paises_comercio_zero = valor_uss[valor_uss['Total_valor'] == 0]

    st.dataframe(paises_comercio_zero, use_container_width=True)

    #mostrando o meu código python dentro do meu layout
    codigo_python ="""
    # retirando dos dataframe quantidade_l e valor_uss os países que não compraram vinho com o brasil
    quantidade_l_s = quantidade_l.drop(paises_comercio_zero.index, axis=0)
    valor_uss_s = valor_uss.drop(paises_comercio_zero.index, axis=0)

    # ordenando por maior quantidade e maior valor
    quantidade_l_ordenado_por_total = quantidade_l_s.sort_values(by='Total_quantidade', ascending = False)
    valor_uss_s_ordenado_por_total = valor_uss_s.sort_values(by='Total_valor', ascending = False)
    
    # passo 1: retirando a coluna total dos dataframes
    quantidade_l_ordenado_por_total = quantidade_l_ordenado_por_total.drop('Total_quantidade', axis=1)
    valor_uss_s_ordenado_por_total = valor_uss_s_ordenado_por_total.drop('Total_valor', axis=1)

    # passo 2: criando um dataframe com 10 países que mais compraram vinho do brasil
    quantidade_l_ordenado_por_total_top10 = quantidade_l_ordenado_por_total.head(10)
    valor_uss_s_ordenado_por_total_top10 = valor_uss_s_ordenado_por_total.head(10)

    # passo 3: transpondo os dataframe para que seja possível visualizar a serie temporal
    quantidade_l_ordenado_por_total_top10 = quantidade_l_ordenado_por_total_top10.T
    valor_uss_s_ordenado_por_total_top10 = valor_uss_s_ordenado_por_total_top10.T

    # passo 4: mostrando os dataframes
    display(quantidade_l_ordenado_por_total_top10.head(2))
    display(valor_uss_s_ordenado_por_total_top10.head(2))
    """
    st.code(codigo_python, language='python')

    # retirando dos dataframe quantidade_l e valor_uss os países que não compraram vinho com o brasil
    quantidade_l_s = quantidade_l.drop(paises_comercio_zero.index, axis=0)
    valor_uss_s = valor_uss.drop(paises_comercio_zero.index, axis=0)

    # ordenando por maior quantidade e maior valor
    quantidade_l_ordenado_por_total = quantidade_l_s.sort_values(by='Total_quantidade', ascending = False)
    valor_uss_s_ordenado_por_total = valor_uss_s.sort_values(by='Total_valor', ascending = False)

    # passo 1: retirando a coluna total dos dataframes
    quantidade_l_ordenado_por_total = quantidade_l_ordenado_por_total.drop('Total_quantidade', axis=1)
    valor_uss_s_ordenado_por_total = valor_uss_s_ordenado_por_total.drop('Total_valor', axis=1)

    # passo 2: criando um dataframe com 10 países que mais compraram vinho do brasil
    quantidade_l_ordenado_por_total_top10 = quantidade_l_ordenado_por_total.head(10)
    valor_uss_s_ordenado_por_total_top10 = valor_uss_s_ordenado_por_total.head(10)

    # passo 3: transpondo os dataframe para que seja possível visualizar a serie temporal
    quantidade_l_ordenado_por_total_top10 = quantidade_l_ordenado_por_total_top10.T
    valor_uss_s_ordenado_por_total_top10 = valor_uss_s_ordenado_por_total_top10.T

    st.dataframe(quantidade_l_ordenado_por_total_top10, use_container_width=True)
    st.dataframe(valor_uss_s_ordenado_por_total_top10, use_container_width=True)

    

with tab2:
    st.write('### Estudo')

    fig, ax = plt.subplots(figsize=(10, 6))
    exportacao_long_por_pais.head(10).plot(kind='bar', ax=ax)
    st.pyplot(fig)

    st.write('Nos últimos 15 anos, o Brasil exportou 87.982.432 litros de vinho, totalizando o valor de U$$ 112.644.316,00. Os maiores consumidores de vinhos brasileiros são Paraguai e Rússia. Os 10 países que mais compraram do Brasil nos últimos 15 anos foram: Paraguai, Rússia, Estados Unidos, China, Reino Unido, Espanha, Países Baixos, Alemanha, Japão, Haiti')

    fig, ax = plt.subplots(figsize=(10, 6))
    exportacao_long_por_dolar_por_litro = exportacao_long_por_pais.head(10)
    exportacao_long_por_dolar_por_litro = exportacao_long_por_dolar_por_litro.sort_values(by='dolar_por_litro', ascending=False)
    exportacao_long_por_dolar_por_litro.head(5).plot(kind='bar', y='dolar_por_litro', ax=ax)

    st.pyplot(fig) 
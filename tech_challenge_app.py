# bibliotecas

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.display.float_format = '{:,.2f}'.format
import streamlit as st

st.write('# Tech Challenge Vinícola')

#Criando o layout da aplicação
tab0, tab1, tab2 = st.tabs(["Apresentação do negócio:", "Limpeza", "Análise inicial"])

with tab1:
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

    df_aux = pd.read_csv('codigo_iso-alpha_top10_paises_importadores_vinho.csv', sep=';', encoding='UTF-8')

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

    df_aux = pd.read_csv('codigo_iso-alpha_top10_paises_importadores_vinho.csv', sep=';', encoding='UTF-8')

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


with tab0:
    dados = pd.read_csv("ExpVinho.csv",encoding="utf-8-sig", sep=";",thousands=".", decimal=",")
    quantidade = ['País','2008','2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    df_quantidade = dados[quantidade].copy()
    dados2 = df_quantidade.set_index("País")
    dados2["Total"] = dados2.sum(axis=1)
    dados_ordenados = dados2.sort_values("Total", ascending=False)
    dados_mensal = dados_ordenados.drop(columns=["Total"])
    valores = ['País','2010.1', '2011.1', '2012.1', '2013.1', '2014.1', '2015.1', '2016.1', '2017.1', '2018.1', '2019.1', '2020.1', '2021.1', '2022.1']
    df_valores = dados[valores].copy()
    dados_valores2 = df_valores.set_index("País")
    dados_valores2["Total"] = dados_valores2.sum(axis=1)
    dados_ordenados_vl = dados_valores2.sort_values("Total", ascending=False)
    dados_mensal_vl = dados_ordenados_vl.drop(columns=["Total"])
    base_vl_qtd = pd.merge(dados_ordenados, dados_ordenados_vl, on='País')
    colunas_usaveis = ['Total_x', 'Total_y']
    base_totais = base_vl_qtd[colunas_usaveis].copy()
    base_totais["PPL"] = base_totais['Total_x']/base_totais['Total_y']
    quantidade_set = ['País','2008','2009','2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    df_quantidade_set = exportacao[quantidade].copy()
    qtd_set01 = df_quantidade.set_index("País")
    qtd_set01["Total"] = qtd_set01.sum(axis=1)
    qtd_set02 = qtd_set01.sort_values("Total", ascending=False)
    qtd_set03 = qtd_set02.drop(columns=["Total"])


    st.write('### Relatórios iniciais')
    st.markdown('<p style="text-align: center;"> Analisando os dados de exportação dos produtos da vinícola vitivinicultura, baseando-se nos últimos 15 anos e tendo como país de origem o Brasil. <br> Os países que lideram a exportação de vinhos dos anos em questão, com um montante em quantidade e valores expressivos como contribuintes do lucro brasileiro em vinhos são: Paraguai, Rússia, Estados Unidos, Reino Unido, China e Espanha. Estes são os países que estão em maior evidência como mostram os gráficos. <br>Obtivemos os seguintes pontos que consideramos relevantes e que destacamos de forma visual para uma leitura mais eficaz dos dados coletados conforme apresentado abaixo.</p>', unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)
    st.markdown("---")
    with col1:
        st.markdown('<br><br><br>', unsafe_allow_html=True) 
        st.markdown('<p style="text-align: center;">Este gráfico representa os cinco principais países que o Brasil exportou vinho nos últimos 15 anos, baseado no valor total de compra por país. É possível observar que o Paraguai se destaca com o valor total de exportação de vinhos comparado aos outros países. Em seguida temos a Rússia com um valor de compra superior a 15 milhões e o gráfico segue uma tendência decrescente a China que possui valor inferior comparado aos demais.</p>', unsafe_allow_html=True)

    with col2:
        cores = ['red', 'blue', 'pink', 'orange', 'yellow']
        grafico_vl = dados_ordenados_vl.head(5).plot( y='Total', kind='bar', color=cores, title='Valores Exportação Vinhos')
        fig1 = grafico_vl.get_figure()
        plt.xticks(rotation=45)
        st.pyplot(fig1)

    col3, col4 = st.columns(2)
    st.markdown("---")
    with col3:
        cores = ['red', 'blue', 'pink', 'orange', 'yellow']
        grafico1 = dados_ordenados.head(5).plot( y='Total', kind='bar', color=cores, title='Quantidade (Litros) Exportação Vinhos')
        fig1 = grafico1.get_figure()
        plt.xticks(rotation=45)
        st.pyplot(fig1)

    with col4:
        st.markdown('<br><br><br>', unsafe_allow_html=True) 
        st.markdown('<p style="text-align: center;">Ao lado temos a representação de exportação de vinhos do Brasil por quantidade em litros exportada entre os cinco principais países em nossa amostra de dados. Por essa medição a Rússia ultrapassa o Paraguai diferente do primeiro gráfico, concluindo-se que apesar do valor de compra do Paraguai ser superior, a Rússia em quantidades por litros é maior.</p>', unsafe_allow_html=True)

    col5, col6 = st.columns(2)
    st.markdown("---")
    with col5:
        st.markdown('<br><br><br>', unsafe_allow_html=True) 
        st.markdown('<p style="text-align: center;">O gráfico representa o valor exportado aos países por ano. É possível identificar que a Rússia se destaca em alguns períodos como maior cliente no ramo da exportação do Brasil e passa a dividir essa posicão com o Paraguai nos próximos anos.</p>', unsafe_allow_html=True)

    with col6:
        dados_ordenados2 = dados_mensal / 1000
        axis = dados_ordenados2.head(5).T.plot(figsize=(10, 6))
        fig = plt.gcf()  # Obtém a figura atual
        st.pyplot(fig)

    col7, col8 = st.columns(2)
    st.markdown("---")
    with col7:
        fig, ax = plt.subplots(figsize=(10, 6))
        exportacao_long_por_dolar_por_litro = exportacao_long_por_pais.head(10)
        exportacao_long_por_dolar_por_litro = exportacao_long_por_dolar_por_litro.sort_values(by='dolar_por_litro', ascending=False)
        exportacao_long_por_dolar_por_litro.head(5).plot(kind='bar', y='dolar_por_litro', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col8:
        st.markdown('<br><br><br>', unsafe_allow_html=True) 
        st.markdown('<p style="text-align: center;">Esse gráfico traz a visão de vendas mais lucrativas para o Brasil, analisando quantidade em dolar por litro fornecido aos países descritos no gráfico. O obtendo um lucro acima de 3.5 milhões de dólares pelo Reino Unido, como o maior contribuinte desse lucro, seguido dos Países baixos, Alemanha, Estados Unidos e Japão.</p>', unsafe_allow_html=True)

    col9, col10 = st.columns(2)
    st.markdown("---")
    with col9:
        st.markdown("<p style='text-align: center;'><br><br><br><br><br>Nos últimos 15 anos, o Brasil exportou 87.982.432 litros de vinho, totalizando o valor de U$$ 112.644.316,00.<br> Os maiores consumidores de vinhos brasileiros são Paraguai e Rússia. O gráfico representa a quantidade de exportação do total do Brasil em cada país por quantidade em litros e o valor em dólar. Os 10 países que mais compraram do Brasil nos últimos 15 anos foram: Paraguai, Rússia, Estados Unidos, China, Reino Unido, Espanha, Países Baixos, Alemanha, Japão, Haiti.</p>", unsafe_allow_html=True)

    with col10:
        fig, ax = plt.subplots(figsize=(5, 3))
        columns_to_plot = ['quantidade_l', 'valor_uss']
        bar_width = 1.2
        data = exportacao_long_por_pais.head(10)
        
        # Defina a largura das barras (ajuste o valor conforme necessário)
        data.plot(kind='bar', ax=ax, color=['blue', 'green'], width=bar_width)
        
        ax.legend(labels=['Quantidade (litros)', 'Valor (em US$)'])
        ax.set_xticklabels(data.index, rotation=45, fontsize=5)
        st.pyplot(fig)

    col11, col12 = st.columns(2)
    st.markdown("---")

    with col11:
        qtd_set04 = qtd_set03 / 1000
        fig, ax = plt.subplots(figsize=(10, 6))
        qtd_set04.head(5).T.plot(kind='line', ax=ax, title='Exportação')
        ax.axhline(y=5900, color='r', linestyle='-')
        st.pyplot(fig)

    with col12:
        st.markdown("<p style='text-align: center;'><br><br>O gráfico representa o valor exportado aos países por ano. É possível identificar que a representatividade da Rússia nos gráficos anteriores é devido aos picos de compras ocorridos entre os anos 2008-2010 e 2011-2014 como é possível visualizar ao lado. Se estabiliza após a queda e se mantém em uma linha linear de exportação, enquanto o Paraguai tem uma crescente a partir de 2016 e que se mantém em um aumento gradativo até o ano de 2022. Um país com grande potencial podemos ter de ganho para exportação de vinho no Brasil.</p>", unsafe_allow_html=True)
    
    
    st.markdown("<p style='text-align: center;'><br><br>Conclusão dos estudos comparativos dos dados onde construímos nossa análise, foi que o Brasil lucra um valor total na exportação em vinícolas de 87.982.432 litros de vinho, totalizando o valor de U$$ 112.644.316,00. Entre os países de maior índice de exportação e importação sugerimos o Paraguai como melhor opção para investimento do Brasil para lucros no mercado de exportação, pela sua tendência crescente e continua ao longo dos anos e pela escassez de importação devido à falta de produtos brutos para comercio de vinho no país. </p>", unsafe_allow_html=True)

    
    
    
 
st.markdown("# Integrantes do grupo")
st.markdown("* Ariane Santana Barros - rm352052")
st.markdown("* Lana Morgado Martinez - rm349562")
st.markdown("* Paula Pereira dos Santos - Rm350669")
st.markdown("* Talita Silvestre Matias de Oliveira - rm352443")
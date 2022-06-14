import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import streamlit as st
import time
import datetime

plt.rcParams['figure.figsize'] = [13,5]

# Função para plotar a imagem
def plot_image(dados, month, equipment):
    fig, ax = plt.subplots()
    legenda_grafico = ['> 2000 mGy', "<2000 mGy"]
    ax.pie(dados, labels = legenda_grafico, autopct='%.2f%%')
    ax.set_title(f'Indicadores geral {month} {datetime.date.today().year} - {equipment}', fontsize=14)
    ax.legend(title = 'Kerma Acumulado (mGy)', bbox_to_anchor=(1, 0, 0.5, 1),
              shadow = True, fontsize = 10, title_fontsize = 12)
    fig.savefig('Graficos\Doses acumuladas 01 - Siemens Artis One.png', dpi = 100)
    
    return fig

def plot_dose_intervalado(df, dados, month, equipment):
    fig, ax = plt.subplots()
    legenda_intervalada = [' DOSES < 300 mGy', 'DOSES > 300 mGy e < 500 mGy',
                                  'DOSES > 500 mGy e < 1000 mGy',
                                  'DOSES > 1000 mGy e < 1500 mGy',
                                  'DOSES > 1500 mGy e < 2000 mGy',
                                  'DOSES > 2000 mGy e < 4000 mGy',
                                  'DOSES > 4000 mGy']
    ax.pie(dados, labels = legenda_intervalada, autopct='%.2f%%', colors =["#97EB6E", "#297305", "#285ECB", "#EBF258", "#C7CF22", 
                                                                           "#DF4B44", "#BB0B03"])
    ax.set_title(f'Indicadores geral {month} {datetime.date.today().year} - {equipment}', fontsize=14)
    ax.legend(title = f'Indicador Geral - {equipment} \n \nNúmero de procedimentos realizados: {len(df.kerma)}',
              bbox_to_anchor=(1.65, 0.09, 0.5, 1),
              shadow = True, fontsize = 10, title_fontsize = 12)
    fig.savefig('Graficos\Doses acumuladas 02 - Siemens Artis One.png', dpi = 100)
    
    return fig

def plot_pka(df, dados, month, equipment):
    fig,ax = plt.subplots()
    legenda_pka = [' Pka < 300 Gy.cm2', 'Pka > 300 Gy.cm2 e < 500 Gy.cm2',
                      'Pka > 500 Gy.cm2']
    plt.pie(dados, labels = legenda_pka, colors = ["#97EB6E", "#297305", "#285ECB", "#EBF258", "#C7CF22", 
                                                                           "#DF4B44", "#BB0B03"], autopct='%.2f%%')
    plt.legend(title = f'Indicador Geral - {equipment} (Pka) \nNúmero de procedimentos realizados: {len(df.pka)}',
               bbox_to_anchor=(1.55, 0, 0.5, 1), shadow = True, fontsize = 10, title_fontsize = 12)
    plt.title(f'PKA Procedimento {month} {datetime.date.today().year} - {equipment}', fontsize = 14)
    fig.savefig('Graficos\PKA - Siemens Artis One.png', dpi = 100)
    return fig

def app():
    equipamento = st.session_state['siemens']
    st.title(f'Indicadores gerais do equipamento: {equipamento}')
    mes = st.selectbox('Qual mês os indicadores serão gerados?', ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                                                                 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
    tabela_hscn1 = st.file_uploader(f'Selecione a tabela de dados referete ao mês: {mes}',
                                  help = 'A tabela de dados precisa ser formatada!')
    if tabela_hscn1 is None:
        st.warning('Selecione a tabela para começar')
    
    else: 
        sala_siemens = pd.read_excel(tabela_hscn1, header = [0], sheet_name=1)
        sala_siemens = sala_siemens.astype(str)
        checkbox = st.checkbox(f'Ver tabela dos dados do equipamento {equipamento}')
        if checkbox:
            st.write(sala_siemens)
        
        st.write('### Dashboard para os indicadores')
        mapa = {"DATA" : "data",
               "REGISTRO PACIENTE" : "registro_paciente",
               "NOME DO PACIENTE": "nome_paciente",
               "PROCEDIMENTO ": "procedimento",
               "PROTOCOLO UTILIZADO ": "protocolo_utilizado",
               "FLUORO": "fluoro",
               "FRAMES CINE  (FPS)": "fps",
               "TEMPO TOTAL FLUORO (min)": "tempo_fluoro",
               "KERMA ACUMULADO (mGy)": "kerma",
               "PRODUTO KERMA ÁREA (mGycm^2)": "pka"}

        sala_siemens.rename(columns = mapa, inplace = True)
        df_siemens = sala_siemens

        # Dados para Gráfico 01

        maior_dose = []
        menor_dose = []

        siemens = [float(x) for x in df_siemens.kerma]
        for i in siemens:
            if i >= 2000:
                maior_dose.append(i)
            else:
                menor_dose.append(i)

        dados_kerma = [len(maior_dose), len(menor_dose)]

        range_um = []
        range_dois = []
        range_tres = []
        range_quatro = []
        range_cinco = []
        range_seis = []
        range_sete = []

        for i in siemens:
            if i < 300:
                range_um.append(i)
            elif i >= 300 and i < 500:
                range_dois.append(i)
            elif i>= 500 and i < 1000:
                range_tres.append(i)
            elif i>= 1000 and i < 1500:
                range_quatro.append(i)
            elif i>= 1500 and i < 2000:
                range_cinco.append(i)
            elif i >= 2000 and i < 4000:
                range_seis.append(i)
            elif i > 4000:
                range_sete.append(i)
            else:
                print('Erro.')

        dados_kerma_intervalado = [len(range_um), len(range_dois), len(range_tres), len(range_quatro), len(range_cinco), len(range_seis),
                                       len(range_sete)]

        siemens_pka = [float(x) / 100 for x in df_siemens.pka]
        
        
        pka_300 = []
        pka_300_500 = []
        pka_500 = []

        for j in siemens_pka:
            if j < 300:
                pka_300.append(j)
            elif j >= 300 and j < 500:
                pka_300_500.append(j)
            elif j >=500:
                pka_500.append(j)
        
        dados_pka = [len(pka_300), len(pka_300_500), len(pka_500)]
        
        # Visualizando gráficos
        st.markdown('### Gráficos - Doses Pacientes')
        
        c1,c2 = st.columns([1,2])
        with c1:
            st.write(plot_image(dados_kerma, mes, equipamento))
            st.write(plot_pka(df_siemens, dados_pka, mes, equipamento))
            
        with c2:
            st.write(plot_dose_intervalado(df_siemens, dados_kerma_intervalado, mes, equipamento))
            
        button_export_graph = st.button('Exportar gráficos')
        
        if button_export_graph:
            with st.spinner('Exportando gráficos...'):
                time.sleep(1.5)
            st.success('Gráficos salvos com sucesso!')

    
    
    
        
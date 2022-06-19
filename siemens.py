import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import streamlit as st
import time
import datetime

plt.rcParams['figure.figsize'] = [13,5]

# Função para plotar a imagem
def plot_image(dados, month, equipment, procedimento):
    fig, ax = plt.subplots()
    legenda_grafico = ['> 2000 mGy', "<2000 mGy"]
    ax.pie(dados, labels = legenda_grafico, autopct='%.2f%%')
    ax.set_title(f'Indicadores {procedimento} {month} {datetime.date.today().year} \n{equipment}', fontsize=14)
    ax.legend(title = 'Kerma Acumulado (mGy)', bbox_to_anchor=(1, 0, 0.5, 1),
              shadow = True, fontsize = 10, title_fontsize = 12)
    fig.savefig(f'Graficos\Siemens Artis One\Doses {procedimento} - Siemens Artis One.png', dpi = 100)
    
    return fig

def plot_dose_intervalado(df, dados, month, equipment, procedimento):
    fig, ax = plt.subplots()
    legenda_intervalada = [' DOSES < 300 mGy', 'DOSES > 300 mGy e < 500 mGy',
                                  'DOSES > 500 mGy e < 1000 mGy',
                                  'DOSES > 1000 mGy e < 1500 mGy',
                                  'DOSES > 1500 mGy e < 2000 mGy',
                                  'DOSES > 2000 mGy e < 4000 mGy',
                                  'DOSES > 4000 mGy']
    ax.pie(dados, labels = legenda_intervalada, autopct='%.2f%%', colors =["#97EB6E", "#297305", "#285ECB", "#EBF258", "#C7CF22", 
                                                                           "#DF4B44", "#BB0B03"])
    ax.set_title(f'Indicadores {procedimento} {month} {datetime.date.today().year} \n {equipment}', fontsize=14)
    ax.legend(title = f'Indicador {procedimento} {equipment} \n \nNúmero de procedimentos realizados: {len(df.kerma)}',
              bbox_to_anchor=(1.65, 0.09, 0.5, 1),
              shadow = True, fontsize = 10, title_fontsize = 12)
    fig.savefig(f'Graficos\Siemens Artis One\Doses {procedimento} intervalada - Siemens Artis One.png', dpi = 100)
    
    return fig

def plot_pka(df, dados, month, equipment, procedimento):
    fig,ax = plt.subplots()
    legenda_pka = [' Pka < 300 Gy.cm2', 'Pka > 300 Gy.cm2 e < 500 Gy.cm2',
                      'Pka > 500 Gy.cm2']
    plt.pie(dados, labels = legenda_pka, colors = ["#97EB6E", "#297305", "#285ECB", "#EBF258", "#C7CF22", 
                                                                           "#DF4B44", "#BB0B03"], autopct='%.2f%%')
    plt.legend(title = f'Indicador {procedimento} - {equipment} (Pka) \nNúmero de procedimentos realizados: {len(df.pka)}',
               bbox_to_anchor=(1.55, 0, 0.5, 1), shadow = True, fontsize = 10, title_fontsize = 12)
    plt.title(f'PKA Procedimento {procedimento} {month} {datetime.date.today().year} \n {equipment}', fontsize = 14)
    fig.savefig(f'Graficos\Siemens Artis One\PKA {procedimento} - Siemens Artis One.png', dpi = 100)
    return fig

def gerando_indicadores(dados):

    maior_dose = []
    menor_dose = []

    philips = [float(x) for x in dados.kerma]
    for i in philips:
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

    for i in philips:
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

    philips_pka = [float(x) / 1000 for x in dados.pka]


    pka_300 = []
    pka_300_500 = []
    pka_500 = []

    for j in philips_pka:
        if j < 300:
            pka_300.append(j)
        elif j >= 300 and j < 500:
            pka_300_500.append(j)
        elif j >=500:
            pka_500.append(j)

    dados_pka = [len(pka_300), len(pka_300_500), len(pka_500)]
    
    return dados_kerma, dados_kerma_intervalado, dados_pka


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
            
        st.write("---")
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
        
        lista_protocolo = list(df_siemens.protocolo_utilizado)
        for i in range(len(lista_protocolo)):
            if lista_protocolo[i][0] == 'C':
                lista_protocolo[i] = 'Cardio'
                
            elif lista_protocolo[i][0] == 'V':
                lista_protocolo[i] = 'Vascular'
                
            elif lista_protocolo[i][0] == 'N':
                lista_protocolo[i] = 'Neurologia'
                
            elif lista_protocolo[i][0] == 'Q':
                lista_protocolo[i] = 'Quimio'
                
        df_siemens.protocolo_utilizado = lista_protocolo
        df_siemens.protocolo_utilizado = df_siemens.protocolo_utilizado.str.upper()
        
        cardio_siemens = df_siemens[df_siemens.protocolo_utilizado == 'CARDIO']
        vascular_siemens = df_siemens[df_siemens.protocolo_utilizado == 'VASCULAR']
        neuro_siemens = df_siemens[df_siemens.protocolo_utilizado == 'NEUROLOGIA']
        quimio_siemens = df_siemens[df_siemens.protocolo_utilizado == 'QUIMIO']
        
        lista_protocolos_utilizados = list(df_siemens.protocolo_utilizado.unique())
        lista_protocolos_utilizados.insert(0,'Selecione uma opção')
        
        # Visualizando gráficos
        st.markdown('### Gráficos - Doses Pacientes')
        options_procedimentos = st.selectbox('Selecione o procedimento utilizado:', lista_protocolos_utilizados)
        if options_procedimentos == 'Selecione uma opção':
            st.warning('Nenhum procedimento selecionado')
            
        elif options_procedimentos == 'CARDIO':
            # Filtrando por procedimento 
            a, b, c = gerando_indicadores(cardio_siemens)
            
            c1,c2 = st.columns([1,2])
            with c1:
                st.write(plot_image(a, mes, equipamento, options_procedimentos))
            
                st.write(plot_pka(cardio_siemens, c, mes, equipamento, options_procedimentos))
            
            with c2:
                st.write(plot_dose_intervalado(cardio_siemens, b, mes, equipamento, options_procedimentos))

            button_export_graph = st.button('Exportar gráficos')

            if button_export_graph:

                with st.spinner('Exportando gráficos...'):
                    time.sleep(1.5)
                st.success('Gráficos salvos com sucesso!')
                      
        elif options_procedimentos == 'VASCULAR':  
            vasc1, vasc2, vasc3 = gerando_indicadores(vascular_siemens)
            
            c1,c2 = st.columns([1,2])
            with c1:
                st.write(plot_image(vasc1, mes, equipamento, options_procedimentos))
            
                st.write(plot_pka(vascular_siemens, vasc3, mes, equipamento, options_procedimentos))
            
            with c2:
                st.write(plot_dose_intervalado(vascular_siemens, vasc2, mes, equipamento, options_procedimentos))

            button_export_graph = st.button('Exportar gráficos')

            if button_export_graph:

                with st.spinner('Exportando gráficos...'):
                    time.sleep(1.5)
                st.success('Gráficos salvos com sucesso!')
                
        elif options_procedimentos == 'NEUROLOGIA':  
            neuro1, neuro2, neuro3 = gerando_indicadores(neuro_siemens)
            
            c1,c2 = st.columns([1,2])
            with c1:
                st.write(plot_image(neuro1, mes, equipamento, options_procedimentos))
            
                st.write(plot_pka(neuro_siemens, neuro3, mes, equipamento, options_procedimentos))
            
            with c2:
                st.write(plot_dose_intervalado(neuro_siemens, neuro2, mes, equipamento, options_procedimentos))

            button_export_graph = st.button('Exportar gráficos')

            if button_export_graph:

                with st.spinner('Exportando gráficos...'):
                    time.sleep(1.5)
                st.success('Gráficos salvos com sucesso!')
                
        elif options_procedimentos == 'QUIMIO':  
            quimio1, quimio2, quimio3 = gerando_indicadores(quimio_siemens)
            
            c1,c2 = st.columns([1,2])
            with c1:
                st.write(plot_image(quimio1, mes, equipamento, options_procedimentos))
            
                st.write(plot_pka(quimio_siemens, quimio3, mes, equipamento, options_procedimentos))
            
            with c2:
                st.write(plot_dose_intervalado(quimio_siemens, quimio2, mes, equipamento, options_procedimentos))

            button_export_graph = st.button('Exportar gráficos')

            if button_export_graph:

                with st.spinner('Exportando gráficos...'):
                    time.sleep(1.5)
                st.success('Gráficos salvos com sucesso!')
                
        st.write('---')
        st.markdown(f"### Número total de procedimentos no {equipamento} em {mes}")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Cardiologia", f"{len(cardio_siemens)}")
        col2.metric("Vascular", f"{len(vascular_siemens)}")
        col3.metric("Outros", f"{len(neuro_siemens) + len(quimio_siemens)}")
        col4.metric("Total", f"{len(df_siemens)}")
        st.markdown(f"### Número de procedimentos no {equipamento} em {mes} por médico")
    

    
    
    
        
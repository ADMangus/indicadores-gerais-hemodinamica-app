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
    ax.set_title(f'Indicadores {procedimento} {month} {datetime.date.today().year} - {equipment}', fontsize=14)
    ax.legend(title = 'Kerma Acumulado (mGy)', bbox_to_anchor=(1, 0, 0.5, 1),
              shadow = True, fontsize = 10, title_fontsize = 12)
    
    fig.savefig(f'Graficos\Philips\Doses {procedimento} - Philips.png', dpi = 100)
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
    ax.legend(title = f'Indicador {procedimento} - {equipment} (Doses Pacientes) \nNúmero de procedimentos realizados: {len(df.kerma)}',
              bbox_to_anchor=(1.65, 0.1, 0.5, 1),
              shadow = True, fontsize = 10, title_fontsize = 12)
    fig.savefig(f'Graficos\Philips\Doses {procedimento} intervalada - Philips.png', dpi = 100)
    
    return fig

def plot_pka(df, dados, month, equipment, procedimento):
    fig,ax = plt.subplots()
    legenda_pka = [' Pka < 300 Gy.cm2', 'Pka > 300 Gy.cm2 e < 500 Gy.cm2',
                      'Pka > 500 Gy.cm2']
    plt.pie(dados, labels = legenda_pka, colors = ["#97EB6E", "#297305", "#285ECB", "#EBF258", "#C7CF22", 
                                                                           "#DF4B44", "#BB0B03"], autopct='%.2f%%')
    plt.legend(title = f'Indicador {procedimento} - {equipment} (Pka) \nNúmero de procedimentos realizados: {len(df.pka)}',
               bbox_to_anchor=(1.55, 0, 0.5, 1), shadow = True, fontsize = 10, title_fontsize = 12)
    plt.title(f'PKA Procedimento {procedimento} {month} {datetime.date.today().year} - {equipment}', fontsize = 14)
    fig.savefig(f'Graficos\Philips\PKA {procedimento} - Philips.png', dpi = 100)
    return fig

def plot_medicos(dados, month, equipment, procedimento, medico):
    fig, ax = plt.subplots()
    legenda_grafico = ['> 2000 mGy', "<2000 mGy"]
    ax.pie(dados, labels = legenda_grafico, autopct='%.2f%%')
    ax.set_title(f'Indicadores {procedimento} {month} {datetime.date.today().year} \n{equipment}: {medico}', fontsize=14)
    ax.legend(title = 'Kerma Acumulado (mGy)', bbox_to_anchor=(1, 0, 0.5, 1),
              shadow = True, fontsize = 10, title_fontsize = 12)
    fig.savefig(f'Graficos\Philips\Doses {procedimento} {medico} - Philips.png', dpi = 100)
    
    return fig

def plot_pka_medicos(aa, dados, month, equipment, procedimento, medico):
    fig,ax = plt.subplots()
    legenda_pka = [' Pka < 300 Gy.cm2', 'Pka > 300 Gy.cm2 e < 500 Gy.cm2',
                      'Pka > 500 Gy.cm2']
    plt.pie(dados, labels = legenda_pka, colors = ["#97EB6E", "#297305", "#285ECB", "#EBF258", "#C7CF22", 
                                                                           "#DF4B44", "#BB0B03"], autopct='%.2f%%')
    plt.legend(title = f'Indicador {procedimento} - {equipment} (Pka) \nNúmero de procedimentos realizados: {len(aa.pka)}',
               bbox_to_anchor=(1.55, 0, 0.5, 1), shadow = True, fontsize = 10, title_fontsize = 12)
    plt.title(f'PKA Procedimento {procedimento} {month} {datetime.date.today().year} \n {equipment}', fontsize = 14)
    fig.savefig(f'Graficos\Philips\PKA {procedimento} {medico} - Philips.png', dpi = 100)
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
    equipamento = st.session_state['philips']
    st.title(f'Indicadores gerais do equipamento: {equipamento}')
    #st.info('Prestar atenção para importar a tabela correta do equipamento')
    mes = st.selectbox('Qual mês os indicadores serão gerados?', ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                                                                 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
    
    
    tabela_hscn = st.file_uploader(f'Selecione a tabela de dados referete ao mês: {mes}',
                                  help = 'A tabela de dados precisa ser formatada!')
    if tabela_hscn is None:
        st.warning('Selecione a tabela para começar')
    
    else: 
        
        sala_philips = pd.read_excel(tabela_hscn, header = [0], sheet_name=1)
        sala_philips = sala_philips.astype(str)
        checkbox = st.checkbox(f'Ver tabela dos dados do equipamento {equipamento}')
        if checkbox:
            st.write(sala_philips)
        
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
               "PRODUTO KERMA ÁREA (mGycm^2)": "pka",
               "MÉDICO EXECUTOR": "medico"}

        sala_philips.rename(columns = mapa, inplace = True)
        df_philips = sala_philips
        
        lista_protocolo = list(df_philips.protocolo_utilizado)
        for i in range(len(lista_protocolo)):
            if lista_protocolo[i][0] == 'C':
                lista_protocolo[i] = 'Cardio'
                
            elif lista_protocolo[i][0] == 'V':
                lista_protocolo[i] = 'Vascular'
        
        df_philips.protocolo_utilizado = lista_protocolo
        df_philips.protocolo_utilizado = df_philips.protocolo_utilizado.str.upper()
        
        cardio_philips = df_philips[df_philips.protocolo_utilizado == 'CARDIO']
        vascular_philips = df_philips[df_philips.protocolo_utilizado == 'VASCULAR']
        
        lista_protocolos_utilizados = list(df_philips.protocolo_utilizado.unique())
        lista_protocolos_utilizados.insert(0,'Selecione uma opção')
        
        # Visualizando gráficos
        st.markdown('### Gráficos - Doses Pacientes')
        
        options_procedimentos = st.selectbox('Selecione o procedimento utilizado:', lista_protocolos_utilizados)
        if options_procedimentos == 'Selecione uma opção':
            st.warning('Nenhum procedimento selecionado')
            
        elif options_procedimentos == 'CARDIO':
            # Filtrando por procedimento 
            a, b, c = gerando_indicadores(cardio_philips)
            
            c1,c2 = st.columns([1,2])
            with c1:
                st.write(plot_image(a, mes, equipamento, options_procedimentos))
            
                st.write(plot_pka(cardio_philips, c, mes, equipamento, options_procedimentos))
            
            with c2:
                st.write(plot_dose_intervalado(cardio_philips, b, mes, equipamento, options_procedimentos))

            button_export_graph = st.button('Exportar gráficos')

            if button_export_graph:

                with st.spinner('Exportando gráficos...'):
                    time.sleep(1.5)
                st.success('Gráficos salvos com sucesso!')
                      
        elif options_procedimentos == 'VASCULAR':  
            vasc1, vasc2, vasc3 = gerando_indicadores(vascular_philips)
            
            c1,c2 = st.columns([1,2])
            with c1:
                st.write(plot_image(vasc1, mes, equipamento, options_procedimentos))
            
                st.write(plot_pka(vascular_philips, vasc3, mes, equipamento, options_procedimentos))
            
            with c2:
                st.write(plot_dose_intervalado(vascular_philips, vasc2, mes, equipamento, options_procedimentos))

            button_export_graph = st.button('Exportar gráficos')

            if button_export_graph:

                with st.spinner('Exportando gráficos...'):
                    time.sleep(1.5)
                st.success('Gráficos salvos com sucesso!')
                
        st.write('---')
        st.markdown(f"### Número total de procedimentos no {equipamento} em {mes}")
        col1, col2, col3 = st.columns(3)
        col1.metric("Cardiologia", f"{len(cardio_philips)}")
        col2.metric("Vascular", f"{len(vascular_philips)}")
        col3.metric("Total", f"{len(df_philips)}")
        #------------------------------------------------------------------------------------------
        st.markdown(f"### Número de procedimentos no {equipamento} em {mes} por médico")
        medicos_cardiologia = ['Azmus', 'Bruno', 'Mascarenhas', 'Fabio', 'Beltrame']
        id_cardiologia = np.arange(1,6)
        medicos_radiologia = ['Medronha', 'Fernando', 'Silvio', '', '']
        id_radiologia = [6,7,8, 0, 0]
        medicos_neurologia = ['Raupp', 'Gabriel', 'Marcio', '', '']
        id_neurologia = [9,10,11,0,0]
        medicos_vascular = ['Joel', 'Jean', 'Pezzela', 'Berger', 'Argenta']
        id_vascular = np.arange(12,17)
        
        medicos = pd.DataFrame({'Cardiologia': medicos_cardiologia,
                        'id_cardiologia': id_cardiologia,
                        'Radiologia': medicos_radiologia,
                        'id_radiologia': id_radiologia,
                        'Neurologia': medicos_neurologia,
                        'id_neurologia': id_neurologia,
                        'Vascular': medicos_vascular,
                       'id_vascular': id_vascular})
        
        tabela_geral = st.checkbox('Mostrar legenda')
        if tabela_geral:
            st.write(medicos)
            
        lista_cardio_filtrada = list(cardio_philips.medico.unique())
        lista_cardio_filtrada.insert(0,'Selecione uma opção')
        lista_vascular_filtrada = list(vascular_philips.medico.unique())
        lista_vascular_filtrada.insert(0,'Selecione uma opção')
        
        procedimento = st.selectbox('Selecione o procedimento que deseja obter informações', lista_protocolos_utilizados)
        if procedimento == 'Selecione uma opção':
            st.warning('Selecione o procedimento')
        elif procedimento == 'CARDIO':
            medico_selecionado = st.selectbox('Selecione o médico que deseja obter infomações', lista_cardio_filtrada)
            if medico_selecionado == '1.0':
                st.markdown(f"### Indicadores do médico: {medicos.Cardiologia[0]}")
                df = cardio_philips[cardio_philips.medico == '1.0']
                st.write(df)
                azmus_kerma, a, azmus_pka = gerando_indicadores(df)
                st.write(plot_medicos(azmus_kerma, mes, equipamento,procedimento ,medicos.Cardiologia[0]))
                st.write(plot_pka_medicos(df, azmus_pka, mes, equipamento,procedimento ,medicos.Cardiologia[0]))
                
            elif medico_selecionado == '2.0':
                st.markdown(f"### Indicadores do médico: {medicos.Cardiologia[1]}")
                df = cardio_philips[cardio_philips.medico == '2.0']
                st.write(df)
                bruno_kerma, b, bruno_pka = gerando_indicadores(df)
                st.write(plot_medicos(bruno_kerma, mes, equipamento,procedimento ,medicos.Cardiologia[1]))
                st.write(plot_pka_medicos(df, bruno_pka, mes, equipamento,procedimento ,medicos.Cardiologia[1]))
                
            elif medico_selecionado == '3.0':
                st.markdown(f"### Indicadores do médico: {medicos.Cardiologia[2]}")
                df = cardio_philips[cardio_philips.medico == '3.0']
                st.write(df)
                mascarenhas_kerma, c, mascarenhas_pka = gerando_indicadores(df)
                st.write(plot_medicos(mascarenhas_kerma, mes, equipamento,procedimento ,medicos.Cardiologia[2]))
                st.write(plot_pka_medicos(df,mascarenhas_pka, mes, equipamento,procedimento ,medicos.Cardiologia[2]))
        
            elif medico_selecionado == '4.0':
                st.markdown(f"### Indicadores do médico: {medicos.Cardiologia[3]}")
                df = cardio_philips[cardio_philips.medico == '4.0']
                st.write(df)
                fabio_kerma, d, fabio_pka = gerando_indicadores(df)
                st.write(plot_medicos(fabio_kerma, mes, equipamento,procedimento ,medicos.Cardiologia[3]))
                st.write(plot_pka_medicos(df, fabio_pka, mes, equipamento,procedimento ,medicos.Cardiologia[3]))
        
            elif medico_selecionado == '5.0':
                st.markdown(f"### Indicadores do médico: {medicos.Cardiologia[4]}")
                df = cardio_philips[cardio_philips.medico == '5.0']
                st.write(df)
                beltrame_kerma, e, beltrame_pka = gerando_indicadores(df)
                st.write(plot_medicos(beltrame_kerma, mes, equipamento,procedimento ,medicos.Cardiologia[4]))
                st.write(plot_pka_medicos(df, beltrame_pka, mes, equipamento,procedimento ,medicos.Cardiologia[4]))
                
            elif medico_selecionado == 'Selecione uma opção':
                st.warning('Selecione o médico')
                
            else: 
                st.error('Médico não encontrado')
            
            
        elif procedimento == 'VASCULAR':
            medico_selecionado = st.selectbox('Selecione o médico que deseja obter infomações', vascular_philips.medico.unique())
            if medico_selecionado == '12.0':
                st.markdown(f"### Indicadores do médico: {medicos.Vascular[0]}")
                df = vascular_philips[vascular_philips.medico == '12.0']
                st.write(df)
                joel_kerma, f, joel_pka = gerando_indicadores(df)
                st.write(plot_medicos(joel_kerma, mes, equipamento,procedimento ,medicos.Vascular[0]))
                st.write(plot_pka_medicos(df, joel_pka, mes, equipamento,procedimento ,medicos.Vascular[0]))
                
            elif medico_selecionado == '13.0':
                st.markdown(f"### Indicadores do médico: {medicos.Vascular[1]}")
                df = vascular_philips[vascular_philips.medico == '13.0']
                st.write(df)
                jean_kerma, g, jean_pka = gerando_indicadores(df)
                st.write(plot_medicos(jean_kerma, mes, equipamento,procedimento ,medicos.Vascular[1]))
                st.write(plot_pka_medicos(df, jean_pka, mes, equipamento,procedimento ,medicos.Vascular[1]))
                
            elif medico_selecionado == '14.0':
                st.markdown(f"### Indicadores do médico: {medicos.Vascular[2]}")
                df = vascular_philips[vascular_philips.medico == '14.0']
                st.write(df)
                pezzela_kerma, h, pezzela_pka = gerando_indicadores(df)
                st.write(plot_medicos(pezzela_kerma, mes, equipamento,procedimento ,medicos.Vascular[2]))
                st.write(plot_pka_medicos(df, pezzela_pka, mes, equipamento,procedimento ,medicos.Vascular[2]))
                
            elif medico_selecionado == '15.0':
                st.markdown(f"### Indicadores do médico: {medicos.Vascular[3]}")
                df = vascular_philips[vascular_philips.medico == '15.0']
                st.write(df)
                berger_kerma, i, berger_pka = gerando_indicadores(df)
                st.write(plot_medicos(berger_kerma, mes, equipamento,procedimento ,medicos.Vascular[3]))
                st.write(plot_pka_medicos(df, berger_pka, mes, equipamento,procedimento ,medicos.Vascular[3]))
                
            elif medico_selecionado == '16.0':
                st.markdown(f"### Indicadores do médico: {medicos.Vascular[4]}")
                df = vascular_philips[vascular_philips.medico == '16.0']
                st.write(df)
                argenta_kerma, j, argenta_pka = gerando_indicadores(df)
                st.write(plot_medicos(argenta_kerma, mes, equipamento,procedimento ,medicos.Vascular[4]))
                st.write(plot_pka_medicos(df, argenta_pka, mes, equipamento,procedimento ,medicos.Vascular[4]))
                
            elif medico_selecionado == 'Selecione uma opção':
                st.warning('Selecione o médico')
                
            else: 
                st.error('Médico não encontrado')

    
    
    
        
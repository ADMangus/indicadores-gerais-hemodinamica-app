import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import streamlit as st
import time
from PIL import Image

def app():
    st.title('Página Inicial')
    
    st.write('### Seja Bem-vindo')
    st.write(''' Para iniciar uso da ferramenta é preciso cadastrar o nome do Cliente, com a finalidade do preenchimento do relatório final para os indicadores de dose do serviço de Hemodinâmica.
        
    ''')
    form = st.form(key='my_form', clear_on_submit=True)
    cliente = form.text_input('Digite o nome do cliente',
                              help='Digite o nome por extenso!',
                              placeholder = 'Digite aqui')
    cod = form.text_input('Digite o código do cliente', 
                         placeholder = 'Digite o número do cliente aqui')
    
    arquivo = st.session_state['diretorio'] + st.session_state['cadastro']
    
    save_button = form.form_submit_button('Salvar dados')
    
    if save_button: 
        
        graficos_philips = f'{st.session_state.graficos}\Philips'
        graficos_siemens = f'{st.session_state.graficos}\Siemens Artis One'
        
        try: 
            os.makedirs(st.session_state['graficos'],  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
            
        try: 
            os.makedirs(graficos_philips,  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
            
        try: 
            os.makedirs(graficos_siemens,  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
            
        try: 
            os.makedirs(st.session_state['relatorio'],  exist_ok = True)
        except OSError as error:
            st.write('Diretório não pode ser criado')
        
        
        df = pd.read_csv(arquivo, sep=";")
        df.loc[len(df.index)] = [cod, cliente]
        df.to_csv(arquivo, sep=";",index=False)
        
        with st.spinner('Carregando...'):
            time.sleep(1.2)
        st.success('Informações preenchidas e salvas com sucesso!')
        
        
    
    
    
   
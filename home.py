import Hemo
import siemens
import philips
import relatorio
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import streamlit as st
import datetime

from configparser import ConfigParser

#Layout
st.set_page_config(layout="wide")

config = ConfigParser()
config.read("hsnc.ini")
nome_equipamento_philips = config['lista_equipamentos']['philips']
nome_equipamento_siemens = config['lista_equipamentos']['siemens']
g = config['path']['path_graph']
relat = config['path']['path_relatorio']
img = config['path']['imagem']
dire = config['path']['diretorio']
cadastro_clientes = config['lista_equipamentos']['cadastro_clientes']


if 'philips'  not in st.session_state:
    st.session_state['philips'] = nome_equipamento_philips
    
if 'siemens'  not in st.session_state:
    st.session_state['siemens'] = nome_equipamento_siemens

if 'imagem' not in st.session_state:
    st.session_state['imagem'] = img
    
if 'graficos' not in st.session_state:
    st.session_state['graficos'] = g
    
if 'relatorio' not in st.session_state:
    st.session_state['relatorio'] = relat
    
if 'diretorio' not in st.session_state:
    st.session_state['diretorio'] = dire
    
if 'cadastro' not in st.session_state:
    st.session_state['cadastro'] = cadastro_clientes
 

PAGES = { "Página Inicial": Hemo,
         "Siemens Artis One": siemens,
         "Philips": philips,
         "Exportar Relatório": relatorio
}

st.sidebar.title('Navegação')
selection = st.sidebar.selectbox("Qual equipamento você deseja?", list(PAGES.keys()))
st.sidebar.markdown("""---""")
st.sidebar.info('Desenvolvido por Arthur D. Mangussi')

    
page = PAGES[selection]
page.app()








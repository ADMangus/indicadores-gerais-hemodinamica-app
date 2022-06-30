import aspose.words as aw
import streamlit as st
import datetime
import time
import pandas as pd
import aspose.pydrawing as drawing

def app():
    # create document object
    st.title('Relatório para o serviço de Hemodinâmica')
    mes = st.selectbox('Qual mês os indicadores serão gerados?', ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                                                                 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'])
    nome_equipamento = st.selectbox('Qual equipamento você deseja preencher o relatório', ['', 'Siemens Artis One', 'Philips'],
                              format_func = lambda x: 'Selecione uma opção' if x == '' else x)
        
        
    if nome_equipamento == '':
        st.warning('Selecione o ID do equipamento')
    else:
        arquivo = st.session_state['diretorio'] + st.session_state['cadastro']
        df = pd.read_csv(arquivo, sep=";")
            
        list_clientes = list(df.nome_cliente)
        list_clientes.insert(0,"Selecione uma opção")
            
        cliente = st.selectbox('Selecione o cliente', list_clientes,
                                  format_func = lambda x: 'Selecione uma opção' if x == '' else x)
        if cliente == 'Selecione uma opção':
            st.warning('Selecione o cliente')
            
        else:                      
        
            butao = st.checkbox('Exportar Relatório')
            if butao:

                filename = st.session_state['diretorio'] + "\Folha timbrada digital.docx"
                doc = aw.Document(filename)

                # create a document builder object
                builder = aw.DocumentBuilder(doc)
                font = builder.font
                font.size = 11
                font.name = "Eurostile LT Std"
                font.bold = False
                font.color = drawing.Color.black
                
                #Formatando a data do relatório
                m = datetime.date.today().month
                if m == 1:
                    month = 'Janeiro'
                elif m == 2:
                    month = 'Fevereiro'
                elif m == 3:
                    month = 'Março'
                elif m == 4:
                    month = 'Abril'
                elif m == 5:
                    month = 'Maio'
                elif m == 6:
                    month = 'Junho'
                elif m == 7:
                    month = 'Julho'
                elif m == 8:
                    month = 'Agosto'
                elif m == 9:
                    month = 'Setembro'
                elif m == 10:
                    month = 'Outubro'
                elif m == 11:
                    month = 'Novembro'
                elif m == 12:
                    month = 'Dezembro'


                # add text to the document
                builder.writeln(f"Porto Alegre, {datetime.date.today().day} de {month} de {datetime.date.today().year}")
                builder.write('\n')
                builder.writeln(f"Prezados Médicos do Serviço de Hemodinâmica do {cliente}")

                # set paragraph formatting
                paragraphFormat = builder.paragraph_format
                paragraphFormat.first_line_indent = 8
                paragraphFormat.alignment = aw.ParagraphAlignment.JUSTIFY


                # add text
                builder.write('\n')
                builder.writeln(f"Os gráficos abaixo representam o cenário de doses do setor da hemodinâmica para o equipamento {nome_equipamento} no mês de {mes} de {datetime.date.today().year}. Como nos preocupamos com as doses dos pacientes e colaboradores, realizamos esses levantamentos para acompanhar e realizar o processo de otimização das doses.")
                builder.write('\n')
                builder.writeln("Nosso principal objetivo é avaliar e extinguir as possibilidades de ocorrência de efeitos determinísticos nos pacientes devido ao uso da radiação ionizante. Esses efeitos são aqueles que possuem um limiar de dose para ocorrer, podendo ser: lesões na pele, depilações ou até mesmo catarata. ")
                builder.write('\n')
                builder.writeln(f"Em {mes}, o assentamento de doses dos procedimentos cardíacos realizados no equipamento {nome_equipamento}, pode-se verificar, na Figura 1, que XX% dos procedimentos são abaixo de 2000 mGy ou 2Gy. Com base na ICRP (International Commission on Radiological Protection) é recomendado que os valores de dose sejam abaixo de 2Gy, considerando que esse é o limite para a ocorrência de efeito determinístico não severo. A Figura 2 ilustra que XX% dos procedimentos vasculares são abaixo do limite de 2000 mGy.")
                builder.write('\n')
                builder.writeln("Figura 1: Procedimentos da cardiologia.")
                builder.write('\n')
                IMAGEM1 = st.session_state['graficos'] + f'\{nome_equipamento}\Doses CARDIO - {nome_equipamento}.PNG'
                builder.insert_image(IMAGEM1)
                builder.write('\n')
                builder.writeln("Figura 2: Procedimentos vasculares.")
                builder.write('\n')
                IMAGEM2 = st.session_state['graficos'] + f'\{nome_equipamento}\Doses VASCULAR - {nome_equipamento}.PNG'
                builder.insert_image(IMAGEM2)
                builder.write('\n')
                builder.writeln(f"Abaixo segue o indicador para demais faixas de dose nos pacientes da hemodinâmica para o equipamento {nome_equipamento}:")
                builder.write('\n')
                builder.write('\n')
                builder.writeln("Figura 3: Procedimentos da cardiologia.")
                builder.write('\n')
                IMAGEM3 = st.session_state['graficos'] + f'\{nome_equipamento}\Doses CARDIO intervalada - {nome_equipamento}.PNG'
                builder.insert_image(IMAGEM3)
                builder.write('\n')
                builder.writeln("Figura 4: Procedimentos vasculares.")
                builder.write('\n')
                IMAGEM4 = st.session_state['graficos'] + f'\{nome_equipamento}\Doses VASCULAR intervalada - {nome_equipamento}.PNG'
                builder.insert_image(IMAGEM4)
                builder.write('\n')
                builder.writeln("A tabela abaixo demonstra os limites de dose para efeitos determinísticos:")
                builder.write('\n')
                builder.writeln("Figura 5: Limites de dose para efeitos determinísticos.")
                builder.write("\n")
                IMAGEM5 = st.session_state['graficos'] + '\efeitos.PNG'
                builder.insert_image(IMAGEM5)
                builder.write('\n')
                builder.write('\n')
                builder.writeln('A partir desses dados, gostaríamos de sugerir novos protocolos de cuidados e acompanhamentos com os pacientes:')
                builder.write('\n')

                # insert item
                builder.writeln("1-Todas as doses devem ser registradas e inseridas nos laudos dos pacientes;")
                builder.write('\n')
                builder.writeln("2-Quando doses forem acima de 1Gy (1000 mGy), realizar a notificação ao paciente e ao médico executor caso exista possibilidade de refazer o procedimento nos próximos 60 dias;")
                builder.write('\n')
                builder.writeln("3-Realizar o acompanhamento dermatológico para pacientes que passaram por procedimentos com doses superiores a 2Gy (2000mGy).")
                builder.write('\n')

                builder.writeln(f'Outra estimativa importante definida no trabalho (STECKER, 2009) é considerar os valores de Produto Kerma Área (PKA). Nesse trabalho publicado no Journal of Vascular and Interventional Radiology considera-se que uma dose de radiação significativa seria um PKA superior a 50 Gy · cm^2. Considerando isso, foi realizado um levantamento dos valores de PKA dos procedimentos para o mês de {mes}: ')

                builder.write('\n')
                builder.writeln("Figura 6: PKA para procedimentos da cardiologia.")
                builder.write('\n')
                IMAGEM6 = st.session_state['graficos'] + f'\{nome_equipamento}\PKA CARDIO - {nome_equipamento}.PNG'
                builder.insert_image(IMAGEM6)
                builder.write('\n')
                builder.writeln("Figura 7: PKA para procedimentos vasculares.")
                builder.write('\n')
                IMAGEM7 = st.session_state['graficos'] + f'\{nome_equipamento}\PKA VASCULAR - {nome_equipamento}.PNG'
                builder.insert_image(IMAGEM7)
                builder.write('\n')
                if nome_equipamento == 'Siemens Artis One':
                    builder.writeln("Figura 8: PKA para procedimentos da neurologia.")
                    builder.write('\n')
                    IMAGEMneuro = st.session_state['graficos'] + f'\{nome_equipamento}\PKA NEUROLOGIA - {nome_equipamento}.PNG'
                    builder.insert_image(IMAGEMneuro)
                    builder.write('\n')
                    builder.writeln("Figura 9: PKA para procedimentos da quimioterapia.")
                    builder.write('\n')
                    IMAGEMquimio = st.session_state['graficos'] + f'\{nome_equipamento}\PKA QUIMIO - {nome_equipamento}.PNG'
                    builder.insert_image(IMAGEMquimio)
                    builder.write('\n')
                    builder.writeln(f'De acordo com os dados coletados durante o mês de {mes}, YY% dos procedimentos cardíacos, YY% dos procedimentos vasculares, YY% dos procedimentos da neurologia e YY% dos procedimentos da quimioterapia possuíram PKA abaixo do valor considerado significativo de 500 Gy · cm2.')
                    builder.write('\n')
                    builder.writeln('ATENÇÃO!')
                    builder.write('\n')


                    builder.writeln(f'É muito importante se atentar às unidades que estamos trabalhando. O equipamento da {nome_equipamento} disponibiliza indicadores de PKA, que são apresentados em µGy.m2. Sendo assim, para podermos comparar com valores de referência, devemos realizar conversões. Um valor apresentado no equipamento como 22690 µGy · m2, parece assustador. Porém, quando trabalhamos nas unidades corretas (dividindo por 100), verificamos que equivale a 226,90 Gy · cm2.')
                    
                elif nome_equipamento == 'Philips':
                    builder.writeln('De acordo com os dados coletados durante o mês de abril, YY% dos procedimentos cardíacos e YY% dos procedimentos vasculares possuíram PKA abaixo do valor considerado significativo de 500 Gy · cm2.')
                    builder.write('\n')
                    builder.writeln('ATENÇÃO!')
                    builder.write('\n')
                    builder.writeln(f'É muito importante se atentar às unidades que estamos trabalhando. O equipamento da {nome_equipamento} disponibiliza indicadores de PKA, que são apresentados em mGy.cm2. Sendo assim, para podermos comparar com valores de referência, devemos realizar conversões. Um valor apresentado no equipamento como 22690 mGy · cm2, parece assustador. Porém, quando trabalhamos nas unidades corretas (dividindo por 1000), verificamos que equivale a 22,690 Gy · cm2.')
                builder.write('\n')
                IMAGEM8 = st.session_state['graficos'] + '\pka_tabela.PNG'
                builder.insert_image(IMAGEM8)
                builder.write('\n')
                builder.writeln(f'Em anexo a este relatório, estão presente os indicadores individuais para cada médico, com base nos procedimento realizados. Estou à disposição para que possamos otimizar as doses mantendo a melhor qualidade do procedimento,')
                
                builder.write('\n')
                builder.writeln(f'Anexo I - Cardiologia')
                builder.write('\n')
                builder.writeln(f'Gráficos referentes ao médico Azmus')
                
                
                
                # save document
                nome_relatorio = st.session_state['relatorio'] + f'\{nome_equipamento} {mes}-{datetime.date.today().year}' + '.docx'
                doc.save(nome_relatorio)
                with st.spinner('Emitindo relatório...'):
                    time.sleep(1)
                st.success('Relatório emitido com sucesso!')
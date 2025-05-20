
#https://docs.haystack.deepset.ai/docs/huggingfacelocalgenerator
import os
import torch
import sys

import streamlit as st
from transformers import pipeline


class Oracle:
    

    def __init__(self):

        pass
        
    
    
      
    def streamlit(self):

       
        
        st.set_page_config(
            page_title="Chat bot Icomon",
            page_icon="📊",
            layout="wide",  # Alternativas: 'centered' ou 'wide'
        )

        st.title("Chat bot Icomon")
        st.image(
                "ico.jpg",  # Caminho para a imagem
                width=100,
                #use_container_width=False,
            
            )
        st.write("Olá, sou um assistente virtual. Como posso ajudar você hoje?")
        user_input = st.text_input("Digite sua pergunta:")
       
        if "historico" not in st.session_state:
            st.session_state.historico = []
        
        
    
        if st.button("Enviar") and user_input.strip() != "":

           
            model_name = "deepset/roberta-base-squad2"

            # a) Get predictions
            nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
            QA_input = {
                'question': user_input,
                'context': """
                
                            'A Icomom é uma empresa que presta serviço na área de telecomunicações. Atualmente presta serviço para estas empresas: Vtal, Oi, Vivo.A Icomon possui sede em São Paulo na rua São Evaristo número 333, filial em Curitiba na Avenida Maringa, em Pinhais. '
                            'A Icomon foi fundada em 2010, por um grupo de amigos que se conheceram na faculdade.Seus nomes são: João, Maria, José e Ana.'
                            'A Icomon conta com mais de 100 colaboradores, sendo 50 deles na sede e 50 na filial.'
                            'A Icomon teve lucro de 33.000 milhões de reais no ano de 2022.'
                            'macro atividades são as seguintes: INST-FTTH, MUD-FTTH,REP-FTTH, RET-FTTH.'
                            'A Icomom possui os seguintes estados no relatorio fsl: Atribúido, Concluído com sucesso,Concluído sem sucesso,Recebido.'
                            'A Icomom possui os seguintes id companhia no relatorio fsl: TIM,LIGGA00084,SPEEDBOAT,PALLU,TEXNET,BWTELECOM00031,SOMA00041,FLIXFIBRA00019,Axxel,ASAP00018,CLAROWHS,LOVIZWH,	Oi,EQUATORIAL,WLANFIBRA00081	

                            
                            
                            """
            
            
            }
            resposta_bot = nlp(QA_input)
        
            

            # Armazena no histórico
            st.session_state.historico.append(("Você", user_input))
            st.session_state.historico.append(("Bot", resposta_bot))

        # Exibe o histórico
        st.markdown("### Conversa:")
        for remetente, texto in st.session_state.historico:
            if remetente == "Você":
                st.markdown(f"**🧑 {remetente}:** {texto}")
            else:
                st.markdown(f"**🤖 {remetente}:** {texto}")
        
        
    

        

def main():
   
    
   
    execute = Oracle()
   
    execute.streamlit()
    

if __name__ == '__main__':
    main()



    











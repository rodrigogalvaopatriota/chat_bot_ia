
#https://docs.haystack.deepset.ai/docs/huggingfacelocalgenerator


import streamlit as st
from transformers import pipeline
import os
import pandas as pd
import json


class Oracle:
    

    def __init__(self):

        pass
        
    
    
    
    def contexto(self,user_input):
        #self.update_produtividade_context()
        if 'produtividade' in user_input:
            with open('contextos//contexto_produtividade.json', 'r') as file:
                contexto_file = file.read()
        if 'garantia' in user_input:
            with open('contextos//contexto_garantia.json', 'r') as file:
                contexto_file = file.read()
        if 'repetid' in user_input:
            with open('contextos//contexto_repetida.json', 'r') as file:
                contexto_file = file.read()
        if 'eficacia inst' in user_input:
            with open('contextos//contexto_eficacia_instalacao.json', 'r') as file:
                contexto_file = file.read()
        if 'eficacia reparo' in user_input:
             with open('contextos//contexto_eficacia_reparo.json', 'r') as file:
                contexto_file = file.read()
        if 'cumprimento insta' in user_input:
             with open('contextos//contexto_cumprimento_instalacao.json', 'r') as file:
                contexto_file = file.read()
        if 'cumprimento reparo' in user_input:
            with open('contextos//contexto_cumprimento_reparo.json', 'r') as file:
                contexto_file = file.read()
        if 'telefone' in user_input:
            with open('contextos//contexto_telefone.json', 'r') as file:
                contexto_file = file.read()
        if 'endereço' in user_input and 'sa' in user_input:
            with open('contextos//contexto_sa_endereco.json', 'r') as file:
                contexto_file = file.read()
 
     
        return contexto_file
    
    
   

    def load_model_roberta_large(self,user_input,context):
        #contexto = self.contexto()
        print(context)
        model_name = "deepset/roberta-large-squad2"
        #print(f'no modelo {model_name}, vamos executar o seguinte contexto: {contexto}')
        #from transformers import pipeline
        # a) Get predictions
        nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
        QA_input = {
            'question': user_input,
            'context': context
                        
        
        
        }
        resposta_bot = nlp(QA_input)
        
        return resposta_bot['answer']

        
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
        #if 'produtividade' in user_input:

       
        if "historico" not in st.session_state:
            st.session_state.historico = []
        
        
    
        if st.button("Enviar") and user_input.strip() != "":

           

            #resposta_bot = self.load_model_roberta(user_input)
            choose_context = self.contexto(user_input)
            resposta_bot = self.load_model_roberta_large(user_input=user_input,context=choose_context)
            #resposta_bot = self.load_model_ollama_3(user_input)


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



    











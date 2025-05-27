
#https://docs.haystack.deepset.ai/docs/huggingfacelocalgenerator


import streamlit as st
from transformers import pipeline
import os
import pandas as pd
import json
import subprocess

class Oracle:
    

    def __init__(self):

        pass
        
    
    
    
    def contexto(self):
        self.update_context()
        with open('contexto.json', 'r') as file:
            contexto_file = file.read()
            
      
        return contexto_file
    
    
   
    
    
    def load_model_tinyllama(self,user_input):

        contexto = self.contexto()
        resumo = contexto
        amostra = contexto
        prompt = user_input
        prompt = f"""
        {user_input}:

        Resumo estatístico:
        {resumo}

        Amostra de dados:
        {amostra}

        Gere insights sobre tendências, possíveis problemas e recomendações.
        """

        comando = ['ollama', 'run', 'tinyllama']
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        saida, erro = processo.communicate(input=prompt)

        
        #print("\n### Insights Gerados ###\n")
        #print(saida)
        return saida


    def load_model_roberta_large(self,user_input):
        contexto = self.contexto()
        print(contexto)
        model_name = "deepset/roberta-large-squad2"
        #print(f'no modelo {model_name}, vamos executar o seguinte contexto: {contexto}')
        #from transformers import pipeline
        # a) Get predictions
        nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
        QA_input = {
            'question': user_input,
            'context': contexto
                        
        
        
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
       
        if "historico" not in st.session_state:
            st.session_state.historico = []
        
        
    
        if st.button("Enviar") and user_input.strip() != "":

           

            #resposta_bot = self.load_model_roberta(user_input)
            #resposta_bot = self.load_model_roberta_large(user_input)
            resposta_bot = self.load_model_tinyllama(user_input)

        
            

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
    #set_execute = input('Digite 1 para executar streamlit.Digite 2 para executar modelo roberta large.Digite 3 para executar modelo roberta base,digite 4 para carregar o modelo longformer, digite 4 para verificar contexto: ')
    #execute.update_produtividade_context()
    execute.streamlit()
    

    #execute.load_model_mistral(user_input='Quais foram os presidentes dos Estadus Unidos?')

if __name__ == '__main__':
    main()



    











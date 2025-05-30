
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
        if 'email' in user_input:
            with open('contextos//contexto_email.json', 'r') as file:
                contexto_file = file.read()
        if 'cumprimento agendamento insta' in user_input:
            with open('contextos//contexto_cumprimento_agendamento_instalacao.json', 'r') as file:
                contexto_file = file.read()
        if 'cumprimento agendamento rep' in user_input:
            with open('contextos//contexto_cumprimento_agendamento_reparo.json', 'r') as file:
                contexto_file = file.read()
        if 'eficacia rep' in user_input:
            with open('contextos//contexto_eficacia_reparo.json', 'r') as file:
                contexto_file = file.read()
        if 'eficacia inst' in user_input:
            with open('contextos//contexto_eficacia_instalacao.json', 'r') as file:
                contexto_file = file.read()
    
            
 
     
        return contexto_file
    
    def load_model_llama3(self,user_input,context):

        model_path = 'meta-llama/Meta-Llama-3-8B-Instruct'
        pipe = pipeline("text-generation", model=model_path, torch_dtype=torch.bfloat16, device_map="auto")

        question = user_input
        messages = [
            {
                "role": "system",
                "content": f"Você é um especialista em analise de indicadores. Considere o seguinte contexto:\n{context}",
            },
            {"role": "user", "content": f"{question}"},
        ]
        prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        outputs = pipe(prompt, max_new_tokens=2048, do_sample=True, temperature=0.6, top_k=50, top_p=0.95)
        #print(outputs[0]["generated_text"])
        resultado = str(outputs[0]["generated_text"]).split('assistant<|end_header_id|>')[1]
        return resultado
   

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
        st.write("Olá, sou assistente virtual de indicadores Icomon, possuo respostas para estes indicadores:")
        st.write("Produtividade, repetido, garantia.Cumprimentos de agendamentos: instalação e reparo.Eficácias: instalação e reparo.")
        st.write("Meu conhecimento ainda está restrito aos coordenadores de campo do estado do Paraná.")
        st.write("Por enquanto respondo perguntas simples com respostas curtas, logo vou aprender a analisar e fornecer repostas complexas.")
        st.write("Aqui vão algumas dicas de perguntas:")
        st.write("Qual foi o resultado do indicador garantia do elisson?")
        st.write("Qual o resultado da garantia do elisson?")
        st.write("Qual o resultado da garantia do supervisor elisson?")
        st.write(" ")
                          
        
        
        user_input = st.text_input("Digite sua pergunta:")
        #if 'produtividade' in user_input:

       
        if "historico" not in st.session_state:
            st.session_state.historico = []
        
        
    
        if st.button("Enviar") and user_input.strip() != "":

           

           
            choose_context = self.contexto(user_input)
            #resposta_bot = self.load_model_roberta_large(user_input=user_input,context=choose_context)
            resposta_bot = self.load_model_llama3(user_input=user_input,context=choose_context)
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



    











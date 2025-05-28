
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
 
     
        return contexto_file
    
    
    def update_produtividade_context(self):
        #C:\Users\55419\Documents\icomon\spot\thiago\Handover - TH\Handover - TH\robos\resultados_produtividade\nelson\top_bottom_tecnico
        path_df_context_produtividade = os.path.join('C:\\', 'Users', '55419', 'Documents', 'icomon', 'spot', 'thiago', 'Handover - TH', 'Handover - TH', 'robos', 'resultados_produtividade', 'nelson', 'top_bottom_tecnico', 'resultado_top_bottom_PR_Supervisor.xlsx')
        path_chat_bot    = os.path.join('C:\\', 'Users', '55419', 'Documents', 'icomon', 'spot', 'python', 'oracle')
        
        
        columns_produtividade = ['Supervisor', 'produtividade_x']
        df_context_produtividade = pd.read_excel(path_df_context_produtividade,usecols=columns_produtividade)
        df_context_produtividade['Supervisor'] = df_context_produtividade['Supervisor'].astype(str).str.lower()
       

        print(f'Carregando o dataframe de contexto: {path_df_context_produtividade}')
        print(f'Colunas do dataframe: {df_context_produtividade.columns}')
        print(f'Número de linhas no dataframe: {len(df_context_produtividade)}')
        df_context_produtividade = df_context_produtividade.dropna()
        
        
        df_context_produtividade ['context'] = ''
        for index,row in df_context_produtividade.iterrows():
            #context+= f'{str(row["Supervisor"])} têm o resultado de: {str(row["produtividade_x"])}'
            #df_context_produtividade.at[index, 'context'] = f'{str(row["Supervisor"])} têm o resultado de {str(round(row["produtividade_x"],4))}'
            if 'basilio' in str(row['Supervisor']).lower():
                df_context_produtividade.at[index, 'context'] = f'produtividade de basilio: {str(round(row["produtividade_x"],4))}'
               
            if 'heider' in str(row['Supervisor']).lower():
                df_context_produtividade.at[index, 'context'] = f'produtividade de heider: {str(round(row["produtividade_x"],4))}'
               
            if 'elisson' in str(row['Supervisor']).lower():
                df_context_produtividade.at[index, 'context'] = f'produtividade elisson: {str(round(row["produtividade_x"],4))}'
                
            if 'clemilson' in str(row['Supervisor']).lower():
                df_context_produtividade.at[index, 'context'] = f'produtividade clemilson: {str(round(row["produtividade_x"],4))}'
               
            if 'eduardo' in str(row['Supervisor']).lower():
                df_context_produtividade.at[index, 'context'] = f'produtividade eduardo: {str(round(row["produtividade_x"],4))}'
               
            if 'tony' in str(row['Supervisor']).lower():
                df_context_produtividade.at[index, 'context'] = f'produtividade tony: {str(round(row["produtividade_x"],4))}'
               
      
        df_context_produtividade = df_context_produtividade[['context']].copy()
        df_context_produtividade[['key','value']] = df_context_produtividade['context'].str.split(':', expand=True)

        # Limpar espaços
        df_context_produtividade['key'] = df_context_produtividade['key'].str.strip()
        df_context_produtividade['value'] = df_context_produtividade['value'].str.strip()
        
        # Criar Series (chave-valor)
        series = pd.Series(df_context_produtividade['value'].values, index=df_context_produtividade['key'])

        # Salvar como JSON
        series.to_json(f'{path_chat_bot}//contextos//contexto_produtividade.json', indent=4)  # pandas >= 1.1.0 tem indent
        
        return series
       
    
    def update_gerenciais_context(self):

       
       # 1. Abrir o JSON existente
        with open('contexto.json', 'r') as f:
            contexto = json.load(f)
            print(type(contexto))
            print(contexto)

        # 2. Adicionar novos valores
        contexto['a produtividade de Jose'] = '5,215'
        contexto['a produtividade de Maria'] = '6,123'

        # 3. Salvar de volta no mesmo arquivo
        with open('contexto.json', 'w') as f:
            json.dump(contexto, f, indent=4)
            
        with open('contexto.json', 'r') as f:
            contexto = json.load(f)
            print(type(contexto))
            print(contexto)

        pass
    
    
    def load_model_tinyllama(self,user_input):
        #meta-llama/Meta-Llama-3-8B-Instruct
        #
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
        #C:\Users\55419\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
        comando = ['C:\\Users\\55419\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\ollama', 'run', 'tinyllama']
        processo = subprocess.Popen(comando, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        saida, erro = processo.communicate(input=prompt)

        
        #print("\\n### Insights Gerados ###\n")
        #print(saida)
        return saida


    
    def load_model_ollama_2(self):
        from ollama import chat
        from ollama import ChatResponse
        
        response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': 'Why is the sky blue?',
        },
        ])
        print(response['message']['content'])
        # or access fields directly from the response object
        #print(response.message.content)

        
    
    
    def load_model_llama(self,user_input):
        contexto = self.contexto()
        # Install transformers from source - only needed for versions <= v4.34
        # pip install git+https://github.com/huggingface/transformers.git
        # pip install accelerate
        #meta-llama/Meta-Llama-3-8B-Instruct
        #TinyLlama/TinyLlama-1.1B-Chat-v0.6
        import torch
        from transformers import pipeline

        pipe = pipeline("text-generation", model="meta-llama/Meta-Llama-3-8B-Instruct", torch_dtype=torch.bfloat16, device_map="auto")
        print(f' o modelo tinnyllama vai processar o contexto: {contexto}')
        # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
        messages = [
            {
                "role": "system",
                "content": f"Você é um analista de dados especialista em produtividade. Considere o seguinte contexto:\n{contexto}",
            },
            {"role": "user", "content": f"{user_input}"},
        ]
        prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        #outputs = pipe(prompt, max_new_tokens=16, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
        outputs = pipe(prompt, max_new_tokens=16, do_sample=False)
        generated_text = outputs[0]["generated_text"]

        #resposta = generated_text[len(prompt):].strip()

        #print(generated_text)
        return generated_text
        

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
    #set_execute = input('Digite 1 para executar streamlit.Digite 2 para executar modelo roberta large.Digite 3 para executar modelo roberta base,digite 4 para carregar o modelo longformer, digite 4 para verificar contexto: ')
    #execute.update_produtividade_context()
    execute.streamlit()
    #execute.load_model_tinyllama(user_input='qual a produtividade do elisson?')
    #execute.load_model_llama(user_input='qual o resultado do heider?')
    

    #execute.load_model_mistral(user_input='Quais foram os presidentes dos Estadus Unidos?')

if __name__ == '__main__':
    main()



    











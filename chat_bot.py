
#https://docs.haystack.deepset.ai/docs/huggingfacelocalgenerator


import streamlit as st
#from transformers import pipeline


class Oracle:
    

    def __init__(self):

        pass
        
    
    
    
    def contexto(self):
        with open('contexto.json', 'r') as file:
            contexto_file = file.read()
            
       
      
        return contexto_file
    
    
    def load_model_roberta_large(self,user_input):
        contexto = self.contexto()
        model_name = "deepset/roberta-large-squad2"
        #print(f'no modelo {model_name}, vamos executar o seguinte contexto: {contexto}')
        from transformers import pipeline
        # a) Get predictions
        nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
        QA_input = {
            'question': user_input,
            'context': contexto
                        
        
        
        }
        resposta_bot = nlp(QA_input)
        return resposta_bot['answer']

    
    def load_model_roberta_base(self,user_input):
        contexto = self.contexto()
        model_name = "deepset/roberta-base-squad2"
        #print(f'no modelo {model_name}, vamos executar o seguinte contexto: {contexto}')
        from transformers import pipeline
        # a) Get predictions
        nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
        QA_input = {
            'question': user_input,
            'context': contexto
                        
        
        
        }
        resposta_bot = nlp(QA_input)
        return resposta_bot
      
    
    def load_model_long_former(self, user_input):
        import torch
        from transformers import AutoTokenizer, AutoModelForQuestionAnswering
        contexto = self.contexto()
        tokenizer = AutoTokenizer.from_pretrained("allenai/longformer-base-4096")
        model_name = "allenai/longformer-base-4096"
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        #print(f'no modelo {model_name}, vamos executar o seguinte contexto: {contexto}')
        inputs = tokenizer(
            user_input,
            contexto,
            return_tensors="pt",
            truncation=True,
            max_length=4096
        )

        with torch.no_grad():
            outputs = model(**inputs)

        start = torch.argmax(outputs.start_logits)
        end = torch.argmax(outputs.end_logits) + 1

        resposta_bot = tokenizer.convert_tokens_to_string(
            tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start:end])
        )

        return resposta_bot
    
    
    def load_model_long_former_2(self, user_input):
        context = self.contexto()

        from transformers import AutoTokenizer, AutoModelForQuestionAnswering
        import torch

        # Modelo fine-tuned para SQuAD1
        model_name = "valhalla/longformer-base-4096-finetuned-squadv1"

        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)

        question = user_input
        #context = """
        #Longformer is a transformer model designed for long documents. 
        #It combines local and global attention patterns to efficiently process longer sequences. 
        #"""

        inputs = tokenizer(question, context, return_tensors="pt", max_length=4096, truncation=True)

        with torch.no_grad():
            outputs = model(**inputs)

        answer_start = torch.argmax(outputs.start_logits)
        answer_end = torch.argmax(outputs.end_logits) + 1

        answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))

        #print("Answer:", answer)
        return answer

    
    
    
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
            resposta_bot = self.load_model_roberta_large(user_input)
        
            

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
    
    execute.streamlit()

if __name__ == '__main__':
    main()



    











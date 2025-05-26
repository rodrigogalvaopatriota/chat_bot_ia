
#https://docs.haystack.deepset.ai/docs/huggingfacelocalgenerator


import streamlit as st
#from transformers import pipeline


class Oracle:
    

    def __init__(self):

        pass
        
    
    
    
    def contexto(self):
        with open('contexto.json', 'r') as file:
            contexto_file = file.read()
            
        #from transformers import AutoTokenizer

        #model_name = "valhalla/longformer-base-4096-finetuned-squadv1"
        #tokenizer = AutoTokenizer.from_pretrained(model_name)
        # contexto ruim
        contexto = """
            
                        'A Icomom é uma empresa que presta serviço na área de telecomunicações.'
                        'A icomon presta serviços para estas empresas: Vtal, Oi, Vivo.'
                        'o campo macro atividades possuem estes valores: INST-FTTH, MUD-FTTH,REP-FTTH, RET-FTTH.'
                        'o campo estado possuem estes valores: Atribúido, Concluído com sucesso,Concluído sem sucesso,Recebido.'
                        'o campo id companhia possuem estes valores: TIM,LIGGA,SPEEDBOAT,PALLU,TEXNET,BWTELECOM,SOMA,FLIXF,Axxel,ASA,CLARO,LOVIZWH,Oi,EQUATORIAL,WLANFIBRA	
                        'indicador cumprimento agendamento instalação no mes de maio:95%'
                        'indicador cumprimento agendamento instalação no mes de abril: 94%'
                        'indicador cumprimento agendamento instalação no mes de março: 93%'
                        'indicador cumprimento agendamento instalação no mes de fevereiro: 92%'
                        'indicador cumprimento agendamento instalação no mes de janeiro: 91%'
                        'indicador cumprimento agendamento reparo no mes de janeiro: 81%'
                        'indicador cumprimento agendamento reparo no mes de fevereiro: 82%'
                        'indicador cumprimento agendamento reparo no mes de março: 83%'
                        'indicador cumprimento agendamento reparo no mes de abril: 84%'
                        'indicador cumprimento agendamento reparo no mes de maio: 85%'
                        'indicador garantia no mes de janeiro: 71%'
                        'indicador garantia no mes de fevereiro: 72%'
                        'indicador garantia no mes de março: 73%'
                        'indicador garantia no mes de abril: 74%'
                        'indicador garantia no mes de maio: 75%'



                        

                    """
        
        
        
        #melhor contexto
        contexto_1 = """
                        "O Brasil foi descoberto em 1500 por Pedro Álvares Cabral."
                        "Nesta época, o Brasil era habitado por indígenas."
                        "A primeira capital do Brasil foi Salvador, na Bahia."
                        "O Brasil é o maior país da América do Sul."
                        "A língua oficial do Brasil é o português."
                        "O Brasil é conhecido por sua diversidade cultural e natural."
                        "O Brasil é o lar da Floresta Amazônica, a maior floresta tropical do mundo."
                        "O Brasil é famoso por seu carnaval, samba e futebol."
                        "O Brasil é o maior produtor de café do mundo."
                        "O Brasil tem uma rica história de colonização e imigração."
                        "O Brasil é o lar de várias cidades icônicas, como Rio de Janeiro e São Paulo."
                        "A média salarial no Brasil varia de acordo com a região e o setor."
                        "o brasileiro ganha em média R$ 2.500,00 por mês."
                        "O Brasil é o maior país da América Latina."
                        "A capital do Brasil é Brasília."
                        "A capital do Parana é Curitiba."
                        "A capital do Rio de Janeiro é a cidade do Rio de Janeiro."
                        "A capital de São Paulo é a cidade de São Paulo."
                        "A capital do Rio Grande do Sul é Porto Alegre."
                        "A capital do Rio Grande do Norte é Natal."
                        "A capital do Ceará é Fortaleza."
                        "A capital do Maranhão é São Luís."
                        "A capital do Piauí é Teresina."
                        "A capital do Pará é Belém."
                        "A capital do Amazonas é Manaus."
                        "A capital do Acre é Rio Branco."
                        "A capital de Roraima é Boa Vista."
                        "A capital do Amapá é Macapá."
                        "A capital do Tocantins é Palmas."
                        "A capital do Maranhão é São Luís."
                        "A capital do Piauí é Teresina."
                        "A capital do Ceará é Fortaleza."
                        "A capital do Rio Grande do Norte é Natal."
                        "A capital do Paraíba é João Pessoa."
                        "A capital de Pernambuco é Recife."
                        "A capital do Alagoas é Maceió."
                        "A capital de Sergipe é Aracaju."
                        "A capital da Bahia é Salvador."
                        "A capital do Espírito Santo é Vitória."
                        "A capital de Minas Gerais é Belo Horizonte."

                        """

        contexto_3 = """
                       'A Icomon é uma empresa que presta serviço na área de telecomunicações.
                        ela presta serviços para estas empresas: Vtal, Oi, Vivo.
                        A icomon possui estes indicadores: agendamento,garantia.
                        Foi fundada em 2010.
                        Foi fundada por Elias Bragneto, André Aranha, Pedro Anizio, Marcelo Xives.
                        Possui sede em São Paulo.
                        Possui filiais nestes estados: Paraná, Rio de Janeiro, Rio Grande do Sul, Santa Catarina, Maranhão, Piauí.
                        A lucatividade no ano de 2022 foi de 10%, possibilitando um crescimento de 5% em relação ao ano de 2021.
                        Com isso, a icomon se tornou uma das maiores empresas de telecomunicações do Brasil.Estamos projetando uma contratação de 150 colaboradores para o estado do Paraná.
                        No mes de maio tivemos o resultado de 95% de cumprimento de agendamento de instalação.

                    """
        
        
        #tokens = tokenizer.encode(contexto)
        #print("Total de tokens no contexto:", len(tokens))
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



    











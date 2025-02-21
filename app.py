import json
import os
import streamlit as st

# Função para exibir as perguntas com as opções
def display_question(question):
    # Concatenar a pergunta, número e descrição
    question_text = f"**Q{question['question_number']}:** {question['question']}"
    
    # Exibir a pergunta e a descrição no mesmo bloco com o mesmo estilo
    st.markdown(question_text)
    
    # Exibir as opções
    for option in question['options']:
        st.write(f"{option['option']} {option['text']}")

    # Exibir o link
    st.write(f"[Link para a questão]({question['url']})")

# Função para exibir a explicação e a resposta
def display_answer(question):
    st.write(f"**Resposta correta:** {question['selected_answer']}")
    st.write(f"**Explicação:** {question['explanation']}")
    
    if question['suggested_answer']:
        st.write(f"**Resposta sugerida:** {question['suggested_answer']}")

# Função principal para criar a interface com Streamlit
def main():
    st.title("Gerador de Perguntas e Respostas")

    # Definindo o caminho para o diretório local onde o arquivo JSON está
    json_file = os.path.join("all_questions.json")

    # Verificando se o arquivo JSON existe
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            questions = json.load(f)
        st.write(f"Total de perguntas carregadas: {len(questions)}")

        # Sidebar: lista de botões para cada pergunta
        question_numbers = [question['question_number'] for question in questions]
        selected_question_number = st.sidebar.selectbox("Escolha uma pergunta", question_numbers)

        # Encontrando a pergunta selecionada
        selected_question = next((q for q in questions if q['question_number'] == selected_question_number), None)

        # Exibindo a pergunta selecionada
        if selected_question:
            display_question(selected_question)

            # Mostrar resposta e explicação ao clicar no botão
            if st.button(f"Mostrar resposta para Q{selected_question_number}"):
                display_answer(selected_question)

    else:
        st.error(f"Arquivo JSON não encontrado no caminho: {json_file}")

if __name__ == "__main__":
    main()

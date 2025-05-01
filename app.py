import json
import os
import streamlit as st

# Função para exibir as perguntas com as opções
def display_question(question, language):
    # Concatenar a pergunta, número e descrição
    if language == "Português":
        question_text = f"**Q{question['question_number']}:** {question.get('question_pt', question['question'])}"
    else:
        question_text = f"**Q{question['question_number']}:** {question['question']}"
    
    # Exibir a pergunta e a descrição no mesmo bloco com o mesmo estilo
    st.markdown(question_text)
    
    # Exibir as opções
    for option in question['options']:
        option_text = option.get('text_pt', option['text']) if language == "Português" else option['text']
        st.write(f"{option['option']} {option_text}")

    # Exibir o link
    st.write(f"[Link para a questão]({question['url']})")

# Função para exibir a explicação e a resposta
def display_answer(question, language):
    st.write(f"**Resposta correta:** {question['selected_answer']}")
    
    explanation = question.get('explanation_pt', question['explanation']) if language == "Português" else question['explanation']
    st.write(f"**Explicação:** {explanation}")
    
    if question['suggested_answer']:
        st.write(f"**Resposta sugerida:** {question['suggested_answer']}")

# Função para a página de perguntas e respostas
def question_page():
    st.title("Gerador de Perguntas e Respostas")

    # Seleção de idioma
    language = st.sidebar.radio("Idioma", ["Português", "English"])

    # Definindo o caminho para o diretório local onde o arquivo JSON está
    json_file = os.path.join("all_questions.json")

    # Verificando se o arquivo JSON existe
    if os.path.exists(json_file):
        with open(json_file, "r") as f:
            questions = json.load(f)
        st.write(f"Total de perguntas carregadas: {len(questions)}")

        # Sidebar: lista de botões para cada pergunta
        question_numbers = [question['question_number'] for question in questions]
        
        # Usando session_state para armazenar o número da pergunta selecionada
        if 'current_question' not in st.session_state:
            st.session_state.current_question = question_numbers[0]  # Inicializa com a primeira pergunta
        selected_question_number = st.sidebar.selectbox(
            "Escolha uma pergunta", question_numbers, index=question_numbers.index(st.session_state.current_question)
        )

        # Atualiza o número da questão selecionada no session_state
        st.session_state.current_question = selected_question_number

        # Encontrando a pergunta selecionada
        selected_question = next((q for q in questions if q['question_number'] == st.session_state.current_question), None)

        # Exibindo a pergunta selecionada
        if selected_question:
            display_question(selected_question, language)

            # Mostrar resposta e explicação ao clicar no botão
            if st.button(f"Mostrar resposta para Q{selected_question_number}"):
                display_answer(selected_question, language)

            # Botão para passar para a próxima questão
            if st.button("Próxima questão"):
                current_index = question_numbers.index(st.session_state.current_question)
                if current_index < len(question_numbers) - 1:
                    st.session_state.current_question = question_numbers[current_index + 1]
                    st.experimental_rerun()

    else:
        st.error(f"Arquivo JSON não encontrado no caminho: {json_file}")

# Função para a página de download de arquivos
def download_page():
    st.title("Download de Arquivos")

    # Lista de arquivos
    files = [
        "ai_practitioner_aif_c01.xlsx",
        "alexa_skill_builder_specialty.xlsx",
        "big_data_bds.xlsx",
        "cloud_practitioner.xlsx",
        "cloud_practitioner_clf_c02.xlsx",
        "data_analytics_das_c01.xlsx",
        "data_engineer_dea_c01.xlsx",
        "database_specialty.xlsx",
        "developer_associate.xlsx",
        "developer_associate_dva_c02.xlsx",
        "devops_engineer_dop_c01.xlsx",
        "devops_engineer_dop_c02.xlsx",
        "machine_learning_engineer_mla_c.xlsx",
        "machine_learning_specialty_mls_.xlsx",
        "sap_on_aws_pas_c01.xlsx",
        "security_specialty.xlsx",
        "security_specialty_scs_c02.xlsx",
        "solutions_architect_professiona.xlsx",
        "solutions_architect_saa_c02.xlsx",
        "solutions_architect_saa_c03.xlsx",
        "sysops_administrator.xlsx",
        "sysops_administrator_soa_c02.xlsx",
        "advanced_networking_ans_c01.xlsx"
    ]
    
    # Criar botões de download para os arquivos
    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                st.download_button(
                    label=f"Exame {file}",
                    data=f,
                    file_name=file,
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
        else:
            st.write(f"Arquivo não encontrado: {file}")

# Função principal para criar a interface com Streamlit
def main():
    # Sidebar com opção de navegação entre as páginas
    page = st.sidebar.radio("Escolha a página", ("Perguntas e Respostas - Solution Architech Associate", "Download de Exames Excel"))

    if page == "Perguntas e Respostas - Solution Architech Associate":
        question_page()
    elif page == "Download de Exames Excel":
        download_page()

if __name__ == "__main__":
    main()

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

# Função para a página de perguntas e respostas
def question_page():
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

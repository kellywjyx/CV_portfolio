import streamlit as st
import base64
from streamlit_pills import pills
from st_aggrid import AgGrid
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
    #initial_sidebar_state="expanded",
)

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="600" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
email = "mailto:kellywongjieyin@gmail.com"
linkedin = "https://www.linkedin.com/in/kelly-wong-jie-yin-a64023205/"
website = "https://github.com/kellywjyx/"

col1, col2 = st.columns([1,1])
with col1:
    st.title('Hi, I\'m Kelly Wong')
    #st.write('Contact Information: [Your Email](mailto:kellywongjieyin@gmail.com), [LinkedIn Profile](https://www.linkedin.com/in/kelly-wong-jie-yin-a64023205/), [GitHub Profile](https://github.com/kellywjyx/)')
    button1, button2, button3= st.columns([1,1,1])
    with button1:
        st.link_button('📧 Email',email)
    with button2:
        st.link_button('✉️ Linkedin',linkedin)
    with button3:
        st.link_button('🔗 Github',website)
        
    st.header('About Me')
    st.write("I am currently a final year student at Nanyang Technological University, where I am pursuing a Bachelor's degree in Data Science and Artificial Intelligence. I am exploring different career paths, with a particular interest in becoming a Data Scientist. Please feel free to reach out to me if you would like to collaborate or discuss any opportunities. I am eager to connect and learn from professionals in the industry.")
    button1, button2, button3 = st.columns([1,1,1])
    with button1:
        if st.button('Show Resume',key='1'):            
            show_pdf("Kelly Wong Resume 2023 v3.pdf")
    with button2:
        st.button('Close Resume',key='2') 
    with button3:
        with open("Kelly Wong Resume 2023 v3.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(label="Download Resume", key='3',
                data=PDFbyte,
                file_name="Kelly_Wong_Jie_Yin_resume.pdf",
                mime='application/octet-stream')

with col2:
    st.image('IMG_1452.jpeg', width=600)
    
st.markdown('---')

st.header('Technical Skills')
pills("Technical Skills",['Python','SQL','R','Java'],['🐍','📂','📊','📕'],index=None,label_visibility="collapsed")
st.markdown('---')

st.header('Projects')
col_1,col_2 = st.columns([1,1])
with col_1:
    st.markdown('#### Flowers Classification Using Neural Networks')
    st.write('[GitHub](https://github.com/kellywjyx/flower_102/tree/main)')
    acc = ['88.13%','84.92%','97.11%','79.10%','82.90%']
    f1_score = ['0.882','0.850','0.971','0.443','0.829']
    models = ['ResNet-50','MobileNet V2','Vision Transformers','K-Shot Learning','Triplet Loss Network']
    df_models = pd.DataFrame([models,acc,f1_score]).T
    df_models.columns = ['Model','Test Accuracy','F1 Score']
    st.write('This project focuses on flower recognition using the Oxford Flowers 102 dataset, a challenging task due to the \
        variability and complexity of natural environments. The project investigates into various techniques such as ResNet-50, \
        MobileNetV2, Transformers ViT, K-Shot learning, and Triplet Loss network for flower classification, aiming to contribute \
        to the broader understanding of image classification in natural settings​. Experiments with different architectures like \
        ResNet-50, MobileNetV2, Transformers ViT, K-Shot learning, and Triplet Loss network are detailed. ')
    st.markdown(df_models.style.hide(axis="index").to_html(), unsafe_allow_html=True)
    

with col_2:
    st.markdown('#### Dashboard for NTU SCSE Professors')
    st.write('[Dashboard](https://ddp-scse-dashboard-kelly.streamlit.app/)')
    st.write("This project is mainly about creating a dashboard to showcase NTU SCSE Professors, display an individual faculty \
        member's profile, including background information, research profile, quantitative metrics, and collaboration network.\
        This dashboard can be an effective marketing tool for the university, showcasing its intellectual capital and attracting\
        talented individuals to join as students or staff members, and facilitate interdisciplinary research by connecting faculty \
        members with complementary skills and interests.")
    
st.markdown('')
col_5,_ = st.columns([1,1])
with col_5:
    st.markdown('#### Sentiment Analysis for Social Media Posts during COVID-19')
    st.write('[GitHub](https://github.com/kellywjyx/Sentiment-Analysis-for-COVID-19-Facebook-data)')
    st.write('The study employed Latent Dirichlet Allocation (LDA) for topic modeling on Facebook posts from the Ministry of Health \
        (MOH) and Ministry of Education (MOE). Eight dominant topics were identified, with the most prevalent being imported cases \
        and vaccination. Sentiment analysis was performed using LSTM models, and BERT. It revealed a predominance of \
        negative sentiment across all platforms, particularly in response to key COVID-19 related events.')
st.markdown('---')
st.header('Experience')
col_3,col_4 = st.columns([1,1])
with col_3:
    col_31,col_32 = st.columns([1,2])
    with col_31:
        st.markdown('')
        st.image('dbs-bank-logo.png')
    with col_32:
        st.subheader('Data Science Intern')
        st.markdown('##### DBS, Singapore (Jul 2023 - Sep 2023)')
        st.markdown("- Kickstarted project to implement Computer Vision models to pick up datapoints from more than 1000 scanned \
            PDFs for audit checks and apply similarity search techniques to identify potential discrepancies among the PDF \
            documents.\n- Engaged in projects to construct knowledge graphs for large language models (LLM) by implementing \
            Named Entity Recognition (NER) models.\n- Support the development, execution, and refinement of automated \
            systems to detect and validate suspicious transactions for escalation using Python and Tableau.")
    
with col_4:
    col_41, col_42 = st.columns([1,2])
    with col_41:
        #st.markdown('')
        st.image('KPMG-Logo.jpeg')
    with col_42:
        st.subheader('Management Intern')
        st.markdown('##### KPMG, Singapore (Dec 2022 - Feb 2023)')
        st.markdown('- Engaged in projects to implement Alteryx workflows for Extract, Transform, Load (ETL) processes and Power BI \
            dashboards for data visualization as part of the solution to streamline the generation of tax related documents.\n- Engaged \
            in projects to implement Optical Character Recognition (OCR) to pick up datapoints from invoices.')
        
col_7,_ = st.columns([1,1])
with col_7:
    col_71,col_72 = st.columns([1,2])
    with col_71:
        #st.markdown('')
        st.image('OCBC-Bank-Logo.jpeg')
    with col_72:
        st.subheader('STEM@OCBC Intern')
        st.markdown('##### OCBC, Singapore (May 2022 - Dec 2022)')
        st.markdown('- Support the CFS Risk & Prevention team to analyze, develop and implement data driven solutions covering \
            Sales, Anti-Money Laundering (AML) and Operations surveillance.\n- Support the development, execution, and refinement \
            of automated systems to detect and validate suspicious transactions for escalation using Python and Power \
            BI.\n- Support projects to enhance leverage of analytics tools (ML and voice-to-text) to uncover new unknown risk \
            typologies.')

# import streamlit as st
# from langchain.prompts import PromptTemplate
# # from langchain.llms import CTransformers
# from langchain_community.llms import CTransformers

# ## Function To get response from LLAma 2 model

# def getLLamaresponse(input_text,no_words,blog_style):

#     ### LLama2 model
#     llm=CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
#                       model_type='llama',
#                       config={'max_new_tokens':256,
#                               'temperature':0.01})
    
#     ## Prompt Template

#     template="""
#         Write a blog for {blog_style} job profile for a topic {input_text}
#         within {no_words} words.
#             """
    
#     prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
#                           template=template)
    
#     ## Generate the ressponse from the LLama 2 model
#     response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
#     print(response)
#     return response






# st.set_page_config(page_title="Generate Blogs",
#                     page_icon='🤖',
#                     layout='centered',
#                     initial_sidebar_state='collapsed')

# st.header("Generate Blogs 🤖")

# input_text=st.text_input("Enter the Blog Topic")

# ## creating to more columns for additonal 2 fields

# col1,col2=st.columns([5,5])

# with col1:
#     no_words=st.text_input('No of Words')
# with col2:
#     blog_style=st.selectbox('Writing the blog for',
#                             ('Researchers','Data Scientist','Common People'),index=0)
    
# submit=st.button("Generate")

# ## Final response
# if submit:
#     st.write(getLLamaresponse(input_text,no_words,blog_style))


# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain_community.llms import CTransformers

# ## Function to get response from LLaMA 2 model
# def getLLamaresponse(input_text, no_words, blog_style):
#     ### LLaMA 2 model
#     llm = CTransformers(
#         model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',
#         model_type='llama',
#         config={'max_new_tokens': 256, 'temperature': 0.01}
#     )
    
#     ## Prompt Template
#     template = """
#         Write a blog for {blog_style} job profile for a topic {input_text}
#         within {no_words} words.
#     """
    
#     prompt = PromptTemplate(
#         input_variables=["blog_style", "input_text", "no_words"],
#         template=template
#     )
    
#     ## Generate the response from the LLaMA 2 model
#     response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
#     print(response)
#     return response

# st.set_page_config(
#     page_title="Generate Blogs",
#     page_icon='🤖',
#     layout='centered',
#     initial_sidebar_state='collapsed'
# )

# st.header("Generate Blogs 🤖")

# input_text = st.text_input("Enter the Blog Topic")

# ## Creating two more columns for additional fields
# col1, col2 = st.columns([5, 5])

# with col1:
#     no_words = st.text_input('No of Words')
# with col2:
#     blog_style = st.selectbox('Writing the blog for',
#                               ('Researchers', 'Data Scientist', 'Common People'), index=0)
    
# submit = st.button("Generate")

# ## Final response
# if submit:
#     st.write(getLLamaresponse(input_text, no_words, blog_style))
    
    
    
    




# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain_community.llms import CTransformers
# import time

# def getLLamaresponse(input_text, no_words, blog_style):
#     print("Starting model initialization:", time.ctime())
#     llm = CTransformers(
#         model='model/llama-2-7b-chat.ggmlv3.q4_0.bin',  # Try q4_0 for faster performance
#         model_type='llama',
#         config={'max_new_tokens': 128, 'temperature': 0.01}
#     )
#     print("Model initialized:", time.ctime())
    
#     template = """
#         Write a blog for {blog_style} job profile for a topic {input_text}
#         within {no_words} words.
#     """
#     prompt = PromptTemplate(
#         input_variables=["blog_style", "input_text", "no_words"],
#         template=template
#     )
#     print("Prompt created:", time.ctime())
    
#     response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
#     print("Response generated:", time.ctime())
#     print(response)
#     return response

# st.set_page_config(
#     page_title="Generate Blogs",
#     page_icon='🤖',
#     layout='centered',
#     initial_sidebar_state='collapsed'
# )

# st.header("Generate Blogs 🤖")

# input_text = st.text_input("Enter the Blog Topic")
# col1, col2 = st.columns([5, 5])

# with col1:
#     no_words = st.text_input('No of Words')
# with col2:
#     blog_style = st.selectbox('Writing the blog for',
#                               ('Researchers', 'Data Scientist', 'Common People'), index=0)

# submit = st.button("Generate")

# if submit:
#     if input_text and no_words.isdigit():
#         st.write(getLLamaresponse(input_text, int(no_words), blog_style))
#     else:
#         st.error("Please provide a valid topic and number of words.")

    
    
    
    



import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
import time
import os

def getLLamaresponse(input_text, no_words, blog_style):
    print("Starting model initialization:", time.ctime())
    model_path = r'E:\LLM Project\model\llama-2-7b-chat.ggmlv3.q8_0.bin'
    
    # Check if model file exists
    if not os.path.exists(model_path):
        st.error(f"Model file not found at {model_path}. Please download it or update the path.")
        return None
    
    try:
        llm = CTransformers(
            model=model_path,
            model_type='llama',
            config={'max_new_tokens': 128, 'temperature': 0.01}
        )
        print("Model initialized:", time.ctime())
        
        template = """
            Write a blog for {blog_style} job profile for a topic {input_text}
            within {no_words} words.
        """
        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", "no_words"],
            template=template
        )
        print("Prompt created:", time.ctime())
        
        response = llm.invoke(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
        print("Response generated:", time.ctime())
        print(response)
        return response
    except Exception as e:
        st.error(f"Error during model processing: {str(e)}")
        return None

st.set_page_config(
    page_title="Generate Blogs",
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

if submit:
    if input_text and no_words.isdigit():
        response = getLLamaresponse(input_text, int(no_words), blog_style)
        if response:
            st.write(response)
    else:
        st.error("Please provide a valid topic and number of words.")
    
    
# cd E:\LLM Project
# .\venv\Scripts\activate
# pip install -U langchain-community streamlit langchain
# streamlit run app.py
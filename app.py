
import os
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

# Set API key for OpenAI Service
os.environ['OPENAI_API_KEY'] = 'YOUR_OPEN_AI_KEY'

# Create an instance of OpenAI LLM
llm = OpenAI(temperature=0.1, verbose=True)
embeddings = OpenAIEmbeddings()
# Create and load PDF Loader
loader = PyPDFLoader('DDGuide.pdf')
# Split pages from pdf 
pages = loader.load_and_split()
# Load documents into vector database aka ChromaDB
store = Chroma.from_documents(pages, embeddings, collection_name='designdesigner')

# Create vectorstore info object
vectorstore_info = VectorStoreInfo(
    name="designdesigner",
    description="a digital designer's guide",
    vectorstore=store
)
# Convert the document store into a langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

# Add the toolkit to an end-to-end LC
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
st.title('👾 GPT Digital Design Engineer')
# Create a text input box for the user
prompt = st.text_input('Input your prompt here')

#Prompt logic
if prompt:
    response = agent_executor.run(prompt)
    st.write(response)
    
    with st.expander('Document Similarity Search'):
        # Find the relevant pages
        search = store.similarity_search_with_score(prompt) 
        # Write out the first 
        st.write(search[0][0].page_content) 



import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
from llama_index.llms import Ollama

st.set_page_config(page_title="Local: Chat with your own content!", layout="wide", initial_sidebar_state="auto", menu_items=None)

st.image("logo.png", width=400)
st.title("Your content + your local AI language model = your privacy.")
knowledgebase = st.text_input("You are interacting with the content in this folder:", value="data" )
system_prompt= st.text_area("Enter the role this AI assitant should play:" , value="You are my expert advisor. Assume that all questions are related to the data folder indicated above. For each fact you respond always include the reference document and page or paragraph. Keep your answers based on facts. Cite the source document next to each paragraph response you provide. Do not hallucinate features.")

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me a question:"}
    ]


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing docs – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir=knowledgebase, recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(embed_model="local", llm=Ollama(model="zephyr", temperature=0.5))  #try model="zephyr" for better but slower results.
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="context", verbose=True) #modes might be "condense_question" or "context" or "simple"

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            lenght_sources = len(response.source_nodes)
            with st.expander("Show References"):
                for i in range(lenght_sources):
                    st.write(response.source_nodes[i].metadata)
            
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history

import streamlit as st
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import WebBaseLoader

st.set_page_config(page_title="RAG Q&A", page_icon="🤖", layout="wide")
st.title("🔗 Link-based Q&A with RAG")


link = st.text_input("Paste a link (website/article):")
user_question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if link and user_question:
        with st.spinner("Processing..."):
            try:
                loader = WebBaseLoader(link)
                docs = loader.load()

                embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
                vectorstore = FAISS.from_documents(docs, embeddings)

                retriever = vectorstore.as_retriever()
                llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
                qa_chain = RetrievalQA.from_chain_type(
                    llm=llm,
                    retriever=retriever,
                    return_source_documents=True
                )

                result = qa_chain({"query": user_question})

                st.subheader("Answer")
                st.write(result["result"])

                with st.expander("Sources"):
                    for doc in result["source_documents"]:
                        st.markdown(f"- {doc.metadata.get('source', 'Unknown')}")

            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter both a link and a question.")

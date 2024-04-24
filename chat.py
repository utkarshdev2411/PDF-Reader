import streamlit as st
from PyPDF2 import PdfReade
from langchain.text_splitter import RecursiveSplitter
import os 

from langchain_google_genai import GoogleGenerativeAIEmbeddings

import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv 

load_dotenv()

genai.configure(api_keys=os.getenv("Google_API_KEY"))
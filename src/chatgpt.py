import os

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory

api_key = os.getenv("GPT_TOKEN")


llm = ChatOpenAI(openai_api_key=api_key, model='gpt-3.5-turbo')

conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory()
)

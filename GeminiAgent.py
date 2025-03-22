import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

class GeminiAgent:
    def __init__(self, MODE):
        self.api_key = os.environ.get("GOOGLE_API_KEY"),
        self.model = MODE.get("model")
        self.temperature = MODE.get("temperature")
        self.top_p = MODE.get("top_p")
        self.top_k = MODE.get("top_k")
        self.max_output_tokens = MODE.get("max_output_tokens")
        self.content = MODE.get("content")

        self.chat_model = ChatGoogleGenerativeAI(
            model= self.model,
            temperature= self.temperature,
            max_tokens= self.max_output_tokens,
            top_k= self.top_k,
            top_p= self.top_p
        )
        self.system_message = SystemMessage(
            content= self.content
        )

    def chat_response(self, user_input):
        chat_history = []
        messages = [self.system_message] + chat_history + [HumanMessage(content=f" *USER BUSINESS * {user_input}.")]
        # Generate response from Gemini
        response = self.chat_model(messages)
        reply = response.content
        # Print response
        print(f"Gemini: {reply}")
        # Store conversation history
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(response)
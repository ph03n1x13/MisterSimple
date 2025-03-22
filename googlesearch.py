import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()

class GoogleSearch:
    def __init__(self):
        self.model = 'gemini-2.0-flash'
        self.client = genai.Client(
            api_key=os.environ.get("GOOGLE_API_KEY"),
            # location='us-central1',
        )
        self.tools = [
            types.Tool(google_search=types.GoogleSearch())
        ]
        self.content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=1000,
        tools=self.tools,
        response_mime_type="text/plain",
    )


    def search_google(self, search_string):
        search_content = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(
                        text=f"{search_string}"),
                ],
            ),
        ]
        for chunk in self.client.models.generate_content_stream(
            model=self.model,
            contents=search_content,
            config=self.content_config,
            ):
            print(chunk.text, end='')
from googlesearch import GoogleSearch
from GeminiAgent import GeminiAgent
from config import  CODER_MODE, TEST_CASE_MODE

google_search_agent = GoogleSearch()

while True:
    user_input = input("\nPrompt: ")
    if user_input == "exit":
        print("Good Bye...")
        break
    elif user_input.startswith("search for "):
        search_string = user_input.replace("search for ", "")
        print(f"searching for google: {search_string}")
        google_search_agent.search_google(search_string)

    elif user_input.startswith("code for "):
        gemini_agent = GeminiAgent(CODER_MODE)
        print(f"Agent Mode Coder")
        chat_string = user_input.replace("code for ", "")
        gemini_agent.chat_response(chat_string)
        while True:
            user_input = input("Coder Mode: ")
            if user_input.startswith('exit'):
                break
            else:
                gemini_agent.chat_response(user_input)

    elif user_input.startswith("test case for "):
        gemini_agent = GeminiAgent(TEST_CASE_MODE)
        print(f"Agent Mode Test Case Writer")
        chat_string = user_input.replace("test case for ", "")
        gemini_agent.chat_response(chat_string)
        while True:
            user_input = input("Test Case Mode: ")
            if user_input.startswith('exit'):
                break
            else:
                gemini_agent.chat_response(user_input)

    else:
        print(f"{user_input} is not recognised")
        print("Options:\n search for <search string>\n"
              "code for <the code you want in Python>\n"
              "test case for <scenario>\n")

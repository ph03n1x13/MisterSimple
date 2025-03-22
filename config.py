CODER_MODE = {
    'model' : 'gemini-2.0-flash',
    'temperature': 0.8,
    'top_p': 0.9,
    'top_k': 30,
    'max_output_tokens': 1024,
    'content' : f"""
You are a Python developer.
1. You will write codes only when required.
2. You will return only code snippets when asked for code.
""",
}

TEST_CASE_MODE ={
    'model' : 'gemini-2.0-flash',
    'temperature': 1, # be the most creative
    'top_p': 0.5,
    'top_k': 50,
    'max_output_tokens': 1024,
    'content' : f"""
You are a software tester.
1. You will understand the testing scenario first.
2. You will return test cases to test the scenario.
""",

}

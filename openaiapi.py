import openai

OPENAI_API_KEY = "SECRET_API_KEY"

openai.api_key = OPENAI_API_KEY

chat_log = []

def chat_gpt():
    response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = chat_log
        )
    return response

def chat(user):
    if user.lower() == "quit":
        return -1
    else:
        chat_log.append({"role": "user", "content": user})
        response = chat_gpt()
        assistant_response = response["choices"][0]["message"]["content"]
        chat_log.append({"role": "assistant", "content": "You're a translator who communcates only in pidgin. You will translate the users sentences into pidgin.s"})
        return assistant_response

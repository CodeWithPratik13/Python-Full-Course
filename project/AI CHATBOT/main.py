from openai import OpenAI

key = " Api key"

messages = []

client = OpenAI(
    api_key= key,
)

def completion(message):
    global messages
    chat_completion = client.chat.completions.create( messages = messages,
    
        model = "gpt- 4o",
    )

    # print(chat_completion)
    message = {
        "role": "assistance",
        "content" : chat_completion.choices[0].message.Content
    }
    messages.append(message)
    print(f"jarvis: {message["content"]}")

if __name__ == "__main__":
    user_question = input(f"jarvis: Hi i am jarvis, How may i help you ?\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)
from openai import OpenAI

client = OpenAI()

# accepts the preferred model and messages list definition
# calls the openai api
# returns the response content
def get_api_chat_response_message(model, messages):

   # call API
   api_response = client.chat.completions.create(
        model= model,
        messages= messages
)
   # extracted response from api, assign it to a variable   
   response_content = api_response.choices[0].message.content

   # return the response content 
   return response_content

# user prompt to ask the question
user_input = input("\nAsk somting...\n\n")

# variables for the python function
model="gpt-3.5-turbo"

messages=[
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."}, 
    {"role": "user", "content": user_input}
]

# call the funtion, assign it to the variable response_for_user
response_for_user = get_api_chat_response_message(model, messages)

print("\n" + response_for_user + "\n")
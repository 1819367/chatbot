from openai import OpenAI

client = OpenAI()

# accepts the user content as a parameter
# attemps to define what kind of input the content is
def set_user_input_category(user_input):
   # determine if input is a question, create a dictionary
   question_keywords = ["who", "what", "when", "where", "why", "how", "?"]
   # search the user_input string for a substring of one of the keywords
   # set to lower case using .lower()
   for keyword in question_keywords:
      if keyword in user_input.lower():
         return "question"
   return "statement"

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
user_input = input("\nAsk something...\n\n")

# variables for the python function
model="gpt-3.5-turbo"

messages=[
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."}, 
    {"role": "user", "content": user_input}
]

# call the funtion, assign it to the variable response_for_user
response_for_user = get_api_chat_response_message(model, messages)

# tailored the output to the user
if set_user_input_category(user_input) == "question":
   response_for_user = "Good question! " + response_for_user

print("\n" + response_for_user + "\n")
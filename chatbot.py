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
# user_input = input("\nAsk something...\n\n") commented out for the plot_prompt

# variables for the python function
model="gpt-3.5-turbo"

plot_description = """In the heart of the bustling metropolis of Astoria, the old Henderson House stands as a
silent sentinel, its imposing facade a stark contrast to the modern skyscrapers that
surround it. Once a grand mansion, it now sits abandoned, its windows broken, its
once-luxurious gardens now a tangle of weeds and ivy. The house is said to be haunted, its
halls echoing with the whispers of a tragic past.

hen seventeen-year-old Mia Alvarez moves to Astoria with her family, she is immediately
drawn to the mystery of the old house. Despite the warnings of her new friends, Mia
becomes determined to uncover the truth behind the rumors that surround it.

As Mia delves deeper into the history of the Henderson House, she discovers a dark and
twisted tale. The house was once the home of the wealthy and influential Henderson
family, until one fateful night when a series of mysterious disappearances rocked the city.
The family was never seen again, and the house was left abandoned, a grim reminder of
the tragedy that had befallen it.

Determined to unravel the mystery, Mia enlists the help of her friends, including the
charming and enigmatic Alex. Together, they embark on a dangerous journey into the heart
of the city's dark underbelly, where they must confront not only the malevolent spirits that
haunt the Henderson House but also the sinister forces that seek to keep its secrets buried.

As they dig deeper, Mia and her friends uncover a web of lies and deceit that stretches
back decades, and they realize that the key to solving the mystery may lie closer to home
than they ever imagined. But with each step closer to the truth, they also draw closer to
danger, and Mia must confront her own fears if she is to uncover the secrets of the
Henderson House and escape its haunting legacy."""

# ask the model to summarize the plot description
# use f-string and """ for readability and reducing duplicate code 
# use special characters to tell the model to only refer to that text inside <>
plot_prompt = f"""

Summarize the text below in between < and >, in no more than 50 words.

<{plot_description}>

Refer to the book title "The Henderson House" in your summary. Write this as a single, continuous paragraph without any line breaks or verse structure. The summary should be a concise, flowing narrative capturing the main elements of the plot.
"""

# replaced user_input with plot_prompt in the message array for user
messages=[
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."}, 
    {"role": "user", "content": plot_prompt} 
]

# call the funtion, assign it to the variable response_for_user
response_for_user = get_api_chat_response_message(model, messages)

# tailored the output to the user
# if set_user_input_category(user_input) == "question":
#    response_for_user = "Good question! " + response_for_user

# commented out previous print statement
# print("\n" + response_for_user + "\n")


# updated the API call's variable name from response_for_user to book_dummary
book_summary = get_api_chat_response_message(model, messages)


# dictionary of book reviews as a list
book_reviews = [
   "I read The Forgotten House and found it to be average. The writing was decent, and the plot was somewhat engaging, but it didn't leave a lasting impression on me.",

   "I found The Forgotten House to be predictable and lacking in originality. The plot felt formulaic, and the characters were one-dimensional. Overall, a disappointing read.",

   "A thrilling tale that kept me on the edge of my seat! The author expertly weaves together mystery, suspense, and a touch of the supernatural. A must-read for fans of young adult fiction!",

   "The writing style of this book didn't resonate with me. I found it to be overly descriptive, which slowed down the pacing of the story. The characters also felt clichéd and uninteresting.",

   "I struggled to connect with the characters in this book. They felt flat and underdeveloped, which made it difficult to care about their fates. The plot, while intriguing, was ultimately let down by the lack of depth in the characters.",

   "I couldn't put this book down! The characters are relatable, the plot is engaging, and the setting is beautifully described. A captivating read from start to finish!",

   "The Forgotten House was an okay read. The story was interesting enough to keep me turning the pages, but I didn't feel particularly invested in the characters or the outcome.",

   "The Forgotten House is a hauntingly beautiful story that lingers long after the final page. The author's descriptive prose brings the city to life, while the mystery keeps you guessing until the end. Highly recommend!",

   "An atmospheric masterpiece! The author's vivid descriptions make you feel like you're right there in the city, exploring its secrets alongside the characters. A captivating and immersive read!",

   "While the premise of The Forgotten House was intriguing, I felt that the execution fell short. The story lacked depth and complexity, and the ending left me feeling unsatisfied. Overall, not a book I would recommend.",

   "The Forgotten House was an alright book. The premise was intriguing, but the execution fell a bit flat for me. I think it could have been more engaging with stronger character development.",

   "A gripping mystery with a supernatural twist! The characters are well-developed, the plot is fast-paced, and the setting is richly detailed. A definite must-read for fans of the genre!",

   "The Forgotten House started off strong, but I found the middle portion of the book to be slow and repetitive. The resolution felt rushed and unsatisfying, leaving me wanting more.",

   "I finished The Forgotten House and felt indifferent about it. The story was fine, but it didn't leave a lasting impression on me. It's a decent read if you're looking for something light."
]

# create an empty string
book_reviews_with_sentiments = []

for review in book_reviews:
   review_prompt = f"""

      Analyze the sentiment of the book review below, enlosed in tripple backticks.  
      Respond with a single word: either 'Positve' or 'Negative'.

      ```{review}```
      """
   review_messages = [
      {"role": "system", "content": "You are a sentiment analysis expert. Provide concise, accurate sentiment classifications."}, 
      {"role": "user", "content": review_prompt}
   ]

   sentiment = get_api_chat_response_message(model, review_messages).strip()

   book_reviews_with_sentiments.append({
      "review": review,
      "sentiment": sentiment
   })

# updated the print stateement to for book_summary
# print("\n\n" + book_summary + "\n\n")
# print(book_reviews_with_sentiments)

# Sentiment Analysis to generate email content

# new prompt asking the model to generate an email
# initialize an empty list to store positive reviews
positive_reviews = []

# loop through the book_reviews_with_sentiments to get just the positive reviews
for review in book_reviews_with_sentiments:
   if review['sentiment'] == 'Positive':
      positive_reviews.append(review['review'])

# join positive reviews into a single string
positive_reviews_text = "\n" .join(positive_reviews)

email_prompt = f"""
Generate an exciting email that will make people want to buy the book.  Use the following book summary and positive reviews:

Book Summary:
{book_summary}

Positive Reviews:
{positive_reviews_text}

Please include:
1. An engaging opening
2. Highlights from the book summary
3. Quotes from positive reviews
4. A compelling call-to-action to purchase the book
5. A friendly closing

Also, provide 10 different options for email subject lines at the end of your response.
"""
email_messages = [
      {"role": "system", "content": "You are a skilled marketing copywriter specializing in book promotions."}, 
      {"role": "user", "content": email_prompt}
   ]

email_content = get_api_chat_response_message(model, email_messages)
print("Generated Email content: ")
print(email_content)
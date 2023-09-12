import requests
from send_email import send_email

api_key = '9886cf5322904eb0af66f4133917f69b'
url = ('https://newsapi.org/v2/everything?q=tesla&'
       'from=2023-08-12&sortBy=publishedAt&'
       'apiKey=9886cf5322904eb0af66f4133917f69b')

# Make a request
request = requests.get(url)

# Get data as dictionary
content = request.json()

# Creating a txt file to store title and description of articles
filename = 'message-article.txt'
with open(filename, 'w+', encoding='utf-8') as file:
    for article in content['articles']:
        title = file.writelines(article['title'])
        description = file.writelines(article['description'])

# Sending a txt file to a provided email address
send_email(filename)
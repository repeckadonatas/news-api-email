import requests
from send_email import send_email

topic = 'tesla'

api_key = '9886cf5322904eb0af66f4133917f69b'
url = ('https://newsapi.org/v2/everything?'
       f'q={topic}&'
       'sortBy=publishedAt&'
       'apiKey=9886cf5322904eb0af66f4133917f69b&'
       'language=en')

# Make a request
request = requests.get(url)

# Get data as dictionary
content = request.json()

# '''Creating a txt file to store title and description of articles'''
#
# filename = 'message-article.txt'
# with open(filename, 'w+', encoding='utf-8') as file:
#     for article in content['articles']:
#         if article['title'] is not None:
#             title = file.writelines(article['title'] + '\n')
#             description = file.writelines(article['description'] + 2 * '\n')

body = ''
for article in content['articles'][:20]:
    if article['title'] is not None:
        body = ("Subject: Today's news" + '\n'
                + body + article['title'] + '\n'
                + article['description'] + '\n'
                + article['url'] + 2 * '\n')

body = body.encode('utf-8')

# Sending a txt file to a provided email address
send_email(body)

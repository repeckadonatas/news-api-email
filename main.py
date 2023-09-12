import requests

api_key = '9886cf5322904eb0af66f4133917f69b'
url = ('https://newsapi.org/v2/everything?q=tesla&'
       'from=2023-08-12&sortBy=publishedAt&'
       'apiKey=9886cf5322904eb0af66f4133917f69b')

# Make a request
request = requests.get(url)

# Get data as dictionary
content = request.json()

# Access the titles and descriptions of articles
for article in content['articles']:
    print(article['title'])
    print(article['description'])


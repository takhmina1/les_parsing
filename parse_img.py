import requests

image_url = 'https://images.unsplash.com/photo-1554080353-a576cf803bda?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8cGhvdG98ZW58MHx8MHx8&w=1000&q=80'

response = requests.get(image_url)

with open('image.jpg', 'wb') as f:
    f.write(response.content)

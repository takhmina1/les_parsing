
### 1. **Загрузка изображения и сохранение его на диск**

import requests

# URL изображения
image_url = 'https://images.unsplash.com/photo-1554080353-a576cf803bda?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8cGhvdG98ZW58MHx8MHx8&w=1000&q=80'

# Отправляем GET-запрос
response = requests.get(image_url)

# Проверяем, что запрос успешен
if response.status_code == 200:
    # Сохраняем изображение в файл
    with open('photo.jpg', 'wb') as file:
        file.write(response.content)
    print("Изображение успешно сохранено как 'photo.jpg'")
else:
    print(f"Ошибка при загрузке: {response.status_code}")




### 2. **Получение данных с API**

import requests

# URL API (пример API с JSON-ответом)
api_url = 'https://jsonplaceholder.typicode.com/posts/1'

# Отправляем GET-запрос
response = requests.get(api_url)

# Проверяем статус запроса и выводим данные
if response.status_code == 200:
    data = response.json()
    print("Полученные данные:")
    print(data)
else:
    print(f"Ошибка запроса: {response.status_code}")




### 3. **Скачивание текста с веб-страницы**

import requests

# URL страницы
page_url = 'https://www.example.com'

# Отправляем GET-запрос
response = requests.get(page_url)

# Проверяем статус запроса
if response.status_code == 200:
    print("Текст страницы:")
    print(response.text[:500])  # Выводим первые 500 символов текста
else:
    print(f"Ошибка запроса: {response.status_code}")






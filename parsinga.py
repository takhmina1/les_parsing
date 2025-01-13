

### Задание 1: Загрузка изображения из интернета

import requests

# URL изображения
image_url = 'https://images.unsplash.com/photo-1554080353-a576cf803bda?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8cGhvdG98ZW58MHx8MHx8&w=1000&q=80'

try:
    # Отправляем GET-запрос
    response = requests.get(image_url)
    # Проверяем статус запроса
    if response.status_code == 200:
        # Сохраняем изображение в файл
        with open('downloaded_image.jpg', 'wb') as file:
            file.write(response.content)
        print("Изображение успешно сохранено как 'downloaded_image.jpg'")
    else:
        print(f"Ошибка загрузки: код {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")




### Задание 2: Получение данных из API

import requests

# URL API
api_url = 'https://jsonplaceholder.typicode.com/posts/1'

try:
    # Отправляем GET-запрос
    response = requests.get(api_url)
    # Проверяем статус запроса
    if response.status_code == 200:
        # Выводим данные в формате JSON
        data = response.json()
        print("Полученные данные:")
        print(data)
    else:
        print(f"Ошибка запроса: код {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")




### Задание 3: Парсинг веб-страницы

import requests

# URL страницы
page_url = 'https://www.example.com'

try:
    # Отправляем GET-запрос
    response = requests.get(page_url)
    # Проверяем статус запроса
    if response.status_code == 200:
        print("Текст страницы (первые 500 символов):")
        print(response.text[:500])  # Выводим первые 500 символов текста
    else:
        print(f"Ошибка запроса: код {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")



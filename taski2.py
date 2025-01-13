import requests
from bs4 import BeautifulSoup

def parse_page(url):
    try:
        # Отправляем GET-запрос
        response = requests.get(url)
        
        # Проверяем успешность запроса
        if response.status_code == 200:
            print("Страница успешно загружена.")
            # Разбираем HTML с помощью BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Выводим текст страницы
            print("Текст страницы:")
            print(soup.get_text(separator='\n', strip=True))
            
            # Выводим отформатированный HTML-код страницы
            print("\nПолный HTML-код страницы:")
            print(soup.prettify())
        else:
            print(f"Ошибка загрузки страницы. Статус код: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")

# Пример URL для парсинга
url = 'https://kaktus.media/'
parse_page(url)



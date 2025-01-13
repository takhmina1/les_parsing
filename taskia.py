# import requests
# from bs4 import BeautifulSoup

# # URL страницы
# url = 'https://www.example.com'

# # Отправляем GET-запрос
# response = requests.get(url)

# # Проверяем успешность запроса
# if response.status_code == 200:
#     # Разбираем HTML-код
#     soup = BeautifulSoup(response.text, 'html.parser')
#     # Извлекаем заголовок
#     title = soup.title.string
#     print(f"Заголовок страницы: {title}")
# else:
#     print(f"Ошибка загрузки страницы: {response.status_code}")


    
    
import requests
from bs4 import BeautifulSoup

# URL страницы
url = 'https://kaktus.media/'

# Отправляем запрос
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Разбираем HTML с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Выводим весь текст страницы
    print("Текст страницы:\n")
    print(soup.get_text(separator='\n', strip=True))  # Вывод текста с разделением строк
    
    print("\nВсе данные страницы (HTML):\n")
    print(soup.prettify())  # Выводит отформатированный HTML код страницы
else:
    print(f"Ошибка при запросе страницы: {response.status_code}")



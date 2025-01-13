# Задача 1: Извлечение текста из HTML-тега
from bs4 import BeautifulSoup

html_content = "<html><body><h1>Welcome to Python!</h1></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение текста из тега <h1>
print(soup.h1.text)  # Вывод: Welcome to Python!
print()

# Задача 2: Извлечение всех ссылок (тегов <a>) на странице
html_content = """
<html>
<body>
    <a href="https://www.google.com">Google</a>
    <a href="https://www.python.org">Python</a>
</body>
</html>
"""
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение всех ссылок (href) на странице
links = soup.find_all('a')
for link in links:
    print(link.get('href'))  # Вывод: https://www.google.com, https://www.python.org
print()

# Задача 3: Извлечение всех изображений (тегов <img>) с атрибутами src
html_content = """
<html>
<body>
    <img src="image1.jpg" alt="Image 1">
    <img src="image2.jpg" alt="Image 2">
</body>
</html>
"""
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение всех атрибутов src из тегов <img>
images = soup.find_all('img')
for image in images:
    print(image.get('src'))  # Вывод: image1.jpg, image2.jpg
print()

# Задача 4: Извлечение содержимого таблицы
html_content = """
<html>
<body>
    <table>
        <tr>
            <td>Name</td>
            <td>Age</td>
        </tr>
        <tr>
            <td>Alice</td>
            <td>25</td>
        </tr>
        <tr>
            <td>Bob</td>
            <td>30</td>
        </tr>
    </table>
</body>
</html>
"""
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение всех строк таблицы
table_rows = soup.find_all('tr')
for row in table_rows:
    cols = row.find_all('td')
    for col in cols:
        print(col.text)  # Вывод: Name, Age, Alice, 25, Bob, 30
print()

# Задача 5: Извлечение данных с использованием CSS-селекторов
html_content = """
<html>
<body>
    <div class="content">
        <p class="text">Hello, World!</p>
        <p class="text">Welcome to BeautifulSoup!</p>
    </div>
</body>
</html>
"""
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение всех элементов с классом "text"
texts = soup.select('.text')
for text in texts:
    print(text.text)  # Вывод: Hello, World!, Welcome to BeautifulSoup!

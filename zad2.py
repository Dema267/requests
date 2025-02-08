import requests

# URL для получения постов
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса
params = {
    'userId': 1  # Фильтрация записей по userId, равному 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Проверка успешности запроса
if response.status_code == 200:
    # Вывод полученных записей в формате JSON
    posts = response.json()
    print("Полученные записи для userId=1:")
    for post in posts:
        print(post)
else:
    print(f"Ошибка при выполнении запроса: {response.status_code}")
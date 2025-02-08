import requests

# URL для поиска репозиториев на GitHub
url = "https://api.github.com/search/repositories"

# Параметры запроса
params = {
    'q': 'language:html'  # Поиск репозиториев с кодом на HTML
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Вывод статус-кода ответа
print("Status Code:", response.status_code)

# Вывод содержимого ответа в формате JSON
try:
    json_response = response.json()
    print("Response JSON:", json_response)
except ValueError:
    print("Response content is not in JSON format.")
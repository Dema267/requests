import requests

# URL для отправки POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Вывод статус-кода ответа
print("Status Code:", response.status_code)

# Вывод содержимого ответа в формате JSON
try:
    json_response = response.json()
    print("Response JSON:", json_response)
except ValueError:
    print("Response content is not in JSON format.")
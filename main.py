from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


# Интерфейс index.html
@app.route('/')
def index():
    return render_template('index.html')


# Получение ид и токена с от пользователя и отправка запроса на получение настроек
@app.route('/settings', methods=['POST'])
def settings():
    data = request.json
    idInstance = data.get('id')
    apiTokenInstance = data.get('token')

    url = f'https://api.green-api.com/waInstance{idInstance}/getSettings/{apiTokenInstance}'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text.encode('utf8')


# Получение ид и токена с от пользователя и отправка запроса на получение состояния
@app.route('/state', methods=['POST'])
def state():
    # Можно было убрать ид и токен в кортеж, но не было времени
    data = request.json
    idInstance = data.get('id')
    apiTokenInstance = data.get('token')

    url = f'https://api.green-api.com/waInstance{idInstance}/getStateInstance/{apiTokenInstance}'

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text.encode('utf8')


# Отправка сообщения на указанный номер
@app.route('/sendtxt', methods=['POST'])
def sendtxt():
    data = request.json
    idInstance = data.get('id')
    apiTokenInstance = data.get('token')

    # Не знал откуда вытащить ид чата
    chatId = data.get('chatId')
    message = data.get('message')

    url = f'https://api.green-api.com/waInstance{idInstance}/sendMessage/{apiTokenInstance}'

    payload = json.dumps({
        "chatId": chatId,
        "message": message
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text.encode('utf8')


# Отправка файла
@app.route('/sendfile', methods=['POST'])
def sendfile():
    data = request.json
    idInstance = data.get('id')
    apiTokenInstance = data.get('token')

    # Не знал откуда вытащить ид чата снова
    chatId = data.get('chatId')
    file = data.get('file')

    url = f'https://api.green-api.com/waInstance{idInstance}/sendFileByUrl/{apiTokenInstance}'

    payload = json.dumps({
        "chatId": chatId,
        "file": file
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text.encode('utf8')


if __name__ == '__main__':
    app.run(debug=True)

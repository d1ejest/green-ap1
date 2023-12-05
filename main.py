from flask import Flask, render_template, request, jsonify
from whatsapp_api_client_python import API

app = Flask(__name__)

# Объявим idInstance и apiTokenInstance глобальными переменными

USER = API.GreenApi(request.form['idInstance'], request.form['apiTokenInstance'])


# Интерфейс веб-приложения на index.html
@app.route('/')
def index():
    return render_template('index.html')

# Метод получения настроек
@app.route('/settings', methods=['POST'])
def settings():
    response = USER.getSettings()
    return jsonify({'answer': response.text.encode('utf8')})

# Метод получения состояния
@app.route('/state', methods=['POST'])
def state():
    response = USER.getStateInstance()
    return jsonify({'answer': response.text.encode('utf8')})

# Метод отправки сообщения
@app.route('/sendtxt', methods=['POST'])
def sendtxt():
    response = USER.sending.sendMessage('chatId', request.form['message'])
    return jsonify({'answer': response.text.encode('utf8')})

# Метод отправки файлов
@app.route('/sendfile', methods=['POST'])
def sendimage():
    url = request.form['url']
    filename = url.split('/')[-1]
    response = USER.sending.sendFileByUrl('chatId',url,filename)
    return jsonify({'answer': response.text.encode('utf8')})


if __name__ == '__main__':
    app.run(debug=True)
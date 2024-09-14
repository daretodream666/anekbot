
from flask import Flask, request, json
import vk
import random
import time

joke=[line.rstrip('\n') for line in open('/home/takemytea/mysite/jokes.txt')]
nails=open('/home/takemytea/mysite/nails.txt')
token = '2714c610b11d96a76ce1d7a267736b31d1d48efee8f927933f02820056cee578d7410db9a45cb6ea02676'
confirmation_token = 'c56061da'
access_token = '4864867679eb5dd6042cb2d0ffe2303d610cfa6e570fad381489364a01ac036273ccec89613844ec5916d'

app = Flask(__name__)

@app.route('/')
def work():
    return 'It works!'

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    elif data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        if data['object']['text'] == 'анекдот' or data['object']['text'] == 'Анек' or data['object']['text'] == 'анек' or data['object']['text'] == 'Анекдот':
            session = vk.Session()
            api = vk.API(session, v=5.92)
            peer_id = data['object']['from_id']
            jokenum=random.randint(0,29)
            api.messages.send(peer_id=str(peer_id), random_id=random.randint(-999999,999999), message='Ну, слушай анекдот.', access_token = access_token)
            time.sleep(2)
            api.messages.send(peer_id=str(peer_id), random_id=random.randint(-999999,999999), message=joke[jokenum], access_token = access_token)
            return 'ok'
        elif data['object']['text'] == '[club175438921|@anekbot27] анекдот' or data['object']['text'] == '[club175438921|@anekbot27] Анек' or data['object']['text'] == '[club175438921|@anekbot27] анек' or data['object']['text'] == '[club175438921|@anekbot27] Анекдот':
            session = vk.Session()
            api = vk.API(session, v=5.92)
            peer_id = data['object']['peer_id']
            jokenum=random.randint(0,29)
            api.messages.send(peer_id=str(peer_id), random_id=random.randint(-999999,999999), message='Ну, слушай анекдот.', access_token = access_token)
            time.sleep(2)
            api.messages.send(peer_id=str(peer_id), random_id=random.randint(-999999,999999), message=joke[jokenum], access_token = access_token)
            return 'ok'
        elif data['object']['text'] == 'Помощь' or data['object']['text'] == 'помощь':
            session = vk.Session()
            api = vk.API(session, v=5.92)
            user_id = data['object']['from_id']
            api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Ну, смотри.  Пишешь "Анекдот"- получаешь анекдот. Можешь отреагировать "ржу" или "не смешно". Ну вот и всё.', access_token = access_token)
        elif data['object']['text'] == 'Эщкере' or data['object']['text'] == 'эщкере':
            session = vk.Session()
            api = vk.API(session, v=5.92)
            user_id = data['object']['from_id']
            api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Не, ну бля, это бан', access_token = access_token)
            return 'ok'
        elif data['object']['text'] == 'ржу' or data['object']['text'] == 'Ржу':
            session=vk.Session()
            api=vk.API(session, v=5.92)
            user_id=data['object']['from_id']
            api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Я рад, что тебе понравился анекдот. Надеюсь, другой тебе тоже понравится', access_token = access_token)
        elif data['object']['text'] == 'Не смешно' or data['object']['text'] == 'не смешно':
            session=vk.Session()
            api=vk.API(session, v=5.92)
            user_id=data['object']['from_id']
            api.messages.send(user_id=str(user_id), random_id=random.randint(-9999999,999999), message='Ну, ничего не поделать. Может, другой анекдот тебе понравится?', access_token = access_token)
        elif data['object']['text'] == 'А гвозди?' or data['object']['text'] == 'а гвозди?' or data['object']['text'] == 'гвозди' or data['object']['text'] == 'Гвозди' or data['object']['text'] == 'а гвозди' or data['object']['text'] == 'А гвозди':
            session=vk.Session()
            api=vk.API(session, v=5.92)
            user_id=data['object']['from_id']
            api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Ха-ха, ты нашёл секретный анекдот!', access_token = access_token)
            time.sleep(2)
            api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Собирает мама сына в школу. Кладёт ему в рюкзак колбасу, хлеб и гвозди. Сын смотрит, спрашивает: -Мам, нафига? -Ну как нафига?! Проголодаешься-возьмешь колбасу, положишь на хлеб,и съешь. -А гвозди? -Так вот же они!', access_token = access_token)
        else:
            session = vk.Session()
            api = vk.API(session, v=5.92)
            user_id = data['object']['from_id']
            api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Воу, слушай, этот бот не для общения! Если хочешь пообщаться, обратись к моему создателю, @teafromhell', access_token = access_token)
    return 'ok'
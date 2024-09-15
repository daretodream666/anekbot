
from flask import Flask, request, json
import vk
import random
import time

from config import TOKEN, CONFIRMATION_TOKEN, ACCESS_TOKEN

joke=[line.rstrip('\n') for line in open('./mysite/jokes.txt')]
nails=open('./mysite/nails.txt')
token = TOKEN
confirmation_token = CONFIRMATION_TOKEN
access_token = ACCESS_TOKEN

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
        match data['object']['text'].lower():
            case "анекдот" | 'анек':
                session = vk.Session()
                api = vk.API(session, v=5.92)
                peer_id = data['object']['from_id']
                jokenum=random.randint(0,29)
                api.messages.send(peer_id=str(peer_id), random_id=random.randint(-999999,999999), message='Ну, слушай анекдот.', access_token = access_token)
                time.sleep(2)
                api.messages.send(peer_id=str(peer_id), random_id=random.randint(-999999,999999), message=joke[jokenum], access_token = access_token)
                return 'ok' 
            
            case "помощь":
                session = vk.Session()
                api = vk.API(session, v=5.92)
                user_id = data['object']['from_id']
                api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Ну, смотри.  Пишешь "Анекдот"- получаешь анекдот. Можешь отреагировать "ржу" или "не смешно". Ну вот и всё.', access_token = access_token)
            
            case "эщкере":
                session = vk.Session()
                api = vk.API(session, v=5.92)
                user_id = data['object']['from_id']
                api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Не, ну бля, это бан', access_token = access_token)
                return 'ok'
        
            case "ржу":
                session=vk.Session()
                api=vk.API(session, v=5.92)
                user_id=data['object']['from_id']
                api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Я рад, что тебе понравился анекдот. Надеюсь, другой тебе тоже понравится', access_token = access_token)

            case "не смешно":
                session=vk.Session()
                api=vk.API(session, v=5.92)
                user_id=data['object']['from_id']
                api.messages.send(user_id=str(user_id), random_id=random.randint(-9999999,999999), message='Ну, ничего не поделать. Может, другой анекдот тебе понравится?', access_token = access_token)

            case "а гвозди?" | "гвозди" | "а гвозди":
                session=vk.Session()
                api=vk.API(session, v=5.92)
                user_id=data['object']['from_id']
                api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Ха-ха, ты нашёл секретный анекдот!', access_token = access_token)
                time.sleep(2)
                api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message=nails, access_token = access_token)
            case _:
                session = vk.Session()
                api = vk.API(session, v=5.92)
                user_id = data['object']['from_id']
                api.messages.send(user_id=str(user_id), random_id=random.randint(-999999,999999), message='Воу, слушай, этот бот не для общения! Если хочешь пообщаться, обратись к моему создателю, @teafromhell', access_token = access_token)
    return 'ok'
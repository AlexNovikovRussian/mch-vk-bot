import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from bs4 import BeautifulSoup as BS
import asyncio
from requests_html import HTMLSession

token = "0a8ce9d4fcf0b00bd08a6e4ce6110479c1108c4c9ceeb2f3c847443e80a18b3e300855317f2db97cf07b8"

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

def send_message(id, message):
    print("send "+message)
    vk.method('messages.send', {'user_id': id, 'message': message, "v":'5.69'})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            if(request == "/get"):

                print("/get command")

                s = HTMLSession()

                print("inited new session")

                payload = {

                    "isDelayed" : "false",
                    "login" : "+79775543041",
                    "password" : "14121416alex9",
                    "notRememberMe" : "false"

                }
                b = s.post("https://login.mos.ru/sps/login/methods/password", data = payload)
                b.html.render(timeout=30000)
                print("getted mos.ru cookies")

                resp = s.get("https://dnevnik.mos.ru")
                print('getted dnevnik page')
                resp.html.render(timeout=30000)
                print('rendered dnevnik page')

                bs_dm = BS(resp.html.html, "html.parser")
                link = bs_dm.select('a[href*=\'login.mos.ru\']')[0]['href']
                print("dnevnik parsed")
                send_message(event.user_id, link)

            else:
                print("sth else")
                send_message(event.user_id, "Ты ввёл что-то не то! Попробуй ещё раз.")



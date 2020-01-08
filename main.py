import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from bs4 import BeautifulSoup as BS
from selenium import webdriver

dr = webdriver.Chrome()
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

				dr.get("https://www.mos.ru/pgu/ru/services/procedure/0/0/7700000010000187206/")

				el = dr.find_elements_by_xpath("//*[contains(text(), 'Получить услугу')]")
				el[0].click()

				l = dr.find_element_by_id('login')
				l.send_keys("+79775543041")

				l = dr.find_element_by_id('password')
				l.send_keys("14121416alex9")

				l = dr.find_element_by_id('bind')
				l.submit()

				send_message(event.user_id, "done")

            else:
                send_message(event.user_id, "Ты ввёл что-то не то! Попробуй ещё раз.")


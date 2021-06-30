from vk_api import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time, datetime, os

os.system('clear')

attachments, log, crash = '', 0, 0


def Auth():
	global vk_session, vk, longpoll, crash
	crash += 1
	vk_session = vk_api.VkApi(app_id = 2274003, token = '', scope = 'messages');
	vk = vk_session.get_api()
	longpoll = VkLongPoll(vk_session)

	print(f"\n > Подключение к серверу [{crash}] < \n")

Auth()

while True:
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW and event.to_me:

			log += 1

			massage = vk.messages.getDialogs(count = 20, unread = 1)
			print(massage)

			date = datetime.datetime.fromtimestamp(massage['items'][0]['message']['date'])
			data = date.strftime('%H:%M')
			text = massage['items'][0]['message']['body']
			user_id = int(massage['items'][0]['message']['user_id'])

			if user_id > 0:
					user = vk_session.method("users.get", {"user_ids": user_id})
					user_name = user[0]['first_name'] +  ' ' + user[0]['last_name']
			else:
				user_name = 'Сообщество'

			try:
				massage['items'][0]['message']['attachments']
				attachments_status = 1
			except:
				attachments_status = 0

			if attachments_status == 1:
				attachments = massage['items'][0]['message']['attachments'][0]['type']

			else:
				attachments = ''

			if massage['items'][0]['message']['body'] != '' and attachments_status == 0:
				log += 1

				print(f"> [{user_name} | {data} | log: {log}] Сообщение: {text} ")

				try:
					file = open("log.txt", "a", encoding = "utf-8")
					file.write(f"\n\n> [{user_name} ({user_id}) | {data} | log: {log}] Сообщение: {text} ")
					file.close()
				except:
					pass

			if attachments == 'photo':
				url = massage['items'][0]['message']['attachments'][0]['photo']['sizes'][-1]['url']

				if massage['items'][0]['message']['body'] != '':
					print(f"> [{user_name} | {data} | log: {log}] Сообщение: {text} (photo) ")

					try:
						file = open("log.txt", "a", encoding = "utf-8")
						file.write(f"\n\n> [{user_name} ({user_id}) | {data} | log: {log}] URL: {url} ")
						file.close()
					except:
						pass

				else:
					print(f"> [{user_name} | {data} | log: {log}] (photo) ")

					try:
						file = open("log.txt", "a", encoding = "utf-8")
						file.write(f"\n\n> [{user_name} ({user_id}) | {data} | log: {log}] URL: {url} ")
						file.close()
					except:
						pass

			if attachments == 'video':
				url = massage['items'][0]['message']['attachments'][0]['video']['player']

				if massage['items'][0]['message']['body'] != '':
					print(f"> [{user_name} | {data} | log: {log}] Сообщение: {text} (video) ")

					try:
						file = open("log.txt", "a", encoding = "utf-8")
						file.write(f"\n\n> [{user_name} ({user_id}) | {data} | log: {log}] URL: {url} ")
						file.close()
					except:
						pass

				else:
					print(f"> [{user_name} | {data} | log: {log}] (video) ")

					try:
						file = open("log.txt", "a", encoding = "utf-8")
						file.write(f"\n\n> [{user_name} ({user_id}) | {data} | log: {log}] URL: {url} ")
						file.close()
					except:
						pass

			if attachments == 'doc':
				url = massage['items'][0]['message']['attachments'][0]['doc']['url']

				if massage['items'][0]['message']['body'] != '':
					print(f"> [{user_name} | {data} | log: {log}] Сообщение: {text} (document) ")

					try:
						file = open("log.txt", "a", encoding = "utf-8")
						file.write(f"\n\n> [{user_name} ({user_id}) | {data} | log: {log}] Сообщение: {text} (URL: {url}) ")
						file.close()
					except:
						pass

				else:
					print(f"> [{user_name} | {data} | log: {log}] (document) ")

					try:
						file = open("log.txt", "a", encoding = "utf-8")
						file.write(f"\n\n> [{user_name} ({user_id}) | {data} | log: {log}] URL: {url} ")
						file.close()
					except:
						pass

			if attachments == 'sticker':
				url = massage['items'][0]['message']['attachments'][0]['sticker']['images'][0]['url']
				print(f"> [{user_name} | {data} | log: {log}] (sticker) ")

				try:
					file = open("log.txt", "a", encoding = "utf-8")
					file.write(f"\n\n> [{user_name} ({user_id}) | {data} | log: {log}] URL: {url} ")
					file.close()
				except:
					pass

			if attachments == 'audio_message':
				url = massage['items'][0]['message']['attachments'][0]['audio_message']['link_mp3']
				print(f"> [{user_name} | {data} | log: {log}] (audio_message) ")

				try:
					file = open("log.txt", "a", encoding = "utf-8")
					file.write(f"\n\n> [{user_name} ({user_id}) | {data} | log: {log}] URL: {url} ")
					file.close()
				except:
					pass

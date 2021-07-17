from lxml import html
import requests
from datetime import datetime
import info

dic = {
"۰":"0",
"۱":"1",
"۲":"2",
"۳":"3",
"۴":"4",
"۵":"5",
"۶":"6",
"۷":"7",
"۸":"8",
"۹":"9"
}

numbers = [str(i) for i in range(0, 10)]
cpital_word = [chr(i) for i in range(ord('a'), ord('z') + 1)]
small_word = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
alfa = numbers + small_word + cpital_word + [" "]

def write_log(text):
	with open('logfile.txt', 'a') as file:
		file.write(text + '\n')	

def send_sms(message):
	print('Sending SMS...')
	url = 'https://api.kavenegar.com/v1/%s/sms/send.json' % info.key
	Data = {'receptor' : info.receptor,'message':message}
	r = requests.post(url, data = Data)
	if r.ok:
		print("Send SMS To " + info.receptor)

def del_word_fa(string):
	new_word = ""
	for str in string:
		for char in alfa:
			if str == char:
				new_word += char
	return new_word

def conver_number(num):
	new_num = ""
	for i in num:
		try:
			new_num += dic[i]
		except:
			pass
	return int(new_num)	

for url, buy in info.phones.items():
	try:
		page = requests.get(url)
		content = html.fromstring(page.content)
		data = content.xpath('//*[@id="0"]/text()')
		name = del_word_fa(data[1])
		sell = conver_number(data[3])
		if sell <= buy:
			str = name + ' sell ' + str(sell) + ' buy ' + str(buy) +'  At  '+ 					datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			send_sms(str)
			write_log(str)
		else:
			write_log('!!! Not Buy Now ' + name + " sell: " + str(sell) + '  At  ' + 					datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '!!!')   
	except:
		write_log('Not Internet At ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


from lxml import html
import requests
from datetime import datetime

receptor = ''
key = ''


def send_sms(message):
	print('Sending SMS...')

	url = 'https://api.kavenegar.com/v1/%s/sms/send.json' % key
	Data = {'receptor' : receptor,'message':message}

	r = requests.post(url, data = Data)
	if r.ok:
		print("Send")	

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

phones = {'https://torob.com/p/b48f4c3d-1930-498f-a9d1-02880aca8565/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C-redmi-note-9t-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/':4300000

,'https://torob.com/p/7e77eb0b-fb7c-43ca-82e8-ac2d95cbb5ab/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C-poco-x3-pro-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/':5300000

,'https://torob.com/p/04c12e43-b901-4a93-a0ec-6a2fa9ddd93d/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C-redmi-9t-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/':3000000

,'https://torob.com/p/1cc174ed-11cd-4d9a-b205-d9dc3f2afe51/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C-poco-m3-pro-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-6-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/':4300000

,'https://torob.com/p/d0149344-4a4e-4e73-910b-da19a4211e44/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B4%DB%8C%D8%A7%DB%8C%D9%88%D9%85%DB%8C-redmi-note-10-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-128-%D8%B1%D9%85-4-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/':4300000
}

for url, buy in phones.items():
	try:
		page = requests.get(url)
		content = html.fromstring(page.content)
		data = content.xpath('//*[@id="0"]/text()')
		name = del_word_fa(data[1])
		sell = conver_number(data[3])
		if sell <= buy:
			send_sms(name + ' sell ' + str(sell) + ' buy ' + str(buy) +'  At  '+ 					datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
		else:
			print('!!! Not Buy Now ' + name + " sell: " + str(sell) + '  At  ' + 					datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   
	except:
		print('Not Internet At ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

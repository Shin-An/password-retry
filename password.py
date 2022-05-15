# 密碼重試程式
# password = 'a123456'
# 讓使用者重複【最多輸入3次密碼】
# 對的話，就印出"登入成功!"
# 不對的話，就印出"密碼錯誤! 還有__次機會!"

# i = 3
# while i >= 0:
#	password = input('請輸入密碼: ')
#	if password == 'a123456':
#		print('登入成功!')
#		break
#	elif password != 'a123456':
#		i = i - 1
#		print('密碼錯誤!還有', i, '次機會!')
#		if i == 0:
#			break
# 產生結果 試第三次密碼時，會印出還有0次機會

# solve:
password = 'a123456'
i = 3
while i > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break # 逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會!')

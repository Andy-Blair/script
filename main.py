#coding:utf-8
import os
while True:
	user_se = raw_input("1.Backup    2.Update\nPlease Select Number(q for Quit):")
	if not user_se.strip() or user_se == 'q':
		exit()
	elif user_se == '1':
		import backup
	elif user_se == '2':
		import update
	elif user_se != '1' or '2':
		print 'please input a right number!'
	else:
		try:
			err_num = int(user_se)
		except(ValueError,KeyError):
			print 'please input a right number!'
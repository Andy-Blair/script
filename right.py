#coding:utf-8
import shutil
import os
webdir = {'AdviserWeb':'D:\ETS3.0\AdviserWeb','AppService':'D:\ETS3.0\AppService'}
dirlist = []
while True:
	user_se = raw_input("1.Backup    2.Update\nPlease Select Number(q for Quit):")
	if not user_se.strip() or user_se == 'q':
		exit()
	elif user_se == '1':
		print 'AdviserWeb    AppService'#输出所有站点
		user_se = raw_input("Input WebName:")
		for path,dir,flist in os.walk(webdir[user_se]):
			dirlist.append(path)
		num = range(1,len(dirlist)+1)
		dic = dict(map(lambda x,y:[x,y],num,dirlist))#用工厂方法把选择的站点的目录列举出来
		print dic
		while True:
			user_num = raw_input("Input Director Number('q' for Quit):")
			if not user_num.strip() or user_num == 'q':
				break
			else:
				try:
					user_num = int(user_num)
					shutil.copytree(dic[user_num],os.path.join('e:/',os.path.splitdrive(dic[user_num])[1]))#'e'是盘符
				except (ValueError,KeyError,NameError):
					print 'Please Input a Right dir_number!'
					
	elif user_se == '2':
		# shutil.copytree(os.path.join('e:/update/',os.path.splitdrive(dic[user_num])[1]),dic[user_num])
		print dic
	elif user_se != '1' or '2':
		print 'please input a right number!'
	else:
		try:
			err_num = int(user_se)
		except(ValueError,KeyError):
			print 'please input a right number!'
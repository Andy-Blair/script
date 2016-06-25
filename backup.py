# coding:utf-8
import shutil
import os
print 'web1    web2'
webdir = {'web1':'d:\\web\\web1','web2':'d:\\web\\web2'}
dirlist = []
user_se = raw_input("Input WebName:")
for path,dir,flist in os.walk(webdir[user_se]):
	dirlist.append(path)
num = range(1,len(dirlist)+1)
dic = dict(map(lambda x,y:[x,y],num,dirlist))#���ù�����������һ���ֵ�
#if user_se == 'web2':
#	for w2path,w2d,w2list in os.walk(web2):
#		web2list.append(w2path)
#	#print web2list
#	w2num = range(1,len(web2list)+1)
#	dic = dict(map(lambda x,y:[x,y],w2num,web2list))
print dic
user_num = 'a'
while user_num.strip():
	user_num = raw_input("Input Director Number('q' for Quit):")
	if not user_num.strip() or user_num == 'q':
		break
	else:
		try:
			user_num = int(user_num)
			shutil.copytree(dic[user_num],os.path.join('e:/',os.path.splitdrive(dic[user_num])[1]))#'e'���̷�
		except (ValueError,KeyError):
			print 'Please Input a Right dir_number!'
	user_num = str(user_num)

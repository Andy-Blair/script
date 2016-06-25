import os
only_s = []
only_d = []
source = 'd:/1/'
destination = 'e:/1/'
sour = os.listdir(source)
dest = os.listdir(destination)
for s in sour:
	if not s in dest:
		only_s.append(os.path.join(source,s))
for d in dest:
	if not d in sour:
		only_d.append(os.path.join(destination,d))
diff_file = file('e:/diff_file.txt','w')
print >> diff_file,"only in source:%s\nonly in destination:%s"%(only_s,only_d)
diff_file.close()
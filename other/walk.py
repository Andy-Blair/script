import os
only_s = []
only_d = []
sour = []
dest = []
source = 'd:\\1'
destination = 'e:\\1'
for path,d,flist in os.walk(source):
	for fname in flist:
		sour.append(os.path.join(path,fname))
for path,d,flist in os.walk(destination):
	for fname in flist:
		dest.append(os.path.join(path,fname))
for s in sour:
	if not s in dest:
		only_s.append(s)
for d in dest:
	if not d in sour:
		only_d.append(d)
diff_file = file('e:/diff.txt','w')
print >> diff_file,"only in source:%s\nonly in destination:%s"%(only_s,only_d)
diff_file.close()
# coding:utf-8
# 只压缩一级目录中的文件和文件夹
import zipfile
import os
z = zipfile.ZipFile("d:\\test.zip", 'w')
testdir = 'd:\\config'
for d in os.listdir(testdir):
    z.write(testdir+os.sep+d)
z.close()

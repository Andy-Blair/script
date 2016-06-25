# coding:utf-8
# 压缩指定目录下所有文件以及子目录中文件
import os
import zipfile
f = zipfile.ZipFile('d:\\archive.zip', 'w', zipfile.ZIP_DEFLATED)
startdir = "d:\\config"
# 在for循环中使用os模块的walk方法遍历指定文件夹下的每一级目录
for dirpath, dirnames, filenames in os.walk(startdir):
    for filename in filenames:
        f.write(os.path.join(dirpath, filename))
f.close()

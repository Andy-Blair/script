# -*- coding: utf-8 -*-
import os
import zipfile
import time


def zip_w(zip_dir):
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    zip_path = zip_dir.split("\\")
    # 通过判断压缩的文件路径，确保压缩文件名显示正常
    if zip_path[1]:
        zip_filename = zip_path[1]
    else:
        zip_filename = zip_path[0].split(':')[0].upper()
    z = zipfile.ZipFile(zip_filename + '_' + date + '.zip', 'w', zipfile.ZIP_DEFLATED)
    if os.path.isdir(zip_dir):
        for dir_path, dir_names, file_names in os.walk(zip_dir):
            for file_name in file_names:
                z.write(os.path.join(dir_path, file_name))
    else:
        z.write(zip_dir)
    z.close()


os.system('cls')
while True:
    Dir_IN = raw_input('备份文件（结束[E]）:').strip('\"\'\\')
    if os.path.isdir(Dir_IN) or os.path.isfile(Dir_IN):
        zip_w(Dir_IN)
    elif Dir_IN.upper() == "E":
        break
    else:
        print "输入无效，重新输入"
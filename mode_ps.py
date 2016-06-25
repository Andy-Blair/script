# coding:utf-8
import psutil
import datetime
mem = psutil.virtual_memory()
print mem.total / 1024 / 1024
print mem.used / 1024 / 1024
print mem.free / 1024 / 1024
print psutil.cpu_count()
print psutil.cpu_times()
print psutil.disk_partitions()
print psutil.users()
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(("%Y-%m-%d %H:%M:%S"))

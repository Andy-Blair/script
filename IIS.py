# -*- coding: utf-8 -*-
import os
import re


# web站点列表（列表）
def web_list():
    web = re.findall(r'\"([^"]+)\"', os.popen('c:\\Windows\\System32\\inetsrv\\appcmd.exe list site').read())
    return web


# web站点对应的本地目录（字典）
def web_dir():
    webs_list = web_list()
    vir_dir = re.findall(r'\(([^()]+)\)', os.popen('c:\\Windows\\System32\\inetsrv\\appcmd.exe list vdir').read())
    vd_list = []
    for phy_path in vir_dir:
        """""
        if p.find("%SystemDrive%") != -1:
            vd_list.append(p.replace("%SystemDrive%","c:").split(':',1)[1])
        else:
            vd_list.append(p.split(':', 1)[1])
        """""
# 这个语句与上文if可以达到同样效果，因为列表【vdir】中只有一个“%SystemDrive%”
        vd_list.append(phy_path.replace("%SystemDrive%", "c:").split(':', 1)[1])
    webs_dir = dict(zip(webs_list, vd_list))
    return webs_dir

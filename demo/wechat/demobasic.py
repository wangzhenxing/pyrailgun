#    coding: UTF-8
#    User: princehaku
#    Date: 13-2-12
#    Time: 1:01
#
__author__ = 'haku'
from pyrailgun import RailGun
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

railgun = RailGun()

railgun.setTask(file("basic.json"))
railgun.fire();
nodes = railgun.getShells()
file = file("./result.txt", "w+")
for id in nodes:
    node = nodes[id]
    file.write(node.get('name', [""])[0] + "\n")
    file.write(node.get('view_count', [""])[0] + "\n")
    file.write(node.get('types', [""])[0] + "\n")
    file.write(node.get('author', [""])[0] + "\n")
    file.write(node.get('publish_time', [""])[0] + "\n")
    file.write(node.get('require', [""])[0] + "\n")
    file.write(node.get('qrcode', [""])[0] + "\n")
    file.write(node.get('introduction', [""])[0] + "\n")
    file.write(node.get('img_logo', [""])[0] + "\n")
    file.write(node.get('img_show', [""])[0] + "\n=========\n")


#"url": "http://xcx.9.cn/app/${0,1}${0,1,2,3,4,5,6,7,8,9}${0,1,2,3,4,5,6,7,8,9}${0,1,2,3,4,5,6,7,8,9}${0,1,2,3,4,5,6,7,8,9}",

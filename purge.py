# pip  install pyyaml == 5.3.1
import yaml
import os

fileNamePath = os.path.split(os.path.realpath(__file__))[0]
yamlPath = os.path.join(fileNamePath,'./friends/friends.yml')
f = open(yamlPath,'r',encoding='utf-8')
cont = f.read()
x = yaml.load(cont, Loader=yaml.FullLoader)
items=x[1]['items']

for i in items:
    print(i['url'])

    shell= "curl https://purge.jsdelivr.net/gh/MHG-LAB/friends-gallery@gh-page/img/"+i['title']+".jpg"
    d=os.popen(shell)
    print(shell)
    f=d.read()
    print(f)






#!/usr/bin/python3
import requests, json, os,feedparser
from urllib import parse
from datetime import  datetime
url = 'http://192.168.101.8:5244/api'
UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
Authorization=''

headers = {
    'UserAgent': UserAgent,
    'Authorization': Authorization
}

ct_json = {
    'Content-Type': 'application/json'
}

def log(text):
	logfile=open('log.txt','a')
	time= datetime.now().strftime("%y/%m/%d | %H:%M:%S")
	content=time+' '+text
	logfile.write(content+'\n')
	print(content)
	logfile.close()

# 通过用户名、密码获取 token
def getToken(username, password):
    data = {
        'username': username,
        'password': password
    }
    log('Login AList')
    try:
        return json.loads(requests.post(f'{url}/auth/login', data=json.dumps(data), headers={'Content-Type': 'application/json'}).text)
    except Exception as e:
        log('Login AList Error!')
        return {'code': -1, 'message': e}


def Aria2(path,durl):
    data = { 
    'path': path,
    'urls':[durl]
      }
    log('AList to Aria, path:'+path+', url:'+durl)
    try:
        return json.loads(requests.post(f'{url}/fs/add_aria2', data=json.dumps(data), headers=dict(headers, **ct_json)).text)
    except Exception as e:
        return {'code': -1, 'message': e}

Authorization=getToken('admin','I7KsovEB')
headers = {
    'UserAgent': UserAgent,
    'Authorization': str(Authorization)[55:-3]
}
f = open("token.txt", "w")
f.write(str(Authorization)[55:-3])
f.close()

#print(Aria2("/OD E5 (Anime)/新番订阅",'https://mikanime.tv/Download/20230713/f3f2c3f0e545ed7f20ab487db34dda9a5d8f4302.torrent'))

def toaria2(title,index,content):
	num=len(content.entries)-int(index)
	for i in range(len(content.entries)):
		entries = content['entries'][i]
		Aria2('/OD E5 (Anime)/'+title,'magnet:?xt=urn:btih:'+str(entries).split('magnet:?xt=urn:btih:')[1].split("\'")[0])
		if i+1 ==num:
			break




def getrssupdate(rssurl):
	content=feedparser.parse(rssurl)
	return content
def getindexupdate(content):
	return len(content.entries)

dir=os.getcwd()+'/rss'
flist=os.listdir(dir)
log('Find Rss Files:'+str(flist))
text_list = []
for file in flist:
  with open(os.path.join(dir, file),"r", encoding="UTF-8") as f:
   	    	text_list.append(f.read())
log('Start  Rss Queue')
for i in range(len(text_list)):
	content=text_list[i]
	index=content.split(',')[0]
	url=content.split(',')[1]
	title=flist[i].split('.')[0]
	content=getrssupdate(url)
	if int(getindexupdate(content)) > int(index):
		f = open(dir+'/'+title+".txt", "w")
		f.write(str(len(content.entries))+','+url)
		f.close()
		toaria2(title,index,content)
		index=getindexupdate(content)
	log('Start checking for updates:['+str(title)+"],newindex="+str(index)+",updateurl="+str(url))

log('All Done!')

import requests, json, os
from  loger import log
from urllib import parse

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

# 新建文件夹
def MakeDir(path):
    data = { 'path': path }
    log('MakeDir: '+path)
    try:
        return json.loads(requests.post(f'{url}/fs/mkdir', data=json.dumps(data), headers=dict(headers, **ct_json)).text)
    except Exception as e:
        log('MakeDir Error!')
        return {'code': -1, 'message': e}
        
# 上传文件
def Upload(localPath, remotePath, fileName, password = ''):
    upload_header = {
        'UserAgent': UserAgent,
        'Authorization': Authorization,
        'File-Path': parse.quote(f'{remotePath}/{fileName}'),
        'Password': password,
        'Content-Length': f'{os.path.getsize(localPath)}'
    }
    try:
        return json.loads(requests.put(f'{url}/fs/put', headers=upload_header, data=open(localPath, 'rb').read()).text)
    except Exception as e:
        return {'code': -1, 'message': e}
        
def Aria2(path,durl):
    data = { 
    'path': path,
    'urls':[durl],
    "tool": "aria2",
    "delete_policy": "delete_on_upload_succeed"
      }
    log('AList to Aria, path:'+path+', url:'+durl)
    try:
        return json.loads(requests.post(f'{url}/fs/add_offline_download', data=json.dumps(data), headers=dict(headers, **ct_json)).text)
    except Exception as e:
        return {'code': -1, 'message': e}


def toaria2(title,index,content):
	num=len(content.entries)-int(index)
	for i in range(len(content.entries)):
		entries = content['entries'][i]
		Aria2('/OD E5 (Anime)/'+title,'magnet:?xt=urn:btih:'+str(entries).split('magnet:?xt=urn:btih:')[1].split("\'")[0])
		if i+1 ==num:
			break

Authorization=getToken('admin','I7KsovEB')
headers = {
    'UserAgent': UserAgent,
    'Authorization': str(Authorization)[55:-3]
}

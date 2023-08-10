import os,feedparser,func
from  loger import log
from func import toaria2
from datetime import  datetime

def getrssupdate(rssurl):
	content=feedparser.parse(rssurl)
	return content
def getindexupdate(content):
	return len(content.entries)

dir=os.getcwd()+'/rss'
flist=os.listdir(dir)
log('Start Check Rss Files:'+str(flist))
text_list = []
for file in flist:
  with open(os.path.join(dir, file),"r", encoding="UTF-8") as f:
   	    	text_list.append(f.read())
log('Read  Rss Queue')
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

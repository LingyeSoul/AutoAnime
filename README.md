# AutoAnime
+ AutoAnime is a simple Python script that makes an Rss subscription and pushes Alist offline downloads. 
+ AutoAnime是一个用于订阅Rss并推送Alist离线下载的Python脚本
# Setup
1. 确认已安装Python3，并且使用pip3安装了feedparser,requests,json库
  Confirm that Python 3 is installed and that the feedparser, requests, and JSON libraries are installed using pip3
2. 随后下载AutoAnime.py，并在当前文件夹新建名为rss的文件夹，在rss文件夹内新增订阅"title.txt"
  Then download the AutoAnime. Py, create a new folder named RSS in the current folder, and add the subscription "title. Txt" "in the RSS folder
3. 编辑AutoAnime.py修改第四行的url指向的API地址
  Edit the AutoAnime. Py to modify the API address pointed to by the URL in the fourth line
4. "title.txt"的title为订阅的番剧标题，文件内容应为"i,url"，其中i为集数，初次订阅请填0,url为RSS订阅地址，然后就可以享受了
  The title of "title.txt" is the title of the subscribed drama, the file content should be "i, url", where i is the number of episodes, please fill in 0 for the first subscription, url is the RSS subscription address, and then you can enjoy it

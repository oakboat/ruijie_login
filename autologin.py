import json
import re
from urllib import request
from tkinter import messagebox

filename = "info.json"
with open(filename, "r") as f:
    info = json.load(f)
    account = info["name"]
    password = info["password"]
captiveReturnCode = request.urlopen("http://www.google.cn/generate_204").getcode()
if captiveReturnCode == 204:
    messagebox.showinfo(title="恭喜", message="你已连接网络，无需登录")
else:
    loginPageURL = request.urlopen("http://www.google.cn/generate_204").read().decode()
    loginPageURL = re.search(r"'(.*)'", loginPageURL).group(1)
    loginURL = loginPageURL.split("?")[0].replace("index.jsp", "InterFace.do?method=login")
    queryString = loginPageURL.split("?")[1]
    data = "userId=" + account + "&password=" + password +"&service=&queryString=" + queryString + "&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false"
    postdata = data.encode()
    req = request.Request(loginURL, data=postdata)
    resp = request.urlopen(req).read().decode()
    resp = json.loads(resp)["message"]
    if resp == "":
        messagebox.showinfo(title="提示", message="登录成功")
    else:
        messagebox.showinfo(title="提示", message=resp)
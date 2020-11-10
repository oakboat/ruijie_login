import tkinter
from tkinter import messagebox
import json
import re
from urllib import request

def login():
  with open(filename, "w") as f:
    info = {
      "name": eN.get(),
      "password": eP.get()
    }
    json.dump(info, f)
  account = eN.get()
  password = eP.get()
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

filename = "info.json"
root = tkinter.Tk()
root.geometry("500x300")
root.title("校园网登录器")
lN = tkinter.Label(root, text="账号")
lN.pack()
vN = tkinter.StringVar(root, value="")
eN = tkinter.Entry(root, textvariable=vN)
eN.pack()
lP = tkinter.Label(root, text="密码")
lP.pack()
vP = tkinter.StringVar(root, value="")
eP = tkinter.Entry(root, show="*", textvariable=vP)
eP.pack()
try:
  with open(filename, "r") as f:
    info = json.load(f)
    vN.set(info["name"])
    vP.set(info["password"])
except:
  pass
lB = tkinter.Button(root, text="登录", command=login)
lB.pack()

root.mainloop()
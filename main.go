package main

import (
	"fmt"
	"net/http"
	"net/url"
	"os"
	"io/ioutil"
)

func NetStatus() bool {
	u, _ := url.Parse("http://www.google.cn/generate_204")
	q := u.Query()
	u.RawQuery = q.Encode()
	res, err := http.Get(u.String())
	if err != nil {
		fmt.Println("0")
		return false
	}
	resCode := res.StatusCode
	res.Body.Close()
	if err != nil {
		fmt.Println("0")
		return false
	}
	if (resCode == 204) {
		return true
	}
	return false
}

func Usage() {
	fmt.Println("使用方法:")
	fmt.Println(os.Args[0], "你的账号", "你的密码")
}

func main() {
	args := os.Args
	if args == nil || len(args) <2{
        Usage()
        return
	}
	account := args[1]
	passwd := args[2]
	if NetStatus() {
		fmt.Println("你已连接网络,无需登录")
	}else{
		response,err := http.Get("http://www.google.cn/generate_204")
		if(err!=nil){
			fmt.Println(err)
		}
		defer response.Body.Close()
		body,err := ioutil.ReadAll(response.Body)
		fmt.Println(string(body))
	}
}
package main

import (
	"fmt"
	"net/http"
	"os"
	"log"
)

func main() {
	args := os.Args
	if args == nil || len(args) <2{
        fmt.Println("使用方法:")
		fmt.Println(os.Args[0], "你的账号", "你的密码")
        return
	}
	// account := args[1]
	// passwd := args[2]
	resp, err := http.Get("http://www.google.cn/generate_204")
	if err != nil {
        log.Fatal(err)
    }
	if resp.StatusCode == 204 {
		fmt.Println("你已连接网络,无需登录")
	} else {
		
	}
}
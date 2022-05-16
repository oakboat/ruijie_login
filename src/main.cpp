#include <iostream>
#include <string>
#include "httplib.h"

int getLoginData(httplib::Result& res, std::string& loginURL, std::string& loginPath, std::string& queryString);

int main(int argc, char** argv)
{
	if (argc != 3)
	{
		std::cout << "Ê¹ÓÃ·½·¨:" << std::endl
			<< "³ÌÐòÃû ÄãµÄÕËºÅ ÄãµÄÃÜÂë" << std::endl
			<< "ÀýÈç:./ruijie_login 123456 123456" << std::endl;
		return -1;
	}
	std::string username = argv[1];
	std::string password = argv[2];
	httplib::Result checkResult = httplib::Client("http://www.google.cn").Get("/generate_204");
	if (!checkResult)
	{
		std::cout << "µÇÂ½×´Ì¬¼ì²éÊ§°Ü" << std::endl;
		return -1;
	}
	if (checkResult->status == 204)
	{
		std::cout << "ÄãÒÑÁ¬½ÓÍøÂç,ÎÞÐèµÇÂ¼" << std::endl;
		return 0;
	}
	std::string loginURL, loginPath, queryString;
	getLoginData(checkResult, loginURL, loginPath, queryString);
	queryString = "userId=" + username + "&password=" + password + "&service=&queryString=" + queryString + "&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false";
	//std::cout << loginURL << std::endl;
	//std::cout << loginPath << std::endl;
	//std::cout << queryString << std::endl;
	httplib::Result loginResult = httplib::Client(loginURL).Post(loginPath.c_str(), queryString, "application/x-www-form-urlencoded");
	size_t result = loginResult->body.find("\"result\":\"success\"");
	if (result == std::string::npos)
	{
		std::cout << "µÇÂ¼Ê§°Ü" << std::endl;
	}
	else 
	{
		std::cout << "µÇÂ¼³É¹¦" << std::endl;
	}
	return 0;
}

int getLoginData(httplib::Result& res, std::string& loginURL, std::string& loginPath, std::string& queryString)
{
	size_t index1, index2, index3, index4, index5;
	index1 = res->body.find_first_of("'");
	index2 = res->body.find("/eportal");
	index3 = res->body.find("index.jsp");
	index4 = res->body.find_first_of("?");
	index5 = res->body.find_last_of("'");
	if (index1 == std::string::npos || index2 == std::string::npos || index3 == std::string::npos || index4 == std::string::npos || index5 == std::string::npos)
	{
		return 0;
	}
	loginURL = res->body.substr(index1 + 1, index2 - index1 - 1);
	loginPath = res->body.substr(index2, index3 - index2);
	loginPath += "InterFace.do?method=login";
	queryString = res->body.substr(index4 + 1, index5 - index4 - 1);
	return 1;
}
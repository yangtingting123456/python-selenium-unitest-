import  requests
import json
#post接口测试样例
#post请求的请求头
headinfo = {
   "Content-Type":"application/json"
}
#请求数据
param={
    "username":"mting",
    "password":"ytt123456"

    }
#post请求
res=requests.post(url='https://w3-test.aboutcg.org/auth/auth/login',data=param,json=headinfo).json()
print(res)
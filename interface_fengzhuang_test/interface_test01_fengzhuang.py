import  requests,json
token=None
def send_get(url,data):
    res= requests.get(url=url,data=data).json()

    return res


def send_post(url,data):
    res= requests.post(url=url,data=data).json()
    return res

# url='https://w3-test.aboutcg.org/api/auth/message/sendMailCode?mail=3048903923@qq.com&isModifyMail=false'
# data={
#
# }
#
#  print(send_get(url,data))

url2='https://w3-test.aboutcg.org/auth/auth/login'
data2={
    "username":"mting",
    "password":"ytt123456"
}
print(send_post(url2,data2))
import  requests
#get接口测试样例
data={
    "courseType":"3",
    "courseName":"",
    "isVip":"false",
    "isFree":"false",
    "isPublishTime":"true",
    "isHeat":"false",
    "industryId":"-1",
     "skillId":"-1",
      "softwareId":"-1",
       "levelId":"-1",
      "pageNo":"-1",
     "searchCourseType":"-1"
    }
req=requests.get(url='https://w3-test.aboutcg.org/api/course/getSearchCategoryList?',params=data)
print(req.text)
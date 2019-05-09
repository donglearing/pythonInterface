import requests
import json
import traceback
import unittest

class MyTest(unittest.TestCase):
    def test_gettoken(self):
        self.url = "http://58.211.38.72:62080/backend/user/login"
        self.body = {"username":"super", "password":"Connext@0101"}
        #body = "{\n\"username\":\"super\",\n\"password\":\"Connext@0101\"\n}"
        self.headers = {'content-type': 'application/json'}
        self.params=json.dumps(body)
        print(params)
        self.res = requests.post(url=url, data=params, headers=headers)
        self.token=res.json()['token']
        return token

    def login(self,user,pwd):
        url = "http://58.211.38.72:62080/backend/user/login"
        body = {"username":user, "password": pwd}
        #body = "{\n\"username\":\"super\",\n\"password\":\"Connext@0101\"\n}"
        headers = {'content-type': 'application/json'}
        params=json.dumps(body)
        print(params)
        res = requests.post(url=url, data=params, headers=headers)
        results = json.loads(res.text)
        try:
            if res.status_code==200:
                if results['code']==0:
                    print("Success")
                else:
                    print("fail")
                    print(results['code'])
                    print res.text
            else:
                raise Exception("error is:%s" %res.status_code)
        except:
            traceback.print_exc()

        #return res.text
    '''def k8sproject(self):
        #gettoken=gettoken()
        url='http://58.211.38.72:62080/backend/vmproject/ParentProjectService/ParentProject/Query'
        body={}
        headers = {'content-type': 'application/json','token': MyTestSuite.gettoken()}
        res = requests.post(url=url, data=body, headers=headers)
        try:
            if res.status_code==200:
                if json.loads(res.text)['code']==0:
                    print('sucess')
                else:
                    print('fail')
                    print(json.loads(res.text))
            else:
                raise Exception('error is :%s'%res.status_code)
        except:
            traceback.print_exc()'''



if __name__ == "__main__":
   # userlist=['super','super', '111','demo']
    #pwdlist=["11","Connext@0101", "111","demo"]
    #for i in range(len(userlist)):
        #print userlist[i]
       # MyTestSuite.login(userlist[i],pwdlist[i])
       # res1=post(userlist[i],pwdlist[i])
       # results=json.loads(post(userlist[i],pwdlist[i]))
        #print results['total']

    suite = unittest.TestSuite()
    #suite.addTest(MyTestSuite("login("super",""Connext@0101")))
    suite.addTest(MyTest('login'))

    runner = unittest.TestSuite(suite)
    runner.run(suite)
   # print "success case:",result_statistics.num_success
    #print "fail case:",result_statistics.num_fail




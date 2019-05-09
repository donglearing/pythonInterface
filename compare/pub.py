import requests
import json
import traceback
class Pubdev:
    def test(self,parm):
        print('ttttttt=')
    def test_gettoken(self):
        url = "http://58.211.38.72:62080/backend/user/login"
        body = {"username":"super", "password":"Connext@0101"}
        #body = "{\n\"username\":\"super\",\n\"password\":\"Connext@0101\"\n}"
        headers = {'content-type': 'application/json'}
        params=json.dumps(body)
        print(params)
        res = requests.post(url=url, data=params, headers=headers)
        #token = res.json()['object']['token']
        token = res.text
        print(token)
        return token
   # token = test_gettoken()
    '''def k8sproject(self,token=test_gettoken()):
        #gettoken=gettoken()
        url='http://58.211.38.72:62080/backend/vmproject/ParentProjectService/ParentProject/Query'
        body={}
        headers = {'content-type': 'application/json','token': token}
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
    def vmProject(self,token):
        url = 'http://58.211.38.72:62080/backend/vmproject/ParentProjectService/ParentProject/Add'
        body = {'parent_project_name':'333','hosts':[]}
        headers = {'content-type': 'application/json','token': token}
        #res = requests.post(url=url, data=body, headers=headers)
        params=json.dumps(body)
        print(params)
        res = requests.post(url=url, data=params, headers=headers)
        print res.text
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
            traceback.print_exc()


if __name__ == '__main__':
    test1 = Pubdev()
    test1.test_gettoken()
    test1.vmProject(token=test1.test_gettoken())



import requests
import json
class RunMethod:
    '''def __init__(self,url,):'''
    def post_main(self,url,data,header):
        res = None
        if header != None:
            res= requests.post(url=url,data=data,headers=header)
            print("resjsom=", res.json)
            #return res.json()
            return res

            #return res.text
        else:
            res = requests.post(url,json)
            return res.json()
    #def run_main(self,method,url=None,data=None,header=None):
    def run_main(self, method, url, data, header):
        #res = None
        if method == 'post':
            res = self.post_main(url,data,header)
            return res
        else:
            print('no method')

if __name__ == '__main__':
    run = RunMethod()
    url = 'http://10.128.0.150:8002/backend/user/login'
    headerstring = {'Content-Type': 'application/json;charset=UTF-8'}
    bodystring = {'username': 'super', 'password': 'Connext@0101'}
    body = json.dumps(bodystring)
    method = 'post'
    #res3 = requests.post(url=url,data=body,headers=headerstring)
    res3 = run.run_main('post',url=url, data=body, header=headerstring)
    print(res3)
    #res = run.post_main(url=url,data=body,header=headerstring)
    res = run.post_main(url, body, headerstring)
    method = 'post'

    res1 = run.run_main(method,url,body,headerstring)
    print(res1.json()['data']['token'])
   # print(res1['code'])


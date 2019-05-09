import requests
import json
import pub
class K8snamespace:
    def newNamespace(self,token,ip,port):
        url = "http://"+ ip +":"+ port +"/backend/v1/newparentproject"
        #url = 'http://'+58.211.38.72:62080/backend/v1/newparentproject'
        #body = {'parentprojectname':'suntt2','cpu':'333','memory':'33','pods':'33','clusternodegroupid':0,'clusternodegroupid2':[0]}

        body = {"parentprojectname":"3333","cpu":"333","memory":"333","pods":"333","clusternodegroupid":0,"clusternodegroupid2":[0]}

        headers = {'content-type': 'application/json'}#,'token': token}
        print(url)
        params = json.dumps(body)
        print(params)
        print len(params)
        #urljson=json.dumps()
        res = requests.post(url, json=body, headers=headers)
        print(res)
        print(res.text)
        #try:
        if res.status_code == 200:
            if json.loads(res.text)['code']==0:
                print('sucess')

            else:
                print('fail')
                print(json.loads(res.text)['code'])
        else:
            print(res.status_code)

            ''' if json.loads(res.text)
            if json.loads(res.text)['code']==0:
                    print('sucess')
                else:
                    print('fail')
                    print(json.loads(res.text))
            else:
                raise Exception('error is :%s'%res.status_code)'''

if __name__ == '__main__':
    ip = '58.211.38.72'
    port = '62080'
    token = pub.Pubdev().test_gettoken()
    K8snamespace().newNamespace(token,ip,port)




from operation_data.get_data import GetData
from base.RunMethod import RunMethod
from tool.operation_excel import OperateExcel
from operation_data.dependent_data import DependentData
import json
from tool.operation_json import OperrationJson



class Run_test:
    def __init__(self):
        self.data = GetData()
        self.runMethod = RunMethod()

    def run_case(self):
        rows = self.data.get_case_lines()
        #row = 0
        for row in range(1, rows):
            is_run = self.data.get_is_run(row)
            print(is_run)
            if is_run == True:
                url = self.data.get_url(row)
                print(url)
                method = self.data.get_request_method(row)
                print(method)
                #header = self.data.get_header(row)
                depend_case = self.data.is_depend(row)
                print(depend_case)
                #request_data = self.data.get_data_for_json(row)
                request_data = self.data.get_request_data(row)
                body = json.dumps(request_data)

                print(request_data)
                #method = 'post'
                #url = 'http://10.128.0.150:8002/backend/user/login'
                headers = {"Content-Type": "application/json;charset=UTF-8"}
                #headers = json.dumps(headerstring)

                '''bodystring = {"username" : "super", "password" : "Connext@0101"}
                body = json.dumps(bodystring)'''

                #res = self.runMethod.run_main(method, url, request_data, headers)
                print("==========")
                #print(res)
                if depend_case != None:
                    depend_data = DependentData(depend_case)
                    depend_res = depend_data.run_dependent(depend_data.case_id)
                    print(depend_res)
                    #self.depend_data = DependentData(depend_case)

                    # 获取依赖响应数据
                    depend_response_key = depend_data.get_data_for_key(row)
                    # 获取依赖的key（数据依赖字段excel）
                    depend_key = self.data.get_depend_field(row)
                    print(depend_key)
                    #request_data[depend_key] = depend_response_key
                    #op_json = OperrationJson('../dataconfig/user.json')
                    # header = OperrationJson.get_data('token')

                    #headers = {'Content-Type': 'application/json;charset=UTF-8'}
                    #body = {'username': 'super', 'password': 'Connext@0101'}
                else:
                    res = self.runMethod.run_main(method, url, request_data, headers)
                    print(res)

            else:
                print("NO way")


if __name__ == '__main__':
    run = Run_test()
    run.run_case()
    '''headers = {"Content-Type": "application/json;charset=UTF-8"}
    res_login=run.runMethod.run_main('post', 'http://10.128.0.150:8002/backend/user/login', '{"username": "super","password": "Connext@0101"}', headers)
    print(res_login)
    token=res_login.json()['data']['token']
    print(token)
    #run.run_case()
    row = 2
    url = run.data.get_url(row)
    print(url)
    method = run.data.get_request_method(row)
    request_data = run.data.get_request_data(row)
    print(request_data)
    body = json.dumps(request_data)
    headers1 = {"Content-Type": "application/json;charset=UTF-8","Authorization":token}

    res = run.runMethod.run_main(method, url, request_data, headers1)
    print(res.text)
    #row = OperateExcel.get_lines()
    #a=GetData.get_case_lines()'''


                    #json.dumps(depend_res[depend_key])







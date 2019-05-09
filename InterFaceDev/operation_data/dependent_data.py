
# coding: utf-8
import sys
import json
sys.path.append("..")
# sys.path.append('E:\\learn\\python\\InterFaceDev')
from base.RunMethod import RunMethod
from jsonpath_rw import parse
from tool.operation_excel import OperateExcel
from operation_data.get_data import GetData


class DependentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperateExcel()
        self.data = GetData()
    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self) :
        row_data = self.opera_excel.get_rows_num(self.case_id)
        return row_data
    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()

        row = self.opera_excel.get_rows_num(self.case_id)
        request_data = self.data.get_data_for_json(row)
        # self.get_case_line_data(case_id)
        header = self.data.get_header(row)
        #headers = json.dumps(header)
        method = self.data.get_request_method(row)
        url = self.data.get_url(row)
        data = self.data.get_data_for_json(row)
        res = RunMethod.run_main(method, url, data, header)
        return json.loads(res)
    # 根据依赖的key去获取执行依赖测试case的响应,然后返回
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle[0]]

if __name__== '__main__':
    dep = DependentData('case-02')

    dep_res = dep.run_dependent(dep.case_id)
    print(dep_res)
    # row = dep.opera_excel.get_rows_num(dep.case_id)
    # print row
    #data = {"code":0,"data":{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTcwNTIwMjcsImlhdCI6MTU1Njg3OTIyNywianRpIjoiMTU1Njg3OTIyNy0xMDAwMDEyNy4wLjAuMSJ9.mq2BCLEVMFnR11lvu2qeOYtjLvk-gzcjWUFlApd_UA8","privileges":{"superuser":1,"infar":0,"k8s":0,"vm":0,"app":0,"maintenance_support":0}},"error":"","pagination":"null"}
    #res = "data.token"
    #print(res)

    '''json_exe = parse(res)
    print(json_exe)
    madle = json_exe.find(data)
    print(madle)
    print([math.value for math in madle])'''










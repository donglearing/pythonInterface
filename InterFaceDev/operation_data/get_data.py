#!/usr/bin/python3
#coding:utf-8
import sys
sys.path.append("..")
import xlrd
try:
    from .import data_config
except Exception:
    import data_config
from tool.operation_excel import OperateExcel
from tool.connect_db import OperationMysql
from tool.operation_json import  OperrationJson
import xlwt
import tool.connect_db
#获取excel中的内容
class GetData:
    def __init__(self):
        self.opera_excel = OperateExcel()
    #case = None
    #获取case数
    '''def get_case_lines(self,case):
        casename= 'r'+case
        workbook = xlrd.open_workbook(casename)
        sheet = workbook.sheet_by_index(0)
        row = sheet.ncols'''
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取是否执行
    def get_is_run(self,row):
        flag = None

        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_vaule(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag


        '''workbook = xlrd.open_workbook(casename)
        sheet = workbook.sheet_by_index(0)'''
    #是否携带header
    def get_header(self, row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_vaule(row,col)
        if header != '':
            return header
        else:
            return None
    #获取请求方式
    def get_request_method(self,row):
        col = int(data_config.get_requestway())
        return self.opera_excel.get_cell_vaule(row,col)
    #获取url
    def get_url(self,row):
        col = int(data_config.get_url())
        return self.opera_excel.get_cell_vaule(row,col)
    #获取请求数据
    def get_request_data(self,row):
        col = int(data_config.get_data())
        return self.opera_excel.get_cell_vaule(row,col)
    #通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperrationJson()
        # 获取excel的请求数据
        get_request_data = self.get_request_data(row)
        request_data = opera_json.get_data(get_request_data)


    #获取预期结果
    def get_except(self,row):
        col = int(data_config.get_expect())
        return self.opera_excel.get_cell_vaule(row,col)

    #通过sql获取预期结果
    def get_expect_data_for_mysql(self,row):
        getSql = OperationMysql()
        sql = self.get_except(row)
        res = getSql.search_one(sql)
        return res
    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_vaule(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key
    #判断是否有case依赖,获取caseid
    def is_depend(self,row):
        col = int(data_config.get_case_depend())
        case_depend = self.opera_excel.get_cell_vaule(row,col)
        if case_depend == '':
            return None
        else:
            return case_depend
    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(data_config.get_field_depent())
        data = self.opera_excel.get_cell_vaule(row,col)
        if data == '':
            return None
        else:
            return data
if __name__ == '__main__':
    data = GetData()
    operaExcel = OperateExcel()
    lines = data.get_case_lines()
    print(lines)
    headers = data.get_header(3)
    print(headers)
    depend = data.get_depend_field(3)
    print(depend)
    #print(data.get_data_for_json(3))
    opera_json = OperrationJson()
    get_request_data = data.get_request_data(3)
    print(get_request_data)
    #request_data = opera_json.get_data(get_request_data)



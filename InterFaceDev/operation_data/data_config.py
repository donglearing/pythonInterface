#coding:utf-8
class globle_var:
    id = '0'
    request_name='1'
    url='2'
    run ='3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect='10'
    result ='11'
    #获取caseid
def get_caseid():
    return globle_var.id
    #获取url
def get_url():
    return globle_var.url
    #获取用例名字
def get_requestname():
    return globle_var.request_name
    #获取是否执行
def get_run():
    return globle_var.run
    #获取请求类型
def get_requestway():
    return globle_var.request_way
    #获取header
def get_header():
    return globle_var.header
    #获取case依赖
def get_case_depend():
    return globle_var.case_depend
    #获取数据依赖，依赖的返回值
def get_data_depend():
    return globle_var.data_depend
    #获取数据字段依赖
def get_field_depent():
    return globle_var.field_depend
    #获取请求数据
def get_data():
    return globle_var.data
def get_expect():
    return globle_var.expect
def get_result():
    return globle_var.result
if __name__ == '__main__':
    hearder = get_header()
    print(hearder)





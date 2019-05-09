#coding:utf-8
import xlrd
#import sys
import xlwt
import xlutils
#sys.path.append('E:\learn\python\InterFaceDev')
from xlutils.copy import copy
class OperateExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id

        else:
            self.file_name='../case/testcase.xlsx'
            self.sheet_id=0
        self.data = self.get_data()
    '''获取sheet页中的内容'''
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables
    '''获取单元格行数'''
    def get_lines(self):
        tables = self.data
        return tables.nrows
    '''获取某一个单元格的内容'''
    def get_cell_vaule(self,row,col):
        return self.data.cell_value(row,col)


    '''写入数据'''
    def write_value(self,row,col,value):
        '''
        写入excle数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        readdata= xlrd.open_workbook(self.file_name)
        writedata= copy(readdata)
        sheet_data = writedata.getsheet(0)
        sheet_data.write(row,col,value)
        writedata.sava(self.file_name)


    # 根据对应的caseid找到对应的行号
    #def get_row_num(self,case_id):
       # num = 0



    #根据对应的caseid 找到对应行的内容
    def get_rows_data(self,case_id):
        num = self.data.get_rows_num(case_id)
        rows_data = self.data.get_row_values(num)
        return rows_data
    #根据对应的caseid找到对应的行号
    def get_rows_num(self,case_id,col_id):
        cols_data = self.get_cols_data(col_id)
        num = 0
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num + 1

    #获取行号，找到该行的内容
    def get_row_values(self,row):
        tables = self.data
        row_data=tables.row_values(row)
        return row_data
    #获取某一列的内容
    def get_cols_data(self,col_id):
        tables = self.data
        if col_id != None:
            cols = tables.col_values(col_id)
        else:
            cols = self.col_values(0)
        return cols
if __name__ == '__main__':
    opers = OperateExcel()
    print(opers.get_cell_vaule(0,1))
    print(opers.get_lines())
    col = opers.get_cols_data(0)
    print(col)
    opers.get_rows_num('case-02',0)











    '''def get_case_lines(self,case):
        casename= 'r'+case
        workbook = xlrd.open_workbook(casename)
        sheet = workbook.sheet_by_index(0)
        row = sheet.ncols'''



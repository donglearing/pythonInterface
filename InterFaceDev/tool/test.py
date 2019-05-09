import xlrd

dir = "E:\learn\Jmeter资料\接口测试用例.xlsx"
case = xlrd.open_workbook(dir)
sheet = case.sheet_by_index(0)
sheet.col_values()

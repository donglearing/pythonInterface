import os
from xlrd import open_workbook
from xml.etree import ElementTree
from readConfig import proDir


def get_xls(xls_name, sheet_name):
    cls = []
    #get xls path
    xlsPath = os.path.join(proDir ,"restFile", xls_name)
    #open xls file
    file = open_workbook(xlsPath)
    #get sheet by sheetname
    sheet = file.sheet_by_name(sheet_name)


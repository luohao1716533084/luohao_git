#coding:utf-8

import xlwt
import os

dirpath = "C:/Users/Administrator/Desktop/昆明/测试/测试报告"
list_dirs = os.walk(dirpath)

list_filenames = []
for i in list_dirs:
    list_filenames.append(i[2])

list_filename = list_filenames[0]

def write_excel(list_filename):
    sub_filename = dirpath.split('/')
    workbook = xlwt.Workbook(encoding="utf-8") #创建workbook
    worksheet = workbook.add_sheet(sub_filename[-1]) #创建sheet
    for i in range(len(list_filename)):
        worksheet.write(i, 0, list_filename[i])    #写入数据

    workbook.save('Excel_Workbook.xls')

if __name__ == '__main__':
    write_excel(list_filename)




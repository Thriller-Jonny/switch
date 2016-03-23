# -*- coding: utf-8 -*- 
import xdrlib, sys
import xlrd
import xlwt

def open_excel(file = 'file.xls'):
	try:
		data = xlrd.open_workbook(file)
		return data
	except Exception(e):
		print(str(e))

def create_excel():
	try:
		data = xlwt.Workbook()
		return data
	except Exception(e):
		print(str(e))

# -*- ����������ȡExcel����е�����   ����:file��Excel�ļ�·��     colnameindex����ͷ���������е�����  ��by_index��������� -*-
#���colnamesһ�¾ͻ��������
def excel_table_read_byindex(file = 'file.xls', colnameindex = 0, by_index = 0):
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows #����
	ncols = table.ncols #����
	#colnames =  table.row_values(colnameindex) #ĳһ������ 
	list = []
	for rownum in range(0, nrows):
		row = table.row_values(rownum)
		if row:
			list.append(row)
			#app = {}
			#for i in range(len(colnames)):
				#app[colnames[i]] = row[i]
			#list.append(app)
	return list

#�������ƻ�ȡExcel����е�����   ����:file��Excel�ļ�·��     colnameindex����ͷ���������е�����  ��by_name��Sheet1����
#���colnamesһ�¾ͻ��������
def excel_table_read_byname(file = 'file.xls', colnameindex = 0, by_name = u'Sheet1'):
	data = open_excel(file)
	table = data.sheet_by_name(by_name)
	nrows = table.nrows #���� 
	#colnames =  table.row_values(colnameindex) #ĳһ������ 
	list =[]
	for rownum in range(0, nrows):
		row = table.row_values(rownum)
		if row:
			list.append(row)
			#app = {}
			#for i in range(len(colnames)):
			#	app[colnames[i]] = row[i]
			#list.append(app)
	return list

#����excel
def excel_table_write_byindex(file = 'file.xls', content = [], by_name = u'Sheet1'):
	data = create_excel()
	sheet = data.add_sheet(by_name, cell_overwrite_ok = True) #����sheet
	
	for rownum in range(0, len(content)):
		for colnum in range(0, len(content[rownum])):
			#rowindex = content.index(row)
			#colindex = row.index(col)
			sheet.write(rownum, colnum, content[rownum][colnum])
	
	data.save(file)
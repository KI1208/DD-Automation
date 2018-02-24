#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd

book = xlrd.open_workbook('Sample_SurveySheet_r0.0.xlsx')
sheet_names = book.sheet_names()
print(sheet_names)

sheet = book.sheet_by_name('Basic')

partyid = sheet.cell(2, 5)
model = sheet.cell(4, 5)
serialnumber = sheet.cell(5, 5)
hostname = sheet.cell(19, 5)
domainname = sheet.cell(20, 5)
dgw = sheet.cell(21, 5)

# 全セルの値主取得
# for row_index in range(sheet.nrows):
#     for col_index in range(sheet.ncols):
#         val = sheet.cell_value(rowx=row_index, colx=col_index)
#         print('cell[{},{}] = {}'.format(row_index, col_index, val))

config = {
    'PartyID': partyid,
    'Model': model,
    'SerialNumber': serialnumber,
    'HostName': hostname,
    'DomainName': domainname,
    'DefaultGateway': dgw
}



#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import json

book = xlrd.open_workbook('Sample_SurveySheet_r0.0.xlsx')
sheet_names = book.sheet_names()
print(sheet_names)

sheet = book.sheet_by_name('Basic')

# partyid = sheet.cell_value(2, 5)
model = sheet.cell_value(4, 5)
serialnumber = sheet.cell_value(5, 5)
hostname = sheet.cell_value(19, 5)
domainname = sheet.cell_value(20, 5)
dgw = sheet.cell_value(21, 5)

# 全セルの値取得
# for row_index in range(sheet.nrows):
#     for col_index in range(sheet.ncols):
#         val = sheet.cell_value(rowx=row_index, colx=col_index)
#         print('cell[{},{}] = {}'.format(row_index, col_index, val))

config = {
    # 'PartyID': partyid,
    'Model': model,
    'SerialNumber': serialnumber,
    'HostName': hostname,
    'DomainName': domainname,
    'DefaultGateway': dgw
}

with open('config.json', 'w') as f:
    json.dump(config, f, indent=4, separators=(',', ': '))




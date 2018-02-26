#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import json

class Parse_survey:
    def __init__(self, filename):
        self.filename = filename

    def parse_survey(self):
        book = xlrd.open_workbook(self.filename)
        sheet_names = book.sheet_names()

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

        outputfile = 'config/config_' + serialnumber + '.json'
        with open(outputfile, 'w') as f:
            json.dump(config, f, indent=4, separators=(',', ': '))
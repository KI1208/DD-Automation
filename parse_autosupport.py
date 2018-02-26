#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Parse_autosupport:
    def __init__(self, filename):
        self.filename = filename

    def parse_autosupport(self):
        with open(self.filename) as f:
            for line in f:
                if 'SYSTEM_SERIALNO' in line:
                    serialnumber = line.split('=')[1].rstrip()

                if 'MODEL_NO' in line:
                    model = line.split('=')[1].rstrip()

                if 'HOSTNAME' in line:
                    hostname = line.split('=')[1].split('.')[0].rstrip()
                    domainname = line.split('=')[1].split('.', maxsplit=1)[1].rstrip()

                if 'IPv4 Default Gateway' in line:
                    next(f)
                    next(f)
                    dgw = next(f).split(' ')[0]

        config = {
            # 'PartyID': partyid,
            'Model': model,
            'SerialNumber': serialnumber,
            'HostName': hostname,
            'DomainName': domainname,
            'DefaultGateway': dgw
        }

        outputfile = 'result/config_' + config['SerialNumber'] + '_autosupport.json'
        with open(outputfile, 'w') as f:
            json.dump(config, f, indent=4, separators=(',', ': '))
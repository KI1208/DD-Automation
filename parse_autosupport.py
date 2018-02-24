#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

with open('dd01_autosupport_20180215.log') as f:
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

with open('result.json', 'w') as f:
    json.dump(config, f)
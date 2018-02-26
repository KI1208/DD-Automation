#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from string import Template

class Procgen:
    def __init__(self, filename):
        self.filename = filename

    def procgen(self):
        # Load config from json
        with open(self.filename) as f:
            config = json.load(f)

        # Create Procedure
        with open('procedure_template.md' ) as f:
            template = Template(f.read())
            #do the substitution
            output = template.substitute(config)

        outputfile = 'proc/proc_' + config['SerialNumber'] + '.md'
        with open(outputfile, 'w', encoding='utf-8') as f:
            f.write(output)


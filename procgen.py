#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from string import Template

# Load config from json
with open('config.json') as f:
    config = json.load(f)

# Create Procedure
with open('procedure_template.md' ) as f:
    template = Template(f.read())
    #do the substitution
    output = template.substitute(config)

with open('procedure.md', 'w', encoding='utf-8') as f:
    f.write(output)


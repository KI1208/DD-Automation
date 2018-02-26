#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import difflib

class Compare:
    def __init__(self, filenames):
        self.filenames = filenames

    def compare(self):
        # Load config from json
        # config=[]
        # for x, file in enumerate(self.filenames):
        #     with open(file) as f:
        #         config[x] = f.readlines()
        print(self.filenames)
        f1 = open(self.filenames[0])
        config1 = f1.readlines()
        f2 = open(self.filenames[1])
        config2 = f2.readlines()

        # Compare
        diff = difflib.HtmlDiff()
        table = diff.make_table(config1, config2, fromdesc='From Survey', todesc='From Autosupport', context=True)
        print(table)

        return table


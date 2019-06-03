#!/usr/bin/env python
# coding: utf-8

from csv import writer


def export_csv(fpath: str, data: list):
    with open(fpath, 'w', encoding='utf-8', newline='\n') as fh:
        wr = writer(fh)
        wr.writerows(data)


#!/usr/bin/env python
# coding: utf-8

import os.path as osp
import generator


def test_export_csv_default(tmpdir):
    fh = tmpdir.mkdir("sub").join("expected.csv")
    fh.write("""
    1,name1,200
    2,name2,400
    """.lstrip().replace('    ', ''))
    fpath = osp.join(fh.dirname, 'test.csv')
    
    data = [[1, 'name1', 200], [2, 'name2', 400]]
    generator.export_csv(fpath, data)
    
    assert tmpdir.join("sub/expected.csv").check()
    assert tmpdir.join("sub/test.csv").check()
    assert fh.read() == tmpdir.join("sub/test.csv").read()


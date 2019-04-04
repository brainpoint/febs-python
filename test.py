#! /usr/bin/env python
# coding=utf-8
#================================================================
#   Copyright (C) 2019 BP Ltd. All rights reserved.
#   Author      : brainpoint
#   Created date: 2019-04-07 14:31
#   Description : 
#================================================================

import os
import unittest
import febs

class TestFile(unittest.TestCase):
    def test_dirIsExist(self):
        self.assertEqual(True, febs.file.dirIsExist('./build'))
        self.assertEqual(True, febs.file.dirIsExist('./build/lib'))
        self.assertNotEqual(True, febs.file.dirIsExist('./xxxx'))

    def test_dirExplorerFilesRecursive(self):
        print(febs.file.dirExplorerDirsRecursive('.'))

if __name__ == '__main__':
    unittest.main()
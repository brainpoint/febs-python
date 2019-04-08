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

from febs import file

class TestFile(unittest.TestCase):
    def test_dirIsExist(self):
        self.assertEqual(True, file.dirIsExist('./build'))
        self.assertEqual(True, file.dirIsExist('./build/lib'))
        self.assertNotEqual(True, file.dirIsExist('./xxxx'))

    # def test_dirExplorerFilesRecursive(self):
    #     print(file.dirExplorerDirsRecursive('.'))

    def test_dirAssure(self):
        file.dirAssure('./build/build/build')
        self.assertEqual(True, file.dirIsExist('./build/build/build'))

if __name__ == '__main__':
    unittest.main()
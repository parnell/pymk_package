import unittest
import os, sys
import shutil

from pymk_package.pymk_package import (
    MakePackage
)

TESTIT_PKG = 'testit'
class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        shutil.rmtree(TESTIT_PKG, ignore_errors=True)

    def testit(self):
        cdict = {}
        cdict['package_name'] = TESTIT_PKG
        cdict['class_name'] = 'Make_Package'
        cdict['description'] = ''
        cdict['has_test'] = 'n'
        cdict['git_url'] = ''
        cdict['console_scripts'] = ''
        cdict['install_requires'] = ''
        MakePackage.make_package(cdict)

if __name__ == '__main__':
    unittest.main()

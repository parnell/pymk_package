import unittest
import os, sys
from mk_package.mk_package import (
    MakePackage
)

class BaseTest(unittest.TestCase):
    cdict = {}
    cdict['package_name'] = 'testit'
    cdict['class_name'] = 'Make_Package'
    cdict['description'] = ''
    cdict['has_test'] = 'n'
    cdict['git_url'] = ''
    cdict['console_scripts'] = ''
    cdict['install_requires'] = ''
    MakePackage.make_package(cdict)

if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python


import sys
import unittest

sys.path.append('.')

from module_utils.keycloak_admin import KeycloakAdminAPI


class Module:
    pass


class KeycloakAdminAPITest(unittest.TestCase):

    def setUp(self):
        def dummy(msg):
            return
        self.module = Module()
        self.module.params = {}
        self.module.fail_json = dummy
        pass

    def tearDown(self):
        pass

    def test_init_fails_without_config(self):
        with self.assertRaises(UnboundLocalError):
            kc = KeycloakAdminAPI(self.module)

    @unittest.skip("Need config to work.")
    def test_init_works(self):
        kc = KeycloakAdminAPI(self.module)
        self.assertTrue(kc)


if __name__ == '__main__':
    print unittest.main()

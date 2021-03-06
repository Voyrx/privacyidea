# -*- coding: utf-8 -*-
"""
This tests the file api.lib.utils
"""
from .base import MyApiTestCase

from privacyidea.api.lib.utils import (getParam)
from privacyidea.lib.error import ParameterError


class UtilsTestCase(MyApiTestCase):

    def test_01_getParam(self):
        s = getParam({"serial": ""}, "serial", optional=False, allow_empty=True)
        self.assertEqual(s, "")

        self.assertRaises(ParameterError, getParam, {"serial": ""}, "serial", optional=False, allow_empty=False)

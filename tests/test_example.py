#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# Copyright (C) 2013 <Yurij Bukatkin> <Zaj87@bk.ru>
# This program is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License version 2, as published 
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranties of 
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR 
# PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along 
# with this program.  If not, see <http://www.gnu.org/licenses/>.
### END LICENSE

import sys
import os.path
import unittest
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..")))

from recaller import AboutRecallerDialog

class TestExample(unittest.TestCase):
    def setUp(self):
        self.AboutRecallerDialog_members = [
        'AboutDialog', 'AboutRecallerDialog', 'gettext', 'logger', 'logging']

    def test_AboutRecallerDialog_members(self):
        all_members = dir(AboutRecallerDialog)
        public_members = [x for x in all_members if not x.startswith('_')]
        public_members.sort()
        self.assertEqual(self.AboutRecallerDialog_members, public_members)

if __name__ == '__main__':    
    unittest.main()

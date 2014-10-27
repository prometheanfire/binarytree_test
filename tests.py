#!/usr/bin/env python
#Copyright 2014 Matthew Thode

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

from __future__ import print_function
import unittest
import binarytree_test


class TestCase(unittest.TestCase):
    """A base test case for flask."""

    def create_app(self):
        self.app = binarytree_test.app()

    def check_for_json_loading(self):
        response = self.app.post('/',
                                 data='{"supertree": {"value": 1,"left": {"value": 5,"right":'
                                      '{"value": 3}},"right": {"value": 4,"left": {"value": 2},'
                                      '"right": {"value": 5,"left": {"value": 0},"right": '
                                      '{"value": 8}}}},"subtree": {"value": 4,"right": '
                                      '{"value": 5}}}')
        print(response)
        #self.assert_ assert_status(status_code=204, response='')

if __name__ == '__main__':
    unittest.main()

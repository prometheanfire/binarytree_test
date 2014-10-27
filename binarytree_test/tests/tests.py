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
import json
from binarytree_test.main import app, recursive_bintree_check

PASSING_JSON = ('{"supertree": {"value": 1,"left": {"value": 5,"right":'
                '{"value": 3}},"right": {"value": 4,"left": {"value": 2},'
                '"right": {"value": 5,"left": {"value": 0},"right": '
                '{"value": 8}}}},"subtree": {"value": 4,"right": '
                '{"value": 5}}}')

INVALID_JSON = ('{"supertree": {"value": 1,"left": {"value": 5,"right":'
                '{"value": 3}},"right": {"value": 4,"left": {"value": 2},'
                '"right": {"value": 5,"left": {"value": 0},"right": '
                '{"value": 8}}}},"subtree": {"value": 4,"right": '
                '{"value": 5}}}}')

FAILING_JSON = ('{"supertree": {"value": 1,"left": {"value": 5,"right":'
                '{"value": 3}},"right": {"value": 4,"left": {"value": 2},'
                '"right": {"value": 5,"left": {"value": 0},"right": '
                '{"value": 8}}}},"subtree": {"value": 4,"right": '
                '{"value": 3}}}')

FAILING_SUBTREE = json.loads('{"value": 4,"right": {"value": 3}}')
VALID_SUBTREE = json.loads('{"value": 4,"right": {"value": 5}}')
INVALID_SUBTREE = json.loads('{"values": 4,"right": {"value": 5}}')
VALID_SUPERTREE = json.loads('{"value": 1,"left": {"value": 5, '
                             '"right": {"value": 3}},"right": {'
                             '"value": 4,"left": {"value": 2},'
                             '"right": {"value": 5,"left": {"value": 0},'
                             '"right": {"value": 8}}}}')


class TestCase(unittest.TestCase):
    """A base test case for flask."""

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_check_for_json_loading_invalid(self):
        assert 400 == self.app.post('/', data=INVALID_JSON).status_code

    def test_check_for_json_loading_match(self):
        assert 204 == self.app.post('/', data=PASSING_JSON).status_code

    def test_check_for_json_loading_no_match(self):
        assert 404 == self.app.post('/', data=FAILING_JSON).status_code

    def test_recursive_bintree_check_match(self):
        assert 'matching' == recursive_bintree_check(VALID_SUPERTREE,
                                                     VALID_SUBTREE)

    def test_recursive_bintree_check_no_match(self):
        assert 'no_match' == recursive_bintree_check(VALID_SUPERTREE,
                                                     FAILING_SUBTREE)

    def test_recursive_bintree_check_invalid(self):
        assert 'invalid_format' == recursive_bintree_check(VALID_SUPERTREE,
                                                           INVALID_SUBTREE)

if __name__ == '__main__':
    unittest.main()

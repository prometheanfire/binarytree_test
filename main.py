#!/usr/bin/env python
#Copyright 2013 Matthew Thode

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

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    try:
        data = request.data
        if data == b'':
            data = request.form.copy().popitem()[0]
        binarytree_json = json.loads(data)
    except ValueError:
        return '', 400
    if 'subtree' in binarytree_json and 'supertree' in binarytree_json:
        if 'matching' == recursive_bintree_check(binarytree_json['supertree'],
                                                 binarytree_json['subtree']):
            return '', 204
        else:
            return '', 404
    else:
        return '', 400


def recursive_bintree_check(supertree, subtree):
    # check for formatting of datastructure
    if 'value' in subtree and supertree:
        if subtree['value'] == supertree['value']:
            if 'right' in subtree and 'right' in supertree:
                code = recursive_bintree_check(supertree['right'], subtree['right'])
                if code == 'matching':
                    return code
            if 'left' in subtree and 'left' in supertree:
                code = recursive_bintree_check(supertree['left'], subtree['left'])
                if code == 'matching':
                    return code
            if 'right' not in subtree and 'left' not in subtree:
                return 'matching'
        else:
            if 'right' in supertree:
                code = recursive_bintree_check(supertree['right'], subtree)
                if code == 'matching':
                    return code
            if 'left' in supertree:
                code = recursive_bintree_check(supertree['left'], subtree)
                if code == 'matching':
                    return code
            if 'right' not in supertree or 'left' not in supertree:
                return 'no_match'
    else:
        return 'invalid_format'

if __name__ == '__main__':
    app.run()
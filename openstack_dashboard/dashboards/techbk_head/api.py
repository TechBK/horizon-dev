# -*- coding: utf-8 -*-
#
# Copyright 2014 - StackStorm, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from django.utils.translation import ugettext_lazy as _
from horizon.utils import memoized
from . import logclient
import json

def to_json(func):
    def wrapped(project):
        return json.loads(func(project).text)
    return wrapped

#@memoized.memoized
def log_client():
    #return logclient.Client(base_url='http://httpbin.org')
    return logclient.Client()

@to_json
def projectlog(project):
    data = {'project':project}
    return log_client().get_project_log(data)#.text

@to_json
def test(project):
    data = {'project':project}
    return log_client().test(data)#.text
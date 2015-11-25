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


import requests
from . import config

__author__ = 'techbk'


class HTTPClient(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def _update_headers(self, headers):
        """

        :rtype: dict
        """
        if not headers:
            headers = {}
        content_type = headers.get('content-type', 'application/json; charset=utf-8')
        headers['content-type'] = content_type

        return headers

    def get(self, url, data=None, headers=None, json=None, params=None):
        headers = self._update_headers(headers)

        return requests.get(self.base_url + url, data=data, headers=headers, json=json, params=params)


class Client(object):
    def __init__(self, base_url=None):
        # self._queue = q
        if not base_url:
            base_url = config.LOG_SERVICE_URL
        self.http_client = HTTPClient(base_url)

    # @to_json
    def get_project_log(self, params):
        return self.http_client.get(url='/projectlog', params=params)

    # @to_json
    def test(self, params=None):
        """

        :type params: object
        """
        return self.http_client.get(url='/test', params=params)


if __name__ == "__main__":
    client = Client()
    r = client.get_project_log('nova')
    print("################")
    print(r.text)
    print(r.headers)
    print(r.url)
    print(r.status_code)

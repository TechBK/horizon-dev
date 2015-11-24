# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext_lazy as _
import json 
from horizon import exceptions
from horizon import tabs
from .tables import LogsTable

class ServicelogTab(tabs.TableTab):
    table_classes = (LogsTable,)
    name = _("Service Log")
    slug = "servicelog_tab"
    template_name = ("horizon/common/_detail_table.html")
    preload = False

    def get_logs_data(self):
        obj = '[{"id": 1, "time": "2015-11-14 00:23:46.664", "pid": 4180, "level": "INFO", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 2, "time": "2015-11-14 00:23:46.889", "pid": 4191, "level": "ERROR", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 3, "time": "2015-11-14 00:23:47.264", "pid": 4200, "level": "INFO", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 4, "time": "2015-11-14 00:23:48.664", "pid": 4180, "level": "WARNING", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERM"}, {"id": 5, "time": "2015-11-14 00:23:48.964", "pid": 4191, "level": "INFO", "name": "neutron.openstack.common.service", "content": "[req-0174f305-5689-4076-803c-aef774ae45e0 ] Child caught SIGTERMmmmmmm mmmmmmm mmmmmmmmmm mmmm mmmm mmmm mmmm mmmm mmmmm mmmmmm mmmmmm"}]'
        logs = json.loads(obj)
        context = []
        for log in logs:
            context.append(Log(log['id'], log['time'], log['pid'], log['level'], log['name'], log['content']))
        return context

class InstanceTab(tabs.Tab):
    name = _("Instance Log")
    slug = "instancelog_tab"

    template_name = ("logdashboard/detail/instancelog.html")  # noi de template minh dung
    preload = False

    def get_instances_data(self):
        pass
        # noi de code return context

class DetailTabs(tabs.TabGroup):
    slug = "detail_tabs"
    tabs = (ServicelogTab,InstanceTab)
    sticky = True

class Log:
    def __init__(self, log_id, time, pid, level, name, content):
        self.id = log_id
        self.time = time
        self.pid = pid
        self.level = level
        self.name = name
        self.content = content
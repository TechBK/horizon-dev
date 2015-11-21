from django.utils.translation import ugettext_lazy as _

from horizon import tables



class MyFilterAction(tables.FilterAction):
    name = "myfilter"


class LogsTable(tables.DataTable):
    time = tables.Column("time", verbose_name=_("Time"))
    pid = tables.Column("pid", verbose_name=_("PID"))
    level = tables.Column('level', verbose_name=_("Level"))
    name = tables.Column('name', verbose_name=_("Name"))
    content = tables.Column('content', verbose_name=_("Content"))

    class Meta:
        name = "logs"
        verbose_name = _("Logs")
        table_actions = (MyFilterAction,)
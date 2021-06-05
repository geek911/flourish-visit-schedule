from datetime import datetime
from django.apps import AppConfig as DjangoAppConfig
from dateutil.tz import gettz
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig


class AppConfig(DjangoAppConfig):
    name = 'flourish_visit_schedule'


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP142'
    protocol_name = 'Flourish'
    protocol_number = '142'
    protocol_title = ''
    study_open_datetime = datetime(
        2020, 7, 1, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2025, 6, 30, 23, 59, 59, tzinfo=gettz('UTC'))

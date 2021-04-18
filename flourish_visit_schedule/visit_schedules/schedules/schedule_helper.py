from dateutil.relativedelta import relativedelta
from django.apps import apps as django_apps
from edc_base.utils import get_utcnow

edc_protocol = django_apps.get_app_config('edc_protocol')


class ScheduleHelper:

    def __init__(self, visit, crfs, schedule, visit3000, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.visit_title = visit.title
            self.visit_code = visit.code[:4]
            self.visit = visit
            self.crfs = crfs
            self.schedule = schedule
            self.visit3000 = visit3000 or None

    def create_quarterly_visits(self):

        count = 1
        code_count = count
        rbase = self.visit.rbase
        get_utcnow() - edc_protocol.study_close_datetime

        while(get_utcnow() + (rbase + relativedelta(months=3))
                <= edc_protocol.study_close_datetime):

            timepoint = self.visit.timepoint + count
            rbase = self.visit.rbase + relativedelta(months=(count * 3))

            if rbase.years > 3 and rbase.months < 3:
                self.visit_code = '3000'
                code_count = 1
            # if (self.visit3000 and rbase != self.visit3000.rbase) or not self.visit3000:
            visit_code = str(int(self.visit_code[:4]) + (code_count * 10))
            if 'M' in self.visit.code:
                visit_code = visit_code + 'M'
            visit_dict = {'code': visit_code,
                          'title': self.visit_title[:-1] + str(count + 1),
                          'timepoint': timepoint,
                          'rbase': self.visit.rbase + relativedelta(months=(count * 3)),
                          'rlower': relativedelta(days=0),
                          'rupper': relativedelta(days=0),
                          'crfs': self.crfs,
                          'facility_name': '5-day clinic'}
            self.schedule.add_visit(**visit_dict)
            count += 1
            code_count += 1

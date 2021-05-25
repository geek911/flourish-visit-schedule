from dateutil.relativedelta import relativedelta
from django.apps import apps as django_apps
from edc_base.utils import get_utcnow

edc_protocol = django_apps.get_app_config('edc_protocol')


class ScheduleHelper:

    def __init__(self, visit, crfs, schedule, fu_visit=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.visit_title = visit.title
            self.visit_code = visit.code[:4]
            self.visit = visit
            self.crfs = crfs
            self.fu_visit = fu_visit
            self.schedule = schedule

    def create_quarterly_visits(self):

        count = 1
        rbase = self.visit.rbase + relativedelta(months=(count * 3))

        while((edc_protocol.study_open_datetime + rbase) < edc_protocol.study_close_datetime):

            timepoint = self.visit.timepoint + count

            visit_code = str(int(self.visit_code) + count)
            if (self.fu_visit
                    and (get_utcnow() + rbase)
                    >= (edc_protocol.study_open_datetime + self.fu_visit.rbase)
                    and visit_code[:1] != '3'):
                visit_code = '3' + visit_code[1:]
            if 'M' in self.visit.code:
                visit_code = visit_code + 'M'
            visit_dict = {'code': visit_code,
                          'title': self.visit_title[:-1] + str(count + 1),
                          'timepoint': timepoint,
                          'rbase': rbase,
                          'rlower': relativedelta(days=45),
                          'rupper': relativedelta(days=44),
                          'crfs': self.crfs,
                          'facility_name': '5-day clinic'}
            self.schedule.add_visit(**visit_dict)

            count += 1

            rbase = self.visit.rbase + relativedelta(months=(count * 3))

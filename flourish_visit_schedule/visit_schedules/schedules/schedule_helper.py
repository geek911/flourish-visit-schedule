from dateutil.relativedelta import relativedelta
from django.apps import apps as django_apps

edc_protocol = django_apps.get_app_config('edc_protocol')


class ScheduleHelper:

    def __init__(self, visit, crfs, crfs_prn, schedule, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.visit_title = visit.title
            self.visit_code = visit.code[:4]
            self.visit = visit
            self.crfs = crfs
            self.crfs_prn = crfs_prn
            self.schedule = schedule

    def create_quarterly_visits(self):

        count = 1
        rbase = self.visit.rbase + relativedelta(months=(count * 3))

        while((edc_protocol.study_open_datetime + rbase) < edc_protocol.study_close_datetime):

            timepoint = self.visit.timepoint + count

            visit_code = str(int(self.visit_code) + count)

            if 'M' in self.visit.code:
                visit_code = visit_code + 'M'
            visit_dict = {'code': visit_code,
                          'title': self.visit_title[:-1] + str(count + 1),
                          'timepoint': timepoint,
                          'rbase': rbase,
                          'rlower': relativedelta(days=45),
                          'rupper': relativedelta(days=44),
                          'crfs': self.crfs,
                          'crfs_prn': self.crfs_prn,
                          'facility_name': '5-day clinic'}
            self.schedule.add_visit(**visit_dict)

            count += 1

            rbase = self.visit.rbase + relativedelta(months=(count * 3))

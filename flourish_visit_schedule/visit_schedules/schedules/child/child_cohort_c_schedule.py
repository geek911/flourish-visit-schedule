from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..schedule_helper import ScheduleHelper
from ...crfs import child_c_crf_1000, child_c_crf_3000, child_c_crf_4000

child_c_schedule_1 = Schedule(
    name='cohort_c_schedule1',
    verbose_name='Cohort C Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit1000 = Visit(
    code='1000',
    title='Child Cohort C Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_c_crf_1000,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000',
    title='Child Cohort C Quarterly Visit 1',
    timepoint=1,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_c_crf_3000,
    facility_name='5-day clinic')

visit4000 = Visit(
    code='4000',
    title='Child Cohort C Follow Up Visit',
    timepoint=12,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_c_crf_4000,
    facility_name='5-day clinic')

schedule_helper = ScheduleHelper(visit=visit3000, crfs=child_c_crf_3000,
                                 schedule=child_c_schedule_1, visit4000=visit4000)
schedule_helper.create_quarterly_visits()
child_c_schedule_1.add_visit(visit=visit1000)
child_c_schedule_1.add_visit(visit=visit3000)
child_c_schedule_1.add_visit(visit=visit4000)

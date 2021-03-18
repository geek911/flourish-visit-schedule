from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..schedule_helper import ScheduleHelper
from ...crfs import child_a_crf_1000, child_birth_crf_2000, child_a_crf_3000, child_a_crf_4000

child_a_schedule_1 = Schedule(
    name='child_cohort_a_schedule1',
    verbose_name='Child Cohort A Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohorta',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit1000 = Visit(
    code='1000',
    title='Child Cohort A Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_a_crf_1000,
    facility_name='5-day clinic')

visit2000 = Visit(
    code='2000',
    title='Child Cohort A Birth Visit',
    timepoint=1,
    rbase=relativedelta(months=5),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_birth_crf_2000,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000',
    title='Child Cohort A Quarterly Visit 1',
    timepoint=2,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_a_crf_3000,
    facility_name='5-day clinic')

visit4000 = Visit(
    code='4000',
    title='Child Cohort A Follow Up Visit',
    timepoint=13,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_a_crf_4000,
    facility_name='5-day clinic')

schedule_helper = ScheduleHelper(visit=visit3000, crfs=child_a_crf_3000,
                                 schedule=child_a_schedule_1, visit4000=visit4000)
schedule_helper.create_quarterly_visits()

child_a_schedule_1.add_visit(visit=visit1000)
child_a_schedule_1.add_visit(visit=visit2000)
child_a_schedule_1.add_visit(visit=visit3000)
child_a_schedule_1.add_visit(visit=visit4000)

from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..schedule_helper import ScheduleHelper
from ...crfs import child_c_crf_1000, child_c_crf_2000, child_c_crf_3000

# Enrollment Schedule
child_c_enrollment_schedule_1 = Schedule(
    name='child_c_enrol_schedule1',
    verbose_name='Cohort C Child Enrollment Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortcenrollment',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit1000 = Visit(
    code='1000',
    title='Cohort C Child Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_c_crf_1000,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000',
    title='Cohort C Child Follow Up Visit',
    timepoint=13,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_c_crf_3000,
    facility_name='5-day clinic')

child_c_enrollment_schedule_1.add_visit(visit=visit1000)
child_c_enrollment_schedule_1.add_visit(visit=visit3000)

# Quarterly Schedule
child_c_quarterly_schedule_1 = Schedule(
    name='child_c_quart_schedule1',
    verbose_name='Cohort C Child Quarterly Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortcquarterly',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit2000 = Visit(
    code='2000',
    title='Cohort C Child Quarterly Visit 1',
    timepoint=2,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_c_crf_2000,
    facility_name='5-day clinic')
child_c_quarterly_schedule_1.add_visit(visit=visit2000)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2000, crfs=child_c_crf_2000,
                                 schedule=child_c_quarterly_schedule_1)
schedule_helper.create_quarterly_visits()

# DYAD Schedule
child_c_sec_schedule_1 = Schedule(
    name='child_c_sec_schedule1',
    verbose_name='Cohort C Secondary AimsSchedule V1',
    onschedule_model='flourish_child.onschedulechildcohortcsec',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

child_c_sec_schedule_1.add_visit(visit=visit1000)

# Pool Schedule
child_pool_schedule_1 = Schedule(
    name='child_pool_schedule1',
    verbose_name='Child Pool Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortcpool',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visits = child_c_quarterly_schedule_1.visits
values = visits.values()

for visit in values:
    child_pool_schedule_1.add_visit(visit=visit)
    child_c_sec_schedule_1.add_visit(visit=visit)

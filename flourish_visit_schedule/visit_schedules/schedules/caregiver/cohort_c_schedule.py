from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..schedule_helper import ScheduleHelper
from ...crfs import bc_crf_1000, crf_2000, crf_3000

# Enrollment Schedule
c_enrollment_schedule_1 = Schedule(
    name='cohort_c_enrollment_schedule1',
    verbose_name='Cohort C Enrollment Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit1000 = Visit(
    code='1000M',
    title='Cohort C Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=bc_crf_1000,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000M',
    title='Cohort C Follow Up Visit',
    timepoint=13,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_3000,
    facility_name='5-day clinic')

c_enrollment_schedule_1.add_visit(visit=visit1000)
c_enrollment_schedule_1.add_visit(visit=visit3000)

# Quarterly Schedule
c_quarterly_schedule_1 = Schedule(
    name='cohort_c_quarterly_schedule1',
    verbose_name='Cohort C Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit2000 = Visit(
    code='2000M',
    title='Cohort C Quarterly Visit 1',
    timepoint=1,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_2000,
    facility_name='5-day clinic')

c_quarterly_schedule_1.add_visit(visit=visit2000)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                 schedule=c_quarterly_schedule_1, visit3000=visit3000)
schedule_helper.create_quarterly_visits()

# DYAD Schedule
c_dyad_schedule_1 = Schedule(
    name='cohort_c_dyad_schedule1',
    verbose_name='Cohort C DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyadc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_dyad_schedule_1.add_visit(visit=visit1000)

# Pool Schedule
caregiver_pool_schedule_1 = Schedule(
    name='caregiver_pool_schedule1',
    verbose_name='Caregiver Pool Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcpool',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visits = c_quarterly_schedule_1.visits
values = visits.values()

for visit in values:
    caregiver_pool_schedule_1.add_visit(visit=visit)
    c_dyad_schedule_1.add_visit(visit=visit)

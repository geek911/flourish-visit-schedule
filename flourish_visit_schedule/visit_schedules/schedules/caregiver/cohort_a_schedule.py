from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..schedule_helper import ScheduleHelper
from ...crfs import a_crf_1000, crf_1010, crf_2000, crf_3000

# Enrollment Schedule
a_enrollment_schedule_1 = Schedule(
    name='cohort_a_enrollment_schedule1',
    verbose_name='Cohort A Enrollment Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortaenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit1000 = Visit(
    code='1000M',
    title='Cohort A Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=a_crf_1000,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000M',
    title='Cohort A Follow Up Visit',
    timepoint=13,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_3000,
    facility_name='5-day clinic')

a_enrollment_schedule_1.add_visit(visit=visit1000)
a_enrollment_schedule_1.add_visit(visit=visit3000)

# Birth Schedule
a_birth_schedule_1 = Schedule(
    name='cohort_a_birth_schedule1',
    verbose_name='Cohort A Birth Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortabirth',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit1010 = Visit(
    code='1010M',
    title='Cohort A Birth Visit',
    timepoint=1,
    rbase=relativedelta(months=5),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_1010,
    facility_name='5-day clinic')
a_birth_schedule_1.add_visit(visit=visit1010)

# Quarterly Schedule
a_quarterly_schedule_1 = Schedule(
    name='cohort_a_quarterly_schedule1',
    verbose_name='Cohort A Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortaquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit2000 = Visit(
    code='2000M',
    title='Cohort A Quarterly Visit 1',
    timepoint=2,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_2000,
    facility_name='5-day clinic')
a_quarterly_schedule_1.add_visit(visit=visit2000)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                 schedule=a_quarterly_schedule_1, visit3000=visit3000)
schedule_helper.create_quarterly_visits()

# DYAD Schedule
a_dyad_schedule_1 = Schedule(
    name='cohort_a_dyad_schedule1',
    verbose_name='Cohort A DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyada',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_dyad_schedule_1.add_visit(visit=visit1000)
visits = a_quarterly_schedule_1.visits
values = visits.values()

for visit in values:
    a_dyad_schedule_1.add_visit(visit=visit)

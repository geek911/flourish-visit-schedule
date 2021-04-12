from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..schedule_helper import ScheduleHelper
from ...crfs import bc_crf_1000, crf_2000, crf_3000

# Enrollment Schedule
b_enrollment_schedule_1 = Schedule(
    name='cohort_b_enrollment_schedule1',
    verbose_name='Cohort B Enrollment Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit1000 = Visit(
    code='1000M',
    title='Cohort B Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=bc_crf_1000,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000M',
    title='Cohort B Follow Up Visit',
    timepoint=13,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_3000,
    facility_name='5-day clinic')

b_enrollment_schedule_1.add_visit(visit=visit1000)
b_enrollment_schedule_1.add_visit(visit=visit3000)

# Quarterly Schedule
b_quarterly_schedule_1 = Schedule(
    name='cohort_b_quarterly_schedule1',
    verbose_name='Cohort B Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit2000 = Visit(
    code='2000M',
    title='Cohort B Quarterly Visit 1',
    timepoint=1,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_2000,
    facility_name='5-day clinic')

b_quarterly_schedule_1.add_visit(visit=visit2000)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                 schedule=b_quarterly_schedule_1, visit3000=visit3000)
schedule_helper.create_quarterly_visits()

# DYAD Schedule
b_dyad_schedule_1 = Schedule(
    name='cohort_b_dyad_schedule1',
    verbose_name='Cohort B DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyadb',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_dyad_schedule_1.add_visit(visit=visit1000)

visits = b_quarterly_schedule_1.visits
values = visits.values()

for visit in values:
    b_dyad_schedule_1.add_visit(visit=visit)

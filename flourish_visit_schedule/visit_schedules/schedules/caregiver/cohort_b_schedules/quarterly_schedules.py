from edc_visit_schedule import Schedule
from ....crfs import crf_2001
from ..caregiver_visits.cohort_b_visits import visit2001, visit3000
from ...schedule_helper import ScheduleHelper

# Quarterly Schedules
b_quarterly1_schedule_1 = Schedule(
    name='b_quarterly1_schedule1',
    verbose_name='Cohort B(First Child(ren)) Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_quarterly2_schedule_1 = Schedule(
    name='b_quarterly2_schedule1',
    verbose_name='Cohort B(Second Child(ren)) Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_quarterly3_schedule_1 = Schedule(
    name='b_quarterly3_schedule1',
    verbose_name='Cohort B(Third Child(ren)) Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

# Generate Quarterly Visits
b_quarterly1_schedule_1.add_visit(visit=visit2001)

schedule_helper1 = ScheduleHelper(visit=visit2001, crfs=crf_2001,
                                  schedule=b_quarterly1_schedule_1,
                                  fu_visit=visit3000)
schedule_helper1.create_quarterly_visits()

visits = b_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    b_quarterly2_schedule_1.add_visit(visit=visit)
    b_quarterly3_schedule_1.add_visit(visit=visit)

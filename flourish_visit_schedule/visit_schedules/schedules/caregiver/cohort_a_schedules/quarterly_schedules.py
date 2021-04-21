from edc_visit_schedule import Schedule

from ...schedule_helper import ScheduleHelper
from ..caregiver_visits.cohort_a_visits import visit2000, visit3000
from ....crfs import crf_2000

# Quarterly Schedules
a_quarterly1_schedule_1 = Schedule(
    name='a_quarterly1_schedule1',
    verbose_name='Cohort A(First Child(ren)) Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortaquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_quarterly1_schedule_1.add_visit(visit=visit2000)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                 schedule=a_quarterly1_schedule_1, visit3000=visit3000)
schedule_helper.create_quarterly_visits()

a_quarterly2_schedule_1 = Schedule(
    name='a_quarterly2_schedule1',
    verbose_name='Cohort A(Second Child(ren)) Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortaquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_quarterly3_schedule_1 = Schedule(
    name='a_quarterly3_schedule1',
    verbose_name='Cohort A(Third Child(ren)) Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortaquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

# Generate Quarterly Visits
visits = a_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    a_quarterly2_schedule_1.add_visit(visit=visit)
    a_quarterly3_schedule_1.add_visit(visit=visit)

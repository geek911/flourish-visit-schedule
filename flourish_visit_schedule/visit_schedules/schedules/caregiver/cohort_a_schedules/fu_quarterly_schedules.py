from edc_visit_schedule import Schedule

from ...schedule_helper import ScheduleHelper
from ..caregiver_visits.cohort_a_visits import visit3001
from ....crfs import crf_2001

# Quarterly Schedules
a_quarterly1_schedule_1 = Schedule(
    name='a_fu_quarterly1_schedule1',
    sequence='4',
    verbose_name='Cohort A(First Child(ren)) FU Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortafu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_quarterly1_schedule_1.add_visit(visit=visit3001)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit3001, crfs=crf_2001,
                                 schedule=a_quarterly1_schedule_1)
schedule_helper.create_quarterly_visits()

a_quarterly2_schedule_1 = Schedule(
    name='a_fu_quarterly2_schedule1',
    sequence='4',
    verbose_name='Cohort A(Second Child(ren)) FU Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortafu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_quarterly3_schedule_1 = Schedule(
    name='a_fu_quarterly3_schedule1',
    sequence='4',
    verbose_name='Cohort A(Third Child(ren)) FU Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortafu',
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


from edc_visit_schedule import Schedule

from ..caregiver_visits.cohort_a_visits import visit3000

# Enrollment Schedules
a_fu1_schedule_1 = Schedule(
    name='a_fu1_schedule1',
    verbose_name='Cohort A(First Child(ren)) Follow Up Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortafu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_fu1_schedule_1.add_visit(visit=visit3000)

a_fu2_schedule_1 = Schedule(
    name='a_fu2_schedule1',
    verbose_name='Cohort A(Second Child(ren)) Follow Up Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortafu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_fu2_schedule_1.add_visit(visit=visit3000)

a_fu3_schedule_1 = Schedule(
    name='a_fu3_schedule1',
    verbose_name='Cohort A(Third Child(ren)) Follow Up Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortafu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_fu3_schedule_1.add_visit(visit=visit3000)

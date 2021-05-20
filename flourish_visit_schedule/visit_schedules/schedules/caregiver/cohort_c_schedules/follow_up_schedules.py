
from edc_visit_schedule import Schedule

from ..caregiver_visits.cohort_a_visits import visit3000

# Enrollment Schedules
c_fu1_schedule_1 = Schedule(
    name='c_fu1_schedule1',
    verbose_name='Cohort C(First Child(ren)) Follow Up Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_fu1_schedule_1.add_visit(visit=visit3000)

c_fu2_schedule_1 = Schedule(
    name='c_fu2_schedule1',
    verbose_name='Cohort C(Second Child(ren)) Follow Up Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_fu2_schedule_1.add_visit(visit=visit3000)

c_fu3_schedule_1 = Schedule(
    name='c_fu3_schedule1',
    verbose_name='Cohort C(Third Child(ren)) Follow Up Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_fu3_schedule_1.add_visit(visit=visit3000)

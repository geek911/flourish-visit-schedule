
from edc_visit_schedule import Schedule

from ..caregiver_visits.cohort_a_visits import visit2000

# Enrollment Schedules
a_enrollment1_schedule_1 = Schedule(
    name='a_enrol1_schedule1',
    sequence='1',
    verbose_name='Cohort A(First Child(ren)) Enrollment Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortaenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_enrollment1_schedule_1.add_visit(visit=visit2000)

a_enrollment2_schedule_1 = Schedule(
    name='a_enrol2_schedule1',
    sequence='1',
    verbose_name='Cohort A(Second Child(ren)) Enrollment Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortaenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_enrollment2_schedule_1.add_visit(visit=visit2000)

a_enrollment3_schedule_1 = Schedule(
    name='a_enrol3_schedule1',
    sequence='1',
    verbose_name='Cohort A(Third Child(ren)) Enrollment Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortaenrollment',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_enrollment3_schedule_1.add_visit(visit=visit2000)

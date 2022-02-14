from edc_visit_schedule import Schedule
from ..caregiver_visits.cohort_a_visits import visit2000D

# Birth Schedules
a_birth1_schedule_1 = Schedule(
    name='a_birth1_schedule1',
    sequence='2',
    verbose_name='Cohort A(First Child(ren)) Birth Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortabirth',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_birth1_schedule_1.add_visit(visit=visit2000D)

a_birth2_schedule_1 = Schedule(
    name='a_birth2_schedule1',
    sequence='2',
    verbose_name='Cohort A(Second Child(ren)) Birth Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortabirth',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_birth2_schedule_1.add_visit(visit=visit2000D)

a_birth3_schedule_1 = Schedule(
    name='a_birth3_schedule1',
    sequence='2',
    verbose_name='Cohort A(Third Child(ren)) Birth Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortabirth',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_birth3_schedule_1.add_visit(visit=visit2000D)

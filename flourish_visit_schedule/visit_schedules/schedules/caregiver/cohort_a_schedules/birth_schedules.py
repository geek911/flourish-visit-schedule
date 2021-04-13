from edc_visit_schedule import Schedule
from ..caregiver_visits.cohort_a_visits import visit1010

# Birth Schedules
a_birth1_schedule_1 = Schedule(
    name='a_birth1_schedule1',
    verbose_name='Cohort A Birth Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortabirth',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_birth1_schedule_1.add_visit(visit=visit1010)

a_birth2_schedule_1 = Schedule(
    name='a_birth2_schedule1',
    verbose_name='Cohort A Birth Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortabirth',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_birth2_schedule_1.add_visit(visit=visit1010)

a_birth3_schedule_1 = Schedule(
    name='a_birth3_schedule1',
    verbose_name='Cohort A Birth Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortabirth',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_birth3_schedule_1.add_visit(visit=visit1010)

from edc_visit_schedule import Schedule
from ..caregiver_visits.cohort_a_visits import visit1000

# Birth Schedules
a_antenatal1_schedule_1 = Schedule(
    name='a_antenatal1_schedule1',
    verbose_name='Cohort A(First Child(ren)) Antenatal Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortaantenatal',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_antenatal1_schedule_1.add_visit(visit=visit1000)

a_antenatal2_schedule_1 = Schedule(
    name='a_antenatal2_schedule1',
    verbose_name='Cohort A(Second Child(ren)) Antenatal Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortaantenatal',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_antenatal2_schedule_1.add_visit(visit=visit1000)

a_antenatal3_schedule_1 = Schedule(
    name='a_antenatal3_schedule1',
    verbose_name='Cohort A(Third Child(ren)) Antenatal Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortaantenatal',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_antenatal3_schedule_1.add_visit(visit=visit1000)

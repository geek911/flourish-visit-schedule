from edc_visit_schedule import Schedule
from .quarterly_schedules import c_quarterly1_schedule_1

# secondary Aims Schedules
c_sec_quart1_schedule_1 = Schedule(
    name='c_sec_quart1_schedule1',
    sequence='1',
    verbose_name='Cohort C(First Child(ren)) Sec Quarterly Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcsecquart',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_sec_quart2_schedule_1 = Schedule(
    name='c_sec_quart2_schedule1',
    sequence='1',
    verbose_name='Cohort C(Second Child(ren)) Sec Quarterly Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcsecquart',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_sec_quart3_schedule_1 = Schedule(
    name='c_sec_quart3_schedule1',
    sequence='1',
    verbose_name='Cohort C(Third Child(ren)) Sec Quarterly Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcsecquart',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visits = c_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    c_sec_quart1_schedule_1.add_visit(visit=visit)
    c_sec_quart2_schedule_1.add_visit(visit=visit)
    c_sec_quart3_schedule_1.add_visit(visit=visit)

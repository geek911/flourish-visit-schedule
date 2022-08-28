from edc_visit_schedule import Schedule
from .quarterly_schedules import a_quarterly1_schedule_1

# secondary Aims Schedules
a_sec_quart1_schedule_1 = Schedule(
    name='a_sec_quart1_schedule1',
    sequence='2',
    verbose_name='Cohort A(First Child(ren)) Sec Quarterly Aims Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortasecquart',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_sec_quart2_schedule_1 = Schedule(
    name='a_sec_quart2_schedule1',
    sequence='2',
    verbose_name='Cohort A(Second Child(ren)) Sec Quarterly Aims Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortasecquart',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_sec_quart3_schedule_1 = Schedule(
    name='a_sec_quart3_schedule1',
    sequence='2',
    verbose_name='Cohort A(Third Child(ren)) Sec Quarterly Aims Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortasecquart',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visits = a_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    a_sec_quart1_schedule_1.add_visit(visit=visit)
    a_sec_quart2_schedule_1.add_visit(visit=visit)
    a_sec_quart3_schedule_1.add_visit(visit=visit)

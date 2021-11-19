from edc_visit_schedule import Schedule
from .quarterly_schedules import b_quarterly1_schedule_1

# Secondary Aims Quartely Schedules
b_sec_quart1_schedule_1 = Schedule(
    name='b_sec_quart1_schedule1',
    sequence='1',
    verbose_name='Cohort B(First Child(ren)) Sec Quarterly Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbsecquart',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sec_quart2_schedule_1 = Schedule(
    name='b_sec_quart2_schedule1',
    sequence='1',
    verbose_name='Cohort B(Second Child(ren)) Sec Quarterly Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbsecquart',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sec_quart3_schedule_1 = Schedule(
    name='b_sec_quart3_schedule1',
    sequence='1',
    verbose_name='Cohort B(Third Child(ren)) Sec Quarterly Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbsecquart',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visits = b_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    b_sec_quart1_schedule_1.add_visit(visit=visit)
    b_sec_quart2_schedule_1.add_visit(visit=visit)
    b_sec_quart3_schedule_1.add_visit(visit=visit)

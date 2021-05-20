from edc_visit_schedule import Schedule
from .quarterly_schedules import b_quarterly1_schedule_1
from ..caregiver_visits.cohort_b_visits import visit2000

# Secondary Aims Schedules
b_sec1_schedule_1 = Schedule(
    name='b_sec1_schedule1',
    sequence='1',
    verbose_name='Cohort B(First Child(ren)) Secondary Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbsec',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sec2_schedule_1 = Schedule(
    name='b_sec2_schedule1',
    sequence='1',
    verbose_name='Cohort B(Second Child(ren)) Secondary Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbsec',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sec3_schedule_1 = Schedule(
    name='b_sec3_schedule1',
    sequence='1',
    verbose_name='Cohort B(Third Child(ren)) Secondary Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbsec',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sec1_schedule_1.add_visit(visit=visit2000)
b_sec2_schedule_1.add_visit(visit=visit2000)
b_sec3_schedule_1.add_visit(visit=visit2000)

visits = b_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    b_sec1_schedule_1.add_visit(visit=visit)
    b_sec2_schedule_1.add_visit(visit=visit)
    b_sec3_schedule_1.add_visit(visit=visit)

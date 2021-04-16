from edc_visit_schedule import Schedule
from ..caregiver_visits.cohort_b_visits import visit1000
from .quarterly_schedules import c_quarterly1_schedule_1

# Secondary Aims Schedules
c_sec1_schedule_1 = Schedule(
    name='c_sec1_schedule1',
    verbose_name='Cohort C(First Child(ren)) Secondary Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulesecc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_sec1_schedule_1.add_visit(visit=visit1000)

c_sec2_schedule_1 = Schedule(
    name='c_sec2_schedule1',
    verbose_name='Cohort C(Second Child(ren)) Secondary Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulesecc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_sec2_schedule_1.add_visit(visit=visit1000)

c_sec3_schedule_1 = Schedule(
    name='c_sec3_schedule1',
    verbose_name='Cohort C(Third Child(ren)) Secondary Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulesecc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_sec3_schedule_1.add_visit(visit=visit1000)

visits = c_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    c_sec1_schedule_1.add_visit(visit=visit)
    c_sec2_schedule_1.add_visit(visit=visit)
    c_sec3_schedule_1.add_visit(visit=visit)
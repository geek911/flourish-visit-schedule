from edc_visit_schedule import Schedule
from ..caregiver_visits.cohort_b_visits import visit1000
from .quarterly_schedules import c_quarterly1_schedule_1

# DYAD Schedules
c_dyad1_schedule_1 = Schedule(
    name='c_dyad1_schedule1',
    verbose_name='Cohort C DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyadc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_dyad1_schedule_1.add_visit(visit=visit1000)

c_dyad2_schedule_1 = Schedule(
    name='c_dyad2_schedule1',
    verbose_name='Cohort C DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyadc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_dyad2_schedule_1.add_visit(visit=visit1000)

c_dyad3_schedule_1 = Schedule(
    name='c_dyad3_schedule1',
    verbose_name='Cohort C DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyadc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_dyad3_schedule_1.add_visit(visit=visit1000)

visits = c_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    c_dyad1_schedule_1.add_visit(visit=visit)
    c_dyad2_schedule_1.add_visit(visit=visit)
    c_dyad3_schedule_1.add_visit(visit=visit)

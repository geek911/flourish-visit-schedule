from edc_visit_schedule import Schedule
from .quarterly_schedules import b_quarterly1_schedule_1
from ..caregiver_visits.cohort_b_visits import visit1000

# DYAD Schedules
b_dyad1_schedule_1 = Schedule(
    name='b_dyad1_schedule1',
    verbose_name='Cohort B DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyadb',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_dyad2_schedule_1 = Schedule(
    name='b_dyad2_schedule1',
    verbose_name='Cohort B DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyadb',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_dyad3_schedule_1 = Schedule(
    name='b_dyad3_schedule1',
    verbose_name='Cohort B DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyadb',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_dyad1_schedule_1.add_visit(visit=visit1000)
b_dyad2_schedule_1.add_visit(visit=visit1000)
b_dyad3_schedule_1.add_visit(visit=visit1000)

visits = b_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    b_dyad1_schedule_1.add_visit(visit=visit)
    b_dyad2_schedule_1.add_visit(visit=visit)
    b_dyad3_schedule_1.add_visit(visit=visit)

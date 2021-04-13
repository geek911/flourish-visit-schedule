from edc_visit_schedule import Schedule
from ..caregiver_visits.cohort_a_visits import visit1000
from .quarterly_schedules import a_quarterly1_schedule_1

# DYAD Schedules
a_dyad1_schedule_1 = Schedule(
    name='a_dyad1_schedule1',
    verbose_name='Cohort A DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyada',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_dyad2_schedule_1 = Schedule(
    name='a_dyad2_schedule1',
    verbose_name='Cohort A DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyada',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_dyad3_schedule_1 = Schedule(
    name='a_dyad3_schedule1',
    verbose_name='Cohort A DYAD Schedule V1',
    onschedule_model='flourish_caregiver.onscheduledyada',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_dyad1_schedule_1.add_visit(visit=visit1000)
a_dyad2_schedule_1.add_visit(visit=visit1000)
a_dyad3_schedule_1.add_visit(visit=visit1000)

visits = a_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    a_dyad1_schedule_1.add_visit(visit=visit)
    a_dyad2_schedule_1.add_visit(visit=visit)
    a_dyad3_schedule_1.add_visit(visit=visit)

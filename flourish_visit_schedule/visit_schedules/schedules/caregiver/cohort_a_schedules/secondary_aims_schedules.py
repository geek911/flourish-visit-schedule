from edc_visit_schedule import Schedule
from ..caregiver_visits.cohort_a_visits import visit2000

# secondary Aims Schedules
a_sec1_schedule_1 = Schedule(
    name='a_sec1_schedule1',
    sequence='1',
    verbose_name='Cohort A(First Child(ren)) Secondary Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortasec',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_sec2_schedule_1 = Schedule(
    name='a_sec2_schedule1',
    sequence='1',
    verbose_name='Cohort A(Second Child(ren))  Secondary Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortasec',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_sec3_schedule_1 = Schedule(
    name='a_sec3_schedule1',
    sequence='1',
    verbose_name='Cohort A(Third Child(ren)) Secondary Aims Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortasec',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_sec1_schedule_1.add_visit(visit=visit2000)
a_sec2_schedule_1.add_visit(visit=visit2000)
a_sec3_schedule_1.add_visit(visit=visit2000)

# visits = a_quarterly1_schedule_1.visits
# values = visits.values()
#
# for visit in values:
    # a_sec1_schedule_1.add_visit(visit=visit)
    # a_sec2_schedule_1.add_visit(visit=visit)
    # a_sec3_schedule_1.add_visit(visit=visit)

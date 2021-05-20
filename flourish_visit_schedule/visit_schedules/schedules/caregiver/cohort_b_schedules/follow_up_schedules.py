
from edc_visit_schedule import Schedule

from ..caregiver_visits.cohort_a_visits import visit3000

# Enrollment Schedules
b_fu1_schedule_1 = Schedule(
    name='b_fu1_schedule1',
    sequence='3',
    verbose_name='Cohort B(First Child(ren)) Follow Up Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_fu1_schedule_1.add_visit(visit=visit3000)

b_fu2_schedule_1 = Schedule(
    name='b_fu2_schedule1',
    sequence='3',
    verbose_name='Cohort B(Second Child(ren)) Follow Up Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_fu2_schedule_1.add_visit(visit=visit3000)

b_fu3_schedule_1 = Schedule(
    name='b_fu3_schedule1',
    sequence='3',
    verbose_name='Cohort B(Third Child(ren)) Follow Up Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_fu3_schedule_1.add_visit(visit=visit3000)

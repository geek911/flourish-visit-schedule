
from edc_visit_schedule import Schedule

from ..caregiver_visits.cohort_b_visits import visit3000

# B Follow-up Schedules
b_fu1_schedule_1 = Schedule(
    name='b_fu1_schedule1',
    sequence='3',
    verbose_name='Cohort B(First Child(ren)) Follow Up Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortbfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_fu1_schedule_1.add_visit(visit=visit3000)

b_fu2_schedule_1 = Schedule(
    name='b_fu2_schedule1',
    sequence='3',
    verbose_name='Cohort B(Second Child(ren)) Follow Up Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortbfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_fu2_schedule_1.add_visit(visit=visit3000)

b_fu3_schedule_1 = Schedule(
    name='b_fu3_schedule1',
    sequence='3',
    verbose_name='Cohort B(Third Child(ren)) Follow Up Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortbfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_fu3_schedule_1.add_visit(visit=visit3000)

# B Sequential Enrolment Follow-up Schedules
visit3000.code = '3000B'
visit3000.title = 'Cohort B SQ Follow Up Visit'

b_sq_fu1_schedule_1 = Schedule(
    name='b_sq_fu1_schedule1',
    sequence='5',
    verbose_name='Cohort B(First Child(ren)) Follow Up Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortbfuseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sq_fu1_schedule_1.add_visit(visit=visit3000)

b_sq_fu2_schedule_1 = Schedule(
    name='b_sq_fu2_schedule1',
    sequence='5',
    verbose_name='Cohort B(Second Child(ren)) Follow Up Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortbfuseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sq_fu2_schedule_1.add_visit(visit=visit3000)

b_sq_fu3_schedule_1 = Schedule(
    name='b_sq_fu3_schedule1',
    sequence='5',
    verbose_name='Cohort B(Third Child(ren)) Follow Up Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortbfuseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_sq_fu3_schedule_1.add_visit(visit=visit3000)


from edc_visit_schedule import Schedule

from ..caregiver_visits.cohort_c_visits import visit3000, visit3000sq

# Enrollment Schedules
c_fu1_schedule_1 = Schedule(
    name='c_fu1_schedule1',
    sequence='3',
    verbose_name='Cohort C(First Child(ren)) Follow Up Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_fu1_schedule_1.add_visit(visit=visit3000)

c_fu2_schedule_1 = Schedule(
    name='c_fu2_schedule1',
    sequence='3',
    verbose_name='Cohort C(Second Child(ren)) Follow Up Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_fu2_schedule_1.add_visit(visit=visit3000)

c_fu3_schedule_1 = Schedule(
    name='c_fu3_schedule1',
    sequence='3',
    verbose_name='Cohort C(Third Child(ren)) Follow Up Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcfu',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_fu3_schedule_1.add_visit(visit=visit3000)

# C Sequential Enrolment Follow-up Schedules
c_sq_fu1_schedule_1 = Schedule(
    name='c_sq_fu1_schedule1',
    sequence='5',
    verbose_name='Cohort C(First Child(ren)) Follow Up Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortcfuseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_sq_fu1_schedule_1.add_visit(visit=visit3000sq)

c_sq_fu2_schedule_1 = Schedule(
    name='c_sq_fu2_schedule1',
    sequence='5',
    verbose_name='Cohort C(Second Child(ren)) Follow Up Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortcfuseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_sq_fu2_schedule_1.add_visit(visit=visit3000sq)

c_sq_fu3_schedule_1 = Schedule(
    name='c_sq_fu3_schedule1',
    sequence='5',
    verbose_name='Cohort C(Third Child(ren)) Follow Up Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortcfuseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_sq_fu3_schedule_1.add_visit(visit=visit3000sq)

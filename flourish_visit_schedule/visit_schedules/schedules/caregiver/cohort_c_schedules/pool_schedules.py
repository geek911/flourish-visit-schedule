from edc_visit_schedule import Schedule
from .quarterly_schedules import c_quarterly1_schedule_1

# Pool Schedule
caregiver_pool1_schedule_1 = Schedule(
    name='pool1_schedule1',
    verbose_name='Caregiver Pool(First Child(ren)) Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcpool',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

caregiver_pool2_schedule_1 = Schedule(
    name='pool2_schedule1',
    verbose_name='Caregiver Pool(Second Child(ren)) Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcpool',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

caregiver_pool3_schedule_1 = Schedule(
    name='pool3_schedule1',
    verbose_name='Caregiver Pool(Third Child(ren)) Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcpool',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visits = c_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    caregiver_pool1_schedule_1.add_visit(visit=visit)
    caregiver_pool2_schedule_1.add_visit(visit=visit)
    caregiver_pool3_schedule_1.add_visit(visit=visit)

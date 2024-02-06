from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from flourish_visit_schedule.visit_schedules.crfs.caregiver_requisitions import \
    brain_ultrasound_requisitions

caregiver_bu_schedule_1 = Schedule(
    name='caregiver_bu_schedule_1',
    sequence='4',
    verbose_name='Caregiver Brain Ultrasound(First Child(ren)) Schedule',
    onschedule_model='flourish_caregiver.onschedulecaregiverbrainultrasound',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
)
caregiver_bu_schedule_2 = Schedule(
    name='caregiver_bu_schedule_2',
    sequence='4',
    verbose_name='Caregiver Brain Ultrasound(Second Child(ren)) Schedule',
    onschedule_model='flourish_caregiver.onschedulecaregiverbrainultrasound',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
)
caregiver_bu_schedule_3 = Schedule(
    name='caregiver_bu_schedule_3',
    sequence='4',
    verbose_name='Caregiver Brain Ultrasound(Third Child(ren)) Schedule',
    onschedule_model='flourish_caregiver.onschedulecaregiverbrainultrasound',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
)

visit2002s = Visit(
    code='2002S',
    title='Brain Ultrasound Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=31),
    rupper=relativedelta(days=31),
    requisitions=brain_ultrasound_requisitions,
    requisitions_unscheduled=brain_ultrasound_requisitions,
    crfs=None,
    crfs_prn=None,
    allow_unscheduled=True,
    facility_name='5-day clinic')

caregiver_bu_schedule_1.add_visit(visit=visit2002s)
caregiver_bu_schedule_2.add_visit(visit=visit2002s)
caregiver_bu_schedule_3.add_visit(visit=visit2002s)

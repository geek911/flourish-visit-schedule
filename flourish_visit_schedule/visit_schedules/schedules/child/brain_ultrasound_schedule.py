from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from flourish_visit_schedule.visit_schedules.crfs.child_requisitions import \
    brain_ultrasound_requisitions

child_brain_ultrasound_schedule = Schedule(
    name='child_bu_schedule',
    sequence='3',
    verbose_name='Child Brain Ultrasound Schedule',
    onschedule_model='flourish_child.onschedulechildbrainultrasound',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
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

child_brain_ultrasound_schedule.add_visit(visit=visit2002s)

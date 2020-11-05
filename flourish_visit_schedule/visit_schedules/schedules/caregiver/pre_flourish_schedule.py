from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ...crfs import crf_pre_consent

pre_flourish_schedule_1 = Schedule(
    name='preflourish_schedule1',
    verbose_name='Pre Flourish Cohort C Schedule V1',
    onschedule_model='flourish_caregiver.onschedulepreflourish',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.preflourishconsent',
    appointment_model='edc_appointment.appointment'
    )

visit0001 = Visit(
    code='0001M',
    title='Cohort C Pre Flourish Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_pre_consent,
    facility_name='5-day clinic')

pre_flourish_schedule_1.add_visit(visit=visit0001)
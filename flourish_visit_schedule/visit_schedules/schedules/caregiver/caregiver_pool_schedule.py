from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ..schedule_helper import ScheduleHelper
from ...crfs import crf_3000

caregiver_pool_schedule_1 = Schedule(
    name='caregiver_pool1_schedule1',
    verbose_name='Pool Schedule V1',
    onschedule_model='flourish_caregiver.onschedulepool1',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit3000 = Visit(
    code='3000M',
    title='Caregiver Pool Quarterly Visit 1',
    timepoint=1,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_3000,
    facility_name='5-day clinic')

schedule_helper = ScheduleHelper(visit=visit3000, crfs=crf_3000,
                                 schedule=caregiver_pool_schedule_1, visit4000=None)
schedule_helper.create_quarterly_visits()

caregiver_pool_schedule_1.add_visit(visit=visit3000)

""" Extra schedules for mothers with more that one child participation. """
caregiver_pool2_schedule_1 = Schedule(
    name='caregiver_pool2_schedule1',
    verbose_name='Pool Schedule2 V1',
    onschedule_model='flourish_caregiver.onschedulepool2',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

caregiver_pool3_schedule_1 = Schedule(
    name='caregiver_pool3_schedule1',
    verbose_name='Pool Schedule3 V1',
    onschedule_model='flourish_caregiver.onschedulepool3',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visits = caregiver_pool_schedule_1.visits
values = visits.values()

for visit in values:
    caregiver_pool2_schedule_1.add_visit(visit=visit)
    caregiver_pool3_schedule_1.add_visit(visit=visit)

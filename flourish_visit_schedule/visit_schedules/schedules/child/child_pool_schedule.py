from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ...crfs import child_bc_crf_3000

child_pool_schedule_1 = Schedule(
    name='child_pool_schedule1',
    verbose_name='Pool Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='edc_appointment.appointment'
    )

visit3000 = Visit(
    code='3000M',
    title='Child Pool Quarterly Visit',
    timepoint=1,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_bc_crf_3000,
    facility_name='5-day clinic')

child_pool_schedule_1.add_visit(visit=visit3000)

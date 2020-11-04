from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ...crfs import bc_crf_1000, crf_2000, crf_3000

cohort_c_schedule_1 = Schedule(
    name='cohort_c_schedule1',
    verbose_name='Cohort C Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortc',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.enrollment',
    appointment_model='edc_appointment.appointment'
    )

visit1000 = Visit(
    code='1000M',
    title='Cohort C Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=bc_crf_1000,
    facility_name='5-day clinic')

visit2000 = Visit(
    code='2000M',
    title='Cohort C Quarterly Visit',
    timepoint=1,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_2000,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000M',
    title='Cohort C Follow Up Visit',
    timepoint=2,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_3000,
    facility_name='5-day clinic')
    
cohort_c_schedule_1.add_visit(visit=visit1000)
cohort_c_schedule_1.add_visit(visit=visit2000)
cohort_c_schedule_1.add_visit(visit=visit3000)

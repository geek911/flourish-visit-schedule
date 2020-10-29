from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit



cohort_a_schedule = Schedule(
    name='cohort_a_schedule',
    verbose_name='Cohort A Schedule',
    )

visit1000 = Visit(
    code='1000M',
    title='cohort_a_schedule',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')
    
cohort_a_schedule.add_visit(visit=visit1000)

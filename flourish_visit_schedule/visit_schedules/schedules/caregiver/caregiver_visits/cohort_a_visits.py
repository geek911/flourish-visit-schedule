from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Visit
from ....crfs import a_crf_1000, crf_1010, crf_2000, crf_3000

visit1000 = Visit(
    code='1000M',
    title='Cohort A Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=a_crf_1000,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000M',
    title='Cohort A Follow Up Visit',
    timepoint=13,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=crf_3000,
    facility_name='5-day clinic')

visit1010 = Visit(
    code='1010M',
    title='Cohort A Birth Visit',
    timepoint=1,
    rbase=relativedelta(months=5),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=crf_1010,
    facility_name='5-day clinic')

visit2000 = Visit(
    code='2000M',
    title='Cohort A Quarterly Visit 1',
    timepoint=2,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    crfs=crf_2000,
    facility_name='5-day clinic')

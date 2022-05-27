from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Visit as BaseVisit
from ....crfs import a_crf_2000, crf_2000d, crf_2001, crf_3000, tb_2_months
from ....crfs import caregiver_crfs_prn, preg_requisitions, requisitions_prn, caregiver_ref_crf_prn
from ....crfs import caregiver_crfs_unscheduled


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled or caregiver_crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)


visit1000 = Visit(
    code='1000M',
    title='Cohort A Antenatal Enrollment Visit',
    timepoint=1,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(weeks=7),
    requisitions=preg_requisitions,
    requisitions_prn=requisitions_prn,
    crfs=a_crf_2000,
    crfs_prn=caregiver_ref_crf_prn,
    facility_name='5-day clinic')

visit2000D = Visit(
    code='2000D',
    title='Cohort A Birth Visit',
    timepoint=2,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=3),
    requisitions=preg_requisitions,
    requisitions_prn=requisitions_prn,
    crfs=crf_2000d,
    crfs_prn=caregiver_ref_crf_prn,
    facility_name='5-day clinic')

visit2000 = Visit(
    code='2000M',
    title='Cohort A Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(months=3),
    requisitions=None,
    requisitions_prn=requisitions_prn,
    crfs=a_crf_2000,
    crfs_prn=caregiver_ref_crf_prn,
    facility_name='5-day clinic')

visit2001 = Visit(
    code='2001M',
    title='Cohort A Quarterly Visit 1',
    timepoint=3,
    rbase=relativedelta(days=90),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    requisitions_prn=requisitions_prn,
    crfs=crf_2001,
    crfs_prn=caregiver_crfs_prn,
    facility_name='5-day clinic')

visit3000 = Visit(
    code='3000M',
    title='Cohort A Follow Up Visit',
    timepoint=14,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=30),
    requisitions=None,
    requisitions_prn=requisitions_prn,
    crfs=crf_3000,
    crfs_prn=caregiver_ref_crf_prn,
    facility_name='5-day clinic')

visit3001 = Visit(
    code='3001M',
    title='Cohort A Follow Up Quarterly Visit 1',
    timepoint=4,
    rbase=relativedelta(days=90),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    requisitions_prn=requisitions_prn,
    crfs=crf_2001,
    crfs_prn=caregiver_crfs_prn,
    facility_name='5-day clinic')

visit2100 = Visit(
    code='2100T',
    title='TB 2 Months Visit',
    timepoint=5,
    rbase=relativedelta(months=2),
    rlower=relativedelta(days=30),
    rupper=relativedelta(days=30),
    requisitions=None,
    requisitions_prn=None,
    crfs=tb_2_months,
    facility_name='5-day clinic')

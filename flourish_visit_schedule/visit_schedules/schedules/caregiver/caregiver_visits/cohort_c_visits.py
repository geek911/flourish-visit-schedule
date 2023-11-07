from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Visit as BaseVisit

from ....crfs import bc_crf_2000, crf_2001, c_crf_3000, caregiver_crfs_prn, requisitions_prn
from ....crfs import caregiver_crfs_unscheduled, caregiver_ref_crf_prn


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


visit2000 = Visit(
    code='2000M',
    title='Cohort C Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(months=3),
    requisitions=None,
    requisitions_prn=requisitions_prn,
    crfs=bc_crf_2000,
    crfs_prn=caregiver_ref_crf_prn,
    facility_name='5-day clinic')

visit2001 = Visit(
    code='2001M',
    title='Cohort C Quarterly Visit 1',
    timepoint=1,
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
    title='Cohort C Follow Up Visit',
    timepoint=14,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=30),
    requisitions=None,
    requisitions_prn=requisitions_prn,
    crfs=c_crf_3000,
    crfs_prn=caregiver_ref_crf_prn,
    facility_name='5-day clinic')

visit3000sq = Visit(
    code='3000C',
    title='Cohort C SQ Follow Up Visit',
    timepoint=14,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=30),
    requisitions=None,
    requisitions_prn=requisitions_prn,
    crfs=c_crf_3000,
    crfs_prn=caregiver_ref_crf_prn,
    facility_name='5-day clinic')

visit3001 = Visit(
    code='3001M',
    title='Cohort C Follow Up Quarterly Visit 1',
    timepoint=2,
    rbase=relativedelta(days=90),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    requisitions_prn=requisitions_prn,
    crfs=crf_2001,
    crfs_prn=caregiver_crfs_prn,
    facility_name='5-day clinic')

visit3001sq = Visit(
    code='3001S',
    title='Cohort C Sec Follow Up Quarterly Visit 1',
    timepoint=2,
    rbase=relativedelta(days=90),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    requisitions_prn=requisitions_prn,
    crfs=crf_2001,
    crfs_prn=caregiver_crfs_prn,
    facility_name='5-day clinic')

from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ..schedule_helper import ScheduleHelper
from ...crfs import child_a_crf_2000, child_birth_crf_2000D, child_a_crf_2001, child_a_crf_3000


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)


# Enrollment Schedule
child_a_enrollment_schedule_1 = Schedule(
    name='child_a_enrol_schedule1',
    sequence='1',
    verbose_name='Cohort A Child Enrollment Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortaenrollment',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit2000 = Visit(
    code='2000',
    title='Cohort A Child Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=30),
    requisitions=None,
    crfs=child_a_crf_2000,
    facility_name='5-day clinic')

child_a_enrollment_schedule_1.add_visit(visit=visit2000)

# Birth Schedule
child_a_birth_schedule_1 = Schedule(
    name='child_a_birth_schedule1',
    sequence='2',
    verbose_name='Cohort A Child Birth Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortabirth',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit2000D = Visit(
    code='2000D',
    title='Cohort A Child Birth Visit',
    timepoint=1,
    rbase=relativedelta(months=5),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=child_birth_crf_2000D,
    facility_name='5-day clinic')
child_a_birth_schedule_1.add_visit(visit=visit2000D)

# Follow Up Schedule
child_a_fu_schedule_1 = Schedule(
    name='child_a_fu_schedule1',
    sequence='4',
    verbose_name='Cohort A Child Follow Up Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortafu',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit3000 = Visit(
    code='3000',
    title='Cohort A Child Follow Up Visit',
    timepoint=13,
    rbase=relativedelta(years=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=child_a_crf_3000,
    facility_name='5-day clinic')

child_a_fu_schedule_1.add_visit(visit=visit3000)

# Quarterly Schedule
child_a_quarterly_schedule_1 = Schedule(
    name='child_a_quart_schedule1',
    sequence='3',
    verbose_name='Cohort A Child Quarterly Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortaquarterly',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit2001 = Visit(
    code='2001',
    title='Cohort A Child Quarterly Visit 1',
    timepoint=2,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    crfs=child_a_crf_2001,
    facility_name='5-day clinic')
child_a_quarterly_schedule_1.add_visit(visit=visit2001)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2001, crfs=child_a_crf_2001,
                                 schedule=child_a_quarterly_schedule_1)
schedule_helper.create_quarterly_visits()

# Secondary Aims Schedule
child_a_sec_schedule_1 = Schedule(
    name='child_a_sec_schedule1',
    sequence='1',
    verbose_name='Cohort A Child Secondary Aims Schedule V1',
    onschedule_model='flourish_child.onschedulechildcohortasec',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

child_a_sec_schedule_1.add_visit(visit=visit2000)
visits = child_a_quarterly_schedule_1.visits
values = visits.values()

for visit in values:
    child_a_sec_schedule_1.add_visit(visit=visit)

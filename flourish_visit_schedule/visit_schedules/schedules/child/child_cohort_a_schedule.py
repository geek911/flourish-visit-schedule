from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ...crfs import child_a_crf_2000, child_birth_crf_2000D, child_a_crf_2001, child_a_crf_3000
from ...crfs import child_crfs_prn, child_crfs_unscheduled
from ..schedule_helper import ScheduleHelper
from ...crfs import child_requisitions


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled or child_crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)


# Enrollment Schedule
child_a_enrollment_schedule_1 = Schedule(
    name='child_a_enrol_schedule1',
    sequence='1',
    verbose_name='Cohort A Child Enrollment Schedule',
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
    rupper=relativedelta(months=3),
    requisitions=None,
    crfs=child_a_crf_2000,
    facility_name='5-day clinic')

child_a_enrollment_schedule_1.add_visit(visit=visit2000)

# Birth Schedule
child_a_birth_schedule_1 = Schedule(
    name='child_a_birth_schedule1',
    sequence='2',
    verbose_name='Cohort A Child Birth Schedule',
    onschedule_model='flourish_child.onschedulechildcohortabirth',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit2000D = Visit(
    code='2000D',
    title='Cohort A Child Birth Visit',
    timepoint=1,
    rbase=relativedelta(months=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=child_birth_crf_2000D,
    requisitions_prn=child_requisitions,
    facility_name='5-day clinic')
child_a_birth_schedule_1.add_visit(visit=visit2000D)

# Follow Up Schedule
child_a_fu_schedule_1 = Schedule(
    name='child_a_fu_schedule1',
    sequence='4',
    verbose_name='Cohort A Child Follow Up Schedule',
    onschedule_model='flourish_child.onschedulechildcohortafu',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit3000 = Visit(
    code='3000',
    title='Cohort A Child Follow Up Visit',
    timepoint=13,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=30),
    requisitions=None,
    crfs=child_a_crf_3000,
    facility_name='5-day clinic')

child_a_fu_schedule_1.add_visit(visit=visit3000)

# Quarterly Schedule
child_a_quarterly_schedule_1 = Schedule(
    name='child_a_quart_schedule1',
    sequence='3',
    verbose_name='Cohort A Child Quarterly Schedule',
    onschedule_model='flourish_child.onschedulechildcohortaquarterly',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit2001 = Visit(
    code='2001',
    title='Cohort A Child Quarterly Visit 1',
    timepoint=2,
    rbase=relativedelta(days=90),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    crfs=child_a_crf_2001,
    crfs_prn=child_crfs_prn,
    facility_name='5-day clinic')
child_a_quarterly_schedule_1.add_visit(visit=visit2001)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2001, crfs=child_a_crf_2001,
                                 crfs_prn=child_crfs_prn, schedule=child_a_quarterly_schedule_1)
schedule_helper.create_quarterly_visits()

# Follow Up Quarterly Schedule
child_a_fu_quarterly_schedule_1 = Schedule(
    name='child_a_fu_quart_schedule1',
    sequence='4',
    verbose_name='Cohort A Child Quarterly Schedule',
    onschedule_model='flourish_child.onschedulechildcohortafu',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visit3001 = Visit(
    code='3001',
    title='Cohort A Child FU Quarterly Visit 1',
    timepoint=4,
    rbase=relativedelta(days=90),
    rlower=relativedelta(days=45),
    rupper=relativedelta(days=44),
    requisitions=None,
    crfs=child_a_crf_2001,
    crfs_prn=child_crfs_prn,
    facility_name='5-day clinic')
child_a_fu_quarterly_schedule_1.add_visit(visit=visit3001)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit3001, crfs=child_a_crf_2001,
                                 crfs_prn=child_crfs_prn, schedule=child_a_fu_quarterly_schedule_1)
schedule_helper.create_quarterly_visits()

# Secondary Aims Schedule
child_a_sec_schedule_1 = Schedule(
    name='child_a_sec_schedule1',
    sequence='1',
    verbose_name='Cohort A Child Secondary Aims Schedule',
    onschedule_model='flourish_child.onschedulechildcohortasec',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

child_a_sec_schedule_1.add_visit(visit=visit2000)

# Secondary Aims Quarterly Schedule
child_a_sec_qt_schedule_1 = Schedule(
    name='child_a_sec_qt_schedule1',
    sequence='2',
    verbose_name='Cohort A Child Secondary Aims Quarterly Schedule',
    onschedule_model='flourish_child.onschedulechildcohortasecquart',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment'
    )

visits = child_a_quarterly_schedule_1.visits
values = visits.values()

for visit in values:
    child_a_sec_qt_schedule_1.add_visit(visit=visit)
    # child_a_sec_schedule_1.add_visit(visit=visit)

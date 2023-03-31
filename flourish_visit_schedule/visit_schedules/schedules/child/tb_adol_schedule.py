
from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from ...crfs.child_crfs import tb_adol_2_months, tb_adol_enrollment, \
    tb_adol_enrollment_unscheduled
from ...crfs.child_requisitions import tb_adol_requisitions

visit2100A = Visit(
    code='2100A',
    title='TB Adolecent Enrollment Cohort',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(months=3),
    requisitions=tb_adol_requisitions,
    crfs=tb_adol_enrollment,
    crfs_unscheduled=tb_adol_enrollment_unscheduled,
    allow_unscheduled=True,
    facility_name='5-day clinic')

visit2200A = Visit(
    code='2200A',
    title='TB Adolescent 2 Months Follow Up Visit',
    timepoint=1,
    rbase=relativedelta(months=2),
    rlower=relativedelta(days=30),
    rupper=relativedelta(days=30),
    requisitions=tb_adol_requisitions,
    crfs=tb_adol_2_months,
    crfs_unscheduled=tb_adol_enrollment_unscheduled,
    allow_unscheduled=True,
    facility_name='5-day clinic')

tb_adol_schedule = Schedule(
    name='tb_adol_schedule',
    verbose_name='TB Adolecent Schedule',
    onschedule_model='flourish_child.onschedulechildtbadolschedule',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment',
    sequence='6',
)

tb_adol_followup_schedule = Schedule(
    name='tb_adol_followup_schedule',
    verbose_name='TB Adolecent 2 Months Follow Schedule',
    onschedule_model='flourish_child.onscheduletbadolfollowupschedule',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment',
    sequence='7',
)

tb_adol_schedule.add_visit(visit2100A)
tb_adol_followup_schedule.add_visit(visit2200A)

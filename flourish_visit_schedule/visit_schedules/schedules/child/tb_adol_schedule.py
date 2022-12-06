
from edc_visit_schedule import Schedule, Visit
from edc_visit_schedule import VisitSchedule, site_visit_schedules


from dateutil.relativedelta import relativedelta
from ...crfs.child_crfs import tb_adol_enrollment
from ...crfs.child_requisitions import tb_adol_requisitions

visit2100A = Visit(
    code='2100A',
    title='TB Adolescent Enrollment Cohort',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(months=3),
    requisitions=tb_adol_requisitions,
    crfs=tb_adol_enrollment,
    facility_name='5-day clinic')


tb_adol_schedule= Schedule(
    name='tb_adol_schedule',
    verbose_name='TB Adolescent Schedule',
    onschedule_model='flourish_child.onschedulechildtbadolschedule',
    offschedule_model='flourish_child.childoffschedule',
    consent_model='flourish_child.childdummysubjectconsent',
    appointment_model='flourish_child.appointment',
    sequence='6',

)


tb_adol_schedule.add_visit(visit2100A)





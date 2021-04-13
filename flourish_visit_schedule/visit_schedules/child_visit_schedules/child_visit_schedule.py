from edc_visit_schedule import VisitSchedule, site_visit_schedules

from ..schedules import child_a_enrollment_schedule_1, child_a_birth_schedule_1
from ..schedules import child_a_quarterly_schedule_1, child_a_dyad_schedule_1
from ..schedules import child_b_enrollment_schedule_1, child_b_quarterly_schedule_1
from ..schedules import child_b_dyad_schedule_1, child_c_enrollment_schedule_1
from ..schedules import child_c_quarterly_schedule_1, child_c_dyad_schedule_1
from ..schedules import child_pool_schedule_1

# Cohort Visit Schedules

child_a_visit_schedule_v1 = VisitSchedule(
    name='child_a_visit_schedule_v1',
    verbose_name='Child Cohort A Visit Schedule 1',
    offstudy_model='flourish_prn.childoffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

child_a_visit_schedule_v1.add_schedule(child_a_enrollment_schedule_1)
child_a_visit_schedule_v1.add_schedule(child_a_birth_schedule_1)
child_a_visit_schedule_v1.add_schedule(child_a_quarterly_schedule_1)
child_a_visit_schedule_v1.add_schedule(child_a_dyad_schedule_1)

child_b_visit_schedule_v1 = VisitSchedule(
    name='child_b_visit_schedule_v1',
    verbose_name='Child Cohort B Visit Schedule 1',
    offstudy_model='flourish_prn.childoffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

child_b_visit_schedule_v1.add_schedule(child_b_enrollment_schedule_1)
child_b_visit_schedule_v1.add_schedule(child_b_quarterly_schedule_1)
child_b_visit_schedule_v1.add_schedule(child_b_dyad_schedule_1)

child_c_visit_schedule_v1 = VisitSchedule(
    name='child_c_visit_schedule_v1',
    verbose_name='Child Cohort C Visit Schedule 1',
    offstudy_model='flourish_prn.childoffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

child_c_visit_schedule_v1.add_schedule(child_c_enrollment_schedule_1)
child_c_visit_schedule_v1.add_schedule(child_c_quarterly_schedule_1)
child_c_visit_schedule_v1.add_schedule(child_c_dyad_schedule_1)
child_c_visit_schedule_v1.add_schedule(child_pool_schedule_1)

# Registering Visit Schedules
site_visit_schedules.register(child_a_visit_schedule_v1)
site_visit_schedules.register(child_b_visit_schedule_v1)
site_visit_schedules.register(child_c_visit_schedule_v1)

from edc_visit_schedule import VisitSchedule, site_visit_schedules

from ..schedules import child_a_enrollment_schedule_1, child_a_birth_schedule_1
from ..schedules import child_a_quarterly_schedule_1, child_a_sec_schedule_1
from ..schedules import child_a_sec_qt_schedule_1, child_b_sec_qt_schedule_1
from ..schedules import child_b_enrollment_schedule_1, child_b_quarterly_schedule_1
from ..schedules import child_b_fu_quarterly_schedule_1, child_c_fu_quarterly_schedule_1
from ..schedules import child_b_sec_schedule_1, child_c_enrollment_schedule_1
from ..schedules import child_c_fu_schedule_1, child_a_fu_quarterly_schedule_1
from ..schedules import child_c_quarterly_schedule_1, child_c_sec_schedule_1
from ..schedules import child_c_sec_qt_schedule_1
from ..schedules import child_pool_schedule_1, child_a_fu_schedule_1, child_b_fu_schedule_1
from ..schedules import tb_adol_schedule

# Cohort Visit Schedules
child_a_visit_schedule_v1 = VisitSchedule(
    name='child_a_visit_schedule_v1',
    verbose_name='Child Cohort A Visit Schedule',
    offstudy_model='flourish_prn.childoffstudy',
    death_report_model='flourish_prn.childdeathreport',
    locator_model='',
    previous_visit_schedule=None)


child_a_visit_schedule_v1.add_schedule(child_a_enrollment_schedule_1)
child_a_visit_schedule_v1.add_schedule(child_a_birth_schedule_1)
child_a_visit_schedule_v1.add_schedule(child_a_quarterly_schedule_1)
child_a_visit_schedule_v1.add_schedule(child_a_sec_schedule_1)
child_a_visit_schedule_v1.add_schedule(child_a_sec_qt_schedule_1)
child_a_visit_schedule_v1.add_schedule(child_a_fu_schedule_1)
child_a_visit_schedule_v1.add_schedule(child_a_fu_quarterly_schedule_1)

child_b_visit_schedule_v1 = VisitSchedule(
    name='child_b_visit_schedule_v1',
    verbose_name='Child Cohort B Visit Schedule',
    offstudy_model='flourish_prn.childoffstudy',
    death_report_model='flourish_prn.childdeathreport',
    locator_model='',
    previous_visit_schedule=None)

child_b_visit_schedule_v1.add_schedule(child_b_enrollment_schedule_1)
child_b_visit_schedule_v1.add_schedule(child_b_quarterly_schedule_1)
child_b_visit_schedule_v1.add_schedule(child_b_sec_schedule_1)
child_b_visit_schedule_v1.add_schedule(child_b_sec_qt_schedule_1)
child_b_visit_schedule_v1.add_schedule(child_b_fu_schedule_1)
child_b_visit_schedule_v1.add_schedule(child_b_fu_quarterly_schedule_1)

child_c_visit_schedule_v1 = VisitSchedule(
    name='child_c_visit_schedule_v1',
    verbose_name='Child Cohort C Visit Schedule',
    offstudy_model='flourish_prn.childoffstudy',
    death_report_model='flourish_prn.childdeathreport',
    locator_model='',
    previous_visit_schedule=None)

child_c_visit_schedule_v1.add_schedule(child_c_enrollment_schedule_1)
child_c_visit_schedule_v1.add_schedule(child_c_quarterly_schedule_1)
child_c_visit_schedule_v1.add_schedule(child_c_sec_schedule_1)
child_c_visit_schedule_v1.add_schedule(child_c_sec_qt_schedule_1)
child_c_visit_schedule_v1.add_schedule(child_pool_schedule_1)
child_c_visit_schedule_v1.add_schedule(child_c_fu_schedule_1)
child_c_visit_schedule_v1.add_schedule(child_c_fu_quarterly_schedule_1)


tb_adol_visit_schedule_v1 = VisitSchedule(
    name='tb_adol_schedule',
    verbose_name='TB Adolecent Schedule',
    offstudy_model='flourish_prn.childoffstudy',
    death_report_model='flourish_prn.childdeathreport',
    locator_model='',
    previous_visit_schedule=None)


tb_adol_visit_schedule_v1.add_schedule(tb_adol_schedule)

# Registering Visit Schedules
site_visit_schedules.register(child_a_visit_schedule_v1)
site_visit_schedules.register(child_b_visit_schedule_v1)
site_visit_schedules.register(child_c_visit_schedule_v1)
site_visit_schedules.register(tb_adol_visit_schedule_v1)
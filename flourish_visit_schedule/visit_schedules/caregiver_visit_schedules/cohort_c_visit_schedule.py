from edc_visit_schedule import VisitSchedule, site_visit_schedules

from ..schedules import c_enrollment1_schedule_1, c_quarterly1_schedule_1
from ..schedules import c_enrollment2_schedule_1, c_quarterly2_schedule_1
from ..schedules import c_enrollment3_schedule_1, c_quarterly3_schedule_1
from ..schedules import c_fu1_schedule_1, c_fu2_schedule_1, c_fu3_schedule_1
from ..schedules import c_fu_quarterly1_schedule_1, c_fu_quarterly2_schedule_1
from ..schedules import c_fu_quarterly3_schedule_1, c_sec_quart1_schedule_1
from ..schedules import c_sec1_schedule_1, caregiver_pool1_schedule_1
from ..schedules import c_sec2_schedule_1, caregiver_pool2_schedule_1
from ..schedules import c_sec3_schedule_1, caregiver_pool3_schedule_1
from ..schedules import c_sec_quart2_schedule_1, c_sec_quart3_schedule_1

# Cohort C Visit Schedules
cohort_c1_visit_schedule_v1 = VisitSchedule(
    name='c1_visit_schedule1',
    verbose_name='Cohort C Visit Schedule',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_c1_visit_schedule_v1.add_schedule(c_enrollment1_schedule_1)
cohort_c1_visit_schedule_v1.add_schedule(c_quarterly1_schedule_1)
cohort_c1_visit_schedule_v1.add_schedule(c_sec1_schedule_1)
cohort_c1_visit_schedule_v1.add_schedule(c_sec_quart1_schedule_1)
cohort_c1_visit_schedule_v1.add_schedule(caregiver_pool1_schedule_1)
cohort_c1_visit_schedule_v1.add_schedule(c_fu1_schedule_1)
cohort_c1_visit_schedule_v1.add_schedule(c_fu_quarterly1_schedule_1)

cohort_c2_visit_schedule_v1 = VisitSchedule(
    name='c2_visit_schedule1',
    verbose_name='Cohort C2 Visit Schedule',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_c2_visit_schedule_v1.add_schedule(c_enrollment2_schedule_1)
cohort_c2_visit_schedule_v1.add_schedule(c_quarterly2_schedule_1)
cohort_c2_visit_schedule_v1.add_schedule(c_sec2_schedule_1)
cohort_c2_visit_schedule_v1.add_schedule(c_sec_quart2_schedule_1)
cohort_c2_visit_schedule_v1.add_schedule(caregiver_pool2_schedule_1)
cohort_c2_visit_schedule_v1.add_schedule(c_fu2_schedule_1)
cohort_c2_visit_schedule_v1.add_schedule(c_fu_quarterly2_schedule_1)

cohort_c3_visit_schedule_v1 = VisitSchedule(
    name='c3_visit_schedule1',
    verbose_name='Cohort C3 Visit Schedule',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_c3_visit_schedule_v1.add_schedule(c_enrollment3_schedule_1)
cohort_c3_visit_schedule_v1.add_schedule(c_quarterly3_schedule_1)
cohort_c3_visit_schedule_v1.add_schedule(c_sec3_schedule_1)
cohort_c3_visit_schedule_v1.add_schedule(c_sec_quart3_schedule_1)
cohort_c3_visit_schedule_v1.add_schedule(caregiver_pool3_schedule_1)
cohort_c3_visit_schedule_v1.add_schedule(c_fu3_schedule_1)
cohort_c3_visit_schedule_v1.add_schedule(c_fu_quarterly3_schedule_1)

# Registering Visit Schedules
site_visit_schedules.register(cohort_c1_visit_schedule_v1)
site_visit_schedules.register(cohort_c2_visit_schedule_v1)
site_visit_schedules.register(cohort_c3_visit_schedule_v1)

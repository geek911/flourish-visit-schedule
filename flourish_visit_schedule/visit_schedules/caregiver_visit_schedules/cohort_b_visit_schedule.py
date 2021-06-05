from edc_visit_schedule import VisitSchedule, site_visit_schedules
from ..schedules import b_sec1_schedule_1, b_sec2_schedule_1, b_sec3_schedule_1
from ..schedules import b_enrollment1_schedule_1, b_enrollment2_schedule_1
from ..schedules import b_enrollment3_schedule_1, b_fu1_schedule_1, b_fu2_schedule_1
from ..schedules import b_quarterly1_schedule_1, b_quarterly2_schedule_1
from ..schedules import b_quarterly3_schedule_1, b_fu3_schedule_1
from ..schedules import b_fu_quarterly1_schedule_1, b_fu_quarterly2_schedule_1
from ..schedules import b_fu_quarterly3_schedule_1

cohort_b1_visit_schedule_v1 = VisitSchedule(
    name='b1_visit_schedule1',
    verbose_name='Cohort B Visit Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_b1_visit_schedule_v1.add_schedule(b_enrollment1_schedule_1)
cohort_b1_visit_schedule_v1.add_schedule(b_quarterly1_schedule_1)
cohort_b1_visit_schedule_v1.add_schedule(b_sec1_schedule_1)
cohort_b1_visit_schedule_v1.add_schedule(b_fu1_schedule_1)
cohort_b1_visit_schedule_v1.add_schedule(b_fu_quarterly1_schedule_1)

cohort_b2_visit_schedule_v1 = VisitSchedule(
    name='b2_visit_schedule1',
    verbose_name='Cohort B2 Visit Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_b2_visit_schedule_v1.add_schedule(b_enrollment2_schedule_1)
cohort_b2_visit_schedule_v1.add_schedule(b_quarterly2_schedule_1)
cohort_b2_visit_schedule_v1.add_schedule(b_sec2_schedule_1)
cohort_b2_visit_schedule_v1.add_schedule(b_fu2_schedule_1)
cohort_b2_visit_schedule_v1.add_schedule(b_fu_quarterly2_schedule_1)

cohort_b3_visit_schedule_v1 = VisitSchedule(
    name='b3_visit_schedule1',
    verbose_name='Cohort B3 Visit Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_b3_visit_schedule_v1.add_schedule(b_enrollment3_schedule_1)
cohort_b3_visit_schedule_v1.add_schedule(b_quarterly3_schedule_1)
cohort_b3_visit_schedule_v1.add_schedule(b_sec3_schedule_1)
cohort_b3_visit_schedule_v1.add_schedule(b_fu3_schedule_1)
cohort_b3_visit_schedule_v1.add_schedule(b_fu_quarterly3_schedule_1)

# Registering Visit Schedules
site_visit_schedules.register(cohort_b1_visit_schedule_v1)
site_visit_schedules.register(cohort_b2_visit_schedule_v1)
site_visit_schedules.register(cohort_b3_visit_schedule_v1)

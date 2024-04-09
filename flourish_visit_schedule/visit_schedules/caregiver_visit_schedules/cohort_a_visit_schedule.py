from edc_visit_schedule import VisitSchedule, site_visit_schedules

from ..schedules import a_enrollment1_schedule_1, a_birth1_schedule_1, \
    a_quarterly1_schedule_1, caregiver_bu_schedule_1, caregiver_bu_schedule_2, \
    caregiver_bu_schedule_3
from ..schedules import a_enrollment2_schedule_1, a_birth2_schedule_1, a_quarterly2_schedule_1
from ..schedules import a_enrollment3_schedule_1, a_birth3_schedule_1, a_quarterly3_schedule_1
from ..schedules import a_fu_quarterly1_schedule_1, a_fu_quarterly2_schedule_1
from ..schedules import a_fu_quarterly3_schedule_1, a_sec_quart1_schedule_1
from ..schedules import a_sec1_schedule_1, a_antenatal1_schedule_1, a_fu1_schedule_1
from ..schedules import a_sec2_schedule_1, a_antenatal2_schedule_1, a_fu2_schedule_1
from ..schedules import a_sec3_schedule_1, a_antenatal3_schedule_1, a_fu3_schedule_1
from ..schedules import a_sq_fu1_schedule_1, a_sq_fu2_schedule_1, a_sq_fu3_schedule_1
from ..schedules import a_sec_fu_quart1_schedule_1, a_sec_fu_quart2_schedule_1, a_sec_fu_quart3_schedule_1
from ..schedules import a_sec_quart2_schedule_1, a_sec_quart3_schedule_1
from ..schedules import a_tb1_2_months_schedule1, a_tb2_2_months_schedule1, a_tb3_2_months_schedule1
from ..schedules import a_tb1_6_months_schedule1, a_tb2_6_months_schedule1, a_tb3_6_months_schedule1

# Cohort A Visit Schedules
cohort_a1_visit_schedule_v1 = VisitSchedule(
    name='a1_visit_schedule1',
    verbose_name='Cohort A Visit Schedule',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_a1_visit_schedule_v1.add_schedule(a_enrollment1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_antenatal1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_tb1_2_months_schedule1)
cohort_a1_visit_schedule_v1.add_schedule(a_tb1_6_months_schedule1)
cohort_a1_visit_schedule_v1.add_schedule(a_birth1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_quarterly1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_sec1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_sec_quart1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_sec_fu_quart1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_fu1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_sq_fu1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_fu_quarterly1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(caregiver_bu_schedule_1)

cohort_a2_visit_schedule_v1 = VisitSchedule(
    name='a2_visit_schedule1',
    verbose_name='Cohort A2 Visit2 Schedule',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_a2_visit_schedule_v1.add_schedule(a_enrollment2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_antenatal2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_tb2_2_months_schedule1)
cohort_a2_visit_schedule_v1.add_schedule(a_tb2_6_months_schedule1)
cohort_a2_visit_schedule_v1.add_schedule(a_birth2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_quarterly2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_sec2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_sec_quart2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_sec_fu_quart2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_fu2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_sq_fu2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_fu_quarterly2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(caregiver_bu_schedule_2)

cohort_a3_visit_schedule_v1 = VisitSchedule(
    name='a3_visit_schedule1',
    verbose_name='Cohort A3 Visit Schedule',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_a3_visit_schedule_v1.add_schedule(a_enrollment3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_antenatal3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_tb3_2_months_schedule1)
cohort_a3_visit_schedule_v1.add_schedule(a_tb3_6_months_schedule1)
cohort_a3_visit_schedule_v1.add_schedule(a_birth3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_quarterly3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_sec3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_sec_quart3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_sec_fu_quart3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_fu3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_sq_fu3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_fu_quarterly3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(caregiver_bu_schedule_3)

# Registering Visit Schedules
site_visit_schedules.register(cohort_a1_visit_schedule_v1)
site_visit_schedules.register(cohort_a2_visit_schedule_v1)
site_visit_schedules.register(cohort_a3_visit_schedule_v1)

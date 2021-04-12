from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import a_enrollment_schedule_1, a_birth_schedule_1, a_quarterly_schedule_1
from .schedules import a_dyad_schedule_1, b_enrollment_schedule_1, b_quarterly_schedule_1
from .schedules import b_dyad_schedule_1, c_enrollment_schedule_1, c_quarterly_schedule_1
from .schedules import c_dyad_schedule_1, caregiver_pool_schedule_1

# Cohort A Visit Schedules

cohort_a_visit_schedule_v1 = VisitSchedule(
    name='cohort_a_visit_schedule1',
    verbose_name='Cohort A Visit Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_a_visit_schedule_v1.add_schedule(a_enrollment_schedule_1)
cohort_a_visit_schedule_v1.add_schedule(a_birth_schedule_1)
cohort_a_visit_schedule_v1.add_schedule(a_quarterly_schedule_1)
cohort_a_visit_schedule_v1.add_schedule(a_dyad_schedule_1)

cohort_b_visit_schedule_v1 = VisitSchedule(
    name='cohort_b_visit_schedule1',
    verbose_name='Cohort B Visit Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_b_visit_schedule_v1.add_schedule(b_enrollment_schedule_1)
cohort_b_visit_schedule_v1.add_schedule(b_quarterly_schedule_1)
cohort_b_visit_schedule_v1.add_schedule(b_dyad_schedule_1)

cohort_c_visit_schedule_v1 = VisitSchedule(
    name='cohort_c_visit_schedule1',
    verbose_name='Cohort C Visit Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_c_visit_schedule_v1.add_schedule(c_enrollment_schedule_1)
cohort_c_visit_schedule_v1.add_schedule(c_quarterly_schedule_1)
cohort_c_visit_schedule_v1.add_schedule(c_dyad_schedule_1)
cohort_c_visit_schedule_v1.add_schedule(caregiver_pool_schedule_1)

# Registering Visit Schedules
site_visit_schedules.register(cohort_a_visit_schedule_v1)
site_visit_schedules.register(cohort_b_visit_schedule_v1)
site_visit_schedules.register(cohort_c_visit_schedule_v1)

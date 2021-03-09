from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import cohort_a_schedule_1, cohort_b_schedule_1
from .schedules import cohort_c_schedule_1, caregiver_pool_schedule_1

# Cohort A Visit Schedules

cohort_a_visit_schedule_v1 = VisitSchedule(
    name='cohort_a_schedule1',
    verbose_name='Cohort A Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='flourish_caregiver.caregiverlocator',
    previous_visit_schedule=None)

cohort_a_visit_schedule_v1.add_schedule(cohort_a_schedule_1)

cohort_b_visit_schedule_v1 = VisitSchedule(
    name='cohort_b_schedule1',
    verbose_name='Cohort B Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='flourish_caregiver.caregiverlocator',
    previous_visit_schedule=None)

cohort_b_visit_schedule_v1.add_schedule(cohort_b_schedule_1)

cohort_c_visit_schedule_v1 = VisitSchedule(
    name='cohort_c_schedule1',
    verbose_name='Cohort C Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='flourish_caregiver.caregiverlocator',
    previous_visit_schedule=None)

cohort_c_visit_schedule_v1.add_schedule(cohort_c_schedule_1)

caregiver_pool_visit_schedule_v1 = VisitSchedule(
    name='caregiver_pool_schedule1',
    verbose_name='Caregiver Pool Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='flourish_caregiver.caregiverlocator',
    previous_visit_schedule=None)

caregiver_pool_visit_schedule_v1.add_schedule(caregiver_pool_schedule_1)

# Registering Visit Schedules
site_visit_schedules.register(cohort_a_visit_schedule_v1)
site_visit_schedules.register(cohort_b_visit_schedule_v1)
site_visit_schedules.register(cohort_c_visit_schedule_v1)
site_visit_schedules.register(caregiver_pool_visit_schedule_v1)
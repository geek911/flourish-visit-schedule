from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import child_a_schedule_1, child_b_schedule_1
from .schedules import child_c_schedule_1, child_pool_schedule_1

# Cohort Visit Schedules

child_a_visit_schedule_v1 = VisitSchedule(
    name='child_a_schedule_v1',
    verbose_name='Cohort A Schedule 1',
    offstudy_model='flourish_prn.offfstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='flourish_caregiver.caregiverlocator',
    previous_visit_schedule=None)

child_a_visit_schedule_v1.add_schedule(child_a_schedule_1)

child_b_visit_schedule_v1 = VisitSchedule(
    name='child_b_schedule_v1',
    verbose_name='Cohort B Schedule 1',
    offstudy_model='flourish_prn.offfstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='flourish_caregiver.caregiverlocator',
    previous_visit_schedule=None)

child_b_visit_schedule_v1.add_schedule(child_b_schedule_1)

child_c_visit_schedule_v1 = VisitSchedule(
    name='child_c_schedule_v1',
    verbose_name='Cohort C Schedule 1',
    offstudy_model='flourish_prn.offfstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='flourish_caregiver.caregiverlocator',
    previous_visit_schedule=None)

child_c_visit_schedule_v1.add_schedule(child_c_schedule_1)

child_pool_visit_schedule_v1 = VisitSchedule(
    name='child_pool_schedule_v1',
    verbose_name='Child Pool Schedule 1',
    offstudy_model='flourish_prn.offfstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='flourish_caregiver.caregiverlocator',
    previous_visit_schedule=None)

child_pool_visit_schedule_v1.add_schedule(child_pool_schedule_1)

# Registering Visit Schedules
site_visit_schedules.register(child_a_visit_schedule_v1)
site_visit_schedules.register(child_b_visit_schedule_v1)
site_visit_schedules.register(child_c_visit_schedule_v1)
site_visit_schedules.register(child_pool_visit_schedule_v1)

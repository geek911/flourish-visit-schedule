from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import cohort_a_schedule

# Cohort Visit Schedules

cohort_a_visit_schedule_v1 = VisitSchedule(
    name='anv_schedule_v1',
    verbose_name='Antenatal Visit Schedule 1',
    offstudy_model='td_prn.maternaloffstudy',
    death_report_model='td_prn.maternaldeathreport',
    locator_model='td_maternal.maternallocator',
    previous_visit_schedule=None)

cohort_a_visit_schedule_v1.add_schedule(cohort_a_schedule)



# Registering Visit Schedules
site_visit_schedules.register(cohort_a_visit_schedule_v1)

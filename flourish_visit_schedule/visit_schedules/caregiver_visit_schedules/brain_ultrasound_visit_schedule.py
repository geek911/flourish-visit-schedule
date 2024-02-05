from edc_visit_schedule import site_visit_schedules, VisitSchedule

from flourish_visit_schedule.visit_schedules.schedules import \
    caregiver_brain_ultrasound_schedule

brain_ultrasound_v = VisitSchedule(
    name='brain_ultrasound_v',
    verbose_name='Brain Ultrasound Visit Schedule',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

brain_ultrasound_v.add_schedule(caregiver_brain_ultrasound_schedule)

site_visit_schedules.register(brain_ultrasound_v)

from edc_visit_schedule import site_visit_schedules, VisitSchedule

from flourish_visit_schedule.visit_schedules.schedules import caregiver_bu_schedule_1, \
    caregiver_bu_schedule_2, caregiver_bu_schedule_3

brain_ultrasound_v1 = VisitSchedule(
    name='brain_ultrasound_v1',
    verbose_name='Brain Ultrasound Visit Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

brain_ultrasound_v2 = VisitSchedule(
    name='brain_ultrasound_v2',
    verbose_name='Brain Ultrasound Visit Schedule 2',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

brain_ultrasound_v3 = VisitSchedule(
    name='brain_ultrasound_v3',
    verbose_name='Brain Ultrasound Visit Schedule 3',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.caregiverdeathreport',
    locator_model='',
    previous_visit_schedule=None)

brain_ultrasound_v1.add_schedule(caregiver_bu_schedule_1)
brain_ultrasound_v2.add_schedule(caregiver_bu_schedule_2)
brain_ultrasound_v3.add_schedule(caregiver_bu_schedule_3)

site_visit_schedules.register(brain_ultrasound_v1)
site_visit_schedules.register(brain_ultrasound_v2)
site_visit_schedules.register(brain_ultrasound_v3)

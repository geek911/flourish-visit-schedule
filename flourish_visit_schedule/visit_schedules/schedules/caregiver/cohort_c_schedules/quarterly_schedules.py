from edc_visit_schedule import Schedule

from ...schedule_helper import ScheduleHelper
from ....crfs import crf_2000
from ..caregiver_visits.cohort_c_visits import visit2000, visit3000

# Quarterly Schedules
c_quarterly1_schedule_1 = Schedule(
    name='c_quarterly1_schedule1',
    verbose_name='Cohort C(First Child(ren)) Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_quarterly1_schedule_1.add_visit(visit=visit2000)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                 schedule=c_quarterly1_schedule_1, visit3000=visit3000)
schedule_helper.create_quarterly_visits()

c_quarterly2_schedule_1 = Schedule(
    name='c_quarterly2_schedule1',
    verbose_name='Cohort C(Second Child(ren)) Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_quarterly2_schedule_1.add_visit(visit=visit2000)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                 schedule=c_quarterly2_schedule_1, visit3000=visit3000)
schedule_helper.create_quarterly_visits()

c_quarterly3_schedule_1 = Schedule(
    name='c_quarterly3_schedule1',
    verbose_name='Cohort C(Third Child(ren)) Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortcquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_quarterly3_schedule_1.add_visit(visit=visit2000)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                 schedule=c_quarterly3_schedule_1, visit3000=visit3000)
schedule_helper.create_quarterly_visits()

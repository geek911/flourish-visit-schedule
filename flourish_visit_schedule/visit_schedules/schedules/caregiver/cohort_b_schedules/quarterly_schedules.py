from edc_visit_schedule import Schedule
from ....crfs import crf_2000
from ..caregiver_visits.cohort_b_visits import visit2000, visit3000
from ...schedule_helper import ScheduleHelper

# Quarterly Schedules
b_quarterly1_schedule_1 = Schedule(
    name='b_quarterly1_schedule1',
    verbose_name='Cohort B Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_quarterly2_schedule_1 = Schedule(
    name='b_quarterly2_schedule1',
    verbose_name='Cohort B Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_quarterly3_schedule_1 = Schedule(
    name='b_quarterly3_schedule1',
    verbose_name='Cohort B Quarterly Schedule V1',
    onschedule_model='flourish_caregiver.onschedulecohortbquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

b_quarterly1_schedule_1.add_visit(visit=visit2000)
b_quarterly2_schedule_1.add_visit(visit=visit2000)
b_quarterly3_schedule_1.add_visit(visit=visit2000)

# Generate Quarterly Visits
schedule_helper1 = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                  schedule=b_quarterly1_schedule_1, visit3000=visit3000)
schedule_helper1.create_quarterly_visits()

schedule_helper2 = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                  schedule=b_quarterly2_schedule_1, visit3000=visit3000)
schedule_helper2.create_quarterly_visits()

schedule_helper3 = ScheduleHelper(visit=visit2000, crfs=crf_2000,
                                  schedule=b_quarterly3_schedule_1, visit3000=visit3000)
schedule_helper3.create_quarterly_visits()

from edc_visit_schedule import Schedule

from ....crfs import crf_2001, caregiver_crfs_prn, requisitions_prn
from ...schedule_helper import ScheduleHelper
from ..caregiver_visits.cohort_c_visits import visit2001

# Quarterly Schedules
c_quarterly1_schedule_1 = Schedule(
    name='c_quarterly1_schedule1',
    sequence='2',
    verbose_name='Cohort C(First Child(ren)) Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_quarterly1_schedule_1.add_visit(visit=visit2001)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit2001, crfs=crf_2001,
                                 crfs_prn=caregiver_crfs_prn, requisitions_prn=requisitions_prn,
                                 schedule=c_quarterly1_schedule_1)
schedule_helper.create_quarterly_visits()

c_quarterly2_schedule_1 = Schedule(
    name='c_quarterly2_schedule1',
    sequence='2',
    verbose_name='Cohort C(Second Child(ren)) Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_quarterly3_schedule_1 = Schedule(
    name='c_quarterly3_schedule1',
    sequence='2',
    verbose_name='Cohort C(Third Child(ren)) Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

# Generate Quarterly Visits
visits = c_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    c_quarterly2_schedule_1.add_visit(visit=visit)
    c_quarterly3_schedule_1.add_visit(visit=visit)

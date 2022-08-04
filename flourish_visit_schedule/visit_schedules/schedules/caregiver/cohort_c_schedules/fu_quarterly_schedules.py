from edc_visit_schedule import Schedule

from ....crfs import crf_2001, caregiver_crfs_prn, caregiver_crfs_unscheduled, requisitions_prn
from ...schedule_helper import ScheduleHelper
from ..caregiver_visits.cohort_c_visits import visit3001

# Follow Up Quarterly Schedules
c_fu_quarterly1_schedule_1 = Schedule(
    name='c_fu_quarterly1_schedule1',
    sequence='4',
    verbose_name='Cohort C(First Child(ren)) FU Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcfuquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_fu_quarterly2_schedule_1 = Schedule(
    name='c_fu_quarterly2_schedule1',
    sequence='4',
    verbose_name='Cohort C(Second Child(ren)) FU Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcfuquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

c_fu_quarterly3_schedule_1 = Schedule(
    name='c_fu_quarterly3_schedule1',
    sequence='4',
    verbose_name='Cohort C(Third Child(ren)) FU Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortcfuquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

# Generate Follow Up Quarterly Visits
c_fu_quarterly1_schedule_1.add_visit(visit=visit3001)

schedule_helper1 = ScheduleHelper(visit=visit3001, crfs=crf_2001,
                                  crfs_unscheduled=caregiver_crfs_unscheduled,
                                  requisitions_prn=requisitions_prn,
                                  crfs_prn=caregiver_crfs_prn,
                                  schedule=c_fu_quarterly1_schedule_1)
schedule_helper1.create_quarterly_visits()

visits = c_fu_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    c_fu_quarterly2_schedule_1.add_visit(visit=visit)
    c_fu_quarterly3_schedule_1.add_visit(visit=visit)

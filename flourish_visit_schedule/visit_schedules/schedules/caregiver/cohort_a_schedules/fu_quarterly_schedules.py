from edc_visit_schedule import Schedule

from ....crfs import crf_2001, caregiver_crfs_prn, caregiver_crfs_unscheduled
from ....crfs import requisitions_prn
from ...schedule_helper import ScheduleHelper
from ..caregiver_visits.cohort_a_visits import visit3001, visit3001sq

# Quarterly Schedules
a_fu_quarterly1_schedule_1 = Schedule(
    name='a_fu_quarterly1_schedule1',
    sequence='6',
    verbose_name='Cohort A(First Child(ren)) FU Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortafuquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_fu_quarterly1_schedule_1.add_visit(visit=visit3001)

# Generate Quarterly Visits
schedule_helper = ScheduleHelper(visit=visit3001, crfs=crf_2001,
                                 crfs_unscheduled=caregiver_crfs_unscheduled,
                                 requisitions_prn=requisitions_prn,
                                 crfs_prn=caregiver_crfs_prn,
                                 schedule=a_fu_quarterly1_schedule_1)

schedule_helper.create_quarterly_visits()

a_fu_quarterly2_schedule_1 = Schedule(
    name='a_fu_quarterly2_schedule1',
    sequence='6',
    verbose_name='Cohort A(Second Child(ren)) FU Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortafuquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_fu_quarterly3_schedule_1 = Schedule(
    name='a_fu_quarterly3_schedule1',
    sequence='6',
    verbose_name='Cohort A(Third Child(ren)) FU Quarterly Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortafuquarterly',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

# Generate Quarterly Visits
visits = a_fu_quarterly1_schedule_1.visits
values = visits.values()

for visit in values:
    a_fu_quarterly2_schedule_1.add_visit(visit=visit)
    a_fu_quarterly3_schedule_1.add_visit(visit=visit)


# Sequential SEC-aims quarterly visits
a_sec_fu_quart1_schedule_1 = Schedule(
    name='a_sec_fu_quart1_schedule1',
    sequence='6',
    verbose_name='Cohort A(First Child(ren)) Sec FU Quarterly Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortasecseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_sec_fu_quart1_schedule_1.add_visit(visit=visit3001sq)

# Generate SEC-aims quarterly Visits
schedule_helper = ScheduleHelper(visit=visit3001sq, crfs=crf_2001,
                                 crfs_unscheduled=caregiver_crfs_unscheduled,
                                 requisitions_prn=requisitions_prn,
                                 crfs_prn=caregiver_crfs_prn,
                                 schedule=a_sec_fu_quart1_schedule_1,
                                 postfix='S')

schedule_helper.create_quarterly_visits()

a_sec_fu_quart2_schedule_1 = Schedule(
    name='a_sec_fu_quart2_schedule1',
    sequence='6',
    verbose_name='Cohort A(Second Child(ren)) Sec FU Quarterly Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortasecseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

a_sec_fu_quart3_schedule_1 = Schedule(
    name='a_sec_fu_quart3_schedule1',
    sequence='6',
    verbose_name='Cohort A(Third Child(ren)) Sec FU Quarterly Sequential',
    onschedule_model='flourish_caregiver.onschedulecohortasecseq',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.subjectconsent',
    appointment_model='edc_appointment.appointment'
    )

# Generate Quarterly Visits
visits = a_sec_fu_quart1_schedule_1.visits
values = visits.values()

for visit in values:
    a_sec_fu_quart2_schedule_1.add_visit(visit=visit)
    a_sec_fu_quart3_schedule_1.add_visit(visit=visit)

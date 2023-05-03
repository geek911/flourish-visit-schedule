from edc_visit_schedule import Schedule

# Tb Visit Schedules
from ..caregiver_visits.cohort_a_visits import visit2100, visit2200


a_tb1_2_months_schedule1 = Schedule(
    name='a_tb1_2_months_schedule1',
    verbose_name='TB 2 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb2months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

a_tb1_2_months_schedule1.add_visit(visit=visit2100)


a_tb2_2_months_schedule1 = Schedule(
    name='a_tb2_2_months_schedule1',
    verbose_name='TB 2 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb2months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

a_tb2_2_months_schedule1.add_visit(visit=visit2100)

a_tb3_2_months_schedule1 = Schedule(
    name='a_tb3_2_months_schedule1',
    verbose_name='TB 2 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb2months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

a_tb3_2_months_schedule1.add_visit(visit=visit2100)

a_tb1_6_months_schedule1 = Schedule(
    name='a_tb1_6_months_schedule1',
    verbose_name='TB 6 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb6months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

a_tb1_6_months_schedule1.add_visit(visit=visit2200)

a_tb2_6_months_schedule1 = Schedule(
    name='a_tb2_6_months_schedule1',
    verbose_name='TB 6 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb6months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

a_tb2_6_months_schedule1.add_visit(visit=visit2200)

a_tb3_6_months_schedule1 = Schedule(
    name='a_tb3_6_months_schedule1',
    verbose_name='TB 6 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb6months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

a_tb3_6_months_schedule1.add_visit(visit=visit2200)

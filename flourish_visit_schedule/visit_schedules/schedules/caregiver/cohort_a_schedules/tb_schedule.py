from edc_visit_schedule import Schedule

# Tb Visit Schedules
from ..caregiver_visits.cohort_a_visits import visit2100, visit2200

tb_2_months_schedule = Schedule(
    name='tb_2_months_schedule',
    verbose_name='TB 2 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb2months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

tb_2_months_schedule.add_visit(visit=visit2100)

tb_6_months_schedule = Schedule(
    name='tb_6_months_schedule',
    verbose_name='TB 6 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb6months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

tb_6_months_schedule.add_visit(visit=visit2200)




tb_two1_months_schedule = Schedule(
    name='tb_two1_months_schedule1',
    verbose_name='TB 2 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb2months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

tb_two1_months_schedule.add_visit(visit=visit2100)


tb_two2_months_schedule = Schedule(
    name='tb_two2_months_schedule1',
    verbose_name='TB 2 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb2months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

tb_two2_months_schedule.add_visit(visit=visit2100)

tb_two3_months_schedule = Schedule(
    name='tb_two3_months_schedule1',
    verbose_name='TB 2 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb2months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment')

tb_two3_months_schedule.add_visit(visit=visit2100)
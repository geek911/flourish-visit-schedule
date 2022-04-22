from edc_visit_schedule import Schedule

# Tb Visit Schedules
from ..caregiver_visits.cohort_a_visits import visit2100

tb_2_months_schedule = Schedule(
    name='tb_2_months_schedule',
    verbose_name='TB 2 Months Schedule',
    onschedule_model='flourish_caregiver.onschedulecohortatb2months',
    offschedule_model='flourish_caregiver.caregiveroffschedule',
    consent_model='flourish_caregiver.tbinformedconsent',
    appointment_model='edc_appointment.appointment'
    )

tb_2_months_schedule.add_visit(visit=visit2100)

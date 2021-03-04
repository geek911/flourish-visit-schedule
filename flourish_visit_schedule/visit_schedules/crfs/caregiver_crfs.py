from edc_visit_schedule import FormsCollection, Crf

crfs_prn = None

crf_pre_consent = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    name='pre_flourish')

a_crf_1000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=2, model='flourish_caregiver.medicalhistory'),
    Crf(show_order=3, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.arvsprepregnancy',
        required=False),
    Crf(show_order=5, model='flourish_caregiver.maternalarvduringpreg',
        required=False),
    Crf(show_order=6, model='flourish_caregiver.caregiverclinicalmeasurements'),
#     Crf(show_order=7, model='flourish_caregiver.foodfrequencyquestionnaire'),
    Crf(show_order=8, model='flourish_caregiver.caregiverphqdeprscreening',
        required=False),
    Crf(show_order=9, model='flourish_caregiver.caregiverhamddeprscreening',
        required=False),
    Crf(show_order=10, model='flourish_caregiver.caregiveredinburghdeprscreening',
        required=False),
    Crf(show_order=11, model='flourish_caregiver.caregivergadanxietyscreening'),
    Crf(show_order=12, model='flourish_caregiver.ultrasound',
        required=False),
    name='cohort_a_enrollment')

bc_crf_1000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=2, model='flourish_caregiver.medicalhistory'),
    Crf(show_order=3, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.caregiverclinicalmeasurements'),
#     Crf(show_order=5, model='flourish_caregiver.foodfrequencyquestionnaire'),
    Crf(show_order=6, model='flourish_caregiver.caregiverphqdeprscreening'),
    Crf(show_order=7, model='flourish_caregiver.caregiverhamddeprscreening'),
    Crf(show_order=8, model='flourish_caregiver.caregivergadanxietyscreening'),
    name='cohort_bc_enrollment')

crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.maternalarvduringpreg',
        required=False),
    Crf(show_order=2, model='flourish_caregiver.caregiverclinicalmeasurements'),
    Crf(show_order=3, model='flourish_caregiver.substanceuseduringpregnancy'),
    Crf(show_order=4, model='flourish_caregiver.maternalhivinterimhx'),
    Crf(show_order=5, model='flourish_caregiver.maternaldiagnoses'),
#     Crf(show_order=3, model='flourish_caregiver.maternalinterimidccdata'),
    name='birth')

crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=2, model='flourish_caregiver.medicalhistory'),
#     Crf(show_order=3, model='flourish_caregiver.vitalstatus'),
    name='quarterly_calls')

crf_4000 = FormsCollection(
    Crf(show_order=1, model='flourish_caregiver.sociodemographicdata'),
    Crf(show_order=2, model='flourish_caregiver.medicalhistory'),
    Crf(show_order=3, model='flourish_caregiver.hivviralloadandcd4',
        required=False),
    Crf(show_order=4, model='flourish_caregiver.caregiverclinicalmeasurements'),
#     Crf(show_order=5, model='flourish_caregiver.foodfrequencyquestionnaire',
#         required=False),
    Crf(show_order=6, model='flourish_caregiver.caregiveredinburghdeprscreening',
        required=False),
#     Crf(show_order=3, model='flourish_caregiver.vitalstatus'),
    name='follow_up')
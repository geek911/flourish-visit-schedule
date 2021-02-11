from edc_visit_schedule import FormsCollection, Crf

crfs_prn = None

child_a_crf_1000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childbirthscreening',
        required=False),
    Crf(show_order=2, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=3, model='flourish_child.childsociodemographic'),
    Crf(show_order=4, model='flourish_child.childclinicalmeasurements'),
    Crf(show_order=5, model='flourish_child.infantfeeding',
        required=False),
    name='child_cohort_a_enrollment')

child_bc_crf_1000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=3, model='flourish_child.childsociodemographic'),
    name='child_cohort_bc_enrollment')

child_crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.birthdata',
        required=False),
    Crf(show_order=2, model='flourish_child.birthexam'),
    Crf(show_order=3, model='flourish_child.infantcongenitalanomalies'),
    Crf(show_order=4, model='flourish_child.birthfeedingvaccine'),
    Crf(show_order=5, model='flourish_child.infantarvexposure',
        required=False),
    Crf(show_order=6, model='flourish_child.infantfeeding',
        required=False),
    Crf(show_order=7, model='flourish_child.childimmunizationhistory',
        required=False),
    name='birth')

child_a_crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.birthdata'),
    Crf(show_order=2, model='flourish_child.infantfeeding'),
    Crf(show_order=3, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=4, model='flourish_child.childsociodemographic'),
#     Crf(show_order=5, model='flourish_child.hospitalizationhistory'),
#     Crf(show_order=6, model='flourish_child.vitalstatus'),
    name='child_quarterly_calls')

child_bc_crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=2, model='flourish_child.childsociodemographic'),
    Crf(show_order=3, model='flourish_child.childmedicalhistory'),
    Crf(show_order=4, model='flourish_child.academicperformance'),
#     Crf(show_order=5, model='flourish_child.schoolattendance'),
#     Crf(show_order=6, model='flourish_child.vitalstatus'),
#     Crf(show_order=7, model='flourish_child.employment'),
    name='child_quarterly_calls')

child_ab_crf_4000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.infantfeeding',
        required=False),
    Crf(show_order=2, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=3, model='flourish_child.childsociodemographic'),
#     Crf(show_order=4, model='flourish_child.hospitalizationhistory'),
    Crf(show_order=5, model='flourish_child.childclinicalmeasurements'),
#     Crf(show_order=6, model='flourish_child.vitalstatus'),
    name='child_follow_up')

child_c_crf_4000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.infantfeeding',
        required=False),
    Crf(show_order=2, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=3, model='flourish_child.childsociodemographic'),
#     Crf(show_order=4, model='flourish_child.hospitalizationhistory'),
    Crf(show_order=5, model='flourish_child.childclinicalmeasurements'),
#     Crf(show_order=6, model='flourish_child.vitalstatus'),
    name='child_follow_up')
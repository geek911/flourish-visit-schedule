from edc_visit_schedule import FormsCollection, Crf

crfs_prn = None

child_a_crf_1000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childbirthscreening',
        required=False),
    Crf(show_order=2, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=3, model='flourish_child.childsociodemographic'),
    Crf(show_order=4, model='flourish_child.infantfeeding',
        required=False),
    name='child_cohort_a_enrollment')

child_bc_crf_1000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=3, model='flourish_child.childsociodemographic'),
    name='child_cohort_bc_enrollment')

child_crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=2, model='flourish_child.childimmunizationhistory'),
    name='child_quarterly_calls')

child_crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=2, model='flourish_child.childimmunizationhistory'),
    name='child_follow_up')
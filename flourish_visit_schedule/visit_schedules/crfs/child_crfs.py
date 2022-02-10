from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=1, model='flourish_child.childcliniciannotes',
        required=False, additional=False),
    name='child_crf_prn')

crfs_unscheduled = FormsCollection(
    Crf(show_order=1, model='flourish_child.childcliniciannotes'),
    name='unscheduled')

child_a_crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childhivrapidtestcounseling'),
    Crf(show_order=2, model='flourish_child.childbirthscreening',
        required=False),
    Crf(show_order=3, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=4, model='flourish_child.childmedicalhistory'),
    Crf(show_order=5, model='flourish_child.childsociodemographic'),
    Crf(show_order=6, model='flourish_child.childclinicalmeasurements'),
    Crf(show_order=7, model='flourish_child.infantfeeding', required=False),
    Crf(show_order=8, model='flourish_child.childfoodsecurityquestionnaire'),
    Crf(show_order=9, model='flourish_child.childcliniciannotes'),
    Crf(show_order=10, model='flourish_child.childcovid19'),
    Crf(show_order=11, model='flourish_child.childhospitalization'),
    Crf(show_order=12, model='flourish_child.childprevioushospitalization'),
    name='child_cohort_a_enrollment')

child_b_crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childhivrapidtestcounseling'),
    Crf(show_order=2, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=3, model='flourish_child.childmedicalhistory'),
    Crf(show_order=4, model='flourish_child.childclinicalmeasurements'),
    Crf(show_order=5, model='flourish_child.childsociodemographic'),
    Crf(show_order=6, model='flourish_child.childphysicalactivity'),
    Crf(show_order=7, model='flourish_child.childtannerstaging',
        required=False),
    Crf(show_order=8, model='flourish_child.childfoodsecurityquestionnaire'),
    Crf(show_order=9, model='flourish_child.academicperformance',
        required=False),
    Crf(show_order=10, model='flourish_child.childcliniciannotes'),
    Crf(show_order=11, model='flourish_child.childcovid19'),
    Crf(show_order=12, model='flourish_child.childprevioushospitalization'),
    Crf(show_order=13, model='flourish_child.childhospitalization'),
    name='child_cohort_b_enrollment')

child_c_crf_2000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childhivrapidtestcounseling'),
    Crf(show_order=2, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=3, model='flourish_child.childmedicalhistory'),
    Crf(show_order=4, model='flourish_child.childclinicalmeasurements'),
    Crf(show_order=5, model='flourish_child.childsociodemographic'),
    Crf(show_order=6, model='flourish_child.childphysicalactivity'),
    Crf(show_order=7, model='flourish_child.childphqdepressionscreening',
        required=False),
    Crf(show_order=8, model='flourish_child.childphqreferral',
        required=False),
    Crf(show_order=9, model='flourish_child.childgadanxietyscreening',
        required=False),
    Crf(show_order=10, model='flourish_child.childgadreferral',
        required=False),
    Crf(show_order=11, model='flourish_child.childtannerstaging',
        required=False),
    Crf(show_order=12, model='flourish_child.academicperformance',
        required=False),
    Crf(show_order=13, model='flourish_child.childfoodsecurityquestionnaire'),
    Crf(show_order=14, model='flourish_child.childpregtesting',
        required=False),
    Crf(show_order=15, model='flourish_child.childcliniciannotes'),
    Crf(show_order=16, model='flourish_child.childcovid19'),
    Crf(show_order=17, model='flourish_child.childprevioushospitalization'),
    Crf(show_order=18, model='flourish_child.childhospitalization'),
    name='child_cohort_c_enrollment')

child_birth_crf_2000D = FormsCollection(
    Crf(show_order=1, model='flourish_child.birthdata',
        required=False),
    Crf(show_order=2, model='flourish_child.birthexam'),
    Crf(show_order=3, model='flourish_child.infantfeeding'),
    Crf(show_order=4, model='flourish_child.birthfeedingvaccine'),
    Crf(show_order=5, model='flourish_child.infantcongenitalanomalies'),
    Crf(show_order=6, model='flourish_child.infantarvexposure',
        required=False),
    Crf(show_order=7, model='flourish_child.childcliniciannotes'),
    Crf(show_order=8, model='flourish_child.childcovid19'),
    name='birth')

child_a_crf_2001 = FormsCollection(
    Crf(show_order=1, model='flourish_child.birthdata', required=False),
    Crf(show_order=2, model='flourish_child.infantfeeding', required=False),
    Crf(show_order=3, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=4, model='flourish_child.childsociodemographic'),
    Crf(show_order=5, model='flourish_child.childmedicalhistory'),
    Crf(show_order=6, model='flourish_child.childprevioushospitalization'),
    Crf(show_order=7, model='flourish_child.childcovid19'),
    Crf(show_order=8, model='flourish_child.childhospitalization'),
    Crf(show_order=9, model='flourish_child.childprevioushospitalization'),
    name='child_quarterly_calls')

child_b_crf_2001 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=2, model='flourish_child.childsociodemographic'),
    Crf(show_order=3, model='flourish_child.childmedicalhistory'),
    Crf(show_order=4, model='flourish_child.academicperformance'),
    Crf(show_order=5, model='flourish_child.childcovid19'),
    Crf(show_order=6, model='flourish_child.childprevioushospitalization'),
    Crf(show_order=7, model='flourish_child.childhospitalization'),
    name='child_quarterly_calls')

child_c_crf_2001 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=2, model='flourish_child.childsociodemographic'),
    Crf(show_order=3, model='flourish_child.childmedicalhistory'),
    Crf(show_order=4, model='flourish_child.academicperformance',
        required=False),
    Crf(show_order=7, model='flourish_child.childworkingstatus',
        required=False),
    Crf(show_order=8, model='flourish_child.childcovid19'),
    Crf(show_order=9, model='flourish_child.childprevioushospitalization'),
    Crf(show_order=10, model='flourish_child.childhospitalization'),
    name='child_quarterly_calls')

child_a_crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childhivrapidtestcounseling'),
    Crf(show_order=2, model='flourish_child.infantfeeding'),
    Crf(show_order=3, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=4, model='flourish_child.childmedicalhistory'),
    Crf(show_order=5, model='flourish_child.childsociodemographic'),
    Crf(show_order=6, model='flourish_child.childprevioushospitalization'),
    Crf(show_order=7, model='flourish_child.childclinicalmeasurements'),
    Crf(show_order=8, model='flourish_child.childfoodsecurityquestionnaire'),
    Crf(show_order=9, model='flourish_child.childcliniciannotes'),
    Crf(show_order=10, model='flourish_child.childcovid19'),
    Crf(show_order=11, model='flourish_child.childhospitalization'),
    name='child_a_follow_up')

child_b_crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=2, model='flourish_child.childsociodemographic'),
    Crf(show_order=3, model='flourish_child.childclinicalmeasurements'),
    Crf(show_order=4, model='flourish_child.childmedicalhistory'),
    Crf(show_order=5, model='flourish_child.childphysicalactivity'),
    Crf(show_order=6, model='flourish_child.childfoodsecurityquestionnaire'),
    Crf(show_order=7, model='flourish_child.academicperformance'),
    Crf(show_order=8, model='flourish_child.childcliniciannotes'),
    Crf(show_order=9, model='flourish_child.childcovid19'),
    Crf(show_order=10, model='flourish_child.childprevioushospitalization'),
    Crf(show_order=11, model='flourish_child.childhospitalization'),
    name='child_b_follow_up')

child_c_crf_3000 = FormsCollection(
    Crf(show_order=1, model='flourish_child.childimmunizationhistory'),
    Crf(show_order=2, model='flourish_child.childsociodemographic'),
    Crf(show_order=3, model='flourish_child.childclinicalmeasurements'),
    Crf(show_order=4, model='flourish_child.childmedicalhistory'),
    Crf(show_order=5, model='flourish_child.childphysicalactivity'),
    Crf(show_order=6, model='flourish_child.academicperformance',
        required=False),
    Crf(show_order=7, model='flourish_child.childphqdepressionscreening',
        required=False),
    Crf(show_order=8, model='flourish_child.childphqreferral',
        required=False),
    Crf(show_order=9, model='flourish_child.childgadanxietyscreening',
        required=False),
    Crf(show_order=10, model='flourish_child.childgadreferral',
        required=False),
    Crf(show_order=11, model='flourish_child.childcliniciannotes'),
    Crf(show_order=12, model='flourish_child.childcovid19'),
    Crf(show_order=13, model='flourish_child.childprevioushospitalization'),
    name='child_c_follow_up')

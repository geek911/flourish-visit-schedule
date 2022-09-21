from edc_visit_schedule import FormsCollection, Requisition
from flourish_labs import dna_pcr_panel, stool_sample_panel
from flourish_labs import infant_pl_cytokines_panel, rectal_swab_panel

child_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=dna_pcr_panel, required=False, additional=False),
    Requisition(
        show_order=20,
        panel=stool_sample_panel, required=False, additional=False),
    Requisition(
        show_order=30,
        panel=infant_pl_cytokines_panel, required=False, additional=False),
    Requisition(
        show_order=40,
        panel=rectal_swab_panel, required=False, additional=False),
    name='child_requisitions',

)

child_requisitions_bc = FormsCollection(
)

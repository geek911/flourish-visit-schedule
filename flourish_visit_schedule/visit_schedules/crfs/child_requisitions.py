from edc_visit_schedule import FormsCollection, Requisition

from flourish_labs import chemistry_panel, fbc_panel, lead_panel
from flourish_labs import child_pl_store_panel, infant_pl_cytokines_panel, \
    rectal_swab_panel
from flourish_labs import dna_pcr_panel, serum_panel, stool_sample_panel
from flourish_labs import fasting_glucose_panel, fasting_insulin_panel, \
    lithium_heparin_panel

requisitions_prn = FormsCollection(
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
    Requisition(
        show_order=50,
        panel=fasting_glucose_panel, required=False, additional=False),
    Requisition(
        show_order=60,
        panel=fasting_insulin_panel, required=False, additional=False),
    Requisition(
        show_order=70,
        panel=chemistry_panel, required=False, additional=False),
    Requisition(
        show_order=80,
        panel=lead_panel, required=False, additional=False),
    Requisition(
        show_order=90,
        panel=fbc_panel, required=False, additional=False),
    Requisition(
        show_order=100,
        panel=serum_panel, required=False, additional=False),
    Requisition(
        show_order=110,
        panel=child_pl_store_panel, required=False, additional=False),
    Requisition(
        show_order=120,
        panel=lithium_heparin_panel, required=False, additional=False),
    name='requisitions_prn')

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

# Follow Up Requisitions
ab_fu_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=lead_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=fbc_panel, required=True, additional=False),
    Requisition(
        show_order=30,
        panel=child_pl_store_panel, required=True, additional=False),

)

c_fu_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=lead_panel, required=True, additional=False),
    Requisition(
        show_order=20,
        panel=fbc_panel, required=True, additional=False),
    Requisition(
        show_order=30,
        panel=fasting_glucose_panel, required=True, additional=False),
    Requisition(
        show_order=40,
        panel=fasting_insulin_panel, required=True, additional=False),
    Requisition(
        show_order=50,
        panel=chemistry_panel, required=True, additional=False),
    Requisition(
        show_order=60,
        panel=child_pl_store_panel, required=True, additional=False),
    Requisition(
        show_order=70,
        panel=serum_panel, required=True, additional=False),
)

tb_adol_requisitions = FormsCollection(
    Requisition(
        show_order=1,
        panel=lithium_heparin_panel, required=False, additional=False),
)

brain_ultrasound_requisitions = FormsCollection(
    Requisition(
        show_order=1,
        panel=rectal_swab_panel, required=True, additional=False),

    Requisition(
        show_order=30,
        panel=child_pl_store_panel, required=True, additional=False),
)

brain_ultrasound_requisitions = FormsCollection(
    Requisition(
        show_order=1,
        panel=rectal_swab_panel, required=True, additional=False),
    )

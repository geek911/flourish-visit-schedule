from edc_visit_schedule import FormsCollection, Requisition

from flourish_labs import (viral_load_panel, cd4_panel,
                           hematology_panel, cbc_panel, breast_milk_pellet_panel)

requisitions_prn = FormsCollection(
    Requisition(
        show_order=10,
        panel=cd4_panel, required=False, additional=False),
    Requisition(
        show_order=20,
        panel=viral_load_panel, required=False, additional=False),
    Requisition(
        show_order=30,
        panel=hematology_panel, required=False, additional=False),
    Requisition(
        show_order=40,
        panel=cbc_panel, required=False, additional=False),

    name='requisitions_prn')

# Main Study Requisitions
preg_requisitions = FormsCollection(
    Requisition(
        show_order=10,
        panel=viral_load_panel, required=True, additional=False),

    Requisition(show_order=20,
                panel=breast_milk_pellet_panel, required=True, additional=False),
)

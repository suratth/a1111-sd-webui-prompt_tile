import gradio as gr
import hogehoge

import ui_extra_networks_pronpt
from modules import script_callbacks, ui_extra_networks, extra_networks, shared

def before_ui():
    ui_extra_networks.register_page(ui_extra_networks_pronpt.ExtraNetworksPagePRONPT())

script_callbacks.on_before_ui(before_ui)

#shared.options_templates.update(shared.options_section(('extra_networks', "Extra Networks"), {
#    "sd_pronpt": shared.OptionInfo("None", "Add Pronpt Preset to prompt", gr.Dropdown, lambda: {"choices": [""] + [x for x in hogehoge.available_pronpt]}, refresh=hogehoge.list_available_pronpt),
#}))

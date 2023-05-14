import json
import os
import hogehoge
import html
import re

from modules import shared, ui_extra_networks


class ExtraNetworksPagePRONPT(ui_extra_networks.ExtraNetworksPage):
    def __init__(self):
        super().__init__('PRONPT')

    def refresh(self):
        hogehoge.list_available_pronpt()

    def extract_text_between_strings(self,text, start, end=""):
        start_index = text.find(start)
        if start_index == -1:
            return ""
        start_index += len(start)
        if end == "":
            return text[start_index:].rstrip()
        end_index = text.find(end, start_index)
        if end_index == -1:
            return ""
        return text[start_index:end_index].rstrip()

    def list_items(self):
        for name, pronpt_on_disk in hogehoge.available_pronpt.items():
            path, ext = os.path.splitext(pronpt_on_disk.filename)
            
            f = open(pronpt_on_disk.filename,'r')
            data = f.read()
            f.close()

            pos = self.extract_text_between_strings(data,"pro:","neg:")
            neg = self.extract_text_between_strings(data,"neg:","")


            print(pos)
            print(neg)

            yield {
                "name": name,
                "filename": path,
                "preview": self.find_preview(path),
                "description": self.find_description(path),
                "search_term": self.search_terms_from_path(pronpt_on_disk.filename),
                "prompt": (
                    json.dumps(pos)
                    + " + " + json.dumps("")
                    + " + " + json.dumps("")
                ),
                "neg_prompt": (
                    json.dumps(neg)
                    + " + " + json.dumps("")
                    + " + " + json.dumps("")
                ),
                "local_preview": f"{path}.{shared.opts.samples_format}",
                "metadata": json.dumps(pronpt_on_disk.metadata, indent=4) if pronpt_on_disk.metadata else None,
            }

    def create_html_for_item(self, item, tabname):
        preview = item.get("preview", None)

        onclick = item.get("onclick", None)
        if onclick is None:
            onclick = '"' + html.escape(f"""return cardClicked_plus({json.dumps(tabname)}, {item["prompt"]}, {item["neg_prompt"]})""") + '"'

        height = f"height: {shared.opts.extra_networks_card_height}px;" if shared.opts.extra_networks_card_height else ''
        width = f"width: {shared.opts.extra_networks_card_width}px;" if shared.opts.extra_networks_card_width else ''
        background_image = f"background-image: url(\"{html.escape(preview)}\");" if preview else ''
        metadata_button = ""
        metadata = item.get("metadata")
        if metadata:
            metadata_button = f"<div class='metadata-button' title='Show metadata' onclick='extraNetworksRequestMetadata(event, {json.dumps(self.name)}, {json.dumps(item['name'])})'></div>"

        local_path = ""
        filename = item.get("filename", "")
        for reldir in self.allowed_directories_for_previews():
            absdir = os.path.abspath(reldir)

            if filename.startswith(absdir):
                local_path = filename[len(absdir):]

        # if this is true, the item must not be show in the default view, and must instead only be
        # shown when searching for it
        serach_only = "/." in local_path or "\\." in local_path

        args = {
            "style": f"'display: none; {height}{width}{background_image}'",
            "prompt": item.get("prompt", None),
            "tabname": json.dumps(tabname),
            "local_preview": json.dumps(item["local_preview"]),
            "name": item["name"],
            "description": (item.get("description") or ""),
            "card_clicked": onclick,
            "save_card_preview": '"' + html.escape(f"""return saveCardPreview(event, {json.dumps(tabname)}, {json.dumps(item["local_preview"])})""") + '"',
            "search_term": item.get("search_term", ""),
            "metadata_button": metadata_button,
            "serach_only": " search_only" if serach_only else "",
        }

        return self.card_page.format(**args)


    def allowed_directories_for_previews(self):
        return ["D:\sdw\stable-diffusion-webui\stable-diffusion-webui\models\PRONPT"]
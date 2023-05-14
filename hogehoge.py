from typing import *
import os, sys
import re
import glob

from modules import shared, devices, sd_models, errors

metadata_tags_order = {"ss_sd_model_name": 1, "ss_resolution": 2, "ss_clip_skip": 3, "ss_num_train_images": 10, "ss_tag_frequency": 20}

class pronpt_OnDisk:
    def __init__(self, name, filename):
        self.name = name
        self.filename = filename
        self.metadata = {}

        _, ext = os.path.splitext(filename)
        if ext.lower() == ".safetensors":
            try:
                self.metadata = sd_models.read_metadata_from_safetensors(filename)
            except Exception as e:
                errors.display(e, f"reading lora {filename}")

        if self.metadata:
            m = {}
            for k, v in sorted(self.metadata.items(), key=lambda x: metadata_tags_order.get(x[0], 999)):
                m[k] = v

            self.metadata = m

        self.ssmd_cover_images = self.metadata.pop('ssmd_cover_images', None)  # those are cover images and they are too big to display in UI as text


def list_available_pronpt():
    available_pronpt.clear()

    os.makedirs("D:\sdw\stable-diffusion-webui\stable-diffusion-webui\models\PRONPT", exist_ok=True)

    candidates = \
        glob.glob(os.path.join("D:\sdw\stable-diffusion-webui\stable-diffusion-webui\models\PRONPT", '**/*.txt'), recursive=True)

    for filename in sorted(candidates, key=str.lower):
        if os.path.isdir(filename):
            continue

        name = os.path.splitext(os.path.basename(filename))[0]

        available_pronpt[name] = pronpt_OnDisk(name, filename)

available_pronpt: Dict[str, pronpt_OnDisk] = {}

list_available_pronpt()

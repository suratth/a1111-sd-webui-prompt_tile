import os
from modules import paths


def preload(parser):
    parser.add_argument("--PRONPT-dir", type=str, help="Path to directory with PRONPT.", default=os.path.join(paths.models_path, 'PRONPT'))

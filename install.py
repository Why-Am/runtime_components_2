"""Script that installs the config files"""

from pathlib import Path
from sys import stderr

import configuration as cfg

USAGE = "USAGE: install.py"
CONFIGS_DIR_PATH = Path(__file__).parent / "configs"

for config in cfg.INSTALLATION_CONFIGS:
    filepath = CONFIGS_DIR_PATH / config.filename
    if not filepath.exists():
        print(f'Error: could not find file "{config.filename}" at "{filepath}".', file=stderr)
        print("Continuing.", file=stderr)
        continue

    print(f"Installing {config.filename}...")
    # TODO install config

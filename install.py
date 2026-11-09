"""Script that installs the config files"""

import platform
from pathlib import Path
from sys import exit, stderr

from configuration import INSTALLATION_CONFIGS

USAGE = "USAGE: install.py"

WINDOWS = "Windows"
LINUX = "Linux"
# MACOS = "Darwin"  # Not implemented (cannot test)

CONFIGS_DIR_PATH = Path(__file__).parent / "configs"

CURRENT_OS = platform.system()
if CURRENT_OS not in (WINDOWS, LINUX):
    print(f"Error: the operating system {CURRENT_OS} is not supported.", file=stderr)
    exit(1)

config_count = 0
installed_count = 0

for config in INSTALLATION_CONFIGS:
    if CURRENT_OS == WINDOWS:
        install_path = config.windows_install_path
    elif CURRENT_OS == LINUX:
        install_path = config.linux_install_path
    else:
        raise AssertionError("Unreachable")

    if install_path is None:
        continue

    config_count += 1

    filepath = CONFIGS_DIR_PATH / config.filename
    if not filepath.exists():
        print(
            f'Error: could not find file "{config.filename}" at "{filepath}".',
            file=stderr,
        )
        print("Continuing.")
        continue
    if filepath.is_dir():
        print(f'Error: "{filepath}" is a directory, not a file.', file=stderr)
        print("Continuing.")
        continue

    if config.filename != install_path.name:
        print(f'Installing "{config.filename}" as "{install_path.name}"...')
    else:
        print(f'Installing "{config.filename}"...')

    file_contents = filepath.read_text()

    if install_path.is_file():
        if file_contents != install_path.read_text():
            # TODO prompt for now, but add backup capability later
            ans = input(
                f'Contents of the existing file at "{install_path}" differ from that of the file '
                + "being installed. Overwrite (y/n)? "
            )
            if ans.lower() != "y":
                print(f'"{config.filename}" not installed.')
                continue
        else:
            print(f'"{install_path}" already up to date.')
            config_count -= 1
            continue
    else:
        install_path.parent.mkdir(parents=True, exist_ok=True)

    install_path.write_text(file_contents)
    print(f'"{install_path.name}" installed.')
    installed_count += 1

print(f"Installed {installed_count}/{config_count} configs.")

"""Script that installs the config files"""

import platform
from pathlib import Path
from sys import argv, exit, stderr

from configuration import INSTALLATION_CONFIGS

USAGE = "USAGE: install.py [--dry-run]"

WINDOWS = "Windows"
LINUX = "Linux"
# MACOS = "Darwin"  # Not implemented (cannot test)

CONFIGS_DIR_PATH = Path(__file__).parent / "configs"

dry_run = False
for arg in argv[1:]:
    if arg == "--dry-run":
        dry_run = True
    else:
        exit(f"Error: unrecognized argument '{arg}'\n{USAGE}")

if dry_run:
    print("Starting dry run (no files will be changed)...")

CURRENT_OS = platform.system()
if CURRENT_OS not in (WINDOWS, LINUX):
    exit(f"Error: the operating system '{CURRENT_OS}' is not supported.")

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
            f"Error: could not find file '{config.filename}' at '{filepath}'.",
            file=stderr,
        )
        print("Continuing.")
        continue
    if filepath.is_dir():
        print(f"Error: '{filepath}' is a directory, not a file.", file=stderr)
        print("Continuing.")
        continue

    if config.filename != install_path.name:
        print(f"Installing '{config.filename}' as '{install_path.name}'...")
    else:
        print(f"Installing '{config.filename}'...")

    file_contents = filepath.read_text(encoding="utf-8")

    if install_path.is_file():
        if file_contents != install_path.read_text(encoding="utf-8"):
            # TODO prompt for now, but add backup capability later
            ans = input(
                f"Contents of the existing file at '{install_path}' differ from that of the file "
                + "being installed. Overwrite (y/n)? "
            )
            if ans.lower() != "y":
                print(f"'{config.filename}' not installed.")
                continue
        else:
            print("Already up to date.")
            config_count -= 1
            continue
    else:
        if not dry_run:
            install_path.parent.mkdir(parents=True, exist_ok=True)

    if not dry_run:
        install_path.write_text(file_contents, encoding="utf-8")

    print(f"'{install_path.name}' installed.")
    installed_count += 1

print("---")
if dry_run:
    print("Dry run result:")
else:
    print("Result:")
print(f"Installed {installed_count}/{config_count} installable configs.")

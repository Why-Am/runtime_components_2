"""Script that installs the config files"""

import platform
from pathlib import Path
from sys import argv, exit, stderr

from configuration import INSTALLATION_CONFIGS

USAGE = "USAGE: install.py [--dry-run]"

WINDOWS = "Windows"
LINUX = "Linux"
MACOS = "Darwin"

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
if CURRENT_OS not in (WINDOWS, LINUX, MACOS):
    exit(f"Error: the operating system '{CURRENT_OS}' is not supported.")

# A config is pending if it's not already up to date in its installed location.
# We want to keep track of these in particular because these are where issues may arise,
# e.g. missing source files, conflicts, failed writes.
pending_config_count = 0
successfully_installed_count = 0

for config in INSTALLATION_CONFIGS:
    if CURRENT_OS == WINDOWS:
        install_path = config.windows_install_path
    elif CURRENT_OS == LINUX:
        install_path = config.linux_install_path
    elif CURRENT_OS == MACOS:
        install_path = config.macos_install_path
    else:
        raise AssertionError("Unreachable")

    if install_path is None:
        continue

    pending_config_count += 1

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
        # To aid with cross-compatibility, the filename of the final installed file is allowed to
        # differ from that of the file stored in this repository.
        print(f"Installing '{config.filename}' as '{install_path.name}'...")
    else:
        print(f"Installing '{config.filename}'...")

    # Standardize on utf-8
    file_contents = filepath.read_text(encoding="utf-8")

    if install_path.is_file():
        if file_contents != install_path.read_text(encoding="utf-8"):
            # TODO prompt for now, but add backup capability later
            # This protects against accidentally overwriting an existing file that the user may not
            # have known about
            ans = input(
                f"Contents of the existing file at '{install_path}' differ from that of the file "
                + "being installed. Overwrite (y/n)? "
            )
            if ans.lower() != "y":
                print(f"'{config.filename}' not installed.")
                continue
        else:
            print("Already up to date.")
            pending_config_count -= 1
            continue
    else:
        if not dry_run:
            install_path.parent.mkdir(parents=True, exist_ok=True)

    if not dry_run:
        install_path.write_text(file_contents, encoding="utf-8")

    print(f"'{install_path.name}' installed.")
    successfully_installed_count += 1

print("---")
if dry_run:
    print("Dry run result:")
else:
    print("Result:")
print(
    f"Installed {successfully_installed_count}/{pending_config_count} pending configs."
)

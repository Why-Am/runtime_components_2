from dataclasses import dataclass
from pathlib import Path


@dataclass
class InstallationConfig:
    filename: str
    windows_install_path: Path | None = None
    linux_install_path: Path | None = None
    macos_install_path: Path | None = None

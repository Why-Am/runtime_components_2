from pathlib import Path


class InstallationConfig:
    def __init__(
        self,
        filename: str,
        windows_install_path: Path | None = None,
        linux_install_path: Path | None = None,
        macos_install_path: Path | None = None
    ):
        self.filename = filename
        self.windows_install_path = windows_install_path
        self.linux_install_path = linux_install_path
        self.macos_install_path = macos_install_path

from pathlib import PosixPath, WindowsPath


class InstallationConfig:
    def __init__(
        self,
        filename: str,
        windows_install_path: WindowsPath,
        linux_install_path: PosixPath,
        macos_install_path: PosixPath
    ):
        self.filename = filename
        self.windows_install_path = windows_install_path
        self.linux_install_path = linux_install_path
        self.macos_install_path = macos_install_path
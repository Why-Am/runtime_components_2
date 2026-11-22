from pathlib import Path

from library.installation_config_class import InstallationConfig

INSTALLATION_CONFIGS = (
    InstallationConfig(
        filename = "dummy.conf",
        windows_install_path = Path.home() / ".config" / "dummy" / "dummy.conf",
        linux_install_path = Path.home() / ".config" / "dummy" / "dummy.conf",
    ),
    InstallationConfig(
        filename = ".vimrc",
        windows_install_path = Path.home() / "AppData" / "Local" / "nvim" / "init.vim",
        linux_install_path = Path.home() / ".vimrc"
    ),
    InstallationConfig(
        filename = "Microsoft.PowerShell_profile.ps1",
        windows_install_path = Path.home() / "OneDrive" / "Documents" / "WindowsPowerShell" / "Microsoft.PowerShell_profile.ps1"
    ),
    InstallationConfig(
        filename = ".bashrc",
        linux_install_path = Path.home() / ".bashrc"
    )
)

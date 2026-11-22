# Aliases
function Start-Python-REPL { uv run python }
Set-Alias -Name py -Value Start-Python-REPL

function random-practice {
    uv run $HOME\Projects\random_practice\main.py
}

function sync-vault {
    cd $HOME\vault
    lazygit
}

# Improve tab autocomplete
Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete

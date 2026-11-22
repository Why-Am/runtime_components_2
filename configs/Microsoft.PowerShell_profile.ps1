# Aliases
function py {
    uv run python
}

function random-practice {
    uv run $HOME\Projects\random_practice\main.py
}

function sync-vault {
    cd $HOME\vault
    lazygit
}

# Improve tab autocomplete
Set-PSReadLineKeyHandler -Key Tab -Function MenuComplete

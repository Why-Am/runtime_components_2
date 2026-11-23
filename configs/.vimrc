" ~/.vimrc — read by vim every time it starts.
" Lines starting with a double quote are comments.

" ---------------------------------------------------------------------------
" Basics
" ---------------------------------------------------------------------------
set nocompatible            " use vim features, not strict old-vi behavior
syntax on                   " color the code
filetype plugin indent on   " language-aware indentation (C, Python, ...)
set encoding=utf-8
set backspace=indent,eol,start  " backspace works the way you expect

" ---------------------------------------------------------------------------
" What you see
" ---------------------------------------------------------------------------
set number                  " line numbers — compiler errors cite them
set relativenumber          " relative line numbers for easier jumping
set ruler                   " cursor position in the bottom right
set showcmd                 " show partially typed commands
set laststatus=2            " always show the status line
set showmatch               " briefly jump to the matching bracket
set scrolloff=5             " keep 5 lines visible above/below the cursor
set colorcolumn=80          " vertical guide at column 80
set wildmenu                " tab-completion menu for : commands

" ---------------------------------------------------------------------------
" Indentation
" ---------------------------------------------------------------------------
" Match these numbers to your course's code standard.
const tab_size=4            " constant; change this to set tab size
set tabstop=tab_size        " a tab character displays as tab_size columns
set shiftwidth=tab_size     " >> and auto-indent move by tab_size columns
set softtabstop=tab_size    " the Tab key inserts tab_size columns
set expandtab               " insert spaces, never tab characters
set autoindent              " new lines keep the previous line's indent

" Makefiles REQUIRE real tab characters. Without this line, expandtab above
" would silently break every Makefile you edit.
autocmd FileType make setlocal noexpandtab

" ---------------------------------------------------------------------------
" Searching  ( /word  then  n  for next,  N  for previous )
" ---------------------------------------------------------------------------
set incsearch               " jump to matches while you type
set hlsearch                " highlight all matches
set ignorecase              " case-insensitive search...
set smartcase               " ...unless you type a capital letter

" ---------------------------------------------------------------------------
" Convenience
" ---------------------------------------------------------------------------
" Reopen a file at the line where you last left it.
autocmd BufReadPost *
    \ if line("'\"") > 1 && line("'\"") <= line("$") |
    \   exe "normal! g'\"" |
    \ endif


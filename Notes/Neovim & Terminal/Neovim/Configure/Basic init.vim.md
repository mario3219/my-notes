````
" ================================
" Startup Layout (Explorer + Terminal)
" ================================

if argc() == 0
  augroup NvimStartupLayout
    autocmd!
    autocmd VimEnter * call s:StartupView()
  augroup END
endif

function! s:StartupView()
  enew
  silent! Explore
  set number
  wincmd H
  vertical resize 40
  wincmd L

  belowright split
  execute 'terminal'

  " Turn off line numbers inside the terminal
  setlocal nonumber norelativenumber

  wincmd k

  " Ensure line numbers are ON for the editor
  setlocal number 

  resize +20
endfunction

" ================================
" Plugin Manager
" ================================

" Empty

" ================================
" Line Numbers Logic
" ================================

" Global default: numbers ON
set number

" Always disable numbers in terminal buffers
autocmd TermOpen * setlocal nonumber norelativenumber

" Auto-enable numbers when opening a normal file
autocmd BufEnter * if &buftype == '' | setlocal number | endif

" ================================
" Netrw (File Explorer) Cleanup
" ================================

let g:netrw_banner = 0          " No top banner
let g:netrw_liststyle = 3       " Tree-style view
let g:netrw_browse_split = 0    " Open files in the same window
let g:netrw_winsize = 25        " Width percentage
set number

" ================================
" Basic Usability Tweaks
" ================================

set mouse=a                      " Enable mouse
set clipboard=unnamedplus         " Use system clipboard
syntax enable                     " Syntax highlighting
filetype plugin indent on         " Enable filetype plugins

" Line numbers in :Explore
let g:netrw_bufsettings = 'noma nomod nu nowrap ro nobl'
```

" ================================
" Custom commands
" ================================

command! -range -nargs=1 CommentRange <line1>,<line2>s/^/<args>/
command! -range -nargs=1 UnCommentRange <line1>,<line2>s/^<args>//

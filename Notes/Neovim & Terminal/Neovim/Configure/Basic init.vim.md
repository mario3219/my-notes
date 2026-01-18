````
let mapleader = " "
" Start in git repository
"cd D:\git-repositories

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
set number

" Always open files from netrw in a vertical split
let g:netrw_browse_split = 2

" Open splits to the right
let g:netrw_altv = 1

" Keep netrw buffer open
let g:netrw_keepdir = 1

let g:netrw_browse_split = 2
let g:netrw_altv = 1
let g:netrw_winsize = 80

" ================================
" Basic Usability Tweaks
" ================================

set mouse=a                      " Enable mouse
set clipboard=unnamedplus         " Use system clipboard
syntax enable                     " Syntax highlighting
filetype plugin indent on         " Enable filetype plugins

" Line numbers in :Explore
let g:netrw_bufsettings = 'noma nomod nu nowrap ro nobl'

" ================================
" Custom commands
" ================================

command! -range -nargs=1 CommentRange <line1>,<line2>s/^/<args>/
command! -range -nargs=1 UnCommentRange <line1>,<line2>s/^<args>//

" ================================
" Keybinds
" ================================

tnoremap <Esc> <C-\><C-n>
nnoremap <leader><Left> :vertical resize -20<CR>
nnoremap <leader><Right> :vertical resize +20<CR>
nnoremap <leader><Down> :resize -20<CR>
nnoremap <leader><Up> :resize +20<CR>

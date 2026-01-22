Add to init.vim, inside plug# wrapper (if you already have)
```
" Tree-sitter
call plug#begin('~/.vim/plugged')
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
call plug#end()
```

Restart neovim, run:
```
:PlugInstall
```

Add to init.vim plugin section:
```
lua << EOF
require'nvim-treesitter.configs'.setup {
  ensure_installed = { "python" },
  highlight = {
    enable = true,
    additional_vim_regex_highlighting = false,
  },
}
EOF
```

Restart neovim, run:
```
:TSInstall python
```
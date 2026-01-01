```
cd C:\Users\<YOU>\AppData\Local\nvim
mkdir autoload
cd autoload
type nul > plug.vim
curl https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim | clip
```

* Open and paste the copied script into plug.vim
* Edit init.vim and paste the following:

```
call plug#begin('~/AppData/Local/nvim-data/plugged')

" Mason = LSP installer
Plug 'williamboman/mason.nvim'
Plug 'williamboman/mason-lspconfig.nvim'

" Core Neovim LSP
Plug 'neovim/nvim-lspconfig'

" Completion
Plug 'hrsh7th/nvim-cmp'
Plug 'hrsh7th/cmp-nvim-lsp'
Plug 'hrsh7th/cmp-buffer'
Plug 'hrsh7th/cmp-path'
Plug 'hrsh7th/cmp-cmdline'

" Snippets
Plug 'L3MON4D3/LuaSnip'
Plug 'saadparwaiz1/cmp_luasnip'

call plug#end()

```

* Close and reopen neovim

```
:PlugInstall
```

* Open and paste into init.vim:

```
lua << EOF
local cmp = require'cmp'

cmp.setup({
  snippet = {
    expand = function(args)
      require('luasnip').lsp_expand(args.body)
    end,
  },
  mapping = cmp.mapping.preset.insert({
    ['<C-Space>'] = cmp.mapping.complete(),
    ['<CR>'] = cmp.mapping.confirm({ select = true }),
  }),
  sources = cmp.config.sources({
    { name = 'nvim_lsp' },
    { name = 'buffer' },
    { name = 'path' },
  })
})

-- Mason / LSP Setup
require("mason").setup()
require("mason-lspconfig").setup()

local lspconfig = require('lspconfig')
local capabilities = require('cmp_nvim_lsp').default_capabilities()

-- Example LSP servers
lspconfig.pyright.setup{ capabilities = capabilities }
lspconfig.clangd.setup{ capabilities = capabilities }
lspconfig.tsserver.setup{ capabilities = capabilities }
EOF

```

* Close neovim
* Install Nodejs [Node.js — Run JavaScript Everywhere](https://nodejs.org/en)
* Open neovim

```
:Mason
```

Select server with arrows and install by pressing i
* pyright (Python)
* clangd (C++)
* matlab-language-server (Requires java, check using `java -version`)
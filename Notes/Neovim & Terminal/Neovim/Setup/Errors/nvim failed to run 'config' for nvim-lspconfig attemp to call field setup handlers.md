Open
```
~/.config/nvim/lua/plugins/nvim-lspconfig.lua
```

Find:
```
{ 'williamboman/mason.nvim' },
{ 'williamboman/mason-lspconfig.nvim' },
```

replace with:
```
{ 'williamboman/mason.nvim', version = "1.*" },
{ 'williamboman/mason-lspconfig.nvim', version = "1.*" },
```

Restart and run:
```
:Lazy sync
```
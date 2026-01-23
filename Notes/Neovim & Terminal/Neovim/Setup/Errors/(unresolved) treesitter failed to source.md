For now, disable the plugin. Open
```
.config\nvim\lua\plugins\nvim-treesitter.lua
```

And use this instead:
```
return {
  'nvim-treesitter/nvim-treesitter',
  enabled = false,
}
```

And then
```
:Lazy sync
```

****

![[Pasted image 20260123001420.png]]

```
return {
  "nvim-treesitter/nvim-treesitter",
  build = ":TSUpdate",
  lazy = false,
  priority = 1000,
  dependencies = {
    "nvim-treesitter/nvim-treesitter-textobjects",
  },
  opts = {
    highlight = { enable = true },
    indent = { enable = true },
    auto_install = true,
    ensure_installed = { "lua" },
  },
  config = function(_, opts)
    require("vim.treesitter.configs").setup(opts)
  end,
}
```

![[Pasted image 20260123004253.png]]

Solution:
```
mkdir -p ~/.config/nvim/lua/nvim-treesitter
nvim ~/.config/nvim/lua/nvim-treesitter/configs.lua
```

Add this to the file:
```
-- Compatibility alias for plugins expecting `nvim-treesitter.configs`
return require("nvim-treesitter.config")
```

Restart Neovim and run:
```
:Lazy sync
```

Verify
```
:lua print(pcall(require, "nvim-treesitter.configs"))
```

Should print true

![[Pasted image 20260123010209.png]]

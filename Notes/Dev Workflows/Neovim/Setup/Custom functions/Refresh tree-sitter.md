```
-- refresh tree
vim.keymap.set("n", "<leader>r", function()
  require("nvim-tree.api").tree.reload()
end, { desc = "nvim-tree refresh" })
```
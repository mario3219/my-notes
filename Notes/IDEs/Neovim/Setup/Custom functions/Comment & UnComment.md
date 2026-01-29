Add to init.lua

```
vim.api.nvim_create_user_command("CommentRange", function(opts)
  local start_line = opts.line1
  local end_line = opts.line2
  local prefix = opts.args

  for l = start_line, end_line do
    local line = vim.fn.getline(l)
    vim.fn.setline(l, prefix .. line)
  end
end, {
  range = true,
  nargs = 1,
})

vim.api.nvim_create_user_command("UnCommentRange", function(opts)
  local start_line = opts.line1
  local end_line = opts.line2
  local prefix = opts.args

  for l = start_line, end_line do
    local line = vim.fn.getline(l)
    line = line:gsub("^" .. vim.pesc(prefix), "")
    vim.fn.setline(l, line)
  end
end, {
  range = true,
  nargs = 1,
})

```
```
// Vim bindings
"vim.leader": "<space>",

"vim.normalModeKeyBindingsNonRecursive": [
  // Save / Quit
  { "before": ["<leader>", "w", "q"], "commands": [":wq"] },
  { "before": ["<leader>", "q", "q"], "commands": [":q!"] },
  { "before": ["<leader>", "w", "w"], "commands": [":w"] },
  { "before": ["<leader>", "e", "e"], "commands": [":Explore"] },

  // Open URL under cursor (VS Code equivalent of gx)
  {
    "before": ["g", "x"],
    "commands": ["editor.action.openLink"]
  },

  // Split management
  { "before": ["<leader>", "s", "v"], "commands": ["workbench.action.splitEditorRight"] },
  { "before": ["<leader>", "s", "h"], "commands": ["workbench.action.splitEditorDown"] },
  { "before": ["<leader>", "s", "e"], "commands": ["workbench.action.evenEditorWidths"] },
  { "before": ["<leader>", "s", "x"], "commands": ["workbench.action.closeActiveEditor"] },

  // Resize splits
  { "before": ["<leader>", "s", "j"], "commands": ["workbench.action.decreaseViewHeight"] },
  { "before": ["<leader>", "s", "k"], "commands": ["workbench.action.increaseViewHeight"] },
  { "before": ["<leader>", "s", "l"], "commands": ["workbench.action.increaseViewWidth"] },
  { "before": ["<leader>", "s", "h"], "commands": ["workbench.action.decreaseViewWidth"] },

  // Tabs (VS Code = editor groups)
  { "before": ["<leader>", "t", "o"], "commands": ["workbench.action.newEditorGroup"] },
  { "before": ["<leader>", "t", "x"], "commands": ["workbench.action.closeActiveEditor"] },
  { "before": ["<leader>", "t", "n"], "commands": ["workbench.action.nextEditor"] },
  { "before": ["<leader>", "t", "p"], "commands": ["workbench.action.previousEditor"] },

  // Diff / merge
  { "before": ["<leader>", "c", "c"], "commands": ["git.acceptChanges"] },
  { "before": ["<leader>", "c", "j"], "commands": ["git.acceptLeft"] },
  { "before": ["<leader>", "c", "k"], "commands": ["git.acceptRight"] },
  { "before": ["<leader>", "c", "n"], "commands": ["editor.action.diffReview.next"] },
  { "before": ["<leader>", "c", "p"], "commands": ["editor.action.diffReview.prev"] },

  // Quickfix ≈ Problems panel
  { "before": ["<leader>", "q", "o"], "commands": ["workbench.actions.view.problems"] },
  { "before": ["<leader>", "q", "n"], "commands": ["editor.action.marker.next"] },
  { "before": ["<leader>", "q", "p"], "commands": ["editor.action.marker.prev"] },
  { "before": ["<leader>", "q", "c"], "commands": ["workbench.actions.view.problems"] }
]

}
```
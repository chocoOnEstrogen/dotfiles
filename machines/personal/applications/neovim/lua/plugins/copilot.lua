return {
    {
    "github/copilot.vim",
    lazy = false,
    config = function()
        -- Customize key mappings for Copilot
        vim.g.copilot_no_tab_map = true -- Disable default Tab mapping
        vim.api.nvim_set_keymap("i", "<S-Tab>", 'copilot#Accept("<CR>")', { expr = true, silent = true })
    end
  },
}

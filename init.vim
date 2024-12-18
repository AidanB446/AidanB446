:set number relativenumber
:set autoindent
:set mouse=a
:set shiftwidth=4
:set tabstop=4

inoremap <silent><expr> <tab> pumvisible() ? coc#_select_confirm() : "\<C-g>u\<TAB>"
inoremap <silent><expr> <cr> "\<c-g>u\<CR>"
nnoremap <silent> <leader>f :Format<CR>

call plug#begin()

Plug 'catppuccin/nvim', { 'as': 'catppuccin' }
Plug 'mhartington/formatter.nvim'
Plug 'https://github.com/jiangmiao/auto-pairs'
Plug 'xiyaowong/transparent.nvim'
Plug 'alvan/vim-closetag'
Plug 'https://github.com/ray-x/navigator.lua'
Plug 'https://github.com/tc50cal/vim-terminal'
Plug 'windwp/nvim-autopairs'
Plug 'https://github.com/vim-airline/vim-airline'
Plug 'https://github.com/rafi/awesome-vim-colorschemes'
Plug 'https://github.com/tpope/vim-commentary'
Plug 'https://github.com/neoclide/coc.nvim'
Plug 'lewis6991/gitsigns.nvim' 
Plug 'nvim-tree/nvim-web-devicons'  
Plug 'mhartington/formatter.nvim'
Plug 'lewis6991/gitsigns.nvim' 
Plug 'nvim-tree/nvim-web-devicons' 
Plug 'https://github.com/lifepillar/pgsql.vim'
Plug 'nvim-tree/nvim-web-devicons' 
Plug 'akinsho/bufferline.nvim', { 'tag': '*' }
Plug 'prabirshrestha/vim-lsp'

call plug#end()

colorscheme catppuccin

set termguicolors

lua << EOF

require("transparent")
require("bufferline").setup{}

EOF


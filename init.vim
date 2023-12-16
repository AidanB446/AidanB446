:set number relativenumber
:highlight LineNr ctermfg=blue
:colorscheme torte
:set autoindent
:set mouse=a
:set shiftwidth=4
:set tabstop=4


inoremap <silent><expr> <tab> pumvisible() ? coc#_select_confirm() : "\<C-g>u\<TAB>"
inoremap <silent><expr> <cr> "\<c-g>u\<CR>"

call plug#begin()

Plug 'xiyaowong/transparent.nvim'
Plug 'alvan/vim-closetag'
Plug 'https://github.com/ray-x/navigator.lua'
Plug 'https://github.com/tc50cal/vim-terminal'
Plug 'windwp/nvim-autopairs'
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
Plug 'https://github.com/windwp/nvim-ts-autotag'
Plug 'https://github.com/vim-airline/vim-airline'
Plug 'https://github.com/rafi/awesome-vim-colorschemes'
Plug 'https://github.com/tpope/vim-commentary'
Plug 'https://github.com/neoclide/coc.nvim'
Plug 'https://github.com/folke/tokyonight.nvim'
Plug 'https://github.com/romgrk/barbar.nvim'
Plug 'lewis6991/gitsigns.nvim' 
Plug 'nvim-tree/nvim-web-devicons'  
Plug 'https://github.com/windwp/nvim-ts-autotag'
Plug 'mhartington/formatter.nvim'

call plug#end()




lua << EOF

require('nvim-ts-autotag').setup()
require("nvim-autopairs").setup {}
require("transparent")

EOF



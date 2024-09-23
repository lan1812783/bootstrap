" Disable the arrow keys
noremap <Up> <Nop>
noremap <Down> <Nop>
noremap <Left> <Nop>
noremap <Right> <Nop>

" Options
set formatoptions+=j
set hlsearch incsearch smartcase
set laststatus=2
set number relativenumber
set linebreak scrolloff=5
" Shows match position, ref: https://stackoverflow.com/a/4671112
set shortmess-=S
set splitbelow splitright
set whichwrap+=h,l
set wildmenu

" Vertical split separator
set fillchars=vert:│
highlight VertSplit cterm=none ctermfg=Green ctermbg=none

" Netrw, seems like netrw creates new buffer when opened, so it looks like
" expanded folders in tree view collapse when netrw is closed then opened again
let g:netrw_banner = 0
" Auto commands on netrw seems to not work, ref:
" https://vi.stackexchange.com/a/19844
let g:netrw_bufsettings = 'noma nomod nowrap ro nobl colorcolumn& number
      \ relativenumber statusline=Netrw'
let g:netrw_liststyle = 3
let g:netrw_winsize = 25

" Statusline
" Ref: https://shapeshed.com/vim-statuslines/
highlight StatusLineComponent	ctermfg=Black ctermbg=Gray guifg=Black
      \ guibg=Blue
set statusline=
set statusline+=%#StatusLineComponent#
set statusline+=\ 
set statusline+=%f
set statusline+=\ 
set statusline+=%#StatusLine#
set statusline+=\ %m
set statusline+=%=
set statusline+=\ %{&fileencoding?&fileencoding:&encoding}
set statusline+=\ %{&fileformat}
set statusline+=\ %y
set statusline+=\ %p%%
set statusline+=\ %l:%c
set statusline+=\ 
" Statusline for quickfix list and help page
autocmd FileType qf,help setlocal colorcolumn& statusline=%f

" Spell
" Ref: https://stackoverflow.com/a/6009026
set spell spelllang=en_us
highlight clear SpellBad
highlight SpellBad cterm=underline

" Filetype
" Ref: https://stackoverflow.com/a/18415867
set autoindent expandtab shiftround shiftwidth=2 tabstop=2
filetype plugin indent on

" Add default plugins
packadd! matchit

" Column
set colorcolumn=80
highlight ColorColumn ctermbg=DarkGray guibg=DarkGray 

" Undo
let undodir = "/tmp/.vim-undo-dir"
call mkdir(undodir, "p", 0700)
let &undodir=undodir
set undofile

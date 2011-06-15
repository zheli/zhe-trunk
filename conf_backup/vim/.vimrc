set number
set expandtab
set tabstop=8
set shiftwidth=4
set softtabstop=4
set autoindent
:syntax on
let Tlist_Ctags_Cmd='/usr/bin/ctags'
filetype plugin indent on
filetype plugin on
set ofu=syntaxcomplete#Complete
colorscheme delek
set guioptions-=T
"change background color to red for line that is longer than 80 chars
highlight OverLength ctermbg=red ctermfg=white guibg=#592929 
match OverLength /\%81v.\+/

"tab-completion
set wildmode=longest,list,full
set wildmenu

pandoc --biblatex -o CLINC_may9.tex CLINC_may9_compiled.md

find and replace:
`(?<!\n)\n(\w)` → ` $1`

↪ is invalid 

had to size figures

```LaTeX
\documentclass{article}
    % General document formatting
    \usepackage[margin=0.7in]{geometry}
    \usepackage[parfill]{parskip}
    \usepackage[utf8]{inputenc}
    \usepackage{graphicx}
    \usepackage{fullpage} 
    \usepackage{hyperref}

    
    \usepackage[caption=false, font=normalsize, labelfont=sf, textfont=sf]{subfig}
    \usepackage[percent]{overpic}

    
    \usepackage{amsmath,amssymb,amsfonts,amsthm}
    \usepackage[style=apa]{biblatex}
  ```
Doesn't seem to work as expected here:

[LaTeX compilation](https://github.com/shd101wyy/markdown-preview-enhanced/blob/master/docs/code-chunk.md#latex)

[see also](https://github.com/KaTeX/KaTeX/issues/219)

```latex {cmd=true, hide=true}
\documentclass{standalone}
\begin{document}
  Hello world!
\end{document}
```

```latex {cmd=true}
\documentclass{standalone}
\begin{document}
  Hello world again!
\end{document}
```
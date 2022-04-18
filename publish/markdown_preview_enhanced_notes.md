# Producing a clean, readable pdf 
- **option 1: quick** - css filters + MPE → pdf 
  *see sections below for filtering style with css*
  a.) `MPE:Open in Browser` → `RightClick>save-as-pdf`
  b.) `MPE:HTML` → `RightClick>save-as-pdf`
    - looks closest to mpe preview?
    - can customize margins in print dialog
    - try `(cdn hosted)` if images aren't displaying
    
  c.) MPE:Chrome → pdf
  d.) MPE:Prince pdf
  ... could use custom css to make these pdf exports look more like option 2
  
- **option 2: tidy** *(not implemented)* - panflute filters + pandoc pdf render
  - produces professional looking document (with nice margins and fonts)
  - *(can't currently get pandoc export + filters working correctly)*
  

# Using pandoc to create columns & margins
```YAML
classoption: twocolumn
geometry: margin=1.5cm
```

# Using CSS to number sections 
- Heading numbering, inspired by Typora - https://support.typora.io/Auto-Numbering/
`Markdown Preview Enhanced: Customize CSS` → paste in css from 
```css
/* comment / uncomment: */
.markdown-preview.markdown-preview {
  .do-number-sections()
}
```

# using custom CSS importing to hide to-do list items for drafts
https://shd101wyy.github.io/markdown-preview-enhanced/#/customize-css
you can find which css selector to hide by opening html in browser, `right-click`→`inspect` and looking for the tag of the object 


I'm currently using `publish/publish_style.less` to hide...


> !!!! todo list items
> 
> <details><summary>↪collapsible sections</summary>
> 
> nothing to see
> </details>
> 
> and 
> ==highlights==

... using the tag 
```
---
id: "hide-todo"
---
@import "publish/publish_style.less"
```
publish_style.less sets `diplay:none`. This hiding can be toggled by commenting out `id: "hide-todo"`

# Automatic table of contents 
...

# Producing an audio transcription 
1. compile markdown imports to single markdown file 
    - mume / mpe : `mpe:save-as-markdown` 
2. filter non-spoken content out 
    - pandoc: `pandoc -o filtered.md -F panflute in.md`
    - panflute: `cleanup_filter.py` 
3. compile filtered markdown to mp3 
  `markdown_to_mp3.sh`
    - [say](https://ss64.com/osx/say.html): `say -f filtered.md -o sound.aiff`
    - [lame](https://lame.sourceforge.io/): `lame -m m sound.aiff sound.mp3`

# misc.    
https://stackoverflow.com/questions/4779582/markdown-and-including-multiple-files
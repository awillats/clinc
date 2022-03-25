
## Using CSS to number sections 
- Heading numbering, inspired by Typora - https://support.typora.io/Auto-Numbering/
`Markdown Preview Enhanced: Customize CSS` → paste in css from 
```css
/* comment / uncomment: */
.markdown-preview.markdown-preview {
  .do-number-sections()
}
```

## using custom CSS importing to hide to-do list items for drafts
https://shd101wyy.github.io/markdown-preview-enhanced/#/customize-css
you can find which css selector to hide by opening html in browser, `right-click`→`inspect` and looking for the tag of the object 


I'm currently using `publish/publish_style.less` to hide...

---
!!!! todo list items

<details><summary>↪collapsible sections</summary>

nothing to see
</details>

and 
==highlights==

---

... using the tag 
```
---
id: "hide-todo"
---
@import "publish/publish_style.less"
```
setting `diplay:none`. This hiding can be toggled by commenting out `id: "hide-todo"`


----
https://stackoverflow.com/questions/4779582/markdown-and-including-multiple-files
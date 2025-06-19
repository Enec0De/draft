---
title: 文档源代码结构
status: new
---

个人文档代码规范 { #document-structure }
========================================

---

基本结构 { #structure }
-----------------------

以下描述了一个文档的基本骨架，代码行高亮部分为标题格式[^1]：

[^1]: 为了兼顾源代码的可读性而选择，很大程度上也取决于我个人的偏好。

``` markdown title="template.md" linenums="1" hl_lines="5 6 12 13 19"
---
title: 页面标题
---

一级标题
========

<!-- 注释内容 -->

---

二级标题
--------

`---` 为水平分隔线。

*斜体*、**粗体**、***斜粗体***。

### 三级标题

> 引用内容
>
> > 嵌套引用
```

同时建议用以下方式修改渲染的锚点与目录：

``` markdown
...
Heading 1 { #New-H1 data-toc-label="New H1" }
=============================================
...
heading 2 { #New-H2 data-toc-label="New H2" }
---------------------------------------------
...
### Heading 3 { #New-H3 data-toc-label="New H3" }
...
```

!!! info ":octicons-smiley-16:"
    
    约定不使用四级及以上的标题，最多仅使用一层嵌套引用。

---

元数据 { #meta-data }
---------------------

在文档开头用 `---` 包裹：

``` markdown linenums="1" hl_lines="2"
---
title: Getting-started
---

Page title
==========
...
```

可用属性包括：`title`、`description`、`icon`、`status`、`subtitle`、`template`，参考[文档][ref]。

  [ref]: https://squidfunk.github.io/mkdocs-material/reference/

    



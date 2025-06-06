---
title: 文档源代码结构
status: new
---

个人文档代码规范
================

> Entities should not be multiplied beyond necessity.

***

基本骨架 { #skeleton }
----------------------

以下描述了一个文档的基本骨架。

除了文档开头被 `---` 包裹的 title (或status) 元素外，其他均为标准 Markdown 语法：

``` markdown
---
title: 页面标题
---

一级标题
========

***

二级标题
--------

`***` 代表的内容是***水平分隔线***。

上一行末尾为**粗体**加*斜体*。

### 三级标题

#### 四级标题

> 一级引用
> > 二级引用
```

!!! info
    
    若非必要，不使用四级以上的标题，不使用两层以上的嵌套引用。同时，建议每次都用以下方式修改渲染的锚点与目录：

    ``` markdown
    ### Old Heading { #New-Heading data-toc-label="New Heading" }
    ```

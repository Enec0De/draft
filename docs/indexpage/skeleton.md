---
title: Code Skeleton
status: new
---

个人文档代码规范
================

一个仅为个人使用的行文规范。

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

***

### 参考引用 { #reference }

术语，单行脚注[^1]，多行脚注[^2]，以及[链接][Hover me]。

引用图片不做演示，直接提供代码：

*[术语]: abbr.

[^1]: a single line.
[^2]:
    Paragraphs can be written on the next line
    and must be indented by four spaces.

  [Hover me]: https://example.com "网站：example.com"
    
``` markdown
术语，单行脚注[^1]，多行脚注[^2]，以及[链接][Hover me]。

*[术语]: abbr.

[^1]: a single line
[^2]:
    Paragraphs can be written on the next line
    and must be indented by four spaces.

  [Hover me]: https://example.com "网站：example.com"

![图片][image]

  [image]: ../assets/images/jellyfish-outline.svg
```

***

### 列表表格 { #list-and-tab }

#### 1. 普通列表 { #list }

=== "Ordered"

    <div class="grid" markdown>
    
    ``` markdown title="List, ordered"
    1.  Item\_1
    1.  Item\_2
    
        1.  Subitem\_1
        1.  Subitem\_2
    ```
    
    > 1.  Item\_1
    > 1.  Item\_2
    > 
    >     1.  Subitem\_1
    >     1.  Subitem\_2
    
    </div>

=== "Unordered"

    <div class="grid" markdown>

    ``` markdown title="List, unordered"
    - Item\_1
    - Item\_2
    
        - Subitem\_1 
        - Subitem\_2
    ```
    
    > - Item\_1
    > - Item\_2
    > 
    >     - Subitem\_1 
    >     - Subitem\_2
    
    </div>

#### 2. 任务列表 { #task }

<div class="grid" markdown>

``` markdown title="Task list"
- [x] Finished item.
- [ ] Unfinished item. 
    - [ ] Subitem.
```

> - [x] Finished item.
> - [ ] Unfinished item. 
>     - [ ] Subitem.

</div>

!!! info
    若非必要，*普通列表*和*任务列表*，均不使用两层以上的嵌套。

#### 3. 定义列表 { #definition }

<div class="grid" markdown>

``` markdown title="Definition list"
`Definition_1`

:   Content of definition\_1.
```

> `Definition_1`
> 
> :   Content of definition\_1.

</div>

#### 4. 表格 { #table }

=== "Left"

    <div class="grid" markdown>

    ``` markdown hl_lines="2" title="Data table, columns aligned to left"
    | Method      | Description     |
    | :---------- | :-------------- |
    | `GET`       | Fetch resource  |
    | `DELETE`    | Delete resource |
    ```

    | Method      | Description     |
    | :---------- | :-------------- |
    | `GET`       | Fetch resource  |
    | `DELETE`    | Delete resource |

    </div>

=== "Center"

    <div class="grid" markdown>

    ``` markdown hl_lines="2" title="Data table, columns centered"
    | Method      | Description     |
    | :---------: | :-------------: |
    | `GET`       | Fetch resource  |
    | `DELETE`    | Delete resource |
    ```

    | Method      | Description     |
    | :---------: | :-------------: |
    | `GET`       | Fetch resource  |
    | `DELETE`    | Delete resource |

    </div>

=== "Right"

    <div class="grid" markdown>

    ``` markdown hl_lines="2" title="Data table, columns aligned to right"
    | Method      | Description     |
    | ----------: | --------------: |
    | `GET`       | Fetch resource  |
    | `DELETE`    | Delete resource |
    ```

    | Method      | Description     |
    | ----------: | --------------: |
    | `GET`       | Fetch resource  |
    | `DELETE`    | Delete resource |

    </div>

***

### 代码块以及内容表格 { #code-and-content-tab }

#### 1. 基本用法 { #basic }

``` markdown linenums="1" title="Content tabs with code blocks"
=== "Bash"

    ``` bash
    $ printf "Hello World\n"
    ```

=== "Python"

    ``` python
    >>> print("Hello World")
    ```
```

<div class="result" markdown>

=== "Bash"

    ``` bash
    $ printf "Hello World\n"
    ```

=== "Python"

    ``` py
    >>> print("Hello World")
    ```

</div>

#### 2. 结果渲染 { #output }

代码块后可以紧跟以下代码，展示其渲染结果，[效果如上][out]：

  [out]: #basic

``` markdown linenums="1"
<div class="result" markdown>

...

</div>
```

#### 3. 更多用法 { #append }

=== "Title"

    ```` markdown linenums="1" hl_lines="1" title="Code block with title"
    ``` py title="Python"
    ...
    ```
    ````

=== "Line numbers"    

    ```` markdown linenums="1" hl_lines="1" title="Code block with line numbers"
    ``` py linenums="1"
    ...
    ```
    ````

=== "Lines"    

    ```` markdown linenums="1" hl_lines="1" title="Code block with highlighted lines"
    ``` py hl_lines="2 3"
    ...
    ```
    ````

=== "Line ranges"    

    ```` markdown linenums="1" hl_lines="1" title="Code block with highlighted line range"
    ``` py hl_lines="3-5"
    ...
    ```
    ````

#### 4. 嵌入外部文件 { #Embedding-external-files } 

为了方便，一些可执行文件的源代码可以直接导入，后面的两个冒号可以紧接数字，分别代表起始行和结束行。

```` markdown linenums="1"
``` py
;--8<-- "test.py:4:6"

;--8<--
test.py::3
;--8<--
```
````


!!! tip 
    
    内容表格同样可以与其他内容连用，如[表格][list]。

    `--8<--` 符号可以通过添加一个 `;` 的方式转义，即：`;--8<--`，文件也可以以同样的方式跳过。

      [list]: #list-and-tab

***

### 警告框 { #admonitions }

警告框的常用类型为：`note`，`info`，`tip`，`warning`。

其他可选：`abstract`，`success`，`question`，`failure`，`danger`，`bug`，`example`，`quote`。

``` markdown title="Admonitions"
!!! warning "Warning"

    尽量保证简洁，不乱用警告框。
```

<div class="result" markdown>

!!! warning "Warning"

    尽量保证简洁，不乱用警告框。

</div>

***

### 网格 { #grid }

只需要使用带有 `grid` 类的 `div` 标签包裹一组区块，就可以将任意区块元素排列成网格布局。

其中，列表语法是卡片网格的快捷写法。对有序或无序的列表，该语法将其包裹于包含 `grid` 和 `cards` 两个类的 `div` 元素内。

#### 1. 列表语法 {grid-cards}

=== "Card Grid"
    ``` html 
    <div class="grid cards" markdown>
    
    - :fontawesome-brands-linux: **Linux** for me
    - :fontawesome-brands-markdown: **Markdown** for this draft
    - :fontawesome-brands-bilibili: **Bilibili** for animate
    - :fontawesome-brands-python: **Python** for math
    
    </div>
    ```
    
=== "Generic Grid"
    ``` html 
    <div class="grid" markdown>
    
    :fontawesome-brands-linux: **Linux** for me
    { .card }
    
    :fontawesome-brands-markdown: **Markdown** for this draft
    { .card }
    
    :fontawesome-brands-bilibili: **Bilibili** for animate
    { .card }
    
    :fontawesome-brands-python: **Python** for math
    { .card }
    
    </div>
    ```

<div class="grid" markdown>

:fontawesome-brands-linux: **Linux** for me
{ .card }

:fontawesome-brands-markdown: **Markdown** for this draft
{ .card }

:fontawesome-brands-bilibili: **Bilibili** for animate
{ .card }

:fontawesome-brands-python: **Python** for math
{ .card }

</div>

!!! note

    两种写法等价，后者多用于组合不同类型的块。

#### 2. 列表语法补充 { #cards-append }

``` html
<div class="grid cards" markdown>

-   :fontawesome-brands-linux: **Linux** for me
   
    ***
   
    [:octicons-arrow-right-24: Learn More](https://www.kernel.org/)

-   :fontawesome-brands-python: **Python** for math

    ***

    [:octicons-arrow-right-24: Learn More](https://www.python.org/)

</div>
```

<div class="grid cards" markdown>

-   :fontawesome-brands-linux: **Linux** for me
   
    ***
   
    [:octicons-arrow-right-24: Learn More](https://www.kernel.org/)

-   :fontawesome-brands-python: **Python** for math

    ***

    [:octicons-arrow-right-24: Learn More](https://www.python.org/)

</div>

#### 3. 通用网格 { #generic-grd }

```` html 
<div class="grid" markdown>

**This is card.**
{ .card }

> **This is quote.** 

=== "Content tab"

    This is content tab.

``` title="Code tab"
This is code tab.
```

</div>
````

<div class="grid" markdown>

**This is a card.** 
{ .card }

> **This is a quote.** 

=== "Content tab"

    This is content tab.

``` title="Code tab"
This is code tab.
```

</div>

!!! note

    尽量避免多层、不同块的嵌套，包括但不限于网格。

***

### 其他格式 { #others }

#### 1. 快捷键 { #shortcuts }

``` markdown title="Keyboard keys"
++ctrl+alt+del++
```

<div class="result" markdown>

++ctrl+alt+del++

</div>

!!! info
    
    更多的快捷键可以在[官方文档][shortcuts]处指引的[扩展文档][extensions]内查询。

      [shortcuts]: https://squidfunk.github.io/mkdocs-material/reference/formatting/#adding-keyboard-keys
      [extensions]: https://facelessuser.github.io/pymdown-extensions/extensions/tilde/

#### 2. 数学公式 { #math }

用的是 [KaTeX][katex]。

  [katex]: https://katex.org/

---
title: 网格
---

网格 { #grid }
==============

只需要使用带有 `grid` 类的 `div` 标签包裹一组区块，就可以将任意区块元素排列成网格布局。

!!! info 

    列表语法是卡片网格的快捷写法。
 
    > 对有序或无序的列表，该语法将其包裹于包含 `grid` 和 `cards` 两个类的 `div` 元素内。

***

列表语法 {grid-cards}
---------------------

有两种写法。

=== "Card Grid"
    ``` html linenums="1"
    <div class="grid cards" markdown>
    
    - :fontawesome-brands-linux: **Linux** for me
    - :fontawesome-brands-markdown: **Markdown** for this draft
    - :fontawesome-brands-bilibili: **Bilibili** for animate
    - :fontawesome-brands-python: **Python** for math
    
    </div>
    ```
    
=== "Generic Grid"
    ``` html linenums="1"
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

***

每个卡片的内容可以不止一行。

``` html linenums="1"
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

***

通用网格 { #generic-grd }
-------------------------

```` html linenums="1"
<div class="grid" markdown>

**这是卡片内容块** 
{ .card }

> **这是引用内容块** 

=== "Content tab"

    这是内容选项卡.

``` title="Code block"
这是代码块.
```

</div>
````

<div class="grid" markdown>

**这是卡片内容块** 
{ .card }

> **这是引用内容块** 

=== "Content tab"

    这是内容选项卡.

``` title="Code block"
这是代码块.
```

</div>

!!! note

    尽量避免多层、不同块的嵌套。

!!! warning

    我们约定，通用网格内只使用：卡片、引用、代码块、内容选项卡。
    
    *[卡片]: 非列表语法下 { .card } 结尾的块
    *[引用]: 一个或多个 `>` 开头的块

---
title: 代码块
---

代码块以及内容选项卡 { #code-and-content-tab }
============================================

***

基本用法 { #basic }
-------------------

这里同时使用了两个内容格式：**代码块**和**内容选项卡**。

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

***

代码块后紧跟下列代码，展示其渲染结果，[效果如上][out]：

  [out]: #basic

``` markdown linenums="1"
<div class="result" markdown>

...

</div>
```

***

标题、行号、高亮。

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

    ```` markdown linenums="1" hl_lines="1 3" title="Code block with highlighted lines"
    ``` py hl_lines="1 3"
    ...
    ```
    ````

=== "Line ranges"    

    ```` markdown linenums="1" hl_lines="1-3" title="Code block with highlighted line range"
    ``` py hl_lines="1-3"
    ...
    ```
    ````

***

嵌入外部文件 { #Embedding-external-files } 
------------------------------------------

可执行文件的源代码可以直接导入，后面的两个冒号紧接数字，分别代表起始行和结束行。

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

      [list]: list.md/#list-and-tab

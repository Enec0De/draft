---
title: 列表
---

列表表格 { #list-and-tab }
==========================

!!! warning

    我们约定，有序列表仅用相同的符号 `1.` 进行排列。

    若非必要，普通列表和任务列表，均不使用两层以上的嵌套。

***

普通列表 { #list }
------------------

=== ":octicons-file-code-16: `Ordered`"

    <div class="grid" markdown>
    
    ``` markdown title="List, ordered"
    1.  记号 `1.` 后应有2个空格
    1.  可以用反斜杠转义：`1\.`
    
        1.  多层列表注意4个空格缩进对齐
    ```
    
    > 1.  记号 `1.` 后应有2个空格
    > 1.  可以用反斜杠转义：`1\.`
    > 
    >     1.  多层列表注意4个空格缩进对齐
    
    </div>

=== ":octicons-file-code-16: `Unordered`"

    <div class="grid" markdown>

    ``` markdown title="List, unordered"
    - 记号 `-` 后应有1个空格
    - 可以用反斜杠转义：`\-`
    
        - 多层列表注意4个空格缩进对齐
    ```
    
    > - 记号 `-` 后应有1个空格
    > - 可以用反斜杠转义：`\-`
    > 
    >     - 多层列表注意4个空格缩进对齐
    
    </div>

***

任务列表 { #task }
------------------

<div class="grid" markdown>

``` markdown title="Task list"
- [x] 已完成项目
- [ ] 未完成项目
    - [ ] 子项目
```

> - [x] 已完成项目
> - [ ] 未完成项目
>     - [ ] 子项目

</div>

***

定义列表 { #definition }
------------------------

``` markdown title="Definition list"
**佐恩引理**

:   在任何一非空的偏序集中，若任何链（即全序的子集）都有上界，则此偏序集内必然存在（至少一枚）极大元。
```

<div class="result" markdown>

**佐恩引理**

:   在任何一非空的偏序集中，若任何链（即全序的子集）都有上界，则此偏序集内必然存在（至少一枚）极大元。

</div>

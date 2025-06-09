---
title: 参考引用
---

参考引用 { #reference }
=======================

***

中文间不可以穿插术语，但是可以这样：术语。

*[术语]: abbr.

``` markdown linenums="1"
内容间不可以穿插术语，但是可以这样：术语。

*[术语]: abbr.
```

***

使用[链接][Hover me]，注意对齐缩进。

  [Hover me]: https://example.com "网站：example.com"

``` markdown linenums="1"
使用[链接][Hover me]，注意对齐缩进。

  [Hover me]: https://example.com "网站：example.com"
```

***

引用图片不做演示，直接提供代码，和上述的链接类似。同时注意缩进。

``` markdown linenums="1"
![图片][image]

  [image]: ../assets/images/jellyfish-outline.svg
```

***

单行脚注[^1]，多行脚注[^2]。

[^1]: a single line.
[^2]:
    Paragraphs can be written on the next line
    and must be indented by four spaces.

``` markdown linenums="1"
单行脚注[^1]，多行脚注[^2]。

[^1]: a single line.
[^2]:
    Paragraphs can be written on the next line
    and must be indented by four spaces.
```

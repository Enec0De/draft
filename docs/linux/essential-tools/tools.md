---
title: 常用
---

常用
====

列出一些常用的工具，包含一些常用的实践。

---

`wget`: 

```
wget -r -np -nH --cut-dirs=2 -R "index.html*" "https://example.com/dir1/dir2/files/"
```

`bash`:

-   登陆加载：`/etc/profile`
    -   按顺序检索，加载最先检索到的：`~/.bash_profile`，`~/.bash_login`，`~/.profile`
-   交互加载：`~/.bashrc`
-   退出钩子：`~/.bash_logout`

!!! warning "警告"

    如果没在 `~/.profile` 加入以下内容：
    
    ``` bash
    if [ -n "$BASH_VERSION" ]; then
        if [ -f "$HOME/.bashrc" ]; then
            . "$HOME/.bashrc"
        fi
    fi
    ```

    登陆 shell 下不会加载：`/etc/bash.bashrc` 和 `~/.bashrc` 文件。

`zsh`:

-   实例加载（环境变量）：`/etc/zshenv` -> `~/.zshenv`
-   登陆加载（准备环境）：`/etc/zprofile` -> `~/.zprofile`
-   交互加载（交互配置）：`/etc/zshrc` -> `~/.zshrc`
-   登陆加载（登陆任务）：`/etc/zlogin` -> `~/.zlogin`
-   退出钩子：`~/.zlogout` -> `/etc/zlogout`

!!! tip "提示"

    按顺序加载，若前一个不加载，后续文件将不会加载。

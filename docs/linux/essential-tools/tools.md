---
title: 常用工具
---

常用工具
========

列出一些常用的工具，包含一些常用的实践。

---

`kill`：

-   常用信号： 
    ``` bash
    kill -15   # 优雅终止 terminal  
    kill -9    # 直接杀死 kill
    kill -2    # 中断 interrupt 等价于 ^C
    kill -1    
    ```

-   kill -1

    -   `kill -1` 是发送 SIGHUP 使其重载，例如 `systemctl reload`（但不等价）
    -   `nohup` 是忽略 SIGHUP
    -   `disown` 是从 Shell 作业列表移除，避免 SIGHUP

-   参阅 `signal(7)`

---

`wget`: 

``` bash
wget -r -np -nH --cut-dirs=2 -R "index.html*" "https://example.com/dir1/dir2/files/"
```

---

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

---

`zsh`:

-   实例加载（环境变量）：`/etc/zshenv` -> `~/.zshenv`
-   登陆加载（准备环境）：`/etc/zprofile` -> `~/.zprofile`
-   交互加载（交互配置）：`/etc/zshrc` -> `~/.zshrc`
-   登陆加载（登陆任务）：`/etc/zlogin` -> `~/.zlogin`
-   退出钩子：`~/.zlogout` -> `/etc/zlogout`

!!! tip "提示"

    按顺序加载，若前一个不加载，后续文件将不会加载。

---

`sed`:

-   选项：

    -   `-e`：一个 `-e` 一个命令
    -   `-i`：直接修改目标文件
    -   `-n`：抑制默认输出，常与 `p` 命令结合

-   命令：

    -   `s/.../.../g`：`g`表示全局替换
    -   `p`：`sed -n '1,3p' file.txt` 打印 1 到 3 行
    -   `d`：`sed -i '/^$/d' file.txt` 删除空行并保存

-   示例：

    -   `sed -n '/start/,/end/p' file.txt` 打印区间内的所有行
    -   `sed '/start/,/end/d' file.txt` 删除区间内的所有行

---

`awk`:

-   基础结构：`awk 'pattern { action }' file.txt`

    -   示例：执行 `awk '/error/ {print}' log.txt` 匹配包含"error"的行 

-   常用变量：

    -   `$0`：整行
    -   `$1`, `$2`, ...：第1,2,...列
    -   `NF`：字段数量
    -   `NR`：当前行号
    -   `FS`：输入字段分隔符
    -   `OFS`：输出字段分隔符

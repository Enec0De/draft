---
title: Debian 软件包管理
---

Debian 软件包管理
=================

这一章假定最新的稳定版本代号为：**bookworm**。

本文档中，APT 系统的数据源总称为**源列表**。能够在以下文件中的任意位置定义：

-   `/etc/apt/sources.list`
-   `/etc/apt/sources.list.d/*.list`
-   `/etc/apt/sources.list.d/*.source`

*[源列表]: The source list.

---

1. Debian 软件包管理的前提
--------------------------

**1.1. Debian 软件包管理**

-   官方推荐的工具：
    
    -   `apt(8)`，`apt-get(8)`作为其备选
    -   `aptitude`

!!! tip "提示"

    每个软件包都带有使用标准用户接口 `debconf(7)` 的配置脚本，帮助软件包初始化安装过程。

-   作为新手，你应该：
    
    -   在**源列表**中不包含 `testing`，`unstable` 以及不混合使用其他非 Debian 的档案库，例如 Ubuntu。
    -   不要建立 `/etc/apt/preferences`，不要修改 `/var/lib/dpkg` 中的文件。
    -   绝不使用：`dpkg -i random_package` 和 `dpkg --force-all -i random_package`。
    -   从源码直接安装的程序请放到：`/usr/local` 或 `/opt`。

-   强烈建议使用带有安全更新的 stable 套件

    -   在新的主版本发布一个月后，可以根据情况将**源列表**中 stable 版相应的套件名修改为新的（如Debian 13 发布后，将 **bookworm** 修改为 **trixie**）。

-   如果你要用 testing 和 unstable 版，有以下基本的预防措施意见：

    -   将 Debian 系统的 stable 版安装到另一个分区，使系统可以进行**双启动**。
    -   制作安装 CD 便于启动**救援模式**。
    -   考虑安装 `apt-listbugs(1)`。

!!! warning "警告"

    如果你无法做到这些预防措施中的任何一个，那你可能还没做好使用 testing 和 unstable 版的准备。

**1.2. Debian 档案库基础**

**源列表**的格式在 `sources.list(5)` 里面有详尽的描述。

**1.3. 包管理的事件流**

-   更新（`apt update`、`aptitude update`、`apt-get update`）
-   升级（`apt upgrade`、`aptitude safe-upgrade`、`apt-get upgrade`）

    -   更激进的方式，请提前备份：

        `apt full-upgrade`、`aptitude full-upgrade`、`apt get dist-upgrade`

-   安装（`apt install`、`aptitude install`、`apt-get install`）
-   移除（`apt remove`、`aptitude remove`、`apt-get remove`）
-   清除（`apt purge`、`aptitude purge`、`apt-get purge`）

**1.4. 其他相关**

-   你应该阅读优质的官方文档：

    -   `/usr/share/doc/package_name/README.Debian`
    -   `/usr/share/doc/package_name/*`

-   如果包出现了问题：

    -   [Debian bug 跟踪系统（BTS）][debianbug]
    -   请使用 `reportbug(1)` 命令

  [debianbug]: https://www.debian.org/Bugs/

---

2. 基础软件包管理操作
---------------------

-   `apt-get(8)` 和 `apt-cache(8)` 是最**基础**的基于 APT 的软件包管理工具。
-   `apt(8)` 命令是一个用于软件包管理的高级命令行界面。

    -   它基本上是 `apt-get(8)`、`apt-cache(8)` 和类似命令的一个封装，被设计为针对终端用户交互的界面，它默认启用了某些适合交互式使用的选项。

-   `aptitude(8)` 命令是最**通用**的基于 APT 的软件包管理工具。

    -   `aptitude(8)` 不太行，尤其是在处理跨版本的系统升级时。
    -   但是话又说回来，`apt-get(8)` 和 `apt-cache(8)` 可以使用 `/etc/apt/preferences` 来管理软件包的多个版本，比较繁琐；而 `aptitude(8)` 不用，且更直观。
    -   参阅 `/usr/share/doc/aptitude/README`、`apt_preferences(5)`。

!!! note "注意"

    建议用户使用新的 `apt(8)` 命令用于**交互式**的使用场景，而在 shell 脚本中使用 `apt-get(8)` 和 `apt-cache(8)` 命令。

-   软件包活动日志

    -   `/var/log/dpkg.log`
    -   `/var/log/apt/term.log`
    -   `/var/log/aptitude`o

!!! tip "提示"

    我觉得**我自己**需要注意的两个命令：`aptitude search '~c'`、`dpkg -l | grep '^rc'`。

---

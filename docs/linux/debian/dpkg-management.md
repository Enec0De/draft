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

3. 全面的系统升级
-----------------

你应该做的：

-   查看“发行说明”
-   备份整个系统（尤其是数据和配置信息）
-   用 `script(1)` 记录升级过程
-   用 `aptitude unmarkauto pkg_name` 来防止移除软件包
-   移除 `/etc/apt/preferences` 文件（禁用 `apt-pinning`）
-   运行 `apt-get -s dist-upgrade` 评估升级造成的影响
-   最后运行 `apt-get dist-upgrade`

---

4. 高级软件包管理操作
---------------------

-   `dpkg -l pkg_name_pattern` 列出已安装软件包的列表
-   `dpkg -L pkg_name` 根据软件包检索它安装的所有文件
 
    -   `apt-file list pkg_name_pattern`，从**档案库**检索包的文件

-   `dpkg -S file_name_pattern` 根据文件检索它属于的已安装的软件包

    -   `apt-file search file_name_pattern`，从**档案库**检索提供该文件的软件源

-   `dpkg-reconfigure pkg_name` 重置软件包的配置文件

    -   `-plow` 以最详细的方式执行
    -   `configure-debian(8)` 工具以全屏菜单的形式重新配置

-   `dpkg --audit` 软件包的审计系统，用于检测异常的包
-   `dpkg --configure -a` 配置所有**部分安装**的软件包

-   `apt-cache(8)`

    -   `apt-cache policy binary_pkg_name` 从本地缓存显示一个二进制软件包的可用版本、优先级和档案库信息
    -   `apt-cache madison pkg_name` 从本地缓存显示一个软件包的可用版本和档案库信息
    -   `apt-cache showsrc binary_pkg_name` 从本地缓存显示一个二进制软件包的源代码软件包信息

-   `apt-get build-dep pkg_name` 或者 `aptitude build-dep pkg-name`

    -   安装构建软件包所需要的软件包

-   `apt-get source pkg_name` 

    -   从标准档案库下载源代码

-   `dget [*dsc_URL]` 

    -   从其他档案库下载源代码

-   `dpkg-source -x pkg_version-revision.dsc`

    -   从源代码软件包集合（`*.orig.tar.gz` 和 `*.debian.tar.gz` / `*.diff.gz`）中构建代码树

-   `debuild binary`
-   `dpkg -i pkg_name_version-debian.revision_arch.deb`
-   `apt install /path/to/pkg_filename.deb`
-   `debi pkg_name_version-debian.revision_arch.dsc`
-   `dpkg --get-selections '*' >selection.txt`
-   `dpkg --set-selections <selection.txt`
-   `echo pkg_name hold | dpkg --set-selections`

    -   相当于 `aptitude hold pkg_name`

!!! warning "警告"

    对于支持多架构的软件包，应该指定架构名称，如：

    ``` bash
    dpkg -L libglib2.0-0:amd64
    ```

    小心使用 `dpkg -i` 和 `debi`，以及 `dpkg --force-all` 只适用于高手。

-   `aptitude(8)` 以外的其他软件包管理命令使用类似于 shell glob 的通配符。
-   `configure-debian(8)` ->  `dpkg-reconfigure(8)` -> `debconf`。
-   `dget(1)`、`debuild(1)` 和 `debi(1)` 需要 `devscripts` 软件包。
-   使用 `debsums(1)` 通过 `/var/lib/dpkg/info/*.md5sums` 验证已安装的文件。
-   安装软件包 `apt-list bugs` 可以自动检查 Debian BTS 里的严重 bug。
-   安装软件包 `apt-listchanges`，升级时会在 `NEWS.Debian` 中提供重要新闻。
-   一些搜索软件包元数据的工具：

    -   `grep-dctrl(1)`、`grep-status(1)`、`grep-available(1)` 和 `apt-rdepends(8)`。

---

5. Debian 软件包内部管理
------------------------

**5.1. 软件包的档案与元数据**

-   secure ATP 通过用本地安装的 Debian 档案库公钥，来解密 Release.gpg，从而验证**顶层** Release 的完整性。

    -   Packages 和 Sources 文件的完整性则由**顶层** Release 文件内的 MD5sum 值验证。

-   元数据的本地拷贝：

    -   `/var/lib/apt/list/*`
    -   `/var/cache/apt/apt-file/*`

-   软件包状态：

    -   APT 的软件包状态在 `/var/lib/apt/extended_states` 文件中
    -   `aptitude` 的软件包状态在 `/var/lib/aptitude/pkgstates` 文件中

-   软件包的本地副本：`/var/cache/apt/archives/*`
-   Debian 软件包的名称格式，参阅 `dpkg-source(1)`

!!! caution "注意"

    可以用 `dpkg(1)` 提供的命令检查软件包版本，例如 `dpkg --compare-versions 7.0 gt 7.~pre1 ; echo $?`。

**5.2. `dpkg` 命令**

-   `dpkg` 创建的重要文件：

    -   `/var/lib/dpkg/info/package_name.conffiles`
    -   `/var/lib/dpkg/info/package_name.list`
    -   `/var/lib/dpkg/info/package_name.md5sums`
    -   `/var/lib/dpkg/info/package_name.preinst`
    -   `/var/lib/dpkg/info/package_name.postinst`
    -   `/var/lib/dpkg/info/package_name.prerm`
    -   `/var/lib/dpkg/info/package_name.postrm`
    -   `/var/lib/dpkg/info/package_name.config`
    -   `/var/lib/dpkg/alternatives/package_name`
    -   `/var/lib/dpkg/available`
    -   `/var/lib/dpkg/diversions`
    -   `/var/lib/dpkg/statoverride`
    -   `/var/lib/dpkg/status`
    -   `/var/lib/dpkg/status-old`
    -   `/var/backups/dpkg.status*`

!!! tip "提示"

    `udpkg` 命令用于打开 `udeb` 软件包，`udpkg` 命令是 `dpkg` 命令的一个精简版本。

**5.3. 其他工具**

-   `update-alternatives(1)` 命令
-   `dpkg-statoverride(1)` 命令
-   `dpkg-divert(1)` 命令

---

6. 从损坏的系统中恢复
---------------------

---
title: GNU/Linux 教程
---

GNU/Linux 教程
==============

本文档仅仅提供有效的起点，你必须学会自己（从以下原始材料）查找解决方案。

---

0. 原始材料
-----------

这里提供一些寻找解决方案的途径：

-   [Debian 网站][debian]上的通用信息
-   `/usr/share/doc/package_name` 目录下的文档
-   Unix 风格的 manpage: `dpkg -L package_name |grep '/man/man.*/'`
-   GNU 风格的 info page: `dpkg -L package_name |grep '/info/'`
-   [错误报告][bugs]
-   [Debian Wiki][dbwiki] 用于变化和特定的话题
-   国际开放标准组织的的单一 UNIX 规范 [UNIX 系统主页][unix]上
-   自由的百科全书：[维基百科][wiki]
-   [Debian 管理员手册][handbook]
-   来自 [Linux 文档项目(TLDP)][tldr] 的 HOWTO

  [debian]: https://www.debian.org/
  [wiki]: https://www.wikipedia.org/
  [dbwiki]: https://wiki.debian.org/
  [bugs]: https://bugs.debian.org/package_name
  [unix]: https://www.opengroup.org/
  [handbook]: https://www.debian.org/doc/manuals/debian-handbook/
  [tldr]: https://tldp.org/

!!! tip "提示"

    软件包的详细文档，你需要安装软件包名用 "-doc" 作为后缀名的相应文档包来得到。

    ``` bash title="python 的文档包"
    sudo apt install python3-doc
    ```

---

1. 控制台基础
-------------

**1.1. 开机相关**

-   开机时，你遇到的欢迎信息保存在文件 `/etc/motd` 中（Message Of The Day）。

**1.2. 账户权限相关**

-   登陆后你可能会想要创建账户，涉及到的工具有 `adduser(8)` 和 `deluser(8)`。

    -   其底层依靠 `useradd(8)` 和 `userdel(8)`。

-   任意用户下，输入 `su -l` 或 `su` 可以切换到 **root** 账户。

    -   前者不保存当前用户的环境设定，后者则会保存。

-   可以通过以下方式设置特权用户：

    ``` bash
    echo "penguin  ALL=(ALL) ALL" >> /etc/sudoers
    echo "penguin  ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
    ```

    涉及到的工具有 `sudo(8)` 和 `sudoers(5)`。

**1.3. 软件包相关**

-   建议新手安装额外软件包：

    ``` bash
    apt-get update
    ...
    apt-get install mc vim sudo aptitude
    ...
    ```

    但我不太认可它的建议。涉及到的工具有 `apt-get(8)`。

**1.4. 控制台相关**

-   如果你想切换控制台，例如切换到控制台 3，可以这样：`chvt 3`。
-   ++ctrl+d++ 简写为 ^D，退出命令行，等价于输入 `exit`。
-   这时候你输入了许多命令，面对杂乱的屏幕，可以用：`reset` 或 `clear`。

**1.5. 关机相关**

-   几种关机方式：

    -   `shutdown -h now` 适用于多用户模式，安全关机。
    -   `poweroff -i -f` 适用于单用户，断电快速关机。

了解完上面的内容后，你就可以开工了。

---

2. 类 Unix 文件系统
-------------------

**2.1. 文件系统基础**

-   与文件系统相关的工具有 `mount(8)` 和 `umount(8)` ，在安装 `linux-doc` 包后，可以从目录
    `/usr/share/doc/linux-doc-*/Documentation/filesystems/` 中找到每个文件系统支持的挂载选项。

-   关于文件层次的最佳详细实践在文件系统层次标准 `/usr/share/doc/debian-policy/fhs/fhs-*.txt.gz` 和 `hier(7)` 中。
-   不带参数运行 `mount(8)` 以识别文件树和物理实体之间的对应关系。

**2.2. 文件系统权限**

-   显示文件和目录权限相关的工具有：`ls(1)`。
-   设置权限相关的工具有：`chown(1)`，`chgrp(1)`，`chmod(1)`。
-   三个特殊权限位：

    -   Set User ID（SUID）位
    -   Set Group ID（SGID）位
    -   Sticky（粘滞）位

详细用法参考文档，这里提供一些基本用法的示例：

``` bash
ls -alh            # 显示隐藏文件、详细信息、人类可读
chown newowner foo # 给 foo 文件设置所有者
chown newgroup foo # 给 foo 文件设置所属组
chmod a+x foo      # 给 foo 文件添加权限 x
chmod 600 foo      # 给 foo 文件设置权限 rw- --- ---
chmod 1755 tmp     # 给 tmp 文件夹设置权限 rwx r-x r-t
chmod 1754 tmp     # 给 tmp 文件夹设置权限 rwx r-x r-T
```

!!! tip "提示"

    如果你需要在 shell 脚本中访问 `ls -l` 显示的信息，你需要使用相关命令，如 `test(1)`，`stat(1)` 和 `readlink(1)`。shell 内置命令，如 `[` 或 `test`，可能也会用到。

-   将什么权限应用到新建文件受 shell 内置命令 `umask` 的限制。

    -   `(file permissions) = (requested file permissions) & ~(umask value)`
    -   文件权限 = 666 - `umask`
    -   目录权限 = 777 - `umask`
    -   `umask` 一般设置为 0002 或者 0022
    -   参见 `dash(1)`，`bash(1)`，和 `builtins(7)`。

!!! tip "提示"

    通过把 `umask 002` 写入 ~/.bashrc 文件使用 UPG 。

**2.3. 用户和组**

-   使用下面中的一个，将 **penguin** 用户添加到 **bird** 组的方法：

    -   `sudo usermod -aG bird penguin`
    -   `sudo adduser penguin bird`
    -   `sudo vigr` 编辑 `/etc/group` 和 `sudo vigr -s` 编辑 `/etc/gshadow` ，追加 **penguin** 到 **bird** 行。

-   使用下面中的一个，将 **penguin** 用户从 **bird** 组移除的方法：

    -   `sudo usermod -rG bird penguin`
    -   `sudo deluser penguin bird`
    -   `sudo vigr` 编辑 `/etc/group` 和 `sudo vigr -s` 编辑 `/etc/gshadow` ,删除 **bird** 行里面的 **penguin**。

-   使用下面一个应用配置：

    -   冷重启再登陆。
    -   执行 `kill -TERM -1` 并做一些修复行为，比如 `systemctl restart NetworkManager.service` 

!!! note "注意"

    一般用户的 `$PATH` 环境变量下可能没有包含 `/usr/sbin`，而 `usermod`，`adduser`，`vigr` 都在这个目录下。上述命令可以使用绝对路径，或是利用 `su -l`切换到 **root** 用户环境后再执行。

-   设备是另一种文件。因此，如果你从一个用户账户访问某些设备出现问题时，你需要使这个用户成为相关组的成员。

    -   由系统提供的用户和组的完整列表，可以从 `base-passwd` 包提供的 `/usr/share/doc/base-passwd/users-and-groups.html` 中获得。

-   用户和组系统的管理命令，参见 `passwd(5)`，`group(5)`，`shadow(5)`，`newgrp(1)`，`vipw(8)`，`vigr(8)`，以及 `pam_group(8)`。

!!! tip "一些例子"

    你需要属于 **dialout** 组才能重配置调制解调器、拨号到任意地方，等等。但如果 **root** 用户在 `/etc/ppp/peers/` 为受信任点创建了预定义配置文件的话，你只需要属于
    **dip** 组，就可以创建拨号 IP 来连接到那些受信任的点上，需使用的命令行工具包括 `pppd(8)`、`pon(1)` 以及 `poff(1)`。

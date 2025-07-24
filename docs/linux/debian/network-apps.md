---
title: 网络应用
---

网络应用
========

建立网络连接后，你可以运行各种网络应用。

---

1. 网页浏览器
-------------

-   图形界面浏览器：`Firefox ESR`、`Chromium`
-   终端文本浏览器：`lynx`、`w3m`

### 1.1. 伪装用户代理字符串

为了访问一些过度限制的网站，你可能需要伪装网页浏览器程序返回的 User-Agent 字符串。

!!! note "小心"

    这部分内容主要面向需要测试网站兼容性或访问受限内容的开发者/高级用户，普通用户通常不需要修改这个设置。

### 1.2. 浏览器扩展

所有现代的 GUI（图形用户界面）浏览器支持基于 browser extension 的源代码，它在按 web extensions 变成标准化。

---

2. 邮件系统
-----------

### 2.1. 电子邮件基础

电子邮件由三个部分组成：消息的信封、邮件头以及邮件正文。

-   SMTP 用电子邮件信封上的 “To” 和 “From” 来投递邮件。信封上的 “From” 信息也被叫做*退回地址*。
-   电子邮件头也有 “To” 和 “From” 信息。
-   覆盖邮件头和正文数据的电子邮件消息格式被 MIME 扩展。

一些 MUA：`evolution`、`mutt`

### 2.2. 现代邮件服务限制

如果你需要自建邮件服务器，应：

-   使用商业 VPS（非家庭网络）并配置 SPF/DKIM/DMARC。
-   通过智能主机（如 Mailgun、SendGrid）中继邮件，避免端口封锁问题。
-   始终使用端口 587（Submission）而非端口 25（SMTP）发送邮件。

### 2.3. 历史邮件服务端期望

默认期望由 `/usr/sbin/sendmail` 命令发送邮件

-   若目的地为本机，`/usr/sbin/sendmail` 接口进行邮件的本地分发，将邮件投入 `/var/mail/$username`。
-   若目的地为远程主机，`/usr/sbin/sendmail` 接口使用 SMTP 查询 DNS MX 记录传输邮件到目标主机。

### 2.4. 邮件传输代理（MTA）

对于现代移动工作站:

1.  如果只用 GUI 邮件客户端: 完全不需要安装 MTA
1.  如果有程序需要 `sendmail`:

    -   安装 `exim4-daemon-light` 或 `postfix`
    -   配置为通过智能主机发送邮件
    -   确保 `/etc/aliases` 配置正确

### 2.5. 一些配置

-   配置 `exim4` 请阅读 `/usr/share/doc/exim4-base/README.Debian.gz` 官方指导和 `update-exim4.conf(8)`。
-   带有 SASL 的 postfix 配置，请阅读阅读 postfix 文档和关键的手册页。

    -   一些重要的手册：`postfix(1)`、`postconf(1)`、`postconf(5)`、`postmap(1)`、`postalias(1)`

-   这里有一些用于邮件传输、投递和用户代理的邮件地址配置文件

    -   `/etc/mailname`
    -   `/etc/email-addresses`
    -   `/etc/postfix/generic`
    -   `/etc/aliases`

### 2.6. 基础 MTA 操作



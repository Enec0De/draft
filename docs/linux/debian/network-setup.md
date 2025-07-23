---
title: 网络设置
---

网络设置
========

-   关于 Debian 专属的网络手册，请查看 [Debian 管理员手册—网络配置][net]。
-   `systemd` 环境下，可以用 `networkd` 来配置网络。请参考 `systemd-networkd(8)`。

  [net]: https://debian-handbook.info/browse/stable/basic-configuration.html

---

1. 基本网络架构
---------------

给出一些网络配置工具：

-   网络管理：`network-manager`、`network-manager-gnome`、`ifupdown`
-   DHCP/WiFi：`isc-dhcp-client`、`wpasupplicant`、`wireless-tools`
-   诊断工具：`iw`、`iproute2`、`iptables`、`nftables`
-   测试工具：`iputils-ping`、`ethtool`、`nmap`、`tcpdump`
-   高级工具：`wireshark`、`dnsutils`

主机名的解析流程为：

1.  `/etc/nsswitch.conf` 文件里的 `hosts: files dns` 这段规定主机名解析顺序。（代替 `/etc/host.conf` 文件里的 `order` 这段原有的功能。）
1.  `files` 方式首先被调用。在 `/etc/hosts` 文件里面寻找主机名。（`/etc/host.conf` 文件包含 `multi on`。)
1.  `dns` 方式被调用。查询 `/etc/resolv.conf` 文件里面写的互联网域名系统（Domain Name System，DNS）。

下面则是一些其他配置：

-   如果有永久 IP 地址，文件 `/etc/hosts` 内应该有一行如下：

    ```
    12.34.56.78 hostname.example.com hostname
    ```

-   如果 `resolvconf` 软件包没有安装，`/etc/resolv.conf` 是一个静态文件。
-   对于典型 adhoc 局域网环境下的 PC 工作站，除了基本的 `files` 和 `dns` 方式之外，主机名还能够通过 Multicast DNS（mDNS）进行解析。

    -   `libnss-mdns` 插件包提供 mDNS 的主机名解析，GNU C 库（glibc）的 GNU 名字服务转换 Name Service Switch（NSS）功能支持 mDNS。
    -   此时 `/etc/nsswitch.conf` 文件应当有像 `hosts: files mdns4_minimal [NOTFOUND=return] dns` 这样的一段（其它配置参见 `/usr/share/doc/libnss-mdns/README.Debian`）。

-   可以使用 `systemd` 提供的 NSS (Name Service Switch) 模块来替代传统的网络主机名解析方式。

    -   可以联合的模块：`libnss-resolve`、`libnss-myhostname`、`libnss-mymachines`
    -   更多信息参见 `nss-resolve(8)`、`systemd-resolved(8)`、`nss-myhostname(8)` 和 `nss-mymachines(8)`

-   `systemd` 使用 `enp0s25` 之类的“可预测网络接口名称”。
-   私有网络地址范围：`10.0.0.0/8`、`172.16.0.0/12`、`192.168.0.0/16`


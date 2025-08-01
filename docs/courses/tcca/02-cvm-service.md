---
title: 云服务器
status: deprecated
---

计算服务之云服务器 { #cvm-service }
===================================

云服务器，是云计算环境中的一种重要资源。它们是在物理服务器上虚拟化的独立服务器，可以提供与传统服务器相同的功能，但具有更高的灵活性和可扩展性。云服务器可以快速部署、按需扩展，并且只需为实际使用的资源付费。

---

1. KVM 虚拟化技术
-----------------

### 1.1. 虚拟化技术（Virtualization）

将任何一种形式的资源抽象成另一种形式的技术，都是虚拟化。虚拟化是资源的逻辑表示，不受物理限制的约束。

<div class="grid cards" markdown>

-   虚拟化的主要优点：
    
    -   资源共享
    -   成本降低
    -   灵活性高
    -   易于管理
    -   便于维护
    
-   虚拟化的类型：
    
    -   硬件虚拟化
    -   操作系统虚拟化
    -   网络虚拟化
    -   存储虚拟化
    
</div>

虚拟化技术的几个重要概念：

-   Guest OS
-   Guest Machine
-   Hypervisor: 

    -   虚拟化软件层/虚拟机监控机 
    -   Virtual Machine Monitor, VMM

-   Host OS
-   Host Machine

### 1.2. KVM（Kernel-base Virtual Machine）虚拟化技术

KVM 是一种开源的虚拟化技术，它是基于 Linux 内核的虚拟化基础设置。

1.  KVM 虚拟化技术的发展史：

    -   2006 年：由 Qumranet 公司的工程师首次开发并发布。
    -   2007 年：被合并到 Linux 内核当中。
    -   2008 年：红帽收购 Qumranet。
    -   2009 年：成为多数 Linux 发行版的标准虚拟化组件。
    -   2010 年：成为 OpenStack 等云计算平台的首选虚拟化技术之一。
    -   -> 至今：仍是 Linux 虚拟化领域的主要技术之一。

1.  KVM 虚拟化技术的系统架构：

    -   KVM 需要处理器具有硬件虚拟化支持。
    -   KVM 是 Linux 内核的一部分。
    -   QEMU 负责模拟 CPU、内存、磁盘、网络接口和其他硬件资源，以便虚拟机可以使用这些资源。
 
1.  KVM 虚拟化技术的组件架构：

    -   Guest
    -   KVM
    -   QEMU
    -   Libvirt

1.  KVM 虚拟化技术的原理：

    -   KVM 虚拟化技术之 CPU 虚拟化：
        
        有了现代处理器的虚拟化扩展，如 Intel 的 VT-x 和 AMD 的 AMD-V，KVM 模块可以在 VMX Root mode（根模式，相当于 Ring -1）下运行，虚拟机在 VMX Non-Root mode（非根模式，相当于 Ring 0~3）下运行。这样 VMM 可以直接管理硬件资源，减少了上下文切换的开销。
        
    -   KVM 虚拟化技术之内存虚拟化：
     
        通过硬件辅助的虚拟化技术，如 Intel 的 EPT（Extended Page Table）和 AMD 的 RVI（Rapid Virtualization Indexing，也称为 NPT，Nested Page Table），允许 MMU（虚拟内存单元）直接处理从虚拟地址到宿主物理地址的转换，而不需要进行频繁的软件干预。
    
    -   KVM 虚拟化技术之存储虚拟化：
    
        在 KVM 中，存储虚拟化通过模拟和管理虚拟机的存储资源实现，使得虚拟机能像直接访问物理设备一样使用存储资源。
    
        虚拟机通过**前端驱动（Virtio 前端）**将存储 I/O 请求转换为宿主机可理解的请求，将其发送到宿主机的**后段挂载驱动（Virtio 后端）**，进一步传递给宿主机的存储子系统。这里宿主机的存储资源通过**逻辑卷管理（LVM）**为虚拟机提供存储空间。最后，宿主机的**通用块层**统一调度 I/O 请求，将其转换为对应的块设备操作，**设备驱动层**将这些操作请求转换为特定的硬件命令进行处理。
    
    -   KVM 虚拟化技术之网络虚拟化：
    
        KVM 引入 Virtio 半虚拟化网卡技术，通过一种更直接的方式，让**虚拟机**通过 **Virtio 虚拟网卡**直接和**虚拟化层**进行通信，绕过硬件仿真，减少了模拟的开销。之后虚拟化层将网络流量注入**内核网络栈**（L3~L4, IP/TCP），宿主机内核再通过**内核网桥**（L2, MAC），将流量转发到**物理网卡**，与外部网络通信。
    
    !!! note

        加粗字体的出现顺序与对应层次递进的顺序相同。

1.  KVM 虚拟化的作用：
 
    -   显著提高物理服务器资源的利用率
    -   支持批量部署虚拟机
    -   支持实时快照功能
    -   支持克隆功能
    -   支持在线和离线迁移（用于满足服务等级协议 SLA 的核心手段）
    -   支持资源的动态调整

---

2. 云服务器的相关概念与技术
---------------------------

**地域（Region）**

:   云服务器提供商在全球不同地理位置的数据中心集群。每个地域都是一个独立的地理区域，包含多个数据中心。

**可用区（Availability Zone）**

:   在同一地域内的一个或多个物理数据中心，它们之间通过低延迟的网络连接。每个可用区都设计为相互独立，以确保服务的高可用性。

**机型**

:   云服务提供商提供的一系列具有相似性能特点和设计目的的云服务器类型。

**云盘**

:   基于云计算技术的存储解决方案。
  
    ---

    -   其主要特点和优势包括：弹性扩展、高可用性、随时随地访问、易于管理、成本效益、安全性。
    -   云服务商提供的安全措施：数据加密、访问控制、审计日志等。
    -   常见用途包括：数据备份、文件共享、应用程序存储、大数据分析。
  
**镜像**

:   一种虚拟机模板，它包含了操作系统、应用程序和配置等信息。

**快照**

:   一种数据管理技术，用于在特定时间点捕捉和保存数据的状态。

    ---

    -   主要的两种实现方式：写时复制（Copy-On-Write, COW）、写重定向（Redirect-On-Write, ROW）。

    !!! info

        === "写时复制（COW）详细过程"

            | COW 阶段   | `LBA:[0x1000]` | `LBA:[0x2000]` | 读取目标       |
            | :--------: | :------------: | :------------: | :------------: |
            | 创建快照后 | `Hello`        | 空             | `LBA:[0x1000]` |
            | 修改数据后 | `World`        | `Hello`        | `LBA:[0x1000]` |
            | 备注       |                |                | 不查表         |
        
        === "写重定向（ROW）详细过程"

            | ROW 阶段   | `LBA:[0x1000]` | `LBA:[0x2000]` | 读取目标       |
            | :--------: | :------------: | :------------: | :------------: |
            | 创建快照后 | `Hello`        | 空             | `LBA:[0x1000]` |
            | 修改数据后 | `Hello`        | `World`        | `LBA:[0x2000]` |
            | 备注       |                |                | 查表读取       |

**弹性网卡**

:   一种可附加到云服务器上的虚拟网络接口，它允许使用者在云环境中灵活地管理和配置网络。

    ---

    -   主要特点包括：灵活性、可扩展性、高可用性、安全隔离性、简化管理。
    -   使用场景包括：多网络环境、负载均衡、故障转移。

**安全组**

:   一种虚拟防火墙，用于控制一组云服务器的网络通信权限。

    ---

    -   主要特点和优势：状态性、组内共享、粒度控制、易于管理、内置安全。
    -   常见用途包括：限制访问、隔离服务、实现网络分段。

**热迁移**

:   一种在**不关闭**虚拟机的情况下，将其从一个物理主机迁移到另一个物理主机的技术。
  
    ---

    -   具体流程为：迁移开始时，通过 TOR 交换机建立一个高带宽低延迟的数据传输通道。预拷贝阶段，虚拟机的内存页会逐页复制到目标主机，多次迭代拷贝（复制自上次以来发生过变化的内存页）。这个过程会持续到内存页的变化速率低于一定阈值，或者达到最大迭代次数。预拷贝阶段接近完成时，虚拟机会短暂停止运行，通常在在毫秒级别以内，确保最后一批内存页的复制。然后目标主机接管源主机的计算任务。
    -   得以实现的技术支持： 高校的内存复制算法（如脏页追踪、增量复制）、低延迟网络连接与虚拟化平台的支持（如 KVM、VMware vSphere）。
    -   重要应用价值：实现资源的动态调度和负载均衡、在不影响业务运行的情况下进行服务器的升级和维护。

**冷迁移**

:   一种在**关闭**虚拟机的情况下，将其从一个物理主机迁移到另一个物理主机的技术。

    ---

    -   依赖于以下几个关键因素：虚拟机的状态保存和恢复、高效的文件传输机制、虚拟化平台的支持（如 KVM、VMware vSphere）。
    -   重要应用价值： 硬件的维护和升级、资源优化、数据中心迁移。

**故障迁移**

:   一种保护机制。在监测到服务器故障时，将运行在故障服务器上的虚拟机，自动迁移到正常的服务器上。（在此期间，虚拟机的状态和内存会被保存到云盘共享存储中）。

    ---

    -   依赖于以下几个关键因素：高效的故障检测机制、共享存储系统、虚拟化平台的支持（如 KVM、VMware vSphere）。

**弹性伸缩**

:    一种自动调整计算资源的技术，用于应对不断变化的业务需求。

    ---

    -   重要应用价值：应对突发流量、优化资源利用。

---

3. 云服务器 CVM
---------------

### 3.1. 云服务器 CVM 的定义

腾讯云云服务器（Cloud Virtual Machine，CVM）是一种简单高效、处理能力可弹性伸缩的基础云计算服务。可以快速构建更稳定、安全的应用，提升运维效率，降低 IT 硬件成本，让您更专注于核心业务创新，支持随着业务需求的变化来定义实时扩展或缩减云计算资源。

-   计算：

    -   其底层基于 KVM 虚拟化技术。

-   存储：

    -   云存储：具有高可用性、高可靠性，支持数据的可靠存储和快速访问
    -   分布式存储技术：实现冗余备份、快速恢复，确保数据的安全性和完整性

-   网络：

    -   网络架构设计：提供高性能和高可靠性的网络连接
    -   虚拟网络技术：实现虚拟机之间的隔离和安全通信

-   安全防护措施：

    -   网络安全：防火墙，入侵检测、防御系统
    -   主机安全：（操作系统级别）防病毒和漏洞扫描
    -   数据安全：数据加密、访问控制，确保数据的机密性和完整性

### 3.2. CVM 的功能和优势

**CVM 的功能清单：**

| 功能名称     | 功能说明                                                                              |
| :----------: | :------------------------------------------------------------------------------------ |
| 实例管理     | 创建、启动、重启、停止、终止、克隆、镜像、规格调整                                    |
| 网络配置     | 私有网络（VPC）和子网设置、公网 IP 、策略组、内网和外网带宽的配置管理、负载均衡器集成 |
| 存储管理     | 块设备管理、数据的备份和快照、云硬盘的扩容和性能调整                                  |
| 安全与合规   | 密钥对和密码登陆、防火墙、安全组、数据加密和隔离、安全监控、日志审计                  |
| 系统与镜像   | 多操作系统支持、自定义镜像、镜像市场                                                  |
| 自动化与 API | 提供 API 和 SDK 支持自动化部署和管理、云监控、自动化告警、弹性伸缩                    |
| 性能监控     | 实时监控性能指标、设置告警规则、性能数据分析                                          |
| 价格与计费   | 多种付费模式，资源使用和费用管理                                                      |
| 支持与服务   | 技术支持和客服、文档、社区、开发者工具                                                |


**CVM 的功能优势：**

1.  弹性灵活
    
    -   计费模式灵活，节省成本：
    
        -   按量计费、关机不计费、设置定时销毁
        -   包年包月
        -   计费模式转换
    
        ---
    
    -   配置调整灵活，适应不同业务场景：
    
        -   跨示例族调整配置
        -   不关机制作镜像
        -   不关机扩容云硬盘
        -   调整网络带宽
        -   跨机型系列升级、跨可用区热迁移
        -   本地盘转云盘
        -   AS 弹性伸缩
    
1.  高可靠性
    
    -   置放群组：按照容灾纬度打散（母机、机架、交换机）
    -   云盘快照：定期快照
    -   云盘加密：一键开启加密，过程对用户透明，磁盘无性能和容量损耗
   
1.  高安全性
    
    -   主机虚拟化层安全
    -   网络访问层安全
    -   系统层安全
    -   存储层安全
    -   访问控制
    
1.  丰富的镜像支持能力
    
    -    如 Windows，各种主流 Linux 发行版，以及自定义镜像
    
1.  丰富的运维管理能力
    
    -   CVM 运维管理
    -   CVM 云监控
    -   其他 
     
**CVM 的应用场景：**

-   全场景的云服务器实例
-   GPU 高性能异构场景

---

4. 轻量应用服务器
-----------------

### 4.1. 轻量应用服务器的定义

轻量应用服务器（TencentCloud Lighthouse）是新一代开箱即用、面向轻量应用场景的云服务器产品，助力中小企业和开发者便捷高效的在云端构建网站、Web应用、小程序/小游戏、APP、电商应用、云盘/图床和各类开发测试环境，相比普通云服务器更加简单易用且更贴近应用，以套餐形式整体售卖基础云资源并提供高带宽流量包，将热门开源软件融合打包实现一键构建应用，提供极简上云体验。

为什么选择轻量应用服务器：

-   入门简单，使用便捷
-   随用随取，开箱即用
-   节省成本，按需使用
-   稳定可靠，安全性高

### 4.2. 轻量应用服务器的产品优势及应用场景

**产品优势：**

-   简单易用：简化操作复杂度，实现基础设施的自动配置
-   稳定可靠：稳定的网络、I/O读写性能
-   一键秒级构建应用
-   高性价比：多样的付费方式
-   优质镜像
-   安全防护：默认免费开通 DDoS 基础防护，主机安全基础版防护，不同用户间资源全面隔离

**与其他产品对比：**

| 产品优势 | 轻量应用服务器                                       | 云服务器 CVM                                           |
| :------: | :--------------------------------------------------: | :----------------------------------------------------: |
| 用户群体 | 中小企业、开发者                                     | 中大型企业用户                                         |
| 应用场景 | 轻量级应用场景，如：企业网站、博客、微信小程序、图床 | 架构复杂的应用场景，如：高并发网站、大型游戏、机器学习 |
| 计费模式 | 高性价比套餐式售卖，高带宽流量包模式                 | 灵活选配资源，独立叠加计费，固定带宽/流量              |
| 使用体验 | 一站式整合、开箱即用、一键构建、自动创建网络资源     | 面向全业务、用户需自行搭建应用，自行配置               |

相比于传统虚拟专用服务器，轻量级服务器在其基础之上，还有额外功能：

-   应用模板
-   一键部署应用（博客、论坛、公司官网等）
-   应用管理
-   集成其他云产品

**轻量服务器的应用场景：**

| 业务场景     | 场景说明                                   | 推荐应用镜像模板                      |
| :----------: | :----------------------------------------: | :-----------------------------------: |
| 网站搭建     | 提供应用模板，快速构建满足业务诉求的网站   | WordPress、Typecho、宝塔面板          |
| Web 应用     | 提供预置常用 Web 开发平台的应用模板        | LAMP、Node.js、ASP.NET                |
| 小程序后台   | 构建微信小程序、小游戏以及公众号后台服务   | Node.js、OpenFaaS                     |
| 跨境电商     | 外贸独立站、店铺管理环境                   | WooCommerce、WordPress、Windows Serve |
| 私有云盘     | 高性价比存储型套餐、云盘应用镜像           | Cloudreve                             |
| 开发测试环境 | 远程开发、项目测试、运行定时任务、自动任务 | Docker CE、K3s、LAMP、CloudStudio     |
| 云端学习     | 即开即用的学习、开发实验课堂环境           | OpenCloudOS、Ubuntu                   |
| 音视频服务端 | 中小规模音视频互动直播、点播应用服务端     | SRS 音视频服务器、互动直播房间服务      |

---

5. 裸金属云服务器
-----------------

### 5.1. 裸金属云服务器的定义

裸金属云服务器（Cloud Bare Metal，CBM）是基于腾讯云最新虚拟化技术研发的一款拥有极致性能裸金属云服务器。裸金属云服务器兼具虚拟机的灵活弹性、物理机的高稳定、强劲的计算性能，能够完全无缝和腾讯云全产品融合（例如网络，数据库等）。裸金属云服务器可以在极短时间为您构建云端独享的高性能、安全隔离的物理服务器集群。

机上的业务应用可以直接访问裸金属服务器的处理器和内存，无虚拟化开销。同时可以根据业务弹性伸缩物理服务器数量，获取时间缩短为分钟级。容量管理和运维工作由腾讯云专业团队处理。

在腾讯官网中，裸金属服务器特指黑石物理服务器（Cloud Physical Machine）。黑石物理服务器是种可按需购买，按量付费的物理服务器租赁服务。

### 5.2. 裸金属服务器的产品优势和应用场景

**产品优势：**

| 对比项 | 裸金属云服务器             | 托管方式自建 IDC                           |
| :----: | :------------------------: | :----------------------------------------: |
| 弹性 | 弹性扩展、敏捷部署           | 弹性灵活度低，易面临性能过剩、资产贬值问题 | 
| 易用 | 操作简单、灵活运维、云上控制 | 需联系驻场工程师                           | 
| 全面 | 集成各类云服务               | 自建成本高，需自行拉专线、搭建负载均衡     | 
| 安全 | 立体防护、专业支持           | 易被黑客入侵，需购买额外安全防护服务       | 
| 运维 | 7 $\times$ 24 小时运维服务   | 自行维保、缺乏网络问题的解决能力           | 
| 成本 | 按需购买、按量计费           | 租用、运维费用高，易面临设备折旧问题       | 

**应用场景：**

| 业务场景                   | 场景说明                                                                                           |
| :------------------------: | :------------------------------------------------------------------------------------------------: |
| 游戏应用                   | 利用物理机特性应对高 I/O，高 PPS 场景，利用弹性降低游戏公司的成本结构以降低 TCO                    |
| 政企应用                   | 裸金属云服务器实例可以为用户提供独享的、高性能的公有云物理机集群，满足业务需求                     |
| 大数据场景                 | 支持本地 Nvme 高速存储和结合腾讯云对象存储的 COS 的存算分离部署方案，优化大数据业务的性价比        |
| 云原生裸金属容器部署       | 通过弹性网卡 ENI 及云硬盘 CBS，结合容器服务 TKE 的 VPC-CNI 模式，减少 KubeProxy 组件带来的性能损耗 |
| 云上虚拟化软件支持         | 企业在原 IDC 自建的 Xen/KVM 等第三方虚拟化软件，及 OpenStack 等虚拟化调度平台可无缝接入            |
| 高性能计算 HPC/AI 应用部署 | 支持高速低延时的 RDMA 网络互联及最新一代的 CPU 架构和异构 GPU 部件进行计算密集型负载的计算         |

---

6. GPU 云服务器
---------------

### 6.1. GPU 云服务器的定义

GPU 云服务器（Cloud GPU Service）是基于 GPU 的快速、稳定、弹性的计算服务，主要应用于深度学习训练/推理、图形图像处理以及科学计算等场景。 GPU 云服务器提供和标准 CVM  云服务器一致的方便快捷的管理方式。GPU 云服务器通过其强大的快速处理海量数据的计算性能，有效解放用户的计算压力，提升业务处理效率与竞争力。

GPU 云服务器与自建 GPU 服务器的对比：

| 优势 | GPU 云服务器                                               | 自建 GPU 服务器                              |
| :--: | :--------------------------------------------------------: | :------------------------------------------: |
| 弹性 | 分钟级别时间内获取一个或多个弹性伸缩的高性能计算实例       | 机器配置固定，难以满足变化的需求             |
| 性能 | 透传 GPU性能，高效发挥 GPU 性能                            | 用户手工容灾、数据安全不可控                 |
| 易用 | 与腾讯云多种云产品无缝衔接，清晰的安装指引                 | 自行实现装机管理、硬件扩展，需跳板机登陆     |
| 安全 | 不同用户间资源全面隔离，完善的安全组设置，与云安全无缝对接 | 不同用户共享资源，数据不隔离                 |
| 成本 |  提供包月购买方式、硬件跟随主流 GPU 更新步伐、运维成本低   | 高服务器投资运维成本、高功耗、高 IT 运维成本 |

### 6.2. GPU 云服务器的产品优势和应用场景

**产品优势：**

-   实例新能卓越可靠：采用主流的 GPU 和 CPU，有强大的运算能力。
-   服务稳定安全
-   实例部署迅速

**应用场景：**

渲染型应用场景：非线性编辑场景、渲染场景

---

7. 专用宿主机的产品定义
-----------------------

### 7.1. 专用宿主机的产品定义

专用宿主机（CVM Dedicated Host，CDH）提供用户独享的物理服务器资源，满足您资源独享、资源物理隔离、安全、合规需求。购买后，您可在其上灵活创建、管理多种自定义规格的云服务器。

**相关概念：**

| 概念         | 说明                                                           |
| :----------: | :------------------------------------------------------------: |
| 宿主机类型   | 宿主机的类型，不同类型的宿主机硬件配置不同                     |
| 本地硬盘类型 | 宿主机上的磁盘类型，有本地硬盘以及本地 SSD 硬盘两种类型        |
| IP 地址      | 云服务器实例对内和对外的服务地址，即内网 IP 地址和公网 IP 地址 |

### 7.2. 专用宿主机的产品优势和应用场景

**产品优势：**

-   独享资源
-   创建灵活
-   安全合规
-   管理监控
-   轻资产
-   具有云服务器特性

**应用场景：**

-   游戏应用场景
-   金融应用场景

---

8. 云服务器的安全防护
---------------------

### 8.1. 云服务器安全的重要性

云服务器安全对于保障企业数据资产、维护业务连续性、满足合规要求、降低风险成本以及树立良好的企业形象至关重要，因此我们必须高度重视并采取有效措施确保其安全性。

### 8.2. 实现云服务器安全的方式

实现云服务器安全需要从多个方面入手，包括数据加密、访问控制、网络安全、安全审计和日志记录、备份和恢复、安全策略和流程、合规性和标准以及安全培训和意识等。通过综合运用这些措施，可以有效地提高云服务器的安全性，保障企业数据和业务的安全运行。

### 8.3. 腾讯云主机安全介绍

主机安全是一款针对多云主机的安全防护产品（支持腾讯云、非腾讯云主机接入），基于腾讯安全积累的海量威胁数据，利用机器学习为您提供黑客入侵检测和漏洞风险预警等安全防护服务，主要包括密码破解拦截、异常登陆提醒、木马文件检测、高危漏洞检测等安全功能，解决当前服务器面临的主要网络安全风险，帮助企业构建服务器安全防护体系。

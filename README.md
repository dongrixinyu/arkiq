<p align="center">
    <a alt="jionlp logo">
        <img src="https://raw.githubusercontent.com/dongrixinyu/arkiq/refs/heads/main/image/arkiq-logo.jpg" style="width:300px;height:auto;-webkit-mask-image: linear-gradient(to right, transparent, black, transparent);mask-image: linear-gradient(to right, transparent, black, transparent);">
    </a>
</p>

# arkiq 股票交易 AI 辅助预测工具

股票交易是一个挺个性化的事情，每个人有自己的买卖交易策略，各不相同。

不过，不论你怎么操作交易，总离不开**资金面、大盘面、消息面**三个方面。arkiq 能够利用 AI 来实现极具定制化、个性化的自动决策交易。arkiq的目标是，**让每个散户都能用上自动化交易，并且都能定制自己的交易策略**。

## arkiq 特性与优势

- [x] 每日自动抓取财经新闻，分析荐股并推送股票信息；
- [x] 根据用户指定股票，自动分析行情，分析股票买卖策略；
- [ ] 支持用户自定义交易倾向和策略；
- [x] 支持A股；
- [ ] 支持港股；
- [ ] 支持美股；
- [ ] 支持 qmt，ptrade 接口；
- [ ] 支持 windows 平台部署，一键化启动

## arkiq 安装方法 Installation

- 默认采用 [Linux安装方法](../../blob/main/docs/linux_installation.md)
- 对于许多股民来说，并不会编程，也不使用 Linux，因此在 Windows 上的安装，我打算提供一体化打包安装。[Windows安装方法](../../blob/main/docs/windows_installation.md) TODO


## 使用方法

整个界面，依然是对话模式啦！不过，针对特定任务，我做了流程化处理。

- 1、让 AI 预测今天推荐购入或卖出哪些股票，具体到股票名称；
- 2、给 AI 说出一只股票，让 AI 分析是该买入还是卖出。
- 3、其它自由问答内容，你可以随意发挥。

<p align="left">
    <a alt="arkiq demo">
        <img src="https://raw.githubusercontent.com/dongrixinyu/arkiq/refs/heads/main/image/arkiq-demo-image-1.jpg" style="width:500px;height:auto">
    </a>
</p>
<p align="left">
    <a alt="arkiq demo">
        <img src="https://raw.githubusercontent.com/dongrixinyu/arkiq/refs/heads/main/image/arkiq-demo-image-2.jpg" style="width:500px;height:auto">
    </a>
</p>
<p align="left">
    <a alt="arkiq demo">
        <img src="https://raw.githubusercontent.com/dongrixinyu/arkiq/refs/heads/main/image/arkiq-demo-image-3.jpg" style="width:500px;height:auto">
    </a>
</p>


## 原理介绍

股票交易，总离不开**资金面、大盘面、消息面**三个方面。这款智能股票交易软件主要从资金面、消息面制定了操作流程，针对几个特定任务的处理流程如下：

- 1、预测今日股票，给出推荐结果
```
[抓取新闻网页]                    [消息侧建议]
      ● ------> (分析新闻数据) ------> □ --------|   (股票推荐)  (自动交易)
                                                |------ □ -------> ◘
[抓取股票数据]                    [资金侧建议]    |
      ● ------> (分析股价数据) ------> □ --------|

```

- 2、分析指定股票数据，给出建议
```
[抓取指定股票新闻]
        ● ------> (分析新闻数据) ------|   (分析数据)  (自动交易)
                                      |------ □ -------> ◘
[抓取指定股票数据]                     |
        ● ------> (分析股价数据) ------|

```

### TODO

当然，量化交易是个非常复杂的学问，我的工具刚开源，不足之处还是很多，**欢迎大家给建议和意见。**

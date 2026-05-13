---
layout: post
title: "【战斗设计研究】R6与COD21枪械设计与受击模块对比"
date: 2026-04-18 00:00:00 +0800
description: '以R6与COD21为样本，从枪族选取、枪匠改装、动画表现、开火后坐力、特效准星到受击反馈，拆解对比两款FPS战斗设计的差异与底层逻辑'
tags:
- 战斗设计
categories:
- 星跃实战营
---

# 1. R6与COD21在体验、玩法等的差异

在开始详细的分析前，本文先确定2款游戏在目标体验、核心玩法、交战距离几个维度上的不同，如下：

**R6**

* 目标体验：团队合作、强调战术策略（类 RTS 策略决策）、（攻坚的）高紧张感

* 核心玩法：英雄射击+向心进攻的爆破与人质模式。强调信息博弈+地图控制，节奏缓慢，步步为营。

* 交战距离：室内CQB，近距离为主，交战场所多为室内房间走廊。

* BTK：很少，1\~3

**COD21**

* 目标体验：畅快且密集的战斗、快速且流畅的移动与射击的循环、即时反应快速反馈、剧情战斗体验

* 核心玩法：TDM模式。快节奏循环跑图，高速移动+持续交战。

* 交战距离：小巷到开阔地，各种交战距离。

* BTK：较多，2\~5

在确认两款游戏的不同后，本文以游戏设计者想要传达给玩家的体验为指南，拆解两款游戏的战斗设计异同。

***

# 2. 枪械设计

## 2.1 枪族选取

R6中，玩家的体验更多会是快速的突破手、近距离遭遇战的游击、小房间设伏的防守位等。

COD21中，玩家的体验会更加多样，既有近距离遭遇的突袭，也有远距离的狙击手等。为服务于不同的玩法与体验，在枪械的选取取向上两个游戏也有明显差异。

### 2.1.1 武器类型与数量

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-01.png" alt="R6武器列表">
    <figcaption>R6武器列表</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-02.png" alt="COD21配备界面">
    <figcaption>COD21配备界面</figcaption>
  </figure>
</div>

如上图，在武器类型上，R6与COD21的枪族都是很全面的，为：①突击步枪②微冲③轻机枪④DMR⑤狙击⑥手枪

可以发现，两款游戏在枪族数量上，即设计重点存在不少的差异。R6的武器设计重点更多地放在了突击步枪、冲锋枪、霰弹枪等中近距离交战武器上；而COD21的各枪族数量则相较更为均衡，在远距离交战的武器上有更多设计（狙击枪数量）。

|           | **突击** | **微冲** | **霰弹** | **轻机枪** | **DMR** | **狙击枪** |
| --------- | ------ | ------ | ------ | ------- | ------- | ------- |
| **R6数量**  | 26     | 20     | 19     | 8       | 6       | 2       |
| **COD数量** | 14     | 11     | 3      | 5       | 6       | 5       |

### 2.1.2 关键属性字段差异

![R6枪械属性面板](/assets/img/r6-cod21/r6-cod21-03.png)



<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-04.png" alt="">
    
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-05.png" alt="COD21枪械属性面板">
    <figcaption>COD21枪械属性面板</figcaption>
  </figure>
</div>

|       | 属性主要维度 |    |                                                                               |    |                                                                               |                                                                               |     |
| ----- | ------ | -- | ----------------------------------------------------------------------------- | -- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | --- |
| R6    | 伤害     | 射速 | **<span style="color: inherit; background-color: rgb(255,233,40)">摧毁</span>** | 弹药 | 机动                                                                            | 操纵                                                                            | 精准度 |
| COD21 | 伤害     | 射速 | 弹速                                                                            | 弹药 | **<span style="color: inherit; background-color: rgb(255,233,40)">机动</span>** | **<span style="color: inherit; background-color: rgb(255,233,40)">操纵</span>** | 精度  |

如上方图&表所示，除了射击游戏最重要的伤害、射速等核心属性外，游戏体验目标的不同造就了两个游戏在一些关键属性上的选取差异：

1. R6的场景破坏的核心玩法，确定了在R6中“摧毁度”属性的核心地位，同时由于存在不同速度干员的设计，其武器的“机动”属性非核心。
2. COD21的主打为快节奏战斗，3C机动性也高，武器的“机动”“操纵”等属性为核心属性。

## 2.2 枪匠模块

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-06.png" alt="COD21配件改装模块">
    <figcaption>COD21配件改装模块</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-07.png" alt="R6配件改装模块">
    <figcaption>R6配件改装模块</figcaption>
  </figure>
</div>

可以看到，同为偏写实游戏，R6与COD21在枪械改造方面存在很大的差异（COD为核心，R6则边缘）。

COD21的枪匠模块做到了极其细致的底部，外层的瞄准镜、内层的枪机组、子弹类型等都可以通过枪匠模块自定义，这样的改造程度可以将一把武器适配不同打法（XM4改造成近程强化or远程专攻or终成均衡），这由本身游戏的多种类战斗场景决定。

R6的枪械改造模块则是一股极简风，仅有2\~4个配件槽位，对枪械的改造非常有限；这样的设计不会喧宾夺主，不入侵R6的英雄射击、场景破坏等核心玩法，仅仅在游戏内有限的室内CQB场景做微调。

## 2.3 动画模块

本模块以待机状态**Idle动画为例**对比

### 2.3.1 **腰射待机**

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-08.gif" alt="R6腰射待机">
    <figcaption>R6腰射待机</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-09.gif" alt="COD21腰射待机">
    <figcaption>COD21腰射待机</figcaption>
  </figure>
</div>

对比两个游戏在静止状态下的腰射待机Idle动画，存在以下差别：

1. Camera：R6Camera为完全静止，COD21为极其微弱的yaw、pitch与roll轴旋转。
2. Animation：应该都是由枪械为根，带动手臂运动；R6由呼吸起伏、重心微调、手指微动等细节构成，呼吸起伏非常突出（弥补camera静止）；而COD21则主要由枪械重心微变动画构成。

其他姿态如蹲姿，趴姿Idle动画同理，不过默认持枪位发生改变。

### 2.3.2 **ADS待机**

![R6](/assets/img/r6-cod21/r6-cod21-10.gif)

冷知识：左边R6这个其实也是gif动图（

![COD11](/assets/img/r6-cod21/r6-cod21-11.gif)



静止状态下两款游戏的ADS Idle动画差别比较大：

1. Camera：R6完全静止；COD21为较明显的yaw、pitch轴旋转模拟呼吸感。
2. Animation：R6完全静止；COD21配合镜头旋转，枪械有微小但容易察觉到的动画补充。

### 2.3.3 为什么有这样的差异？

本小节以R6与COD21的idle动画做对比，会发现R6在一些状态上的处理，更倾向于不动镜头或尽量小，靠动画补；而COD21倾向于镜头+动画的双重叠加表现（其他状态如行动也如此）。

简单来说，稳定性与沉浸感是矛盾性两头，R6走了稳定性，COD21走了沉浸感。

R6该设计目的为**信息获取优先**，在极小的BTK以及高信息量的博弈中，稳定的3C可以提高玩家专注且有助于其快速做出反应，活着的感觉由动画表现体现。这也在R6的开发者博客Behind the wall中提到过：“由玩家掌控一切”。

COD21的设计目的则是为了**提升游戏的表现力，提高游戏的沉浸感**；镜头+动画的双重表现可以让玩家更准确感受到“我是这名士兵”的感受，并且COD21的信息压力没有R6大，TTK也较长，这样的设计影响并不大。

<span style="color: inherit; background-color: rgb(187,191,196)">Tarkov 也是个有趣的参照：它 TTK 短但选了 COD 的路线（强镜头晃动），因为 Tarkov 追求的是 </span>**<span style="color: inherit; background-color: rgb(187,191,196)">生存恐惧感</span>**<span style="color: inherit; background-color: rgb(187,191,196)"> ，镜头不稳反而增强了紧张和不安全感，服务于它的情绪设计目标。</span>

## 2.4 开火、后坐力模块

### 2.4.1 **先确定几个概念**

viewkick：由相机运动引起后坐力落点的变化。

gunkick：枪身运动导致的后坐力变化。

Visualrecoil：泛指纯粹的视觉后坐力。

### 2.4.2 单发/首发后坐逐帧拆解

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-12.gif" alt="R6">
    <figcaption>R6</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-13.gif" alt="COD21">
    <figcaption>COD21</figcaption>
  </figure>
</div>

* **R6：**

| 帧数        | yaw轴 | roll轴 | pitch轴 | gunkick | Visualrecoil | 备注         |
| --------- | ---- | ----- | ------ | ------- | ------------ | ---------- |
| 0（输入开火指令） |      |       |        |         |              | 无变化        |
| 1         | 几乎不动 | 中幅 逆  | 大幅 上   | 不存在     | 枪身大幅后推       | 最大冲击       |
| 2         | 几乎不动 | 小幅 顺  | 中幅 上   |         | 枪身小幅后推       | 枪身达到最后端    |
| 3         | 几乎不动 | 小幅 顺  | 微幅 上   |         | 枪身小幅前推       | 开始恢复       |
| 4         | 几乎不动 | 小幅 逆  | 不动     |         | 枪身小幅前推       | 上跳到顶点，开始恢复 |
| 5         | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅前推       |            |
| 6         | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅前推       |            |
| 7         | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅前推       | 枪身达到最前端    |
| 8         | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       |            |
| 9         | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       |            |
| 10        | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       |            |
| 11        | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       | 微调         |
| 12        | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       | 微调         |
| 13        | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       | 微调         |
| 14        | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       | 微调         |
| 15        | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       | 微调         |
| 16        | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       | 微调         |
| 17        | 几乎不动 | 不动    | 极微幅 下  |         | 枪身小幅后推       | 完全恢复       |

R6的单发垂直后座力（viewkick的pithch轴变化）粗略示意图：

![](/assets/img/r6-cod21/r6-cod21-14.png)

* **COD21：**

| 帧数        | yaw轴 | roll轴 | pitch轴 | gunkick | Visualrecoil | 备注   |
| --------- | ---- | ----- | ------ | ------- | ------------ | ---- |
| 0（输入开火指令） |      |       |        |         |              | 无变化  |
| 1         | 不动   | 不动    | 不动     | 随机扰动    | 枪身小幅后推       | 开始冲击 |
| 2         | 小幅 左 | 不动    | 小幅 上   | 随机扰动    | 枪身大幅后推       | 最大冲击 |
| 3         | 小幅 右 | 不动    | 小幅 下   | 随机扰动    | 枪身小幅前推       | 开始恢复 |
| 4         |      |       |        | 呼吸晃动    | 枪身小幅前推       | 微调   |
| 5         |      |       |        | 呼吸晃动    | 枪身小幅前推       | 微调   |
| 6         |      |       |        | 呼吸晃动    | 枪身小幅前推       | 完全恢复 |

### 2.4.3 连射拆解

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-15.gif" alt="R6">
    <figcaption>R6</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-16.gif" alt="COD">
    <figcaption>COD</figcaption>
  </figure>
</div>

* **R6：**

viewkick：全程pitch轴不断地上跳，没有回落；从第五发子弹开始yaw轴开始明显旋转，产生了明显水平后座力；roll轴有振幅和频率的随机变化。

gunkick：不存在，准星一直保持于中心位

Visualrecoil：枪身在roll轴的随机旋转；枪身的前后位移（周期性趋势，枪身每几次回推到一个深度）。

R6的垂直后座力（viewkick的pithch轴变化）粗略示意图：

![](/assets/img/r6-cod21/r6-cod21-17.png)

* **COD21：**

viewkick：全程pitch轴不断地上跳，没有回落；前十发子弹yaw轴主要向左明显旋转，十发之后向右旋转，右明显水平后座力由左向右转变；超级大量的roll轴旋转，振幅小，频率更快。

gunkick：随机扰动明显，导致多次射击弹道存在差异

Visualrecoil：枪身的前后位移运动，回推的深度越来越小，运动的趋势是趋近某个深度来回较小位移运动（回推深度到下限）。

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-18.png" alt="大致前后位移趋势">
    <figcaption>大致前后位移趋势</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-19.gif" alt="大致前后位移趋势示意图">
    <figcaption>大致前后位移趋势示意图</figcaption>
  </figure>
</div>

### 2.4.4 差异分析

后坐力主要差异：R6的viewkick在pitch轴上运动幅度远大于COD21，恢复速度也较COD21更慢。

这样的设计差异放大了R6后坐力的限制作用，放大了战术决策的重要性，也更加考验玩家的预瞄和控枪水平，提高了竞技性。

## 2.5 特效模块

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-20.gif" alt="R6">
    <figcaption>R6</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-21.gif" alt="COD21">
    <figcaption>COD21</figcaption>
  </figure>
</div>

射击主要特效有以下几种构成：

1. 枪口：枪口火焰、枪口烟雾
2. 抛壳：抛壳烟雾、弹壳动画
3. 子弹：弹道、弹着点
4. 其他：长时间开枪的热扰动

特效比较重要的就是节奏，需要与开火动画的**节奏配合**：如枪口烟、枪口火焰、抛壳烟雾等的高亮、暗淡、消散。例如根据枪械原理（燃气回推枪机产生后坐与实现抛壳），抛壳动画应该在枪身回推过程中生成，枪口特效应当在抛壳之前等等。

这个模块两个游戏没有明显差异。

## 2.6 准星模块

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-22.gif" alt="">
    
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-23.gif" alt="">
    
  </figure>
</div>

R6：准星不存在 与 动画配合，一直平滑扩散到最大

COD21：准星扩散、回弹、恢复的节奏 与 动画配合（腰射准星来回跳动，枪身恢复收缩一点，枪身后推扩散一点）

***

# 3. 受击模块拆解对比

## 3.1 非开火状态

* **腰射受击**

COD21

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-24.gif" alt="前方受击">
    <figcaption>前方受击</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-25.gif" alt="右方受击">
    <figcaption>右方受击</figcaption>
  </figure>
</div>

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-26.gif" alt="后方受击">
    <figcaption>后方受击</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-27.gif" alt="左方受击">
    <figcaption>左方受击</figcaption>
  </figure>
</div>

1. HUD 层：红色血迹糊屏（前后共用一个，左右受击各不同）、方向指示
2. 镜头层：存在aim punch，镜头会有强烈抖动（三轴都有）
3. 动画层：根据不同受击方向，瞬间的准心扩大与恢复

R6

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-28.gif" alt="前">
    <figcaption>前</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-29.gif" alt="右">
    <figcaption>右</figcaption>
  </figure>
</div>

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-30.gif" alt="后">
    <figcaption>后</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-31.gif" alt="左">
    <figcaption>左</figcaption>
  </figure>
</div>

1. HUD 层：血迹糊屏（四向都不同）、方向指示
2. 镜头层：没有三轴变化，FOV也不变化
3. 后处理层：径向模糊
4. 动画层：根据不同受击方向存在不同枪身移动，左右尤其明显

* **ADS受击**

COD21

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-32.gif" alt="前">
    <figcaption>前</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-33.gif" alt="右">
    <figcaption>右</figcaption>
  </figure>
</div>

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-34.gif" alt="后">
    <figcaption>后</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-35.gif" alt="左">
    <figcaption>左</figcaption>
  </figure>
</div>

1. HUD 层：红色血迹糊屏（前后共用一个，左右受击各不同）、方向指示
2. 镜头层：存在aim punch，镜头会有强烈抖动（三轴都有）
3. 动画层：无枪身动画

R6

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-36.gif" alt="前">
    <figcaption>前</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-37.gif" alt="右">
    <figcaption>右</figcaption>
  </figure>
</div>

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-38.gif" alt="后">
    <figcaption>后</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-39.gif" alt="左">
    <figcaption>左</figcaption>
  </figure>
</div>

1. HUD 层：血迹糊屏（四向都不同）、方向指示
2. 镜头层：没有三轴变化，FOV也不变化
3. 后处理层：径向模糊
4. 动画层：**ADS下没有枪身动画，保持静止**

* **总结**

1. HUD层面：COD21与R6在四向受击都有多种的不同的HUD实现，方便判断攻击方位
2. 镜头层：R6不存在镜头层的变化，COD21会有镜头的强烈抖动
3. 后处理层：R6存在特殊的径向模糊后处理，用以弥补受击反馈的欠缺
4. 动画层：在ADS情况下，COD与R6都不存在枪身动画影响

## 3.2 开火状态

* **腰射开火受击**

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-40.gif" alt="左">
    <figcaption>左</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-41.gif" alt="左">
    <figcaption>左</figcaption>
  </figure>
</div>

* **ADS开火受击**

<div class="figure-row">
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-42.gif" alt="左">
    <figcaption>左</figcaption>
  </figure>
  <figure>
    <img src="/assets/img/r6-cod21/r6-cod21-43.gif" alt="左">
    <figcaption>左</figcaption>
  </figure>
</div>

两个游戏受击表现与不开火状态一致，但R6的方案为纯视觉受击，不影响实际着弹；COD方案为viewkick变动，会影响及时着弹点。

## 3.3 总结

COD21与R6在受击模块都有多个层面的设计，包含HUD、镜头、后处理、动画、音频等等。

主要差异原因在于：

1. COD方案有镜头变化，但跳动与恢复迅速，即便实际影响后坐力也不会对游戏游玩体验造成重大影响，该方案同本文前述，COD方案主要是为了**提高沉浸度**。
2. R6方案则无镜头变化，主要靠HUD、动画、后处理来处理受击反馈，不会实际影响着弹点与后坐力，这个设计方向保证了玩家之间对枪的竞技公平性；但是在竞技性强的FPS中，例如CS，受击是会客观上影响操作的，无论是爆头带来的巨大viewkick还是受击的减速影响都很大。R6明明也强调竞技却没有沿用这样的设计思路，本文认为**主要原因还是R6本身的竞技在于信息的博弈与空间的争夺，不同于CS的核心体验”资源管理 + 硬碰硬对枪“中对枪就是核心环节，这种决策博弈在设计师想要带给玩家的最核心体验**，于是选择了不影响实际着弹的受击方案。

***




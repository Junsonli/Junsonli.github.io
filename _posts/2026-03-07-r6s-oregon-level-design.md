---
layout: post
title: "【关卡设计研究】「俄勒冈乡间屋宅」拆解与《彩虹六号：围攻》关卡设计范式讨论"
date: 2026-03-07
image: '/assets/img/posts/r6s-oregon/image1.jpg'
description: '基于《彩虹六号：围攻》「俄勒冈乡间屋宅」的深度关卡拆解，从动线、阻塞点、区域划分、掩体枪线到可破坏玩法，系统梳理R6S的关卡设计范式与战术博弈逻辑。'
tags:
- 关卡设计
categories:
- 星跃实战营
---

## 前言

## 《彩虹六号：围攻》游戏想带给玩家的核心体验

《彩虹六号：围攻》（以下简称 R6S）是一款以反恐攻坚为核心题材的战术射击游戏，依赖于其关卡、机制、系统等高度耦合的设计，其拥有射击品类中非常顶尖的策略决策深度。

想象这样一个场景：一场以 “围攻” 为核心的室内攻坚战。

* 作为防守方，你们占据了一栋结构复杂的建筑物，面对围攻，将内部改造成具有防御战术的优势阵地，进行阻塞与干扰。
* 作为攻坚小队，你们需要确定目标位置，制定并动态调整攻坚策略，完成目标任务。

上述攻防场景，就是R6S的设计师们想要带给玩家的核心游玩体验。在开发者博客内容“Behind the Wall Series”中，有极为精准的提炼总结：**团队合作、战术策略（类 RTS 策略决策）、（攻坚的）高紧张感。**

> When designing the game, we found that above all else, the No Respawn rule touched the three main pillars of what we want in this game: **teamwork, tactics, and tension.**&#x20;

## 游戏玩法模式

通过怎么样的博弈可以给到玩家这样的体验呢？R6S设计团队给出的答案是——**「有限时间下的空间博弈」**。

有限时间的空间博弈最底层的玩法基础是**场景改造与破坏**，这也是R6S最核心的玩法机制设计；其余机制如信息获取、技能、道具等机制都是对于此核心的策略深化。

R6S实现这种博弈的核心游戏模式为炸弹模式（人质模式的核心博弈也是同样的）。炸弹模式的基本设定：

* **准备阶段45秒，防守方可在室内自由活动，进攻方仅操纵无人机。**&#x884C;动阶段3分钟，双方可完全自由行动。
* 胜利条件：防守方为时间耗尽仍未安装拆弹器；进攻方为安装拆弹器后守卫45s不被拆除；双方都有的歼灭敌方。
* 其他设定：下包以及拆包时间均为7s。进攻方在行动阶段时间耗尽前开始下包可以递延回合时间，归零后中断下包则失败。防守方拆包时间无法递延，必须在45s拆除时间结束前完成。

从模式的设定来看，R6S属于非平衡对抗，体现在在资源的分配上：时间对于防守方来说是优势，而对于进攻方而言是一种有限资源；空间上，防守方具有单方面的先发优势；信息上防守方开局优势，进攻方则具有后发优势。

![双方资源趋势](/assets/img/posts/r6s-oregon/image40.png)

# 「俄勒冈乡间屋宅」关卡拆解

版本：Y11S1

## 1. 关卡核心概念设计分析

### 1.1 **动线**

本文初次拆解动线暂不考虑可破坏玩法，先按照如下思路将显性+静态的动线网络拆解出来。

1. 先标注地图中的核心区（炸弹模式中可以安装拆弹器的区域）
2. 提取出不考虑可破坏玩法的完整动线网络
3. 遵循下列原则标注出主动线（<span style="color: inherit; background-color: rgb(247,105,100)">红色实线</span>）
    * 经过楼梯、区分室内外的门、长走廊等关键结构
    * 高效到达核心区
    * 攻防双方均可通行

根据前述思路，我们可以标注出在不考虑可破坏玩法下「俄勒冈乡间屋宅」静态的<span style="color: inherit; background-color: rgb(247,105,100)">主要</span>或<span style="color: inherit; background-color: rgb(255,233,40)">次要</span>动线。

* **B1层**
<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image38.png" alt="标注目标区"><figcaption>标注目标区</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image37.png" alt="标注完整动线（不考虑破坏）"><figcaption>标注完整动线（不考虑破坏）</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image39.png" alt="标注主动线"><figcaption>标注主动线</figcaption></figure>
</div>

* **1F层**
<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image66.png" alt="标注目标区"><figcaption>标注目标区</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image35.png" alt="标注完整动线（不考虑破坏）"><figcaption>标注完整动线（不考虑破坏）</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image46.png" alt="标注主动线"><figcaption>标注主动线</figcaption></figure>
</div>

* **2F层**
<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image57.png" alt="标注目标区"><figcaption>标注目标区</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image60.png" alt="标注完整动线（不考虑破坏）"><figcaption>标注完整动线（不考虑破坏）</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image61.png" alt="标注主动线"><figcaption>标注主动线</figcaption></figure>
</div>
可以看到每一层都有至少一条长动线切过或经过核心区域并连接大量房间。
* B1F：蓝色通道⇄柱子⇄长走廊（B点）⇄洗衣房（A点）⇄储物间⇄主楼
* 1F：一楼大门⇄大厅（紧挨点内）⇄安保室过道⇄淋浴间过道（紧挨点内）⇄小塔区域（紧挨点内）
* 2F：主楼梯⇄军械室过道⇄奖杯室⇄衣帽间⇄（点内）⇄白楼
在标注出所有动线后，可以发现一些规律：
1. 关卡中防守方摄像头的位置均分布在主动线上。可以以此快速标注出其他关卡主动线的分布。
2. 主动线形态呈现洄游状或鱼骨状，都会经过切过或贯穿核心区，并连接几乎所有房间。

### 1.2  **阻塞点**
1. 动线（尤其是主动线上）上的必经窄口（门、楼梯口、大拐角）
2. 动线交叉口
3. 根据游戏经验，预期会发生战斗的区域
根据前述思路，标注出在动线上的所有阻塞点
* **B1层**
![](/assets/img/posts/r6s-oregon/image62.png)
* **1F层**
![](/assets/img/posts/r6s-oregon/image63.png)
* **2F层**
![](/assets/img/posts/r6s-oregon/image64.png)

### 1.3 **区域划分**
在阻塞点之间，综合距离核心区的距离以及功能划分区域。

* 核心区（<span style="color: inherit; background-color: rgb(247,105,100)">红色</span>）：防守方的最小防线。防守方的所有行为都是基于核心区向外辐射，进攻方的所有行为都是基于该区域收拢。
* 缓冲区（<span style="color: inherit; background-color: rgb(255,233,40)">黄色</span>）：较靠近核心区，且具备防守优势的各类功能区（枢纽、通道）。
* 通道（<span style="color: inherit; background-color: rgb(98,210,86)">绿色</span>）：视野开阔或掩体缺失，不宜防守或久留的区域。
![](/assets/img/posts/r6s-oregon/image65.png)

根据前述思路，划分出不同层区域分布。
* **B1层**
  ![](/assets/img/posts/r6s-oregon/image36.png)
* **1F层**
  ![](/assets/img/posts/r6s-oregon/image41.png)
* **2F层**

![](/assets/img/posts/r6s-oregon/image42.png)

#### 1.3.1 初步梳理与推测

至此，「俄勒冈」单层宏观关卡设计拆解完毕，在此进行初步一些核心概念设计梳理：

* 动线：R6S每层关卡在设计时必然有1条以上主动线穿过或切过核心区。R6S通往核心区的主动线往往具有2条以上；若主动线少如2F，其进攻角度也会比较大。
* 阻塞点：阻塞点的分布较密集，这样的设计偏向近距离战斗，符合室内攻防设定；密集卡点分布也可以给到玩家更大的紧张感，同时强调需要团队配合化解阻塞点。
* 单层区域分布：R6S区域范围小，且分割密集，呈现类似同心圆 “核心区）缓冲区）通道” 分布规律。这样的关卡设计是有利于实现团队合作以及战术策略的体验的。

### 1.4 **掩体与枪线（射线）**

R6S的地图尺寸较小，掩体与枪线的设计相比大地图更加重要，所以对掩体与枪线的设计进行拆解分析是十分必要的。掩体的多少直接决定了关卡区域的防守难度会高度影响玩家的体验，而且与枪线的设计高度相关，所以本文将掩体与射线的设计放在同一个板块进行拆解。

**枪线（射线）**

在关卡设计时，通常避免单点“上帝视角”的压制长枪线。
如通过掩体对枪线进行限制，以此强化与削弱阻塞点、合理设计转角来增加策略和视野范围节奏变化、通过扩大射线交叉角度加强阻塞点收益。

**R6S掩体分类**

根据R6S的3C规则，人物状态分为三类：站姿、蹲姿、趴姿。

据此将R6S的掩体分类为：①站姿完全掩体、②站姿持枪掩体（蹲姿完全掩体）、③蹲姿持枪掩体（趴姿完全掩体）、④复合掩体。

不同掩体作用不尽相同，此处对各掩体的强度进行一个简单排序（综合考虑防护范围、转移灵活度以及对枪线的影响程度等）：复合掩体＞站姿持枪掩体＞站姿完全掩体＞蹲姿持枪掩体

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image9.jpg" alt="蹲姿掩体（站姿持枪掩体）"><figcaption><strong>蹲姿掩体（站姿持枪掩体）</strong><br>享受蹲姿防护范围的同时可以进行直架枪，转移较安全</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image6.jpg" alt="趴姿掩体（蹲姿持枪掩体）"><figcaption><strong>趴姿掩体（蹲姿持枪掩体）</strong><br>享受趴姿防护范围的同时可以进行直架枪，转移较慢</figcaption></figure>
</div>
<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image10.jpg" alt="站姿身高掩体"><figcaption><strong>站姿身高掩体</strong><br>享受完全防护范围，转移安全，架枪范围略小</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image11.jpg" alt="复合掩体"><figcaption><strong>复合掩体</strong><br>综合各类掩体优点</figcaption></figure>
</div>

* **无掩体或少掩体设计**
<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image12.jpg" alt="蓝通"><figcaption>蓝通</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image14.jpg" alt="大塔2楼"><figcaption>大塔2楼</figcaption></figure>
</div>
上图为俄勒冈一些“通道”区的掩体分布情况，我们可以发现“通道”区或是每一层的外围区域的**掩体是设计得很少的甚至是无的**，掩体少的同时枪线也比较单薄，往往只需要面对1条可能的枪线。

在设计上，这样的区域的是有利于进攻方的，倾向于让进攻方占领与突破。信息上进攻方获取途径是可移动的无人机，而防守方几乎都是静态的摄像头（<span style="color: rgb(143,149,158); background-color: inherit">仅echo这样的干员拥有动态的信息获取途径，这或许也是这个干员的设计灵感？</span>）；枪械上，进攻方的枪械多为步枪或射手步枪，空旷地带的战斗会占据优势。

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image13.jpg" alt="冰库"><figcaption>冰库</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image43.png" alt="蓝通枪线切割示意"><figcaption>蓝通枪线切割示意</figcaption></figure>
</div>
可是无掩体的设计不能多用，过多的无掩体设计会使得负空间过多，仅依靠美术的后续点缀无法弥补这一缺陷，最终导致削弱游戏交互性并让玩家感知到空旷与单调（想象一下R6S的室内变成了毛坯房..），也缺少一些可能的策略深度。

如何去改善呢？答案是可以**设计一些低掩护性，低转移性的掩**体。如：B1层冰库和蓝通转角的掩体设计，B1层冰库的掩体设计为靠墙的蹲姿掩体，蓝通的为囊底空间，这些掩体转移困难的，冰库的掩体转移需暴露整个身位，而蓝通的则是无法逃脱（若破开软墙逃脱则为进攻方开辟了到核心区的新动线）。
* **优势掩体设计**

何为优势掩体？本文认为的优势掩体：**转移方便、防护性强**。

优势掩体多设计在缓冲区，设计的目的是产生针对于进攻方的阻塞点（控制权先天在防守方）。

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image44.png" alt="B1层柱位"><figcaption>B1层柱位</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image16.jpg" alt=""></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image17.jpg" alt=""></figure>
</div>
以B1层柱位为例，在该掩体的掩护下，防守方玩家的选择多，可以左/右架住大塔楼梯/蓝通的敌人，同时可以很安全的转移至位于较中心区域的走廊。

本文认为，优势掩体除了是在遵循越靠近核心阻塞力越强这样的趋势外，这个设计对双方玩家的体验感曲线也是很巧妙的设计。设计者在奖励进攻方的同时不惩罚防守方。

对于进攻方而言，通过团队配合、信息收集、道具交换甚至直接刚枪拿下存在优势掩体的缓冲区后，其情绪体验大大上涨；巧妙的是，对于防守方而言，其情绪体验在优势掩体转移方便的属性下，即便被攻破也不会获得较差的体验。<span style="color: rgb(143,149,158); background-color: inherit">（或许外墙的设计也是有这样的设计意图？）</span>

![](/assets/img/posts/r6s-oregon/image45.png)

在「俄勒冈」中有这种体验曲线的掩体设计还有大塔二楼破开软墙后的复合掩体，是对进攻方破开软墙后的奖励：防护性好（站姿+蹲姿），转移方便（可安全从二楼撤离）。

![](/assets/img/posts/r6s-oregon/image15.jpg)
* **核心区的枪线隔断掩体设计**

核心区是防守方的最后腹地，若进攻方已经占领了缓冲区或紧挨核心区的通道等低进攻难度区域，进攻核心区的难度不能很低，应当要付出一定的成本（道具、技能或人物生命）所以对于核心区有一个共性的设计——枪线隔断掩体。

枪线隔断掩体的设计重点在于：限制一条动线、一个区域或一个方向核心区侵入过多枪线。枪线隔断掩体的设计鼓励进攻方多角度进攻（团队合作），同时也是对可破坏玩法的引导，引导玩家通过破坏创造新的枪线；该掩体设计也是提升核心区进攻难度的重要设计。
1. B1层
<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image18.jpg" alt="大塔方向隔断"><figcaption>大塔方向隔断</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image19.jpg" alt="冰库方向不隔断，限制单方向"><figcaption>冰库方向不隔断，限制单方向</figcaption></figure>
</div>

* 1F层
<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image20.jpg" alt="大厅→会议室的隔断"><figcaption>大厅→会议室的隔断</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image47.png" alt="枪线隔断示意图"><figcaption>枪线隔断示意图</figcaption></figure>
</div>

* 2F层

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image21.jpg" alt="白楼梯→游戏厅的隔断"><figcaption>白楼梯→游戏厅的隔断</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image48.png" alt="隔断示意图"><figcaption>隔断示意图</figcaption></figure>
</div>

## 2. 可破坏玩法对于关卡要素以及对战关系的影响

此前的拆解分析多基于静态的关卡结构去分析，由此可推导出攻防双方的对战关系规律：由从外围区域向核心点位推进时，防守方的防守难度逐步降低，而进攻方的进攻难度则持续提升。<span style="color: rgb(143,149,158); background-color: inherit">（曾看见一条有趣弹幕总结：进攻方花1分钟围攻到点外，架枪到最后30s冲点）</span>

R6S作为一款多人竞技的战术射击游戏，双方的失衡绝非设计初衷，而游戏的核心——可破坏机制正是解决这一先天对抗不平衡的关键。这部分将进一步考虑彩六的可破坏玩法对对战关系的影响。

![静态关卡下双方难度曲线](/assets/img/posts/r6s-oregon/image34.png)

### 2.1 R6S的可破坏元素

在开始分析破坏玩法对对战关系的影响前，本文先对彩六的可破坏元素进行梳理与分类。

| **类型**                | **破坏后通行性**<br />   | **破坏方式**                 | **影响关卡要素** | **影响层次**<br /> | **战术作用**                        |
| --------------------- | ------------------ | ------------------------ | ---------- | -------------- | ------------------------------- |
| 软墙（Breakable wall）    | 人物可通行。&#xA;视线可穿透。  | 爆破物 / 枪械 / 技能 / 近战       | 动线、枪线      | 平面             | 快速且低成本地创造平面枪线 / 平面动线            |
| 视线墙<br />（sight wall） | 人物不可通行。&#xA;视线可穿透。 | 爆破物 / 枪械 / 技能 / 近战<br /> | 枪线         | 平面             | 快速且低成本地创造平面枪线                   |
| 可破坏地板（sight floor）    |                    |                          | 枪线         | **立体**         | **垂直空间**枪线，创造制高点优势              |
| 活版门（Hatch）            | 人物可通行。&#xA;视线可穿透。  | 爆破物 / 枪械 / 技能 / 近战       | 动线、枪线      | **立体**         | **连接垂直空间**&#xA;创造新动线与枪线，创造制高点优势 |
| 室内部分物体                | /                  | 爆破物 / 枪械 / 技能 / 近战       | /          | 平面             | 陷阱                              |
| 不可破坏墙体                | 完全阻挡。              | 无法破坏                     | 动线、枪线、掩体   | 平面             |  完全的掩体                          |
| 加固墙                   | 人物可通行。&#xA;视线可穿透。  | 仅硬突破工具与技能                | 动线、掩体      | 平面             | 封锁动线、枪线                         |
| 加固活版门                 | 人物可通行。&#xA;视线可穿透。  | 仅硬突破工具与技能                | 动线、枪线      | **立体**         | 垂直动线封锁，限制进攻方进攻策略。               |

### 2.2 可破坏玩法带来的影响

#### 2.2.1 动线与阻塞点

考虑了破坏因素后，将每一层的动线图重新绘制，表示破坏玩法所带来的“动态”动线&#x4EE5;**<span style="color: inherit; background-color: rgb(187,191,196)">黑色实线</span>**&#x8868;现。

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image49.png" alt="B1F"><figcaption>B1F</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image50.png" alt="1F"><figcaption>1F</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image51.png" alt="2F"><figcaption>2F</figcaption></figure>
</div>
再评估这些“动态”动线对实际动线的影响，去除一些不重要的“动态”动线。去除原则：①连接相同区域（如通道-通道）②对动线路径优化小，不能带来收益（如不跨越阻塞点，不创造完全的新动线）

去除后保留的重要“动态”动线如下：

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image52.png" alt="B1F"><figcaption>B1F</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image53.png" alt="1F"><figcaption>1F</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image54.png" alt="2F"><figcaption>2F</figcaption></figure>
</div>
总结这些由可破坏玩法而产生的“动态”动线出现的规律是：集中于核心区附近。此处大胆推测一下：R6S的软墙以及hatch这类可破坏要素在设计时更多地考虑临近核心区而非通道区，会呈现蛛网一样的内密外疏的规律。

当进攻方玩家占领了临近核心区的缓冲区或一些通道后，这样“动态”动线给予了进攻方玩家更灵活的战术选择，降低了其攻入核心区的难度。当进一步获得更多个方向的空间控制权被拿下，进攻难度会更加下降。

例如，2F中衣帽间的“动态”动线与B1F中蓝通的“动态”动线均为进攻方玩家提供了一条极短的新动线，使进攻方可以绕过原来的静态阻塞点。

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image24.jpg" alt="衣帽间软墙破壁后的新动线，路劲极短"><figcaption>衣帽间软墙破壁后的新动线，路劲极短</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image55.png" alt="不经过奖杯陈列室周围阻塞点"><figcaption>不经过奖杯陈列室周围阻塞点</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image25.jpg" alt="蓝通的新动线，路劲极短"><figcaption>蓝通的新动线，路劲极短</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image56.png" alt="不经过柱位周围阻塞点"><figcaption>不经过柱位周围阻塞点</figcaption></figure>
</div>
值得一提的是，防守方完全封锁所有连接 重要“动态”动线 所需要的强化墙数量，或者说这些 重要“动态”动线 所对应的可破坏元素数量均不大于10个。显然是设计者有意为之，让防守方有能力去封锁一些关键动线，对抗进攻难度的下降，消耗进攻方玩家的资源（时间、道具）。

| B1F：9个 | 1F：10个（厨房+会议室）、10个（厨房+食堂） | 2F：6个 |

<span style="color: rgb(143,149,158); background-color: inherit">（这个数量规律还蛮符合我日常游玩经验中观察到的点位选择的，大家都是优先选顶楼或地下等可破坏要素较少的点位）</span>

#### 2.2.2 掩体与枪线

考虑了破坏因素后，对静态关卡中掩体、枪线隔断以及阻塞点等设计产生较大的影响，枪线伸展的自由度提升，阻塞点收益被削弱甚至被绕行。

* 掩体的削弱、枪线的扩展与交叉

在静态关卡下的优势掩体、枪线隔断掩体的设计，其静态强度会因为平面的软墙以及垂直方向的hatch的可破坏性大幅度削弱。

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image23.jpg" alt="垂直枪线的侵入"><figcaption>垂直枪线的侵入</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image22.jpg" alt="平面枪线扩展"><figcaption>平面枪线扩展</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image26.jpg" alt="原B1F的枪线隔断掩体强度削减"><figcaption>原B1F的枪线隔断掩体强度削减</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image27.jpg" alt="2F的枪线隔断掩体强度削减"><figcaption>2F的枪线隔断掩体强度削减</figcaption></figure>
</div>
hatch以及软墙带来的枪线变化，对于进攻方攻入核心区提供了助力，通过长距离的枪械优势，从防守方手上夺取空间的控制权，进一步压缩防守方空间。

指的一提的是，可破坏元素，尤其是hatch与可破坏地板，在扩展进攻方枪线的同时也为进攻方提供了优势掩体（往往占据制高点）。

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image29.jpg" alt="低处视野小，高处暴露少"><figcaption>低处视野小，高处暴露少</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image28.jpg" alt="高处可以看到更多低处视野，同时转移方便"><figcaption>高处可以看到更多低处视野，同时转移方便</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image58.png" alt="简单示意图"><figcaption>简单示意图</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image30.jpg" alt="进攻方也可以通过控制平面软墙的破坏缺口大小来获取优势掩体"><figcaption>进攻方也可以通过控制平面软墙的破坏缺口大小来获取优势掩体</figcaption></figure>
</div>
换个角度思考：是否存在部分可破坏要素，能在枪线与掩体方面为防守方提供一定反制空间？通过对 “俄勒冈乡间屋宅” 关卡的拆解，我确实发现了少量这类设计的存在。在实际游戏过程中，进攻方也往往会利用这些可破坏要素进行多种多样的开发，产生了涌现。<span style="color: rgb(143,149,158); background-color: inherit">（此处我想感叹一下黑镜的设计，使防守方可以从可破坏要素获利巨多，喜提常年BAN位）</span>

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image33.jpg" alt="阁楼的防守方掩体与枪线"><figcaption>阁楼的防守方掩体与枪线</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image32.jpg" alt="对洗衣房的防守方掩体与枪线"><figcaption>对洗衣房的防守方掩体与枪线</figcaption></figure>
</div>

### 小结

在前述可破坏元素对于关卡要素的影响分析中，本文认为可破坏元素在设计主要针对静态关卡中的攻防失衡的调节，主要考虑进攻方，降低其进攻难度，对于防守方的考虑较少。

# 彩虹六号的关卡设计范式讨论

本章节尝试分析R6S的关卡设计范式，可能更多是对前文中已经出现的思考的总结。

【猜测】制作地图的顺序为：先制作1F的地图，再根据一层的地图制作B1F、2F、3F的地图

* 地面一层地图制作逻辑：划定总体外轮廓（如果具有现实原型），随后根据地图尺寸制作各个区域房间并通过一条主动线
* 以现实原型建筑的外墙轮廓作为地图一层与二层或三层外轮廓。在制作完成地面一层的地图后，再以【地面一层与其他层联通楼梯】为【其他层主动线】起点或始点，制作其他层地图

## 1. 核心概念的设计范式（静态关卡）

### 1.1 关卡尺寸标准Metric

在游戏中，所有干员模型的身高统一为180 cm。

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image3.jpg" alt="窄窗"><figcaption>窄窗</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image31.jpg" alt="窗口高度：90cm"><figcaption>窗口高度：90cm</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image5.jpg" alt="宽窗"><figcaption>宽窗</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image4.jpg" alt="宽窗"><figcaption>宽窗</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image1.jpg" alt="窄门"><figcaption>窄门</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image2.jpg" alt="宽门"><figcaption>宽门</figcaption></figure>
</div>
本文仅对一些常见结构的配置要求进行简单估算，想表达的原则：这些常用的结构在设计上必须能够有精准数据实现模板化、参数化、统一。只有关卡设计尺寸确定后，才能让游戏产出的关卡规范以及生产效率的提升。

* 窄窗配置：120cm×80cm；宽窗配置：120cm×150cm
* 窄门配置：210cm×90cm；宽门配置：210cm×200cm

### 1.2 动线
1. 每一层的都必须有1\~2条**长动线**贯穿或切过核心区，并经过几乎地图的所有结构
2. 长动线的设计不应该过于笔直，应当通过多设置转角、房间等避免
3. 只有１条长动线设计时，不应使进攻角度过小（＜９０°）

### 1.3 阻塞点
1. 阻塞点的设计应当密集，引导近距离战斗
2. 在静态关卡设计下，最后靠近目标点的阻塞点数量不宜过多，应呈现越靠近目标点阻塞点越收拢的规律

### 1.4 区域

R6S的“围攻”是向心型的，所以区域的设计范式本文认为就是前文所述“通道→缓冲区→核心区”的划分。这些区域的设计范式为：
1. 核心区：防守方出生点+炸弹所在地。防守强度最高的区域，是地图的核心
2. 缓冲区：核心区附近的区域，以核心区向外辐射，可以设置为枢纽地带或进攻方进攻路线汇聚处
3. 通道区（外围区域）：倾向于攻防平衡或进攻方优势，使进攻方不至于长时间卡在室外，加快其进入室内的速度

### 1.5 掩体与枪线
1. 针对外围区域，掩体少设计或不放置，并且掩体的可转移性应当弱（如靠墙掩体）
2. 针对外围区域，应减少同时面对的枪线数量（可以有多条枪线，但时间上要分割）
3. 针对缓冲区域，应当设计优势掩体，由防守方先占领。优势掩体属性为**转移方便、防护性强**。
4. 针对核心区域，应当设计掩体阻拦一个方向就向核心区侵入过多的枪线

## 2. 可破坏元素设计原则

### 2.1 软墙的设计范式

1. 软墙的分布应当主要集中于核心区附近
2. 软墙的分布应当主要考虑对攻防平衡的影响
3. 软墙设计主要辅助进攻方进行枪线的扩展为主
4. 软墙设计在考虑进攻方动线时，可以①创造大角度最新动线（如大塔二楼）②大幅度缩短入点时间
5. 核心区与核心区之间应当保持畅通，若静态关卡无法畅通，则应该在核心区与核心区之间设置软墙

### 2.2 ｈａｔｃｈ以及可破坏地板的设计范式
1. 同软墙设计，ｈａｔｃｈ的分布应当也集中于核心区附近
2. 设计hatch时，应当主要考虑对下层的关卡核心概念以及攻防平衡的影响

## 3. 总结

本文认为R6S的关卡设计范式总体思路为：
①先不考虑破坏因素设计静态的关卡，在初始的静态关卡设计中，静态关卡下的动线、掩体与枪线设计蛀牙奥从防守方角度考虑，使静态关卡符合越靠近核心区越难以进攻的总体趋势。

②在原有的静态关卡设计基础上添加可破坏元素的设计，设计时主要从进攻方视角考虑。

# 尝试构建一个关卡layout

设计流程：

1. 先确定基本的建筑外轮廓
2. 随意画两条交叉的主动线（就是直线，后续再慢慢增加拐角等）
3. 再划定两个相邻的核心区
4. 根据本文　核心区／缓冲区／通道　的区域规则划分区域
5. 设计各个区域以及其重要的掩体设计
6. 草图完成
7. Sｋｅｔｃｈｕｐ搭建ｌａｙｏｕｔ并对比例进行一定规范，全程持续调整关卡设计。（版本SU2020）

[📎 ｌｐｊ自制地图（一层）.skp](/assets/attachments/lpj-map.skp)

<div class="figure-row">
<figure><img src="/assets/img/posts/r6s-oregon/image59.png" alt="PPT极其潦草的草图.."><figcaption>PPT极其潦草的草图..</figcaption></figure>
<figure><img src="/assets/img/posts/r6s-oregon/image67.jpg" alt="SU顶视图"><figcaption>SU顶视图</figcaption></figure>
</div>
# 参考

1. [彩虹六号围攻 关卡设计分析](https://cyanl.com/post-4/)
2. [彩虹六号玩法分析 - Ludens的文章 - 知乎](https://zhuanlan.zhihu.com/p/427807698)
3. [FPS类游戏的关卡设计](https://bruceqi93.github.io/2016/11/03/FPS-level-design/)
4. [从《瓦罗兰特》看竞技FPS地图设计](https://www.gcores.com/articles/174759#nopop_ej3cb)
5. [多人游戏（以CS为例）地图设计全攻略](https://zhuanlan.zhihu.com/p/7108613683)
6. [空间类型演译：以平面图探讨《彩虹六号：围攻》 - 暴走的巫師的文章 - 知乎](https://zhuanlan.zhihu.com/p/53571780)
7. [《彩虹六号：围攻》银行地图修正方案](https://zhuanlan.zhihu.com/p/55361704)
8. [《彩虹六号：围攻》修正银行关卡之绘制模型](https://zhuanlan.zhihu.com/p/58798475)
9. [《彩虹六号：围攻》咖啡厅关卡探讨空间类型组构](https://zhuanlan.zhihu.com/p/75380766)
10. [空间类型演译:参数化关卡设计的思考](https://zhuanlan.zhihu.com/p/59413073)
11. [解构游戏地图与关卡设计基本元素——以FPS游戏为例](https://www.bilibili.com/video/BV1jW4y1C74u/?spm_id_from=333.1387.search.video_card.click\&vd_source=7e419c5e5de2c72122c548e322d2f7eb)
12. [R6S百科 - 灰机wiki](https://r6s.huijiwiki.com/wiki/%E9%A6%96%E9%A1%B5)
13. [Dev Blog: Level Design – Kafe](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/6nDqxITrS6tFdhjFkmVnrZ/dev-blog-level-design-kafe)
14. [Behind the Wall Series – One Life](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/4CK0Vbt3CzbYpBDTYgeDCo/behind-the-wall-series-one-life)
15. [Behind The Wall Series – Dev Spotlight](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/2RajWqXiRECRbknzYmBYw6/behind-the-wall-series-dev-spotlight)

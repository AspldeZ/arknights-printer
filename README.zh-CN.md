# Arknights Printer

一个 Agent Skill：把真实主题（一次测量、一个结构、一起事件）做成工业科幻风格的海报或信息图。每张图都是某个机构发出的一份文件：网格外露，标签各有职能，字小，只有一种品牌色，留白充足。

非官方同人项目，与鹰角网络无关。只提取风格，不取作品。

[English](README.md)

| | |
|---|---|
| ![正午影长测景记录](examples/gnomon.png) | ![泰河大桥事故调查页](examples/tay-bridge.png) |

## 安装

把 `arknights-printer/` 复制到 agent 的 skills 目录（Claude Code：`~/.claude/skills/`）。

## 使用

直接要一张关于真实主题的图，例如「做一张关于圭表测影的信息图」。skill 最多问四个问题：画幅尺寸、发件机构、方言、信息密度（疏 / 标准 / 密）。

最适合有真实数据、形状清楚的主题：一次测量、一个剖面、一条路线、一个结构、一起事件的时间线。

## 脚本

需要 Python 3；`render_check.py` 另需 Playwright。

```bash
python3 arknights-printer/scripts/bundle.py page.html -o output/page.html
python3 arknights-printer/scripts/render_check.py output/page.html --medium screen
```

`bundle.py` 把样式、脚本和子集化字体打包成单个文件；`render_check.py` 渲染 PNG，并报告回退字体、文字越界、文字重叠、字号过小和多余饱和色。

## 许可

MIT

# Chunchunheart · Psychology Skills

心理学与自我反思工具包

一个可在 **Windows、macOS、Linux 的 Codex** 中使用的四合一技能包。中文优先，也支持英文。无需额外 API Key、Hermes 或 EvoMap；技能内容是 Markdown 指令与参考资料。

> 用于自我反思、关系沟通与人物分析，不提供临床诊断，也不替代心理治疗。技能文件在本地，但使用云端模型聊天仍需联网，内容会由所选模型服务处理。

## 最简单的安装方式（推荐）

打开 Codex 新聊天，复制发送：

```text
请使用 skill-installer，把 https://github.com/sherrongao/chunchunheart/tree/main/skills/psychology-skills 安装到我的个人技能目录。请完整保留 references 和 upstream 资料，并验证安装结果；如果已有同名技能，先说明差异，不要直接覆盖。
```

**Windows 也使用同一句话。** 不要只复制 `SKILL.md`，参考文件必须一起安装。安装完成后在下一轮调用；未发现时重新启动 Codex。

## 下载后本地安装

在 GitHub 点击 **Code → Download ZIP**，解压完整仓库。

### Windows

在解压后的仓库文件夹打开 PowerShell。有 Python 3 时运行：

```powershell
py -3 .\install.py
```

如果没有 Python，也能手动安装：在资源管理器地址栏输入 `%USERPROFILE%\.agents\skills`，创建不存在的文件夹，再把仓库中的 `skills\psychology-skills` **整个文件夹**复制进去。最后应当存在：

```text
%USERPROFILE%\.agents\skills\psychology-skills\SKILL.md
```

### macOS / Linux

在解压后的仓库文件夹运行：

```sh
python3 install.py
```

也可手动将 `skills/psychology-skills` 复制到 `~/.agents/skills/`。

### 安装目录与旧版兼容

本地安装脚本按[当前官方文档](https://learn.chatgpt.com/docs/build-skills)默认使用用户级 `~/.agents/skills`。部分旧版或内置 skill-installer 使用 `~/.codex/skills`（自定义 `CODEX_HOME` 时使用其 `skills` 子目录）。以你的 Codex 实际配置为准；不要在多个目录重复安装同名技能。

若你的版本使用旧目录，可指定：

```powershell
# Windows PowerShell
py -3 .\install.py --dest "$env:USERPROFILE\.codex\skills"
```

```sh
# macOS / Linux
python3 install.py --dest "${CODEX_HOME:-$HOME/.codex}/skills"
```

Windows 使用 WSL 运行 Codex 时，要装进 WSL 用户的技能目录；Windows 与 WSL 的用户目录不共用。

脚本只复制本仓库的技能文件，不联网、不修改 Codex 配置、不覆盖已有安装。可以用 `--dest` 指定其他技能父目录。

## 怎么使用

新聊天输入：

```text
用 $psychology-skills 帮我分析这件事，并选择合适的模块：……
```

也可以直接指定模块：

| 模块 | 适合的问题 | 示例 |
|---|---|---|
| 行为与人物心理（academic-psychologist） | 行为、动机、虚构人物 | 用 $psychology-skills 分析我为什么总把喜欢的工作拖到截止前才做，先比较不同解释。 |
| 亲密关系（love-skill） | 冲突、沟通、信任修复 | 用 $psychology-skills 的 love-skill 模块帮我梳理争吵，先听我说，不急着给建议。 |
| 荣格自我探索（jungian） | 自我画像、原型、镜像对话 | 用 $psychology-skills 做镜像对话，每次只问一个问题，暂时不给建议。 |
| 深度对话（deep-dialogue） | 价值观、意义、信念检视 | 用 $psychology-skills 探讨“成功”对我意味着什么，可以温和挑战我的想法。 |

安装的是 **一个技能入口、四个内部模块**。`love-skill` 等模块不是另行注册的 `$love-skill` 命令。启用自动选择，但点名 `$psychology-skills` 最明确。同一对话中接着聊即可，无须每轮重复名字。

## 隐私与适配

- 不附带用户聊天记录、心理画像、个人日记或账号信息；上游 profiles 仅为公开的模板和示例。
- 默认不主动保存反思或心理画像。需要保存时由使用者决定内容、范围和位置。
- 不调用上游的 Hermes runtime、EvoMap 发布或遥测接口。
- 对关系、人格与动机的解释是可修正假设；荣格原型是可选隐喻。
- 原文存于 `upstream/` 便于溯源；有效规则是技能入口与适配模块。

## 来源与许可

基于 [agency-skills](https://github.com/bestagentkits/agency-skills)、[love-skill](https://github.com/pajama-studio/love-skill)、[jungian-soul-agent-skills](https://github.com/zhwenchao/jungian-soul-agent-skills)、[deep-dialogue](https://github.com/arikmir/deep-dialogue) 整理。感谢原作者。

这是独立整合版本，不代表原作者或 OpenAI 官方背书。原始版本、保留范围与修改记录见 [SOURCES](skills/psychology-skills/SOURCES.md)。原创整合部分使用 [MIT](LICENSE)；第三方材料保留其许可声明，见 [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md)。

## English quick start

A Chinese-first, English-capable Codex skill combining behavioral/character analysis, relationship communication, Jungian reflection and philosophical dialogue. Works with native Windows, macOS and Linux; no extra runtime is required for the skill itself.

Ask Codex to install `https://github.com/sherrongao/chunchunheart/tree/main/skills/psychology-skills` with skill-installer. Alternatively, download this repository and run `python3 install.py` (`py -3 .\install.py` on Windows). Then ask: `Use $psychology-skills to help me reflect on …`. The default manual-install destination is `~/.agents/skills`; use `--dest` for a different configured skill directory. Existing installations are never overwritten.

Not diagnosis or therapy. Local skill files do not make cloud-model conversations offline or local-only.

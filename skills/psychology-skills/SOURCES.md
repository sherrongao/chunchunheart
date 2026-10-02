# 来源与适配记录

这是基于四个公开仓库整理的跨平台组合包，非上游官方联合发行。根 SKILL.md 与 references/ 是中文 Codex 适配；upstream/ 保留所用上游原文、方法资料及可获取的许可证声明。原始技能入口改名 original.txt，避免重复发现多个入口。

仅启用一个 psychology-skills 技能。未包含或启用 Hermes 运行时、EvoMap 配置、进化发布、联网权限声明和后台任务。未迁移原作者的个人偏好。上游资料可能含有不适用于此环境的指令与未经核实的临床主张，读取时遵循适配入口。保存真实用户数据需单独授权。

## 固定来源版本

- [bestagentkits/agency-skills](https://github.com/bestagentkits/agency-skills/tree/a837f9f81a4dc42b58a9ba87ab65e5110112a9c8)
  - Commit: `a837f9f81a4dc42b58a9ba87ab65e5110112a9c8`
  - 原始入口: `skills/academic/academic-psychologist/SKILL.md`
  - License: MIT; see bundled LICENSE
- [pajama-studio/love-skill](https://github.com/pajama-studio/love-skill/tree/316bf52d90ff7c37f361007fa9ebdbfdbff51ce0)
  - Commit: `316bf52d90ff7c37f361007fa9ebdbfdbff51ce0`
  - 原始入口: `SKILL.md`
  - License: MIT (README declaration; no standalone LICENSE found)
- [zhwenchao/jungian-soul-agent-skills](https://github.com/zhwenchao/jungian-soul-agent-skills/tree/7d2f4dff428d16b9385f445665702b1dc2e3358c)
  - Commit: `7d2f4dff428d16b9385f445665702b1dc2e3358c`
  - 原始入口: `skill.md`
  - License: MIT; see bundled LICENSE
- [arikmir/deep-dialogue](https://github.com/arikmir/deep-dialogue/tree/b9b02ad373e37c8e3d913390f342189179e91bff)
  - Commit: `b9b02ad373e37c8e3d913390f342189179e91bff`
  - 原始入口: `SKILL.md`
  - License: MIT (README declaration; no standalone LICENSE found)

## 打包范围

- Academic：指定的角色心理技能及仓库许可证。
- Love：入口、frameworks、protocols、上游中文资料与 README 许可声明。
- Jungian：入口、六模块、prompts、templates、profiles 模板与示例、方法和安全文档、许可证。源文所提运行时或未收录开发文档不属于可用工具。
- Deep Dialogue：入口、六份理论参考与 README 许可声明。

版本固定在 sources.json；安装后不会自动更新或联网上传。跨平台安装方法见仓库根目录 README.md；本包不依赖固定用户名或绝对路径。通过 `$psychology-skills` 调用，也允许按描述自动选择。

结构依据：[OpenAI Skills 文档](https://developers.openai.com/plugins/build/skills)。

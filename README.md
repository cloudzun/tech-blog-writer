# 技术博客写作助手 - OpenClaw Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-Skill-blue.svg)](https://openclaw.ai)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> 一个完整的 OpenClaw Skill 教学项目，展示如何构建生产级别的 AI 写作助手。

## 🎯 项目简介

这是一个**完整、实用、易学**的 OpenClaw Skill 示例项目，专为学习 Skills 开发而设计。它实现了一个技术博客写作助手，包含：

- ✅ 完整的 Skill 目录结构
- ✅ 质量检测系统（4个维度）
- ✅ 标题生成器（3种公式）
- ✅ 模板系统
- ✅ 配置驱动
- ✅ 详细文档

### 核心功能

| 功能 | 说明 |
|------|------|
| **智能写作流程** | 需求分析 → 内容创作 → 质量检测 → 优化改进 |
| **质量检测** | 技术准确性、可读性、实用性、结构完整性 |
| **标题生成** | 教程型、原理型、实战型三种公式 |
| **模板系统** | 标准化的文章结构模板 |

---

## 📦 安装

### 前置要求

- OpenClaw 2.10+
- Python 3.8+
- Git

### 安装步骤

```bash
# 1. 克隆仓库到 OpenClaw skills 目录
cd ~/.claude/skills/  # 或你的项目 .claude/skills/ 目录
git clone https://github.com/cloudzun/tech-blog-writer.git

# 2. 验证安装
ls -la tech-blog-writer/

# 3. 测试脚本
cd tech-blog-writer/scripts
python3 quality_checker.py "测试内容" --json
```

---

## 🚀 快速开始

### 1. 激活 Skill

在 Claude Code 中输入：

```
帮我写一篇 Docker 入门教程
```

或

```
写技术博客：React Hooks 原理解析
```

### 2. 使用质量检测

```bash
cd scripts/
python3 quality_checker.py "文章内容" --json
```

**输出示例**：
```json
{
  "success": true,
  "score": 85,
  "dimensions": {
    "accuracy": 28,
    "readability": 22,
    "practicality": 20,
    "structure": 15
  },
  "suggestions": [
    "✅ 总分 85 分，已达到优秀标准！"
  ]
}
```

### 3. 生成标题

```bash
python3 title_generator.py "Docker容器化" --count 5
```

**输出示例**：
```
【候选 1】5分钟搞懂 Docker 容器化
  公式: 教程型
  评分: 90/100
  推荐理由: 时间承诺 + 降低门槛

【候选 2】手把手教你用 Docker
  公式: 教程型
  评分: 80/100
  推荐理由: 实战导向 + 详细步骤
```

---

## 📁 目录结构

```
tech-blog-writer/
├── SKILL.md                          # [必需] 核心定义文件
├── README.md                         # 项目说明
├── LICENSE                           # MIT 许可证
├── .gitignore                        # Git 忽略文件
│
├── scripts/                          # 工具脚本
│   ├── quality_checker.py            #   质量检测器（450行）
│   └── title_generator.py            #   标题生成器（300行）
│
├── templates/                        # 文章模板
│   └── tutorial-template.md          #   教程模板
│
├── config/                           # 配置文件
│   └── settings.json                 #   运行时配置
│
├── docs/                             # 文档
│   └── design.md                     #   设计文档
│
└── data/                             # 数据文件
    └── examples.json                 #   示例数据
```

---

## 📖 使用指南

### 完整写作流程

```
步骤1：需求分析
    输入：用户的写作主题
    输出：文章大纲

步骤2：内容创作
    输入：文章大纲
    输出：文章草稿

步骤3：质量检测
    输入：文章草稿
    输出：质量评分报告

步骤4：优化改进
    输入：质量评分报告
    输出：最终文章
```

### 质量检测维度

| 维度 | 满分 | 检测项 |
|------|------|--------|
| **技术准确性** | 30 | 代码示例、语言指定、版本号、输出结果 |
| **可读性** | 25 | 段落长度、标题分层、列表使用 |
| **实用性** | 25 | 步骤说明、完整示例、常见问题 |
| **结构完整性** | 20 | 标题、摘要、总结、逻辑连贯 |

### 标题公式

1. **教程型**：`[时间] + [动作] + [技术] + [结果]`
   - 示例：5分钟搞懂 Docker 容器化

2. **原理型**：`深入理解 [技术] 的 [核心概念]`
   - 示例：深入理解 React Hooks 的工作原理

3. **实战型**：`[动作] + [技术] + [场景]`
   - 示例：用 Docker 实现微服务部署

---

## 🎓 学习路径

### 新手（1小时）

1. ✅ 阅读 `README.md`（10分钟）
2. ✅ 查看 `SKILL.md` 结构（20分钟）
3. ✅ 运行 `quality_checker.py`（15分钟）
4. ✅ 运行 `title_generator.py`（15分钟）

### 进阶（2-3小时）

1. 📖 理解 `SKILL.md` 的设计（30分钟）
2. 🔍 分析 `quality_checker.py` 逻辑（1小时）
3. 🔍 分析 `title_generator.py` 逻辑（1小时）
4. ⚙️ 修改配置文件测试（30分钟）

### 高级（1天）

1. 🛠️ 新增检测维度（2小时）
2. 🛠️ 新增标题公式（1小时）
3. 🛠️ 创建新模板（1小时）
4. ⚡ 优化脚本性能（2小时）
5. 🧪 编写测试用例（2小时）

---

## 🎯 设计亮点

### 1. 完整的 Skill 结构

符合 OpenClaw Skills 标准模板，包含所有推荐组件：

- ✅ SKILL.md（YAML Frontmatter + Markdown Body）
- ✅ scripts/（Python 脚本）
- ✅ templates/（模板文件）
- ✅ config/（配置文件）
- ✅ docs/（文档）
- ✅ data/（数据文件）

### 2. 渐进式披露

- **元数据**：name + description（常驻内存，~100字节）
- **指令**：Markdown Body（按需加载，~10KB）
- **资源**：scripts/、templates/（按需调用）

### 3. Hot Reloading

- 修改 `SKILL.md` 后自动生效
- 无需重启 Claude Code
- 快速迭代开发

### 4. 模块化设计

- 质量检测独立模块
- 标题生成独立模块
- 配置驱动
- 易于扩展

---

## 🔧 配置说明

### settings.json

```json
{
  "preferences": {
    "target_audience": "intermediate",  // 目标读者
    "article_length": "medium",         // 文章长度
    "code_language": "python",          // 代码语言
    "output_language": "chinese"        // 输出语言
  },
  "quality_thresholds": {
    "excellent": 85,  // 优秀标准
    "good": 70,       // 合格标准
    "acceptable": 60  // 可接受标准
  }
}
```

---

## 📝 使用示例

### 示例1：写一篇 Docker 教程

**输入**：
```
帮我写一篇 Docker 入门教程
```

**AI 响应流程**：
1. 分析需求：目标读者是初学者
2. 生成大纲：Docker 是什么 → 为什么需要 → 第一个容器 → 常用命令
3. 创作文章：应用教程模板
4. 质量检测：调用 `quality_checker.py`
5. 输出最终文章

---

### 示例2：优化现有文章

**输入**：
```
帮我优化这篇文章：
（粘贴文章内容）
```

**AI 响应流程**：
1. 调用 `quality_checker.py` 检测
2. 分析问题点（如：缺少代码示例、段落过长）
3. 提供具体修改建议
4. 生成优化后的版本

---

## 🐛 故障排查

### 问题1：Skill 未激活

**症状**：输入触发词没有反应

**解决方案**：
```bash
# 1. 检查 SKILL.md 格式
head -n 5 SKILL.md

# 2. 验证 YAML Frontmatter
# 应该显示：
# ---
# name: tech-blog-writer
# description: 当用户提到"写技术博客"...
# ---

# 3. 尝试重新加载
# 在 Claude Code 中输入：/reload
```

---

### 问题2：脚本执行失败

**症状**：调用脚本时报错

**解决方案**：
```bash
# 1. 检查 Python 版本
python3 --version  # 需要 3.8+

# 2. 检查脚本权限
chmod +x scripts/*.py

# 3. 手动测试脚本
cd scripts/
python3 quality_checker.py "测试内容"
```

---

### 问题3：质量检测不准确

**解决方案**：
- 调整 `config/settings.json` 中的阈值
- 修改 `quality_checker.py` 的检测逻辑
- 参考 `data/examples.json` 中的示例

---

## 🤝 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 贡献方向

- 🐛 修复 Bug
- ✨ 新增功能（新的检测维度、标题公式）
- 📝 改进文档
- 🧪 添加测试用例
- ⚡ 性能优化

---

## 📚 参考资源

- **OpenClaw 官方文档**: https://docs.openclaw.ai
- **Skills 定制指南**: https://github.com/cloudzun/Claude-Code-Guide-Zh
- **M7 Stock Analysis Skill**: 另一个完整的 Skill 示例

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 👤 作者

**HuaQloud**

- GitHub: [@cloudzun](https://github.com/cloudzun)
- Blog: https://blog.huaqloud.com

---

## 🙏 致谢

- OpenClaw 团队提供的优秀框架
- 所有贡献者的宝贵建议

---

## 📊 项目统计

- **代码行数**: ~1,200行
- **文档字数**: ~15,000字
- **文件数量**: 11个
- **开发时间**: 2小时

---

**⭐ 如果这个项目对你有帮助，请给个 Star！**

**📖 更多 OpenClaw Skills 示例，请关注我的 GitHub！**

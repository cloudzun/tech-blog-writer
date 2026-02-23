# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- 增强工作流程可视化（流程图）
- 规范化输出格式（使用 emoji）
- 新增原理解析模板
- 新增实战案例模板
- 新增对比分析模板
- 增加 CHANGELOG.md
- 增加 CONTRIBUTING.md

### Changed
- 优化 SKILL.md 结构
- 重组 scripts 目录（core/utils/tests）
- 统一脚本输出格式
- 分离配置文件（quality_thresholds.json, title_formulas.json）

### Fixed
- 修复标题生成器的评分算法
- 修复质量检测器的段落长度计算

## [1.0.0] - 2026-02-22

### Added
- 初始版本发布
- 实现基础写作流程（需求分析 → 内容创作 → 质量检测 → 优化改进）
- 集成质量检测脚本（4个维度）
- 集成标题生成器（3种公式）
- 支持中英文双语
- 提供教程模板
- 配置驱动设计
- 完整文档（README, design.md）

### Features
- **质量检测系统**
  - 技术准确性（30分）
  - 可读性（25分）
  - 实用性（25分）
  - 结构完整性（20分）

- **标题生成器**
  - 教程型标题
  - 原理型标题
  - 实战型标题

- **模板系统**
  - 教程模板

- **配置系统**
  - settings.json（运行时配置）
  - examples.json（示例数据）

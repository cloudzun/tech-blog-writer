#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
技术博客标题生成器 V1.0

功能：
- 根据主题生成多个标题候选
- 应用3种标题公式
- 评估标题质量

用法：
    python title_generator.py "主题" [--count 5] [--json]

示例：
    python title_generator.py "Docker容器化" --count 5
    python title_generator.py "React Hooks" --json
"""

import sys
import io
import json
from typing import List, Dict
from dataclasses import dataclass, asdict


# ==================================================
# 数据类定义
# ==================================================

@dataclass
class TitleCandidate:
    """标题候选"""
    title: str
    formula: str
    score: int
    reason: str


@dataclass
class TitleReport:
    """标题生成报告"""
    success: bool
    topic: str
    candidates: List[Dict]
    message: str


# ==================================================
# 标题生成器
# ==================================================

class TitleGenerator:
    """技术博客标题生成器"""

    def __init__(self):
        """初始化生成器"""
        self.formulas = {
            "tutorial": {
                "name": "教程型",
                "pattern": "[时间] + [动作] + [技术] + [结果]",
                "templates": [
                    "{time}搞懂 {tech} {aspect}",
                    "手把手教你 {action} {tech}",
                    "{time}掌握 {tech} 的 {aspect}"
                ]
            },
            "principle": {
                "name": "原理型",
                "pattern": "深入理解 [技术] 的 [核心概念]",
                "templates": [
                    "深入理解 {tech} 的 {aspect}",
                    "{tech} 工作原理详解",
                    "{tech} 核心概念全解析"
                ]
            },
            "practical": {
                "name": "实战型",
                "pattern": "[动作] + [技术] + [场景]",
                "templates": [
                    "用 {tech} 实现 {scenario}",
                    "{tech} 实战：{scenario}",
                    "从零开始用 {tech} 搭建 {scenario}"
                ]
            }
        }

    def generate(self, topic: str, count: int = 5) -> TitleReport:
        """
        生成标题候选

        Args:
            topic: 主题关键词
            count: 生成数量

        Returns:
            TitleReport: 标题报告
        """
        try:
            if not topic or not topic.strip():
                return TitleReport(
                    success=False,
                    topic="",
                    candidates=[],
                    message="主题不能为空"
                )

            # 解析主题
            tech, aspect, scenario = self._parse_topic(topic)

            # 生成候选标题
            candidates = []

            # 教程型标题
            candidates.extend(self._generate_tutorial_titles(tech, aspect))

            # 原理型标题
            candidates.extend(self._generate_principle_titles(tech, aspect))

            # 实战型标题
            candidates.extend(self._generate_practical_titles(tech, scenario))

            # 评分排序
            candidates = sorted(candidates, key=lambda x: x.score, reverse=True)

            # 取前N个
            top_candidates = candidates[:count]

            return TitleReport(
                success=True,
                topic=topic,
                candidates=[asdict(c) for c in top_candidates],
                message=f"成功生成 {len(top_candidates)} 个标题候选"
            )

        except Exception as e:
            return TitleReport(
                success=False,
                topic=topic,
                candidates=[],
                message=f"生成失败: {str(e)}"
            )

    def _parse_topic(self, topic: str) -> tuple:
        """解析主题，提取关键词"""
        # 简单实现：假设主题格式为 "技术名称 [方面/场景]"
        parts = topic.split()
        tech = parts[0] if parts else topic
        aspect = parts[1] if len(parts) > 1 else "核心概念"
        scenario = parts[1] if len(parts) > 1 else "实战项目"
        return tech, aspect, scenario

    def _generate_tutorial_titles(self, tech: str, aspect: str) -> List[TitleCandidate]:
        """生成教程型标题"""
        titles = []

        # 模板1：时间 + 搞懂
        title = f"5分钟搞懂 {tech} {aspect}"
        titles.append(TitleCandidate(
            title=title,
            formula="教程型",
            score=self._score_title(title),
            reason="时间承诺 + 降低门槛"
        ))

        # 模板2：手把手
        title = f"手把手教你用 {tech}"
        titles.append(TitleCandidate(
            title=title,
            formula="教程型",
            score=self._score_title(title),
            reason="实战导向 + 详细步骤"
        ))

        # 模板3：从入门到精通
        title = f"{tech} 从入门到精通"
        titles.append(TitleCandidate(
            title=title,
            formula="教程型",
            score=self._score_title(title),
            reason="完整路径 + 系统学习"
        ))

        return titles

    def _generate_principle_titles(self, tech: str, aspect: str) -> List[TitleCandidate]:
        """生成原理型标题"""
        titles = []

        # 模板1：深入理解
        title = f"深入理解 {tech} 的 {aspect}"
        titles.append(TitleCandidate(
            title=title,
            formula="原理型",
            score=self._score_title(title),
            reason="深度内容 + 原理解析"
        ))

        # 模板2：工作原理
        title = f"{tech} 工作原理详解"
        titles.append(TitleCandidate(
            title=title,
            formula="原理型",
            score=self._score_title(title),
            reason="技术深度 + 全面解析"
        ))

        return titles

    def _generate_practical_titles(self, tech: str, scenario: str) -> List[TitleCandidate]:
        """生成实战型标题"""
        titles = []

        # 模板1：用X实现Y
        title = f"用 {tech} 实现 {scenario}"
        titles.append(TitleCandidate(
            title=title,
            formula="实战型",
            score=self._score_title(title),
            reason="实战导向 + 具体场景"
        ))

        # 模板2：实战系列
        title = f"{tech} 实战：{scenario}"
        titles.append(TitleCandidate(
            title=title,
            formula="实战型",
            score=self._score_title(title),
            reason="系列感 + 实践价值"
        ))

        # 模板3：从零开始
        title = f"从零开始用 {tech} 搭建 {scenario}"
        titles.append(TitleCandidate(
            title=title,
            formula="实战型",
            score=self._score_title(title),
            reason="零基础 + 完整项目"
        ))

        return titles

    def _score_title(self, title: str) -> int:
        """评估标题质量（100分制）"""
        score = 50  # 基础分

        # 长度适中（15-30字）
        length = len(title)
        if 15 <= length <= 30:
            score += 20
        elif 10 <= length < 15 or 30 < length <= 35:
            score += 10

        # 包含数字
        if any(char.isdigit() for char in title):
            score += 10

        # 包含动作词
        action_words = ['搞懂', '教你', '实现', '搭建', '掌握', '理解']
        if any(word in title for word in action_words):
            score += 10

        # 包含时间承诺
        if any(word in title for word in ['分钟', '小时', '天']):
            score += 10

        return min(score, 100)

    def generate_report(self, report: TitleReport) -> str:
        """生成可读报告"""
        lines = [
            "=" * 60,
            "技术博客标题生成报告",
            "=" * 60,
            "",
            f"主题: {report.topic}",
            f"生成数量: {len(report.candidates)}",
            "",
            "-" * 60,
            "标题候选（按评分排序）:",
            ""
        ]

        for i, candidate in enumerate(report.candidates, 1):
            lines.append(f"【候选 {i}】{candidate['title']}")
            lines.append(f"  公式: {candidate['formula']}")
            lines.append(f"  评分: {candidate['score']}/100")
            lines.append(f"  推荐理由: {candidate['reason']}")
            lines.append("")

        lines.extend(["-" * 60, f"消息: {report.message}", "=" * 60])
        return "\n".join(lines)


# ==================================================
# 命令行入口
# ==================================================

def main():
    """命令行入口"""
    # 设置UTF-8输出
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer,
        encoding='utf-8'
    )

    # 参数验证
    if len(sys.argv) < 2:
        print("用法: python title_generator.py <主题> [--count N] [--json]")
        print("")
        print("示例:")
        print("  python title_generator.py 'Docker容器化'")
        print("  python title_generator.py 'React Hooks' --count 5")
        print("  python title_generator.py 'Vue3' --json")
        sys.exit(1)

    # 解析参数
    topic = sys.argv[1]
    count = 5
    output_json = False

    for i, arg in enumerate(sys.argv[2:]):
        if arg == "--count" and i + 3 < len(sys.argv):
            count = int(sys.argv[i + 3])
        elif arg == "--json":
            output_json = True

    # 生成标题
    generator = TitleGenerator()
    report = generator.generate(topic, count)

    # 输出结果
    if output_json:
        print(json.dumps(asdict(report), ensure_ascii=False, indent=2))
    else:
        print(generator.generate_report(report))

    # 返回状态码
    sys.exit(0 if report.success else 1)


if __name__ == "__main__":
    main()

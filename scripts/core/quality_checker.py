#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
技术博客质量检测器 V1.0

功能：
- 检测技术准确性
- 评估可读性
- 验证实用性
- 检查结构完整性

用法：
    python quality_checker.py "文章内容" [--json]

示例：
    python quality_checker.py "# Docker教程..." --json
"""

import sys
import io
import json
import re
from typing import Dict, List, Tuple
from dataclasses import dataclass, asdict


# ==================================================
# 数据类定义
# ==================================================

@dataclass
class QualityReport:
    """质量检测报告"""
    success: bool
    score: int
    dimensions: Dict[str, int]
    suggestions: List[str]
    details: Dict[str, any]


# ==================================================
# 质量检测器
# ==================================================

class QualityChecker:
    """技术博客质量检测器"""

    def __init__(self):
        """初始化检测器"""
        self.max_scores = {
            "accuracy": 30,      # 技术准确性
            "readability": 25,   # 可读性
            "practicality": 25,  # 实用性
            "structure": 20      # 结构完整性
        }

    def check(self, content: str) -> QualityReport:
        """
        检测文章质量

        Args:
            content: 文章内容

        Returns:
            QualityReport: 质量报告
        """
        try:
            # 验证输入
            if not content or not content.strip():
                return QualityReport(
                    success=False,
                    score=0,
                    dimensions={},
                    suggestions=["文章内容为空"],
                    details={}
                )

            # 执行各维度检测
            accuracy_score, accuracy_details = self._check_accuracy(content)
            readability_score, readability_details = self._check_readability(content)
            practicality_score, practicality_details = self._check_practicality(content)
            structure_score, structure_details = self._check_structure(content)

            # 计算总分
            dimensions = {
                "accuracy": accuracy_score,
                "readability": readability_score,
                "practicality": practicality_score,
                "structure": structure_score
            }
            total_score = sum(dimensions.values())

            # 生成建议
            suggestions = self._generate_suggestions(
                content,
                dimensions,
                {
                    "accuracy": accuracy_details,
                    "readability": readability_details,
                    "practicality": practicality_details,
                    "structure": structure_details
                }
            )

            return QualityReport(
                success=True,
                score=total_score,
                dimensions=dimensions,
                suggestions=suggestions,
                details={
                    "accuracy": accuracy_details,
                    "readability": readability_details,
                    "practicality": practicality_details,
                    "structure": structure_details
                }
            )

        except Exception as e:
            return QualityReport(
                success=False,
                score=0,
                dimensions={},
                suggestions=[f"检测失败: {str(e)}"],
                details={"error": str(e)}
            )

    def _check_accuracy(self, content: str) -> Tuple[int, Dict]:
        """检测技术准确性（30分）"""
        score = 0
        details = {}

        # 1. 是否有代码示例（10分）
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        if code_blocks:
            score += 10
            details["has_code"] = True
            details["code_count"] = len(code_blocks)
        else:
            details["has_code"] = False
            details["code_count"] = 0

        # 2. 代码块是否指定语言（5分）
        if code_blocks:
            lang_specified = sum(1 for block in code_blocks if re.match(r'```\w+', block))
            if lang_specified == len(code_blocks):
                score += 5
                details["lang_specified"] = True
            else:
                details["lang_specified"] = False
                details["lang_ratio"] = f"{lang_specified}/{len(code_blocks)}"

        # 3. 是否有版本号说明（5分）
        version_patterns = [
            r'v?\d+\.\d+',
            r'Node\.js \d+',
            r'Python \d+',
            r'版本',
            r'version'
        ]
        has_version = any(re.search(pattern, content, re.IGNORECASE) for pattern in version_patterns)
        if has_version:
            score += 5
            details["has_version"] = True
        else:
            details["has_version"] = False

        # 4. 是否有输出示例（10分）
        output_indicators = ['输出', '结果', 'output', 'result', '预期']
        has_output = any(indicator in content for indicator in output_indicators)
        if has_output:
            score += 10
            details["has_output"] = True
        else:
            details["has_output"] = False

        return min(score, self.max_scores["accuracy"]), details

    def _check_readability(self, content: str) -> Tuple[int, Dict]:
        """检测可读性（25分）"""
        score = 0
        details = {}

        # 1. 段落长度适中（10分）
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        if paragraphs:
            avg_paragraph_length = sum(len(p) for p in paragraphs) / len(paragraphs)
            if 100 <= avg_paragraph_length <= 500:
                score += 10
                details["paragraph_length"] = "适中"
            elif avg_paragraph_length < 100:
                score += 5
                details["paragraph_length"] = "偏短"
            else:
                score += 3
                details["paragraph_length"] = "偏长"
            details["avg_paragraph_chars"] = int(avg_paragraph_length)

        # 2. 使用标题分层（10分）
        h2_count = len(re.findall(r'^##\s', content, re.MULTILINE))
        h3_count = len(re.findall(r'^###\s', content, re.MULTILINE))
        if h2_count >= 3:
            score += 5
            details["h2_count"] = h2_count
        if h3_count >= 2:
            score += 5
            details["h3_count"] = h3_count

        # 3. 使用列表（5分）
        list_count = len(re.findall(r'^\s*[-*]\s', content, re.MULTILINE))
        if list_count >= 5:
            score += 5
            details["list_count"] = list_count
        elif list_count > 0:
            score += 3
            details["list_count"] = list_count

        return min(score, self.max_scores["readability"]), details

    def _check_practicality(self, content: str) -> Tuple[int, Dict]:
        """检测实用性（25分）"""
        score = 0
        details = {}

        # 1. 是否有步骤说明（10分）
        step_indicators = ['步骤', 'step', '第一', '第二', '首先', '然后']
        has_steps = any(indicator in content for indicator in step_indicators)
        if has_steps:
            score += 10
            details["has_steps"] = True
        else:
            details["has_steps"] = False

        # 2. 是否有完整示例（10分）
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        if code_blocks:
            # 检查代码块长度（完整性）
            avg_code_length = sum(len(block) for block in code_blocks) / len(code_blocks)
            if avg_code_length > 100:
                score += 10
                details["code_completeness"] = "完整"
            else:
                score += 5
                details["code_completeness"] = "简单"

        # 3. 是否有常见问题（5分）
        faq_indicators = ['常见问题', 'FAQ', 'Q&A', 'Q:', 'A:']
        has_faq = any(indicator in content for indicator in faq_indicators)
        if has_faq:
            score += 5
            details["has_faq"] = True
        else:
            details["has_faq"] = False

        return min(score, self.max_scores["practicality"]), details

    def _check_structure(self, content: str) -> Tuple[int, Dict]:
        """检测结构完整性（20分）"""
        score = 0
        details = {}

        # 1. 是否有标题（5分）
        has_title = bool(re.search(r'^#\s', content, re.MULTILINE))
        if has_title:
            score += 5
            details["has_title"] = True
        else:
            details["has_title"] = False

        # 2. 是否有摘要/前言（5分）
        intro_indicators = ['摘要', '前言', '简介', '背景', 'summary', 'introduction']
        has_intro = any(indicator in content[:500] for indicator in intro_indicators)
        if has_intro:
            score += 5
            details["has_intro"] = True
        else:
            details["has_intro"] = False

        # 3. 是否有总结（5分）
        conclusion_indicators = ['总结', '小结', '结论', 'summary', 'conclusion']
        has_conclusion = any(indicator in content[-500:] for indicator in conclusion_indicators)
        if has_conclusion:
            score += 5
            details["has_conclusion"] = True
        else:
            details["has_conclusion"] = False

        # 4. 逻辑连贯性（5分）
        # 简单检查：是否有过渡词
        transition_words = ['首先', '然后', '接下来', '最后', '因此', '所以']
        transition_count = sum(content.count(word) for word in transition_words)
        if transition_count >= 3:
            score += 5
            details["transition_count"] = transition_count
        elif transition_count > 0:
            score += 3
            details["transition_count"] = transition_count

        return min(score, self.max_scores["structure"]), details

    def _generate_suggestions(self, content: str, dimensions: Dict, details: Dict) -> List[str]:
        """生成改进建议"""
        suggestions = []

        # 技术准确性建议
        if dimensions["accuracy"] < 20:
            if not details["accuracy"].get("has_code"):
                suggestions.append("建议添加代码示例以提高技术准确性")
            if not details["accuracy"].get("lang_specified"):
                suggestions.append("建议为所有代码块指定编程语言")
            if not details["accuracy"].get("has_version"):
                suggestions.append("建议说明技术栈的版本号")
            if not details["accuracy"].get("has_output"):
                suggestions.append("建议添加代码运行结果示例")

        # 可读性建议
        if dimensions["readability"] < 15:
            if details["readability"].get("paragraph_length") == "偏长":
                suggestions.append("部分段落过长，建议拆分为多个小段")
            if details["readability"].get("h2_count", 0) < 3:
                suggestions.append("建议使用更多二级标题（##）组织内容")
            if details["readability"].get("list_count", 0) < 5:
                suggestions.append("建议使用列表（- 或 *）增强可读性")

        # 实用性建议
        if dimensions["practicality"] < 15:
            if not details["practicality"].get("has_steps"):
                suggestions.append("建议添加分步骤的操作指南")
            if details["practicality"].get("code_completeness") == "简单":
                suggestions.append("建议提供更完整的代码示例")
            if not details["practicality"].get("has_faq"):
                suggestions.append("建议添加常见问题（FAQ）部分")

        # 结构完整性建议
        if dimensions["structure"] < 12:
            if not details["structure"].get("has_title"):
                suggestions.append("建议添加文章标题")
            if not details["structure"].get("has_intro"):
                suggestions.append("建议添加摘要或前言部分")
            if not details["structure"].get("has_conclusion"):
                suggestions.append("建议添加总结部分")

        # 总分建议
        total_score = sum(dimensions.values())
        if total_score < 70:
            suggestions.insert(0, f"⚠️ 总分 {total_score} 分，低于合格线（70分），建议重点改进")
        elif total_score < 85:
            suggestions.insert(0, f"✅ 总分 {total_score} 分，已达到合格标准，继续优化可达到优秀")
        else:
            suggestions.insert(0, f"🎉 总分 {total_score} 分，已达到优秀标准！")

        return suggestions

    def generate_report(self, report: QualityReport) -> str:
        """生成可读报告"""
        lines = [
            "=" * 60,
            "技术博客质量检测报告",
            "=" * 60,
            "",
            f"总分: {report.score}/100",
            "",
            "各维度得分:",
            f"  技术准确性: {report.dimensions.get('accuracy', 0)}/{self.max_scores['accuracy']}",
            f"  可读性:     {report.dimensions.get('readability', 0)}/{self.max_scores['readability']}",
            f"  实用性:     {report.dimensions.get('practicality', 0)}/{self.max_scores['practicality']}",
            f"  结构完整性: {report.dimensions.get('structure', 0)}/{self.max_scores['structure']}",
            "",
            "-" * 60,
            "改进建议:",
        ]

        for i, suggestion in enumerate(report.suggestions, 1):
            lines.append(f"  {i}. {suggestion}")

        lines.extend(["", "=" * 60])
        return "\n".join(lines)


# ==================================================
# 命令行入口
# ==================================================

def main():
    """命令行入口"""
    # 设置UTF-8输出（Windows兼容）
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer,
        encoding='utf-8'
    )

    # 参数验证
    if len(sys.argv) < 2:
        print("用法: python quality_checker.py <文章内容> [--json]")
        print("")
        print("示例:")
        print("  python quality_checker.py '# Docker教程...'")
        print("  python quality_checker.py '文章内容' --json")
        sys.exit(1)

    # 解析参数
    content = sys.argv[1]
    output_json = "--json" in sys.argv

    # 执行检测
    checker = QualityChecker()
    report = checker.check(content)

    # 输出结果
    if output_json:
        print(json.dumps(asdict(report), ensure_ascii=False, indent=2))
    else:
        print(checker.generate_report(report))

    # 返回状态码
    sys.exit(0 if report.success else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文本分析工具 V1.0

提供文本基础分析功能：字数统计、段落分析、关键词提取等。

用法:
    python text_analyzer.py <text> [--json]

版本历史:
- V1.0.0 (2026-02-23): 初始版本
"""

import sys
import io
import json
import re
from typing import Dict, List
from dataclasses import dataclass, asdict


@dataclass
class TextStats:
    """文本统计结果"""
    char_count: int
    word_count: int
    paragraph_count: int
    code_block_count: int
    heading_count: int
    list_item_count: int
    avg_paragraph_length: float
    readability_score: int  # 0-100


class TextAnalyzer:
    """文本分析器"""
    
    def analyze(self, text: str) -> TextStats:
        """
        分析文本统计信息
        
        Args:
            text: 输入文本
            
        Returns:
            TextStats: 统计结果
        """
        if not text or not text.strip():
            return TextStats(0, 0, 0, 0, 0, 0, 0.0, 0)
        
        # 字符数
        char_count = len(text)
        
        # 词数（中文按字符，英文按单词）
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
        english_words = len(re.findall(r'\b[a-zA-Z]+\b', text))
        word_count = chinese_chars + english_words
        
        # 段落数
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        paragraph_count = len(paragraphs)
        
        # 代码块数
        code_block_count = len(re.findall(r'```[\s\S]*?```', text))
        
        # 标题数
        heading_count = len(re.findall(r'^#{1,6}\s', text, re.MULTILINE))
        
        # 列表项数
        list_item_count = len(re.findall(r'^\s*[-*]\s', text, re.MULTILINE))
        
        # 平均段落长度
        if paragraph_count > 0:
            avg_paragraph_length = sum(len(p) for p in paragraphs) / paragraph_count
        else:
            avg_paragraph_length = 0.0
        
        # 可读性评分（简化版）
        readability_score = self._calculate_readability(
            char_count, word_count, paragraph_count, 
            code_block_count, heading_count
        )
        
        return TextStats(
            char_count=char_count,
            word_count=word_count,
            paragraph_count=paragraph_count,
            code_block_count=code_block_count,
            heading_count=heading_count,
            list_item_count=list_item_count,
            avg_paragraph_length=round(avg_paragraph_length, 1),
            readability_score=readability_score
        )
    
    def _calculate_readability(
        self, 
        char_count: int, 
        word_count: int, 
        paragraph_count: int,
        code_block_count: int,
        heading_count: int
    ) -> int:
        """
        计算可读性评分（0-100）
        
        评分标准：
        - 段落数量适中（+20）
        - 平均段落长度适中（+20）
        - 有代码示例（+20）
        - 有标题结构（+20）
        - 总字数适中（+20）
        """
        score = 0
        
        # 段落数量（3-20个）
        if 3 <= paragraph_count <= 20:
            score += 20
        elif paragraph_count > 0:
            score += 10
        
        # 平均段落长度（100-500字符）
        if paragraph_count > 0:
            avg_len = char_count / paragraph_count
            if 100 <= avg_len <= 500:
                score += 20
            elif 50 <= avg_len <= 800:
                score += 10
        
        # 代码示例
        if code_block_count >= 1:
            score += 20
        
        # 标题结构（至少3个标题）
        if heading_count >= 3:
            score += 20
        elif heading_count >= 1:
            score += 10
        
        # 总字数（1000-5000字）
        if 1000 <= word_count <= 5000:
            score += 20
        elif 500 <= word_count <= 8000:
            score += 10
        
        return min(score, 100)


def main():
    """命令行入口"""
    # 设置UTF-8输出
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    if len(sys.argv) < 2:
        print("用法: python text_analyzer.py <text> [--json]")
        print("")
        print("示例:")
        print("  python text_analyzer.py '文章内容'")
        print("  python text_analyzer.py '文章内容' --json")
        sys.exit(1)
    
    text = sys.argv[1]
    output_json = "--json" in sys.argv
    
    analyzer = TextAnalyzer()
    stats = analyzer.analyze(text)
    
    if output_json:
        result = {
            "success": True,
            "data": asdict(stats),
            "message": "分析完成"
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("=" * 60)
        print("文本分析报告")
        print("=" * 60)
        print(f"字符数: {stats.char_count}")
        print(f"词数: {stats.word_count}")
        print(f"段落数: {stats.paragraph_count}")
        print(f"代码块数: {stats.code_block_count}")
        print(f"标题数: {stats.heading_count}")
        print(f"列表项数: {stats.list_item_count}")
        print(f"平均段落长度: {stats.avg_paragraph_length} 字符")
        print(f"可读性评分: {stats.readability_score}/100")
        print("=" * 60)


if __name__ == "__main__":
    main()

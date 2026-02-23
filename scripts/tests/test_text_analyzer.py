#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文本分析器测试
"""

import sys
from pathlib import Path

# 添加父目录到路径
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.utils.text_analyzer import TextAnalyzer, TextStats


def test_empty_text():
    """测试空文本"""
    analyzer = TextAnalyzer()
    stats = analyzer.analyze("")
    
    assert stats.char_count == 0
    assert stats.word_count == 0
    assert stats.paragraph_count == 0
    print("✅ test_empty_text passed")


def test_simple_text():
    """测试简单文本"""
    analyzer = TextAnalyzer()
    text = "这是一段测试文本。\n\n这是第二段。"
    stats = analyzer.analyze(text)
    
    assert stats.char_count > 0
    assert stats.word_count > 0
    assert stats.paragraph_count == 2
    print("✅ test_simple_text passed")


def test_code_blocks():
    """测试代码块检测"""
    analyzer = TextAnalyzer()
    text = """
# 标题

这是正文。

```python
print("Hello")
```

更多内容。

```javascript
console.log("World");
```
"""
    stats = analyzer.analyze(text)
    
    assert stats.code_block_count == 2
    assert stats.heading_count >= 1
    print("✅ test_code_blocks passed")


def test_headings_and_lists():
    """测试标题和列表检测"""
    analyzer = TextAnalyzer()
    text = """
# 一级标题

## 二级标题

正文内容。

- 列表项1
- 列表项2
- 列表项3

### 三级标题

* 另一个列表
* 列表项
"""
    stats = analyzer.analyze(text)
    
    assert stats.heading_count >= 3
    assert stats.list_item_count >= 5
    print("✅ test_headings_and_lists passed")


def test_readability_score():
    """测试可读性评分"""
    analyzer = TextAnalyzer()
    
    # 好的文章：有代码、有标题、段落适中
    good_text = """
# Docker 教程

## 什么是 Docker

Docker 是一个容器化平台。

## 安装步骤

按照以下步骤安装：

- 步骤1
- 步骤2
- 步骤3

## 代码示例

```bash
docker run hello-world
```

## 总结

本文介绍了 Docker 的基础知识。
"""
    good_stats = analyzer.analyze(good_text)
    
    # 差的文章：没有代码、没有标题、内容太少
    bad_text = "这是一篇很短的文章。"
    bad_stats = analyzer.analyze(bad_text)
    
    assert good_stats.readability_score > bad_stats.readability_score
    print(f"✅ test_readability_score passed (good: {good_stats.readability_score}, bad: {bad_stats.readability_score})")


def test_chinese_and_english():
    """测试中英文混合"""
    analyzer = TextAnalyzer()
    text = "这是中文 this is English 混合文本。"
    stats = analyzer.analyze(text)
    
    # 应该统计中文字符和英文单词
    assert stats.word_count > 0
    print("✅ test_chinese_and_english passed")


def run_all_tests():
    """运行所有测试"""
    print("=" * 60)
    print("运行文本分析器测试")
    print("=" * 60)
    
    tests = [
        test_empty_text,
        test_simple_text,
        test_code_blocks,
        test_headings_and_lists,
        test_readability_score,
        test_chinese_and_english
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"❌ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"❌ {test.__name__} error: {e}")
            failed += 1
    
    print("=" * 60)
    print(f"测试结果: {passed} 通过, {failed} 失败")
    print("=" * 60)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

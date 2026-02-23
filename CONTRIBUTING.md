# 贡献指南

感谢你考虑为 Tech Blog Writer Skill 做出贡献！

## 🤝 如何贡献

### 报告 Bug

如果你发现了 bug，请创建一个 Issue 并包含以下信息：

1. **Bug 描述**：清晰简洁地描述问题
2. **复现步骤**：详细的复现步骤
3. **预期行为**：你期望发生什么
4. **实际行为**：实际发生了什么
5. **环境信息**：
   - OpenClaw 版本
   - Python 版本
   - 操作系统

### 提出新功能

如果你有新功能的想法，请创建一个 Issue 并包含：

1. **功能描述**：清晰描述新功能
2. **使用场景**：为什么需要这个功能
3. **实现建议**：如果有的话

### 提交代码

1. **Fork 本仓库**
   ```bash
   gh repo fork cloudzun/tech-blog-writer
   ```

2. **克隆你的 Fork**
   ```bash
   git clone https://github.com/你的用户名/tech-blog-writer.git
   cd tech-blog-writer
   ```

3. **创建特性分支**
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **进行更改**
   - 遵循代码规范（见下文）
   - 添加测试（如果适用）
   - 更新文档

5. **提交更改**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

6. **推送到你的 Fork**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **开启 Pull Request**
   - 在 GitHub 上创建 Pull Request
   - 填写 PR 模板
   - 等待 Review

---

## 📝 代码规范

### Python 代码规范

遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范：

```python
# ✅ 好的代码风格
def check_quality(content: str) -> QualityReport:
    """
    检测文章质量
    
    Args:
        content: 文章内容
    
    Returns:
        QualityReport: 质量报告
    """
    # 实现逻辑
    pass

# ❌ 差的代码风格
def checkQuality(content):
    # 没有类型提示
    # 没有 docstring
    pass
```

### 关键规范

1. **命名规范**
   - 函数/方法：`snake_case`
   - 类：`PascalCase`
   - 常量：`UPPER_CASE`
   - 私有方法：`_leading_underscore`

2. **注释规范**
   - 所有公共函数必须有 docstring
   - 复杂逻辑必须有行内注释
   - 注释使用中文

3. **类型提示**
   - 所有函数参数和返回值都要有类型提示
   - 使用 `from typing import` 导入类型

4. **错误处理**
   - 使用 try-except 捕获异常
   - 返回友好的错误信息
   - 不要吞掉异常

### 文档规范

1. **SKILL.md**
   - 使用清晰的章节结构
   - 提供具体的示例
   - 包含好/坏示例对比

2. **README.md**
   - 保持简洁明了
   - 包含快速开始指南
   - 提供完整的使用示例

3. **代码注释**
   - 解释"为什么"而不是"是什么"
   - 使用中文注释
   - 保持注释与代码同步

---

## 🧪 测试规范

### 运行测试

```bash
# 运行所有测试
python3 -m pytest

# 运行特定测试
python3 -m pytest scripts/tests/test_quality.py

# 运行测试并查看覆盖率
python3 -m pytest --cov=scripts
```

### 编写测试

```python
# scripts/tests/test_quality.py
import pytest
from scripts.core.quality_checker import QualityChecker

def test_quality_checker_basic():
    """测试基础功能"""
    checker = QualityChecker()
    result = checker.check("# 测试文章")
    
    assert result.success == True
    assert result.score >= 0
    assert result.score <= 100

def test_quality_checker_empty_input():
    """测试空输入"""
    checker = QualityChecker()
    result = checker.check("")
    
    assert result.success == False
    assert "为空" in result.message
```

---

## 📋 Commit 规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type 类型

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建/工具相关

### 示例

```
feat(quality): add SEO optimization check

- 新增 SEO 优化检测维度
- 检测标题长度、关键词密度
- 提供优化建议

Closes #123
```

---

## 🎯 开发流程

### 1. 本地开发

```bash
# 1. 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate  # Windows

# 2. 安装依赖（如果有）
pip install -r requirements.txt

# 3. 进行开发
# 编辑代码...

# 4. 测试
python3 scripts/quality_checker.py "测试内容"

# 5. 运行测试（如果有）
pytest
```

### 2. 代码 Review

所有 Pull Request 都需要经过 Review：

1. **自我检查清单**
   - [ ] 代码遵循规范
   - [ ] 添加了必要的注释
   - [ ] 更新了相关文档
   - [ ] 测试通过
   - [ ] 没有引入新的警告

2. **Review 关注点**
   - 代码质量
   - 性能影响
   - 安全问题
   - 文档完整性

---

## 🏆 贡献者

感谢所有贡献者！

<!-- 贡献者列表将自动生成 -->

---

## 📞 联系方式

如有问题，请通过以下方式联系：

- **GitHub Issues**: https://github.com/cloudzun/tech-blog-writer/issues
- **Email**: cloudzun@example.com
- **Blog**: https://blog.huaqloud.com

---

**再次感谢你的贡献！** 🎉

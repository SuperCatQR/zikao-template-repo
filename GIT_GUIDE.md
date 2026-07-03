# Git 提交规范（Conventional Commits）

遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范。

## 格式

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

## Type

- **feat**: 新功能
- **fix**: Bug 修复
- **docs**: 文档变更
- **style**: 格式调整（不影响代码逻辑）
- **refactor**: 重构（既不是新功能也不是 Bug 修复）
- **test**: 测试相关
- **chore**: 构建/工具/依赖变更

## Scope

模块或功能域，如：

- `courses`: 课程相关
- `majors`: 专业相关
- `scripts`: 脚本变更
- `ops`: 元文档变更
- `sources`: 原始资料变更

## 示例

```bash
feat(courses): 新增 12345 软件工程课程页
fix(scripts): 修复 URL 规范化尾随标点处理
docs(readme): 更新快速开始步骤
test(build): 补充 split_frontmatter 单元测试
chore(deps): 升级 pytest 到 7.4.3
```

## Breaking Changes

破坏性变更在 footer 添加 `BREAKING CHANGE:`：

```bash
refactor(scripts): 重构路径配置为 TOML

BREAKING CHANGE: 旧的 JSON 配置不再支持，需迁移到 build.toml
```

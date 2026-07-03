# 自考资料库 GitHub Template

通用自考资料库模板，支持任意省份快速启动。

## 特性

- 📁 **三分区架构**：`content/` (发布)、`sources/` (原始资料)、`ops/` (元文档)
- 🔧 **零依赖构建**：Python 标准库生成静态站点
- 🔗 **外链监控**：自动检测考纲/官方链接可用性
- 🧪 **测试覆盖**：pytest 单元测试
- 📦 **Git LFS**：大文件自动管理
- 🚀 **GitHub Actions**：自动部署 + 外链巡检

## 使用模板

1. 点击「Use this template」创建新仓库
2. 克隆到本地：`git clone https://github.com/{your-username}/{your-repo}.git`
3. 初始化省份：`python scripts/bootstrap-province.py guangdong`
4. 编辑 `content/{province}/` 下的课程和专业页
5. 构建站点：`python scripts/build-course-pages.py --base /{your-repo}/`

## 目录结构

```text
your-repo/
├── content/{province}/       # 发布内容
│   ├── courses/              # 课程 Markdown
│   ├── majors/               # 专业计划
│   └── index.md              # 省份首页
├── sources/{province}/       # 原始 PDF、OCR 产物
├── ops/{province}/           # 元文档、检查清单
├── scripts/                  # 构建/巡检脚本
│   ├── build-course-pages.py
│   ├── check-source-links.py
│   └── bootstrap-province.py
├── tests/                    # 单元测试
├── build.toml                # 路径配置
├── .env.example              # 环境变量示例
├── .gitattributes            # Git LFS 配置
└── .github/workflows/        # CI 流水线
```

## 快速开始

### 首次使用检查清单

- [ ] Python 3.8+ 已安装（`python --version`）
- [ ] Git 已安装（`git --version`）
- [ ] Git LFS 已安装（`git lfs version`）
- [ ] 仓库已从模板创建（而非 fork）
- [ ] 本地已克隆（`git clone`）

### 安装依赖

```bash
# 开发依赖（测试、代码检查）
pip install -r requirements-dev.txt

# Git LFS（首次使用）
git lfs install
git lfs pull  # 拉取大文件
```

### 新增省份

```bash
python scripts/bootstrap-province.py sichuan
# 生成 content/sichuan/、sources/sichuan/、ops/sichuan/ 骨架
```

### 构建站点

```bash
# 生产构建
python scripts/build-course-pages.py --base /{your-repo}/

# 本地预览
python scripts/build-course-pages.py --base /
# 浏览器打开 site/index.html
```

### 外链监控

```bash
# 快速统计
python scripts/check-source-links.py --offline

# 在线探测
python scripts/check-source-links.py
```

### 运行测试

```bash
pytest
```

## 配置

### build.toml

路径和监控配置，支持环境变量回退：

```toml
[paths]
courses_dir = "${ZIKAO_COURSES_DIR:content/{province}/courses}"
majors_dir  = "${ZIKAO_MAJORS_DIR:content/{province}/majors}"
out_dir     = "${ZIKAO_OUT_DIR:site}"
```

### .env（可选）

复制 `.env.example` 为 `.env` 并按需修改。

## Git LFS

PDF/压缩包自动走 LFS：

```bash
# 添加大文件
git add sources/jiangsu/some-file.pdf
git commit -m "feat(sources): 新增考纲 PDF"

# LFS 会自动处理，无需手动配置
```

## GitHub Actions

- **Pages 部署**：推送到 `main` 自动构建并发布
- **外链巡检**：每天定时检测外链可用性

启用方法：
1. 仓库 Settings → Pages → Source 选择 `GitHub Actions`
2. 推送时会自动触发 `.github/workflows/deploy.yml`

## 贡献指南

### 提交规范

遵循 Conventional Commits：

```bash
feat(courses): 新增 12345 课程页
fix(scripts): 修复 URL 规范化逻辑
docs(readme): 更新快速开始步骤
test(build): 补充 split_frontmatter 测试
```

### 课程页检查清单

发布前必过 `ops/{province}/course-review-checklist.md` 所有项。

## 常见问题

### 构建错误

**Q: `ModuleNotFoundError: No module named 'build_course_pages'`**

```bash
# 检查是否有 tests/conftest.py
ls tests/conftest.py

# 若无，从模板仓库复制
git checkout origin/main -- tests/conftest.py
```

**Q: 构建后 CSS 样式丢失**

```bash
# 检查 --base 参数是否正确
python scripts/build-course-pages.py --base /{your-repo}/

# 本地预览必须使用 --base /
python scripts/build-course-pages.py --base /
```

**Q: 中文路径乱码**

```bash
# Windows PowerShell 设置 UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001
```

### Git LFS 问题

**Q: 文件显示为指针而非实际内容**

```bash
git lfs pull
```

**Q: 推送时 LFS 配额不足**

```bash
# 检查 LFS 使用量
git lfs ls-files --size

# 清理历史大文件（需 BFG 或 git-filter-repo）
```

## 许可

MIT License

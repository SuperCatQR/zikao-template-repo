# 自考资料库规范模板

通用自考资料库**骨架**。约定目录、命名、版权边界和配置；**不内置**完整构建器（MkDocs / run-gates 请从 `jiangsu-zikao-aio` 复制）。

> 与公开主站 `jiangsu-zikao-aio` 的现行约定对齐（2026-07）：  
> 生产构建 = MkDocs；私仓引用 = `materials://`；状态 = `lifecycle` + `completeness`。

## 包含

| 路径 | 职责 |
|---|---|
| `content/` | 可公开发布的课程页、专业页、索引（示例省 `example`） |
| `sources/` | 原始资料分区：`public-official/` + `processed/` |
| `ops/` | 基线、审计、布局说明 |
| `build.toml` | 路径约定示例 |
| `.gitattributes` | 大文件 Git LFS 规则 |
| `.env.example` | 环境变量示例 |

## 使用

1. GitHub → `Use this template`。
2. 把 `example` 改成省份拼音（如 `jiangsu`）。
3. 课程页：`content/<province>/courses/<5位代码>/index.md`（frontmatter 含 `lifecycle` / `completeness`）。
4. 私有 PDF 只进 private materials 仓；公开仓只写 `materials://...`。

```bash
python -m pytest -q
```

## 路径约定

```text
content/<province>/courses/<code>/index.md
content/<province>/majors/<code>-<slug>/index.md
sources/<province>/public-official/{major-plans,policies,syllabi,textbooks}/
sources/<province>/processed/{major-source,syllabus,policies,source-records}/
ops/<province>/source-links.baseline.json
ops/<province>/sources-layout.md   # 可选，拷自 AIO
```

## 状态枚举（与 AIO 一致）

- **lifecycle:** `draft` → `machine_ready` → `in_review` → `publishable`
- **completeness:** `complete` | `metadata-only` | `missing-source` | `needs-review`

## 可选升级（从 jiangsu-zikao-aio 复制）

需要静态站点、分层闸门、GitHub Actions 时，从 AIO 复制：

- `mkdocs.yml`、`.github/workflows/deploy-pages.yml`
- `scripts/run-gates.py`、`scripts/lib/`、`scripts/check-source-links.py`
- `ops/jiangsu/course-status.md`、`schemas/course.schema.json`

本模板**不假装**自带生产构建器。

## 许可

MIT License

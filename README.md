# 自考资料库规范模板

通用自考资料库骨架。它只约定目录、命名、版权边界和配置；不内置构建器或巡检器。

## 包含

- `content/`：可公开发布的课程页、专业页、索引。
- `sources/`：原始资料分区；仅放可公开保存的来源副本。
- `ops/`：基线、审计、运维记录。
- `build.toml`：路径约定示例，默认使用 `example` 省份。
- `.gitattributes`：为大文件预留 Git LFS 规则。
- `.env.example`：环境变量示例。

## 使用

1. 在 GitHub 点 `Use this template`。
2. 把 `example` 改成省份拼音，如 `jiangsu`。
3. 按 `content/<province>/courses/<code>/index.md` 填课程。
4. 私有 PDF、教材、真题原件只放私仓；公开仓只写 `materials://...` 引用。

```bash
python -m pytest -q
```

## 路径约定

```text
content/<province>/courses/<course-code>/index.md
content/<province>/majors/<major-code>/index.md
sources/<province>/official/
ops/<province>/source-links.baseline.json
```

## 可选升级

需要静态站点生成、外链巡检、GitHub Actions 时，从实际项目复制脚本和 workflow；本模板不假装提供。

## 许可

MIT License

# GIBI-LAB website

Quarto 学术静态网站，使用 GitHub Actions 构建并部署到 GitHub Pages。

网站地址：https://gibi-lab.github.io/

## 日常维护

| 内容 | 修改文件 |
| --- | --- |
| 课题组简介、所属机构、联系信息 | `content/about.md` |
| 研究方向与项目 | `content/research.md` |
| 负责人、成员、校友 | `content/people.md` |
| 论文列表 | `content/publications.md` |
| 新闻动态（最新在前） | `content/news.md` |
| 导航、站名、网址与页脚 | `_quarto.yml` |
| 配色和布局 | `styles.css` |

可以在 GitHub 中直接编辑 Markdown 并提交；推送到 main 后自动发布。建议用 Pull Request 审阅内容，PR 会构建与检查链接但不会部署。

所有未知资料均明确标为待补充。上线真实内容时替换对应占位文本，并在 `_quarto.yml` 更新描述和页脚的筹备状态。不要填写未核实的成果、人物或机构。论文格式见文件中的注释，照片需确认使用权。

## 本地预览

安装 Quarto 1.10.19：https://quarto.org/docs/get-started/

```sh
python3 scripts/prepare_assets.py
quarto preview
```

仅中文构建和检查（完整双语预览见文末）：

```sh
python3 scripts/prepare_assets.py
quarto render
quarto render en
python3 scripts/assemble_languages.py
python3 scripts/check_links.py
```

无需 R、Jupyter、Node 或额外 Python 包。生成目录 `_site/` 不提交。

## 部署配置

仓库 Settings → Pages → Source 选择 **GitHub Actions**。工作流使用 GitHub 自带 GITHUB_TOKEN 和 OIDC，无需保存个人令牌。部署环境为 github-pages。

推送 main 或在 Actions 手动运行 Build and deploy website；成功后访问网站。部署失败可在 Actions 中检查日志；组织策略可能限制 Actions 或 Pages。回滚可 revert 对应提交，重新自动部署。

## 设计与素材

参考 https://horizon-lab.org/ 的简洁学术信息结构，页面与样式独立实现。未复制对方文字、图片、标识或样式文件。本站使用系统字体，无外部字体或图片请求。GIBI LAB 暂用组织名称展示，正式名称待确认。

## 便捷更新与质量检查

每页底部有“编辑本页内容”入口，直接打开对应 Markdown；首页入口编辑课题组简介。完整布局仍在对应 `.qmd` 文件中。无写入权限的用户可通过“反馈问题”提交内容更新表单，经维护者核实后再合并。

网站提供自定义 404 页面、站内搜索、分享元数据和临时 G 字母图标（并非正式课题组标识）。布局支持窄屏、减少动态效果偏好及打印样式。

每次构建检查内部页面、资源、锚点、页面标题、语言设置和图片 alt 属性；检查失败将阻止部署。外部链接不在此检查范围内。内容是否真实仍需人工核实。

## 中英双语与导航

中文顶部为项目（空间影像 / 色彩科学 / 影像评测）、团队成员、研究方向、学术成果、介绍；英文站对应 Project、People、Research、Publication、About。点击站名返回首页，News 保留在首页入口。

中文源文件位于根目录和 `content/`；英文源文件位于 `en/` 和 `en/content/`。三个项目文件分别是 `spatial-imaging`、`color-science`、`imaging-evaluation`，介绍页为 `about.qmd`。更新真实资料时请同步两种语言。

完整双语构建：

```sh
python3 scripts/prepare_assets.py
quarto render
quarto render en
python3 scripts/assemble_languages.py
python3 scripts/check_links.py
python3 -m http.server 8000 --directory _site
```

浏览 http://localhost:8000。两种语言分别构建搜索索引，切换链接在构建时配对当前页面，无需 JavaScript。新增页面须同时创建中文和英文版本；缺少翻译页会阻止发布。两种语言共用根目录 `styles.css`，自动复制的样式文件无需手工编辑。

## 当前视觉风格

当前采用 al-folio 风格的独立 Quarto 实现：白底、紫色链接、轻量标题、简介与抽象示意图并列、动态 / 项目 / 学术成果分区。并非安装 Jekyll 的 al-folio 主题；原有双语构建和内容文件保持可用。参考：https://alshedivat.github.io/al-folio/ 。没有复制对方照片、示例论文或代码，抽象插图为本站原创 SVG，并明确标注为非实验数据。

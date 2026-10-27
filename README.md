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
quarto preview
```

构建和检查：

```sh
quarto render
python3 scripts/check_links.py
```

无需 R、Jupyter、Node 或额外 Python 包。生成目录 `_site/` 不提交。

## 部署配置

仓库 Settings → Pages → Source 选择 **GitHub Actions**。工作流使用 GitHub 自带 GITHUB_TOKEN 和 OIDC，无需保存个人令牌。部署环境为 github-pages。

推送 main 或在 Actions 手动运行 Build and deploy website；成功后访问网站。部署失败可在 Actions 中检查日志；组织策略可能限制 Actions 或 Pages。回滚可 revert 对应提交，重新自动部署。

## 设计与素材

参考 https://horizon-lab.org/ 的简洁学术信息结构，页面与样式独立实现。未复制对方文字、图片、标识或样式文件。本站使用系统字体，无外部字体或图片请求。GIBI LAB 暂用组织名称展示，正式名称待确认。

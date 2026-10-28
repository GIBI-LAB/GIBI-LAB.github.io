"""Combine two static Quarto sites and pair language links without JavaScript."""
from pathlib import Path
import re
import shutil

root = Path('_site')
shutil.copytree('en/_site', root / 'en', dirs_exist_ok=True)
for page in root.glob('*.html'):
    translated = root / 'en' / page.name
    if not translated.exists():
        raise SystemExit(f'Missing English page for {page.name}')
    for target, english in [(page, False), (translated, True)]:
        html = target.read_text()
        destination = ('/' if english else '/en/') + page.name
        label = '中文' if english else 'English'
        count = [0]
        def replace_link(match):
            anchor = match.group()
            text = re.sub(r'<[^>]*>', '', anchor).strip()
            if text != label:
                return anchor
            count[0] += 1
            anchor = re.sub(r'href="[^"]*"', f'href="{destination}"', anchor)
            return anchor.replace('<a ', '<a hreflang="'+('zh-CN' if english else 'en')+'" lang="'+('zh-CN' if english else 'en')+'" ', 1)
        html = re.sub(r'<a\b[^>]*>.*?</a>', replace_link, html, flags=re.S)
        if count[0] != 1:
            raise SystemExit(f'Expected one language switch on {target}, found {count[0]}')
        alternates = '\n'.join(f'<link rel="alternate" hreflang="{lang}" href="https://gibi-lab.github.io{prefix}{page.name}">' for lang,prefix in [('zh-CN','/'),('en','/en/'),('x-default','/')])
        html = html.replace('</head>', alternates+'\n</head>')
        target.write_text(html)
print('Assembled bilingual pages with matching language links.')

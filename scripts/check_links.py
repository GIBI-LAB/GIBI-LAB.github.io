"""Check generated local links and assets without extra dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
root = Path('_site').resolve()
errors = []
class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key not in ('href', 'src') or not value:
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (root / unquote(url.path).lstrip('/') if url.path.startswith('/') else self.page.parent / unquote(url.path))
            if not target.exists():
                errors.append(f'{self.page.relative_to(root)}: {value}')
pages = list(root.rglob('*.html'))
assert pages, 'No rendered pages found'
for page in pages:
    parser = Links()
    parser.page = page
    parser.feed(page.read_text())
if errors:
    raise SystemExit('Broken links:\n' + '\n'.join(errors))
print(f'Checked local links and assets in {len(pages)} HTML pages.')

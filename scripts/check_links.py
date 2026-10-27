"""Validate generated pages, local resources, anchors and basic accessibility."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

root = Path('_site').resolve()
errors = []

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links = path, set(), []
        self.lang = self.in_title = False
        self.title = ''

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'html':
            self.lang = bool(attrs.get('lang'))
        if tag == 'title':
            self.in_title = True
        if tag == 'img' and 'alt' not in attrs:
            errors.append(f'{self.path.name}: image missing alt: {attrs.get("src")}')
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data

pages = {}
for path in root.rglob('*.html'):
    page = Page(path)
    page.feed(path.read_text())
    pages[path.resolve()] = page
assert pages, 'No rendered pages found'
for path, page in pages.items():
    if not page.lang or not page.title.strip():
        errors.append(f'{path.name}: missing page title or language')
    for value in page.links:
        url = urlsplit(value)
        if url.scheme or url.netloc:
            continue
        if not url.path:
            target = path
        elif url.path.startswith('/'):
            target = root / unquote(url.path).lstrip('/')
        else:
            target = path.parent / unquote(url.path)
        target = target.resolve()
        if target.is_dir():
            target /= 'index.html'
        if not target.is_relative_to(root) or not target.exists():
            errors.append(f'{path.name}: missing local target {value}')
        elif url.fragment and target in pages:
            fragment = unquote(url.fragment)
            if fragment not in pages[target].ids and not fragment.startswith(':~:text='):
                errors.append(f'{path.name}: missing anchor {value}')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'Validated links, anchors, titles, language and image alt attributes in {len(pages)} pages.')

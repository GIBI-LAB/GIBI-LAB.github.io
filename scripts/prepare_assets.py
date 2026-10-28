from pathlib import Path
import shutil
for folder in [Path('assets'), Path('en/assets')]:
    folder.mkdir(parents=True, exist_ok=True)
    shutil.copyfile('styles.css', folder / 'styles.css')

from pathlib import Path
import shutil
for folder in [Path('assets'), Path('en/assets')]:
    folder.mkdir(parents=True, exist_ok=True)
    shutil.copyfile('styles.css', folder / 'styles.css')
shutil.copyfile('assets/favicon.svg', 'en/assets/favicon.svg')
shutil.copyfile('assets/lab-study.svg', 'en/assets/lab-study.svg')

# Keep the original font available to both language sites.
shutil.copytree('assets/fonts', 'en/assets/fonts', dirs_exist_ok=True)

import os
import glob

html_files = glob.glob('/Users/pol/Desktop/espai-vall-roure/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # If not already present
    if "apple-touch-icon" not in content:
        # insert right after <head> or right after <link rel="icon"...
        if '<link rel="icon"' in content:
            content = content.replace(
                '<link rel="icon" type="image/png" href="img/logopol (1).png">',
                '<link rel="icon" type="image/png" href="img/logopol (1).png">\n    <link rel="apple-touch-icon" href="img/logopol (1).png">'
            )
        else:
            content = content.replace('<head>', '<head>\n    <link rel="apple-touch-icon" href="img/logopol (1).png">')
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print(f"Updated {len(html_files)} HTML files with apple-touch-icon.")

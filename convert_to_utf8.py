import os
import glob

directory = r"d:\محمود منصور"
extensions = ["*.html", "*.js", "*.css"]

for ext in extensions:
    for filepath in glob.glob(os.path.join(directory, ext)):
        content = None
        encoding_used = None
        for enc in ['utf-8', 'utf-16', 'windows-1256']:
            try:
                with open(filepath, 'r', encoding=enc) as f:
                    content = f.read()
                encoding_used = enc
                break
            except UnicodeDecodeError:
                pass
        
        if content is not None and encoding_used != 'utf-8':
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Converted {os.path.basename(filepath)} from {encoding_used} to utf-8")

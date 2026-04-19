import os
import re

def change_cases(text):
    # gold -> gold
    text = re.sub(r'gold', 'gold', text)
    text = re.sub(r'Gold', 'Gold', text)
    text = re.sub(r'GOLD', 'GOLD', text)
    return text

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = change_cases(content)
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except Exception as e:
        # Some files might be binary or not utf-8
        pass

def main(root_dir):
    # First, replace content in all files
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        if '__pycache__' in dirs:
            dirs.remove('__pycache__')
        if 'venv' in dirs:
            dirs.remove('venv')
            
        for file in files:
            file_path = os.path.join(root, file)
            # Skip some extensions if needed, but doing generic try-except is fine
            process_file(file_path)

    # Note: renames of files and directories can be tricky on Windows if we modify paths mid-walk.
    # It's safer to do bottoms-up walk or separate pass.
    # Let's do a bottom-up walk for renaming files and directories
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for file in files:
            if 'gold' in file.lower():
                old_path = os.path.join(root, file)
                new_file = change_cases(file)
                new_path = os.path.join(root, new_file)
                os.rename(old_path, new_path)
                
        for d in dirs:
            if '.git' == d or '__pycache__' == d or 'venv' == d:
                continue
            if 'gold' in d.lower():
                old_path = os.path.join(root, d)
                new_d = change_cases(d)
                new_path = os.path.join(root, new_d)
                os.rename(old_path, new_path)

if __name__ == '__main__':
    # target workspace
    main(r'c:\Users\calcu\Desktop\ideas\test-gold\gold')

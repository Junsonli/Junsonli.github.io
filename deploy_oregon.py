# -*- coding: utf-8 -*-
import os, shutil, re

# 1. Delete old article and related files
base = r'd:\Junsonli.github.io'
old_post = os.path.join(base, r'_posts\2026-03-07-r6s-oregon-level-design.md')
old_img_dir = os.path.join(base, r'assets\img\posts\r6s-oregon')

if os.path.exists(old_post):
    os.remove(old_post)
    print('Deleted old post')
if os.path.exists(old_img_dir):
    shutil.rmtree(old_img_dir)
    print('Deleted old img dir')

# 2. Find source folder
src_base = r'C:\Users\Administrator\Downloads'
src_folder = None
for name in os.listdir(src_base):
    path = os.path.join(src_base, name)
    if os.path.isdir(path) and ('关卡' in name or '俄勒冈' in name or 'Oregon' in name):
        src_folder = path
        break

if not src_folder:
    print('Source folder not found')
    exit(1)

print(f'Source folder: {src_folder}')

# 3. Create new img dir
new_img_dir = os.path.join(base, r'assets\img\posts\r6s-oregon')
os.makedirs(new_img_dir, exist_ok=True)

# 4. Copy images with simple names
img_map = {}
src_img_dir = os.path.join(src_folder, 'images')
if os.path.exists(src_img_dir):
    img_files = sorted([f for f in os.listdir(src_img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])
    for i, fname in enumerate(img_files, 1):
        ext = os.path.splitext(fname)[1].lower()
        new_name = f'image{i}{ext}'
        shutil.copy2(os.path.join(src_img_dir, fname), os.path.join(new_img_dir, new_name))
        img_map[fname] = f'/assets/img/posts/r6s-oregon/{new_name}'
        print(f'Copied image: {fname} -> {new_name}')

# 5. Copy attachment
attach_map = {}
src_files_dir = os.path.join(src_folder, 'files')
if os.path.exists(src_files_dir):
    for fname in os.listdir(src_files_dir):
        src_path = os.path.join(src_files_dir, fname)
        if fname.endswith('.skp'):
            new_name = 'lpj-map.skp'
            dst = os.path.join(base, r'assets\attachments', new_name)
            shutil.copy2(src_path, dst)
            attach_map[fname] = f'/assets/attachments/{new_name}'
            print(f'Copied attachment: {fname} -> {new_name}')

# 6. Read markdown
md_file = None
for f in os.listdir(src_folder):
    if f.endswith('.md'):
        md_file = os.path.join(src_folder, f)
        break

with open(md_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 7. Replace image paths
for old_name, new_path in img_map.items():
    content = re.sub(
        r'!\[([^\]]*)\]\(<images/' + re.escape(old_name) + r'>\)',
        r'![\1](' + new_path + ')',
        content
    )
    content = re.sub(
        r'!\[([^\]]*)\]\(images/' + re.escape(old_name) + r'\)',
        r'![\1](' + new_path + ')',
        content
    )

# 8. Replace attachment paths
for old_name, new_path in attach_map.items():
    content = re.sub(
        r'\[([^\]]*)\]\(<files/' + re.escape(old_name) + r'>\)',
        r'[📎 \1](' + new_path + ')',
        content
    )
    content = re.sub(
        r'\[([^\]]*)\]\(files/' + re.escape(old_name) + r'\)',
        r'[📎 \1](' + new_path + ')',
        content
    )

# 9. Add front matter
front_matter = '---\nlayout: post\ntitle: "【关卡设计研究】「俄勒冈乡间屋宅」拆解与《彩虹六号：围攻》关卡设计范式讨论"\ndate: 2026-03-07\nimage: \'/assets/img/posts/r6s-oregon/image1.png\'\ndescription: \'基于《彩虹六号：围攻》「俄勒冈乡间屋宅」的深度关卡拆解，从动线、阻塞点、区域划分、掩体枪线到可破坏玩法，系统梳理R6S的关卡设计范式与战术博弈逻辑。\'\ntags:\n- 关卡设计\ncategories:\n- 星跃实战营\n---\n\n'

# 10. Convert heading 1 to heading 2 for main title if present
lines = content.split('\n')
if lines and lines[0].startswith('# '):
    lines[0] = '##' + lines[0][1:]
content = '\n'.join(lines)

final_content = front_matter + content

output_path = os.path.join(base, r'_posts\2026-03-07-r6s-oregon-level-design.md')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print(f'Wrote post to {output_path}')

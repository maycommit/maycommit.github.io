#!/usr/bin/env python3
"""Scans posts/ directory and generates posts.json index."""
import json, os, re

posts = []
for f in sorted(os.listdir('posts'), reverse=True):
    if not f.endswith('.md'):
        continue
    with open(os.path.join('posts', f)) as fh:
        content = fh.read()
    # Parse front matter
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    meta = {}
    if m:
        for line in m.group(1).split('\n'):
            i = line.find(':')
            if i > 0:
                meta[line[:i].strip()] = line[i+1:].strip()
    # Fallback: extract date from filename YYYY-MM-DD-slug.md
    date_match = re.match(r'(\d{4}-\d{2}-\d{2})', f)
    date = meta.get('date', date_match.group(1) if date_match else '')
    title = meta.get('title', f.replace('.md', ''))
    posts.append({'file': f, 'title': title, 'date': date})

# Sort by date descending
posts.sort(key=lambda p: p['date'], reverse=True)

with open('posts.json', 'w') as fh:
    json.dump(posts, fh, ensure_ascii=False, indent=2)

print(f'Generated posts.json with {len(posts)} posts')

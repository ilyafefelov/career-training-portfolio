#!/usr/bin/env python3
import re, sys

PATH = 'projects/final-project/html_board/index.html'
try:
    s = open(PATH, encoding='utf-8').read()
except Exception as e:
    print('ERROR_READING_FILE', PATH, e)
    sys.exit(2)

def extract_tag_block(s, start_token, open_tag, close_tag):
    start = s.find(start_token)
    if start == -1:
        return None
    i = start
    cnt = 0
    j = i
    while j < len(s):
        if s.startswith(open_tag, j):
            cnt += 1
            j += len(open_tag)
        elif s.startswith(close_tag, j):
            cnt -= 1
            j += len(close_tag)
            if cnt == 0:
                return s[start:j]
        else:
            j += 1
    return None

# extract board block
board_block = extract_tag_block(s, '<div class="board">', '<div', '</div>')
if board_block is None:
    print('BOARD_MISSING')
    sys.exit(3)

# extract columns inside board
cols = []
pos = 0
while True:
    m = board_block.find('<div class="col', pos)
    if m == -1:
        break
    # find the full column block
    i = m
    cnt = 0
    j = i
    while j < len(board_block):
        if board_block.startswith('<div', j):
            cnt += 1
            j += 4
        elif board_block.startswith('</div>', j):
            cnt -= 1
            j += 6
            if cnt == 0:
                cols.append(board_block[i:j])
                pos = j
                break
        else:
            j += 1
    else:
        break

results = []
for col in cols:
    title_m = re.search(r'<div class="col-title">\s*([^<]+?)\s*</div>', col, flags=re.I)
    title = title_m.group(1).strip() if title_m else ''
    sticky_count = len(re.findall(r'<div[^>]*class=["\'][^"\']*sticky', col, flags=re.I))
    results.append((title, sticky_count))

# milestones section
mil_block = extract_tag_block(s, '<section class="milestones"', '<section', '</section>')
mil_present = mil_block is not None
mil_count = 0
if mil_present:
    mil_count = len(re.findall(r'<div[^>]*class=["\'][^"\']*sticky', mil_block, flags=re.I))

targets = {
    'Appreciation': ['Appreciation', 'Подяки', 'Дякуємо'],
    'Continue': ['Continue', 'Continue Doing', 'Продовжувати'],
    'Stop': ['Stop', 'Stop Doing', 'Припинити'],
    'Start': ['Start', 'Start Doing', 'Почати'],
    'Actions': ['Actions', 'Дії'],
    'Milestones': ['Проміжні цілі', 'Проміжні цілі на 6-12 місяців', 'Milestones']
}

out = {}
for key, variants in targets.items():
    found = False
    count = 0
    if key == 'Milestones':
        if mil_present:
            found = True
            count = mil_count
    else:
        for t, c in results:
            for v in variants:
                if v.lower() in t.lower():
                    found = True
                    count = c
                    break
            if found:
                break
    out[key] = (found, count)

for k, (found, count) in out.items():
    print(f"{k}: {'present' if found else 'missing'}; sticky_count={count}")

print('---columns---')
for t, c in results:
    print(f"{t}: {c}")

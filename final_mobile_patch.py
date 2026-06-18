import os

files = ['landing_page.html', 'elearning.html', 'akun.html', 'asrama.html', 'bimbingan.html', 'nilai.html', 'pembayaran.html', 'presensi.html', 'index.html', 'login.html']

for f in files:
    filepath = os.path.join(os.getcwd(), f)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. Prevent zoom on focus in mobile
    content = content.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">'
    )

    # 2. Add overflow-x: hidden to .page on mobile to strictly prevent horizontal scrolling
    if '.page { padding: 16px;' in content and 'overflow-x: hidden' not in content.split('.page { padding: 16px;')[1][:20]:
        content = content.replace(
            '.page { padding: 16px; }',
            '.page { padding: 16px; overflow-x: hidden !important; width: 100% !important; }'
        )

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Final patched {f}')


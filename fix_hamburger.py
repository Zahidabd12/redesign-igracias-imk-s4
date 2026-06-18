import os

files = ['landing_page.html', 'elearning.html', 'akun.html', 'asrama.html', 'bimbingan.html', 'nilai.html', 'pembayaran.html', 'presensi.html']

for f in files:
    filepath = os.path.join(os.getcwd(), f)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Check if the HTML button is actually missing
    if '<button class="mobile-menu-btn' not in content:
        content = content.replace('<div class="header-left">', '<div class="header-left">\n                <button class="mobile-menu-btn icon-btn" onclick="toggleSidebar()">\n                    <i class="fa-solid fa-bars"></i>\n                </button>')

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Fixed {f}')

import os
import re

files = ['landing_page.html', 'elearning.html', 'akun.html', 'asrama.html', 'bimbingan.html', 'nilai.html', 'pembayaran.html', 'presensi.html']

css_addition = """
        /* ===== MOBILE SIDEBAR ===== */
        .mobile-overlay {
            display: none; position: fixed; inset: 0;
            background: rgba(0,0,0,.5); z-index: 40;
            opacity: 0; transition: opacity .3s;
        }
        .mobile-overlay.show { display: block; opacity: 1; }
        .mobile-menu-btn { display: none; margin-right: 12px; font-size: 18px; color: var(--text); }
        
        @media (max-width: 900px) {
            .mobile-menu-btn { display: block; }
            .sidebar {
                position: fixed; top: 0; left: 0; height: 100vh;
                transform: translateX(-100%); z-index: 50;
                box-shadow: var(--shadow-xl); transition: transform 0.3s ease;
                display: flex !important;
            }
            .sidebar.show { transform: translateX(0); }
        }
"""

js_func = """function toggleSidebar() {
            document.getElementById('sidebar').classList.toggle('show');
            document.getElementById('mobile-overlay').classList.toggle('show');
        }

        function toggleDark() {"""

for f in files:
    filepath = os.path.join(os.getcwd(), f)
    if not os.path.exists(filepath):
        print(f"Skipping {f}, not found.")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. CSS
    if '.mobile-overlay {' not in content:
        content = content.replace('</style>', css_addition + '    </style>')

    # 2. Sidebar display:none removal
    content = re.sub(r'\.sidebar\s*\{\s*display:\s*none;\s*\}', '', content)

    # 3. HTML Overlay
    if 'id="mobile-overlay"' not in content:
        content = content.replace('<aside class="sidebar">', '<div class="mobile-overlay" id="mobile-overlay" onclick="toggleSidebar()"></div>\n    <aside class="sidebar" id="sidebar">')

    # 4. Header Hamburger
    if 'mobile-menu-btn' not in content:
        content = content.replace('<div class="header-left">', '<div class="header-left">\n                <button class="mobile-menu-btn icon-btn" onclick="toggleSidebar()">\n                    <i class="fa-solid fa-bars"></i>\n                </button>')

    # 5. JS Function
    if 'function toggleSidebar()' not in content:
        content = content.replace('function toggleDark() {', js_func)

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated {f}')


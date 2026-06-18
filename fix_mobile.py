import os

files = ['landing_page.html', 'elearning.html', 'akun.html', 'asrama.html', 'bimbingan.html', 'nilai.html', 'pembayaran.html', 'presensi.html', 'index.html']

css_addition = """
        /* ===== SMARTPHONE RESPONSIVE FIX ===== */
        @media (max-width: 600px) {
            table, .table-wrap, .table-container, .history-table {
                display: block !important;
                width: 100% !important;
                overflow-x: auto !important;
                white-space: nowrap !important;
                -webkit-overflow-scrolling: touch;
            }
            
            .header { padding: 0 16px; }
            .search-input { width: 130px !important; font-size: 12px; }
            .term-pill { display: none !important; }
            .header-profile span { display: none !important; }
            
            .page { padding: 16px; }

            .stats-grid, .facility-grid, .course-grid, .content-grid, .news-grid, .page-grid, .grid-1-3, .grid-2-3 { grid-template-columns: 1fr !important; display: grid !important; }
            .profile-banner { flex-direction: column !important; text-align: center; height: auto !important; padding: 20px !important; }
            .profile-avatar { margin-bottom: 12px; }
            .banner-inner { flex-direction: column; }
            .banner-left { margin-bottom: 20px; }
        }
"""

for f in files:
    filepath = os.path.join(os.getcwd(), f)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Prevent double injection
    if 'SMARTPHONE RESPONSIVE FIX' not in content:
        content = content.replace('</style>', css_addition + '    </style>')

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Fixed {f}')

import os
import re

files = ['landing_page.html', 'elearning.html', 'akun.html', 'asrama.html', 'bimbingan.html', 'nilai.html', 'pembayaran.html', 'presensi.html', 'index.html', 'login.html']

extra_css = """
        /* ===== SURGICAL MOBILE FIXES ===== */
        @media (max-width: 600px) {
            /* Bimbingan Timeline Fix */
            .timeline-top { flex-direction: column; align-items: flex-start !important; gap: 6px !important; }
            .timeline-date { white-space: normal !important; }
            .timeline-card { width: 100% !important; min-width: 0 !important; box-sizing: border-box !important; }
            .timeline-item { gap: 12px !important; }
            
            /* Presensi Scanner Overlap Fix */
            .scanner-panel { position: static !important; height: auto !important; padding: 16px !important; }
            .camera-box { height: 200px !important; margin-bottom: 10px; }
            .attendance-ring-wrap { padding: 10px 0 !important; margin-bottom: 10px !important; }
            
            /* Asrama Header Title Fix */
            .header-left .page-title { font-size: 13px !important; white-space: normal !important; line-height: 1.3 !important; }
            
            /* Fix Nilai Table padding */
            table { white-space: nowrap; }
        }
"""

for f in files:
    filepath = os.path.join(os.getcwd(), f)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # 1. Remove the bad table !important block that breaks table layout and JS toggling
    content = re.sub(r'table,\s*\.table-wrap,\s*\.table-container,\s*\.history-table\s*\{[^}]+\}', '/* Removed bad table block */', content)

    # 2. Wrap tables with responsive div if not already wrapped
    if 'class="table-responsive"' not in content:
        content = re.sub(r'(<table[^>]*>)', r'<div class="table-responsive" style="overflow-x: auto; width: 100%; -webkit-overflow-scrolling: touch; padding-bottom: 8px;">\n\1', content)
        content = content.replace('</table>', '</table>\n</div>')

    # 3. Add the extra surgical CSS
    if 'SURGICAL MOBILE FIXES' not in content:
        content = content.replace('</style>', extra_css + '    </style>')

    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Surgically fixed {f}')


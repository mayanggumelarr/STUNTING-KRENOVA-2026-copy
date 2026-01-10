import sqlite3
import hashlib

def init_database():
    """
    Membuat database krenova_data.db dengan struktur tabel yang diperlukan
    dan menambahkan user default (admin dan user biasa)
    """
    conn = sqlite3.connect('krenova_data.db')
    c = conn.cursor()
    
    # Tabel Users
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  role TEXT NOT NULL,
                  nama_lengkap TEXT)''')
    
    # Tabel Measurements
    c.execute('''CREATE TABLE IF NOT EXISTS measurements
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  tanggal_pengukuran DATE,
                  nama_anak TEXT,
                  usia_bulan INTEGER,
                  gender TEXT,
                  alamat TEXT,
                  berat_badan REAL,
                  tinggi_badan REAL,
                  lingkar_kepala REAL,
                  wfa_zscore REAL,
                  wfa_status TEXT,
                  hfa_zscore REAL,
                  hfa_status TEXT,
                  wfh_zscore REAL,
                  wfh_status TEXT,
                  hcfa_zscore REAL,
                  hcfa_status TEXT,
                  risiko_stunting_persen INTEGER,
                  status_stunting TEXT,
                  created_by TEXT,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Insert default admin jika belum ada
    c.execute("SELECT * FROM users WHERE username='tumbuh'")
    if not c.fetchone():
        admin_pass = hashlib.sha256('12345'.encode()).hexdigest()
        c.execute("INSERT INTO users (username, password, role, nama_lengkap) VALUES (?, ?, ?, ?)",
                  ('tumbuh', admin_pass, 'admin', 'Administrator'))
        print("✓ User admin 'tumbuh' berhasil dibuat")
    else:
        print("ℹ User admin 'tumbuh' sudah ada")
    
    # Insert default user jika belum ada
    c.execute("SELECT * FROM users WHERE username='user'")
    if not c.fetchone():
        user_pass = hashlib.sha256('user123'.encode()).hexdigest()
        c.execute("INSERT INTO users (username, password, role, nama_lengkap) VALUES (?, ?, ?, ?)",
                  ('user', user_pass, 'user', 'User Biasa'))
        print("✓ User biasa 'user' berhasil dibuat")
    else:
        print("ℹ User biasa 'user' sudah ada")
    
    conn.commit()
    conn.close()
    print("\n✓ Database 'krenova_data.db' berhasil dibuat!")
    print("\nInformasi Login:")
    print("=" * 40)
    print("Admin:")
    print("  Username: tumbuh")
    print("  Password: 12345")
    print("\nUser Biasa:")
    print("  Username: user")
    print("  Password: user123")
    print("=" * 40)

if __name__ == "__main__":
    print("Membuat database krenova_data.db...\n")
    init_database()
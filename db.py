import sqlite3

DB_PATH = "sports.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS classifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pdf_path TEXT,
        extracted_text TEXT,
        category TEXT,
        analysis TEXT
    );
    """)

    conn.commit()
    conn.close()


def save_classification(pdf_path, extracted_text, category, analysis):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO classifications (pdf_path, extracted_text, category, analysis)
        VALUES (?, ?, ?, ?)
    """, (pdf_path, extracted_text, category, analysis))

    conn.commit()
    conn.close()

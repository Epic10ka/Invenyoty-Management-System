import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "inventory.db"


def get_connection():

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # allows accessing columns by name
    return conn



def create_table():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS items (
                idn TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                batch TEXT,
                status TEXT NOT NULL
            )
        """)

#CRUD
def insert_item(item):

    # OBS: '?' works as placeholder

    with get_connection() as conn:
        conn.execute(
            "INSERT INTO items (idn, name, batch, status) VALUES (?, ?, ?, ?)",
            (item.id_number, item.name, item.batch, item.status)
        )


def get_all_items():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM items").fetchall()
        return rows  # # each row is accessible as row['name'], row['idn']


def get_item_by_id(idn):
    with get_connection() as conn:
        row = conn.execute("SELECT * FROM items WHERE idn = ?", (idn,)).fetchone()
        return row


def update_item(item):
    with get_connection() as conn:
        conn.execute(
            "UPDATE items SET name = ?, batch = ?, status = ? WHERE idn = ?",
            (item.name, item.batch, item.status, item.id_number)
        )


def delete_item(idn):
    with get_connection() as conn:
        conn.execute("DELETE FROM items WHERE idn = ?", (idn,))


def search_items(termo):
    with get_connection() as conn:
        termo_like = f"%{termo}%"
        rows = conn.execute(
            "SELECT * FROM items WHERE name LIKE ? OR idn LIKE ? OR batch LIKE ?",
            (termo_like, termo_like, termo_like)
        ).fetchall()
        return rows
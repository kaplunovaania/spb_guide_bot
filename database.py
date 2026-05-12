import aiosqlite
import os

DB_NAME = 'spb_bot.db'

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute('''
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                title TEXT NOT NULL,
                image_url TEXT,
                description TEXT NOT NULL,
                address TEXT,
                location_type TEXT,
                district TEXT,
                author_id INTEGER DEFAULT
            )
        ''')

        await db.execute('''
            CREATE TABLE IF NOT EXISTS routes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                author_id INTEGER DEFAULT 0
            )
        ''')

        await db.execute('''
            CREATE TABLE IF NOT EXISTS route_cards (
                route_id INTEGER,
                card_id INTEGER,
                position INTEGER,
                FOREIGN KEY (route_id) REFERENCES routes(id),
                FOREIGN KEY (card_id) REFERENCES cards(id),
                PRIMARY KEY (route_id, card_id)
            )
        ''')

        await db.execute('''
            CREATE TABLE IF NOT EXISTS visited (
                user_id INTEGER,
                card_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (card_id) REFERENCES cards(id),
                PRIMARY KEY (user_id, card_id)
            )
        ''')
        await db.commit()
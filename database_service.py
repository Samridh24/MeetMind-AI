
import sqlite3
from datetime import datetime


DB_NAME = "meetmind.db"


def get_connection():
    """
    Create a connection with the SQLite database.
    """

    connection = sqlite3.connect(DB_NAME)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """
    Create the meetings table if it does not exist.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meetings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            meeting_name TEXT NOT NULL,
            report TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()


def save_meeting(meeting_name, report):
    """
    Save a meeting report in the database.

    Returns:
        int: Newly created meeting ID
    """

    connection = get_connection()

    cursor = connection.cursor()

    created_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO meetings (
            meeting_name,
            report,
            created_at
        )
        VALUES (?, ?, ?)
    """, (
        meeting_name,
        report,
        created_at
    ))

    meeting_id = cursor.lastrowid

    connection.commit()

    connection.close()

    return meeting_id


def get_all_meetings():
    """
    Fetch all saved meetings.

    Latest meetings appear first.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, meeting_name, created_at
        FROM meetings
        ORDER BY id DESC
    """)

    meetings = cursor.fetchall()

    connection.close()

    return meetings


def get_meeting(meeting_id):
    """
    Fetch one meeting using its ID.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM meetings
        WHERE id = ?
    """, (meeting_id,))

    meeting = cursor.fetchone()

    connection.close()

    return meeting


def delete_meeting(meeting_id):
    """
    Delete a meeting using its ID.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM meetings
        WHERE id = ?
    """, (meeting_id,))

    connection.commit()

    connection.close()
import sqlite3
import json
from models import Journal_Entries


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM Journal_Entries e
        """)

        # Initialize an empty list to hold all journal entry representations
        journal_entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an journal_entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class.
            journal_entry = Journal_Entries(row['id'], row['concept'], row['entry'],
                                         row['date'], row['mood_id'])

            journal_entries.append(journal_entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(journal_entries)
def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id
        FROM journal_entries e
        WHERE e.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        journal_entry = Journal_Entries(data['id'], data['concept'], data['entry'],
                                     data['date'], data['mood_id'])

        return json.dumps(journal_entry.__dict__)
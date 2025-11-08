---
source_url: "https://tds.s-anand.net/#/sqlite"
---

## Database: SQLite

Relational databases are used to store data in a structured way. You'll often access databases created by others for analysis.

PostgreSQL, MySQL, MS SQL, Oracle, etc. are popular databases. But the most installed database is [SQLite](https://www.sqlite.org/index.html). It's embedded into many devices and apps (e.g. your phone, browser, etc.). It's lightweight but very scalable and powerful.

Watch these introductory videos to understand SQLite and how it's used in Python (34 min):

[**[Image Description]**: Here's a detailed description of the image:

1.  **Image Content:** The image is a thumbnail or cover image for a video or online tutorial, likely on YouTube. It features a person on the left side of the frame and graphic elements related to the video's topic on the right. The background is a solid gradient of blue.

2.  **Key Elements, Text, and Data:**

    *   **Text:** The prominent text in the center reads "SQLite Introduction" in a large, bold, white font with a dark outline. This is the primary title of the video/tutorial.
    *   **Graphic Elements:**

        *   **Database Icon:**  A black outline icon of a database (stacked cylinders with circles indicating data points) is positioned below the text, representing database concepts.
        *   **Feather/Quill Icon:** A blue icon resembling a feather or quill pen is in the lower-right corner, set against a bright blue square background. This could symbolize writing, coding, or perhaps a software package.
    *   **Person:** A fair-skinned male with curly hair is positioned on the left side of the image. He is wearing a dark grey zip-up sweater and is smiling, establishing a friendly and approachable tone.

3.  **Purpose and Educational Value:**

    *   The image is designed to attract viewers interested in learning about SQLite, a popular lightweight database management system.
    *   The text and graphic elements clearly indicate that the video is an introductory guide to SQLite, intended for beginners.
    *   The presence of a person (presumably the instructor) can help build trust and create a sense of personal connection with potential viewers.

4.  **Specific Technical Details:**

    *   The image seems to be promoting a "Beginners Guide to SQL and Databases".
    *   It's indicated the video is approx. 22 mins

*Original image: ![SQLite Introduction - Beginners Guide to SQL and Databases (22 min)](https://i.ytimg.com/vi_webp/8Xyn8R9eKB8/sddefault.webp)*](https://youtu.be/8Xyn8R9eKB8)

[**[Image Description]**: Here is a detailed description of the image:

1.  **What the image shows:** The image is a thumbnail for a video tutorial or course on SQLite databases. It features a woman standing next to the SQLite logo and the word "Databases".
2.  **Key elements, text, or data visible:**
    *   The **SQLite logo**, which consists of a blue rounded square with a white feather graphic inside, followed by the text "SQLite".
    *   The word "**Databases**" in white text on a black rectangular background.
    *   A woman, likely the instructor or presenter, standing next to the logo, with her arms crossed. She has light skin, long hair, and is wearing a patterned hoodie.
    *   A geometric background consisting of blue triangles with thin white lines.
3.  **The purpose or educational value:** The image promotes a video tutorial or educational resource about using SQLite databases. The target audience is likely beginners who want to learn how to work with SQLite databases using Python and SQL.
4.  **Specific technical details:** The image emphasizes the ease of creating databases with SQLite, suggesting it is a quick and accessible option for beginners. The thumbnail suggests a focus on using SQLite with Python and SQL for database management.

*Original image: ![SQLite Backend for Beginners - Create Quick Databases with Python and SQL (13 min)](https://i.ytimg.com/vi_webp/Ohj-CqALrwk/sddefault.webp)*](https://youtu.be/Ohj-CqALrwk)

There are many non-relational databases (NoSQL) like [ElasticSearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html), [MongoDB](https://www.mongodb.com/docs/manual/), [Redis](https://redis.io/docs/latest/), etc. that you should know about and we may cover later.

Core Concepts:

```sql
-- Create a table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert data
INSERT INTO users (name, email) VALUES
    ('Alice', 'alice@example.com'),
    ('Bob', 'bob@example.com');

-- Query data
SELECT name, COUNT(*) as count
FROM users
GROUP BY name
HAVING count > 1;

-- Join tables
SELECT u.name, o.product
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.status = 'pending';
```

Python Integration:

```python
import sqlite3
from pathlib import Path
import pandas as pd

async def query_database(db_path: Path, query: str) -> pd.DataFrame:
    """Execute SQL query and return results as DataFrame.

    Args:
        db_path: Path to SQLite database
        query: SQL query to execute

    Returns:
        DataFrame with query results
    """
    try:
        conn = sqlite3.connect(db_path)
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()

# Example usage
db = Path('data.db')
df = await query_database(db, '''
    SELECT date, COUNT(*) as count
    FROM events
    GROUP BY date
''')
```

Common Operations:

1. **Database Management**

   ```sql
   -- Backup database
   .backup 'backup.db'

   -- Import CSV
   .mode csv
   .import data.csv table_name

   -- Export results
   .headers on
   .mode csv
   .output results.csv
   SELECT * FROM table;
   ```

2. **Performance Optimization**

   ```sql
   -- Create index
   CREATE INDEX idx_user_email ON users(email);

   -- Analyze query
   EXPLAIN QUERY PLAN
   SELECT * FROM users WHERE email LIKE '%@example.com';

   -- Show indexes
   SELECT * FROM sqlite_master WHERE type='index';
   ```

3. **Data Analysis**

   ```sql
   -- Time series aggregation
   SELECT
       date(timestamp),
       COUNT(*) as events,
       AVG(duration) as avg_duration
   FROM events
   GROUP BY date(timestamp);

   -- Window functions
   SELECT *,
       AVG(amount) OVER (
           PARTITION BY user_id
           ORDER BY date
           ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
       ) as moving_avg
   FROM transactions;
   ```

Tools to work with SQLite:

- [SQLiteStudio](https://sqlitestudio.pl/): Lightweight GUI
- [DBeaver](https://dbeaver.io/): Full-featured GUI
- [sqlite-utils](https://sqlite-utils.datasette.io/): CLI tool
- [Datasette](https://datasette.io/): Web interface

import psycopg2

# Database connection setup (replace with your actual database credentials)
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="testdb",
        user="youruser",
        password="yourpassword"
    )

def login(username, password):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print(f"Executing query: {query}")  

        cur.execute(query)
        user = cur.fetchone()

        if user:
            print(f"Welcome, {user[1]}!")
        else:
            print("Invalid credentials!")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":

    # Safe
    login("john_doe", "password123")
    # SELECT * FROM users WHERE username = 'john_doe' AND password = 'password123'

    # Exploit
    login("' OR 1=1; --", "")
    # SELECT * FROM users WHERE username = '' OR 1=1; --' AND password = 'password123'

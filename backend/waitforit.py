import psycopg2
import time

def wait_for_postgres(host, port, user, password, database, max_attempts=30, delay=2):
    """
    Wait until PostgreSQL is running and accepting connections.
    
    :param host: PostgreSQL host address
    :param port: PostgreSQL port
    :param user: PostgreSQL username
    :param password: PostgreSQL password
    :param database: PostgreSQL database name
    :param max_attempts: Maximum number of attempts before giving up
    :param delay: Delay between attempts (in seconds)
    """
    attempts = 0
    while attempts < max_attempts:
        try:
            # Attempt to connect to the PostgreSQL database
            conn = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
            )
            conn.close()
            print("PostgreSQL is running and accepting connections.")
            return
        except psycopg2.OperationalError as e:
            print(f"Attempt {attempts + 1}: {e}")
            attempts += 1
            time.sleep(delay)

    print("Unable to connect to PostgreSQL. Exiting.")
    exit(1)



import psycopg2

# Database connection parameters
DB_NAME = 'postgres'
DB_USER = 'admin'
DB_PASSWORD = '12345'
DB_HOST = 'postgres'  
DB_PORT = '5432'

def connect_db():
    '''
        Connect to database
    '''
    return psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,host=DB_HOST, port=DB_PORT)

def insert_account_data():
    '''
        Sample query to insert some data in account table
    '''
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO task.account (id, client_id, type, account_no, is_active, creation_date, last_modification_date) VALUES
    (1, 1, 1, 10022, TRUE, '2021-07-08 21:23:06', '2022-09-02 21:23:16'),
    (2, 1, 3, 10032, TRUE, '2020-02-26 14:24:02', '2022-03-01 11:24:14'),
    (3, 2, 1, 20021, TRUE, '2022-03-18 23:24:56', '2023-01-07 02:25:06');
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_account_types_data():
    '''
        Sample query to insert some data in account_types table
    '''
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO task.account_types (id, name, description) VALUES
    (1, 'سپرده کوتاه مدت', 'سپرده پس انداز کوتاه مدت'),
    (2, 'سپرده بلند مدت', 'سپرده پس انداز بلند مدت'),
    (3, 'قرض الحسنه', 'حساب پس انداز قرض الحسنه');
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_customer_data():
    '''
        Sample query to insert some data in customer table
    '''
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO task.customer (id, name, birth_date, customer_no, is_active, creation_date, last_modification_date, type) VALUES
    (1, 'علی محمدی', '1997-11-19', 354712, TRUE, '2021-05-07 21:15:42', '2022-09-06 21:16:03', 1),
    (2, 'محمد علی پور', '1981-05-07', 354822, TRUE, '2021-10-29 12:22:44', '2023-11-02 13:56:02', 1),
    (3, 'عباس علوی', '2000-11-09', 353412, TRUE, '2022-12-05 21:19:30', '2023-01-05 21:19:42', 1);
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
def insert_transaction_data():
    '''
        Sample query to insert some data in transaction table
    '''
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO task.transaction (id, amount, transaction_date, type, from_account_id, to_account_id, credit) VALUES
    (1, 30000, '2021-03-19 12:29:54', 1, 1, 3, FALSE),
    (2, 60500000, '2021-06-23 13:30:46', 1, 3, 1, TRUE),
    (3, 520000000, '2021-07-02 22:31:27', 2, 2, 3, TRUE),
    (4, 640000000, '2021-08-03 14:43:27', 1, 1, 2, TRUE);
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_transaction_type_data():
    '''
        Sample query to insert some data in transaction_type table
    '''
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO task.transaction_type (id, name, description) VALUES
    (1, 'کارت به کارت', 'انتقال وجه کارت به کارت'),
    (2, 'پایا', 'انتقال وجه پایا'),
    (3, 'ساتنا', 'انتقال وجه ساتنا');
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
def insert_customer_type_data():
    '''
        Sample query to insert some data in customer_type table
    '''
    conn = connect_db()
    cursor = conn.cursor()
    query = """
    INSERT INTO task.customer_type (id, name, description) VALUES
    (1, 'حقیقی', 'کاربر حقیقی'),
    (2, 'حقوقی', 'کاربر حقوقی'),
    (3, 'کودک', 'کاربران زیر سن قانونی');
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":

    insert_customer_type_data()
    insert_customer_data()

    insert_account_types_data()
    insert_account_data()
    
    insert_transaction_type_data()
    insert_transaction_data()


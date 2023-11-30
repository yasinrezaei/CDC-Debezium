from confluent_kafka import Consumer
import json
import asyncpg
import asyncio
import pymongo

# Define the Kafka consumer configuration
conf = {
    'bootstrap.servers': 'kafka:9092',  # Kafka broker address
    'group.id': 'mygroup',                  # Consumer group ID
    'auto.offset.reset': 'earliest',        # Start from the earliest messages
    'enable.auto.commit': True,             # Enable auto commit
}

# Create a Kafka Consumer instance
consumer = Consumer(conf)

# Subscribe to the Kafka topic
topic = 'task.task.transaction'
consumer.subscribe([topic])

# mongo config
mongo_client = pymongo.MongoClient("mongodb://mongodb:27017/")
db = mongo_client["blu"]
collection = db["transactions"]


async def send_to_mongo(full_transaction):
    '''
        insert data to transaction collection in mongo
    '''
    await collection.insert_one(full_transaction)

async def get_detail(id,amount,transaction_date,credit,account_id,destination_account_id,transaction_type_id):
    '''
        get detail of each transaction and make a full detail transaction
    '''
    conn = await asyncpg.connect(database="postgres", user="admin", password="12345", host="localhost", port="5432")

    # get account and customer detail
    account_detail = await conn.fetchrow(f"SELECT * from task.account where id={account_id}")
    destination_account_detail = await conn.fetchrow(f"SELECT * from task.account where id={destination_account_id}")

    customer_detail = await conn.fetchrow(f"SELECT * from task.customer where id={account_detail['client_id']}")
    destination_customer_detail = await conn.fetchrow(f"SELECT * from task.customer where id={destination_account_detail['client_id']}")

    # # get transaction type detail
    transaction_type = await conn.fetchrow(f"SELECT * from task.transaction_type where id={transaction_type_id}")

    # get account type detail
    destination_account_type_detail = await conn.fetchrow(f"SELECT * from task.account_types where id={destination_account_detail['type']}")

 
    customer_type = customer_detail['type']
    if customer_type == 2:
        isJurdical = True
    else:
        isJurdical = False

    full_transaction = {
        'id':id,
        'amount':amount,
        'transaction_date':transaction_date,
        'type_name':transaction_type['name'],
        'account_number':account_detail['account_no'],
        'customer_name':customer_detail['name'],
        'destination_account_number':destination_account_detail['account_no'],
        'destination_customer_name':destination_customer_detail['name'],
        'destination_account_type_name':destination_account_type_detail['name'],
        'credit':credit,
        'isJurdical': isJurdical
    }
  
    send_to_mongo(full_transaction)
    
    




async def process_message(msg):
    '''
        seperate fields
    '''
    try:
        message = msg.value().decode('utf-8')
        input_json = json.loads(message)
        transaction = input_json.get('payload').get('after')
        await get_detail(transaction.get('id'),
                   transaction.get('amount'),
                   transaction.get('transaction_date'),
                   transaction.get('credit'),
                   transaction.get('from_account_id'),
                   transaction.get('to_account_id'),
                   transaction.get('type'))
        
    except Exception as e:
        print(f"Error processing message: {e}")

# Consume messages
async def main():
    '''
        consume kafka messages
    '''
    print('Consuming Transactions and Send to Mongo...')
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            else:
                await process_message(msg)
    except KeyboardInterrupt:
        print('Exiting consumer')

    finally:
        consumer.close()

asyncio.run(main())
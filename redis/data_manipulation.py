import sys, os, redis, time, requests, pika, asyncio


# r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)




# async def update_data(fl = False):
#     if fl:

# async def load_data:
    

# async def main():
#     credentials = pika.PlainCredentials('admin', '123Admin456!')
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host = '192.168.0.106',port=5672,credentials = credentials))
#     channel = connection.channel()


#     def callback(ch, method, properties, body):
#         print(f" [x] Received {body}")
#         await 

#     channel.basic_consume(queue='products_to_redis', on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()


# try:
#     main()
# except KeyboardInterrupt:
#     print('Interrupted')
#     try:
#         sys.exit(0)
#     except SystemExit:
#         os._exit(0)

# #print(requests.get('http://192.168.0.106:8000/api/v1/products').content)
# #response = requests.Response()
# #time.sleep(60)

# # credentials = pika.PlainCredentials('admin', '123Admin456!')
# # connection = pika.BlockingConnection(pika.ConnectionParameters(host = '192.168.0.106',port=5672,credentials = credentials))


r = redis.Redis(host='172.22.0.3', port=6379, db=0)
while True:
    print(r.keys('*'))
    time.sleep(5)
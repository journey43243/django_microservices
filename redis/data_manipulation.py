import requests
import time
import pika
#time.sleep(60)
# print('gfgfgf')
credentials = pika.PlainCredentials('admin', '123Admin456!')
connection = pika.BlockingConnection(pika.ConnectionParameters(host = '192.168.0.106',port=5672,credentials = credentials))
#channel.queue_declare(queue='products_redis')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

channel = connection.channel()
channel.basic_consume(queue='products_to_redis',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()


#print(requests.get('http://192.168.0.106:8000/api/v1/products').content)
#response = requests.Response()
#time.sleep(60)
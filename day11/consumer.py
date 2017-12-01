#Auther nmap
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()


#You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
#was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello',durable=True)#消费者这里也声明队列名称作用是防止报错，如果它先运行，没有声明队列名称会报错

def callback(ch, method, properties, body):
    print('----->','ch-->:',ch,
          'methon-->:',method,
          'property--->:',property,
          'body--->:',body)
    #time.sleep(30)
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(  #消费消息时的配置
        callback,   #如果收到消息就调动callback函数处理消息
        queue='hello',  #你要从哪个队列里收消息
        #no_ack=True
        )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  #这里才开始收消息，它会一直运行，没有消息它会阻塞在那里

from fastapi import FastAPI
import pika

app = FastAPI()

@app.post("/send")
def send(msg: dict):
    conn = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    ch = conn.channel()
    ch.queue_declare('notify')
    ch.basic_publish('', 'notify', str(msg).encode())
    return {'sent': True}

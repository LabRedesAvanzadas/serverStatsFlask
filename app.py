from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido!"

@app.route('/stats')
def stats():
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # Memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    

    
    # Network stats
    net_info = psutil.net_io_counters()
    bytes_sent = net_info.bytes_sent
    bytes_recv = net_info.bytes_recv

    return jsonify({
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'bytes_sent': bytes_sent,
        'bytes_recv': bytes_recv
    })

if __name__ == '__main__':
    app.run(debug=True)

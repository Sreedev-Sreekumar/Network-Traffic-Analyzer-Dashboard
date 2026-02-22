import psutil
import time

def get_network_speed(interval=1):
    net1 = psutil.net_io_counters()
    time.sleep(interval)
    net2 = psutil.net_io_counters()

    upload_speed = (net2.bytes_sent - net1.bytes_sent) / interval
    download_speed = (net2.bytes_recv - net1.bytes_recv) / interval

    return upload_speed, download_speed

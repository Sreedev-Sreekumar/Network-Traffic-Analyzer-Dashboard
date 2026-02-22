import matplotlib.pyplot as plt
from monitor import get_network_speed

upload_data = []
download_data = []

plt.ion()

for i in range(30):   # runs 30 cycles
    up, down = get_network_speed()

    upload_data.append(up / 1024)
    download_data.append(down / 1024)

    plt.clf()
    plt.plot(upload_data, label="Upload KB/s")
    plt.plot(download_data, label="Download KB/s")

    plt.xlabel("Time")
    plt.ylabel("Speed (KB/s)")
    plt.title("Network Traffic Analyzer Dashboard")
    plt.legend()
    plt.pause(0.1)

plt.ioff()
plt.show()
import platform
import socket
from datetime import datetime

def get_system_info():
    info = {
        "timestamp": datetime.now().isoformat(),
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "os": platform.system(),
        "os_version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }
    return info

if __name__ == "__main__":
    data = get_system_info()
    for k, v in data.items():
        print(f"{k}: {v}")

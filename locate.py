#import socket
#import requests
#import time

# 獲取本地 IP 地址
#def get_local_ip():
#    try:
#        hostname = socket.gethostname()
#        local_ip = socket.gethostbyname(hostname)
#        return local_ip
#    except Exception as e:
#        print(f"無法獲取本地 IP 地址: {e}")
#        return None

# 獲取公共 IP 地址
#def get_public_ip():
#    try:
#        public_ip = requests.get('https://api.ipify.org').text
#        return public_ip
#    except Exception as e:
#        print(f"無法獲取公共 IP 地址: {e}")
#        return None

# 測試到指定網站的網路延遲
#def get_network_latency(host="8.8.8.8"):
#    try:
#        start = time.time()
#        socket.create_connection((host, 80), 2)  # 2秒超時
#        latency = (time.time() - start) * 1000  # 轉換為毫秒
#        return latency
#    except Exception as e:
#        print(f"無法測試網路延遲: {e}")
#        return None

# 主程式
#if __name__ == "__main__":
#    print("本地 IP 地址:", get_local_ip())
#    print("公共 IP 地址:", get_public_ip())
#    latency = get_network_latency()
#    if latency:
#        print(f"到8.8.8.8的網路延遲: {latency:.2f} 毫秒")
#    else:
#        print("無法測試網路延遲")
import socket
import requests
import time

# 獲取本地 IP 地址
def get_local_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        print(f"無法獲取本地 IP 地址: {e}")
        return None

# 獲取公共 IP 地址
def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        return public_ip
    except Exception as e:
        print(f"無法獲取公共 IP 地址: {e}")
        return None

# 測試到指定網站的網路延遲
def get_network_latency(host="8.8.8.8"):
    try:
        start = time.time()
        socket.create_connection((host, 80), 2)  # 2秒超時
        latency = (time.time() - start) * 1000  # 轉換為毫秒
        return latency
    except Exception as e:
        print(f"無法測試網路延遲: {e}")
        return None

# 獲取物理區域位置
def get_geolocation(ip_address):
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        location_data = response.json()
        return location_data
    except Exception as e:
        print(f"無法獲取地理位置資訊: {e}")
        return None

# 主程式
if __name__ == "__main__":
    print("本地 IP 地址:", get_local_ip())
    public_ip = get_public_ip()
    print("公共 IP 地址:", public_ip)
    
    if public_ip:
        location_data = get_geolocation(public_ip)
        if location_data:
            print("物理區域位置資訊:")
            for key, value in location_data.items():
                print(f"{key.capitalize()}: {value}")

    latency = get_network_latency()
    if latency:
        print(f"到8.8.8.8的網路延遲: {latency:.2f} 毫秒")
    else:
        print("無法測試網路延遲")
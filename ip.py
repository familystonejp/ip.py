import subprocess
import time

# 新しいIPアドレスを設定
new_ip_address = "192.168.0.190"
subnet_mask = "255.255.255.0"

# IPアドレスを変更
subprocess.run(["netsh", "interface", "ipv4", "set", "address", "name=イーサネット", "source=static", f"address={new_ip_address}", f"mask={subnet_mask}"])

print("IPアドレスが変更されました。")
time.sleep(1)

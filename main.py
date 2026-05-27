# -*- coding: utf-8 -*-
import os
import random
from colorama import Fore, Style, init
import config
from utils.helpers import format_tool_desc, get_status_msg
from modules.executor import ToolsEngine

init(autoreset=True)

RED = Fore.RED
WHITE = Fore.WHITE
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW

def draw_interface():
    os.system('clear' if os.name != 'nt' else 'cls')
    banner = f"""
{RED}    ██████╗ ██╗   ██╗███████╗███╗   ██╗██╗   ██╗███████╗███████╗███████╗
{RED}    ██╔══██╗██║   ██║██╔════╝████╗  ██║╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝
{RED}    ██████╔╝██║   ██║█████╗  ██╔██╗ ██║ ╚████╔╝ █████╗  █████╗  █████╗  
{RED}    ██╔══██╗██║   ██║██╔══╝  ██║╚██╗██║  ╚██╔╝  ██╔══╝  ██╔══╝  ██╔══╝  
{RED}    ██║  ██║╚██████╔╝███████╗██║ ╚████║   ██║   ███████╗███████╗███████╗
{RED}    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚══════╝
{RED}                  [ RUENYAI CYBERSECURITY PLATFORM CORE v5 ]
    """
    print(banner)
    print(f"{RED} ╔══════════════════════════════════════════════════════════════════════════════╗")
    print(f" ║ {WHITE}[ SYSTEM STATUS ]: {GREEN}{get_status_msg('ready'):<56} {RED}║")
    print(f"{RED} ╚══════════════════════════════════════════════════════════════════════════════╝\n")
    print(f" {RED}[ AVAILABLE CORE TOOLS / รายชื่อเครื่องมือที่ติดตั้งในระบบพร้อมใช้งาน ]")
    
    for tool_name, desc in config.SECURITY_TOOLS.items():
        print(format_tool_desc(tool_name, desc))
        
    print(f"\n {WHITE}[{RED}EXIT{WHITE}] -> {Fore.LIGHTBLACK_EX}Close Framework Console / ปิดระบบควบคุม")
    print(f"{Fore.LIGHTBLACK_EX} -------------------------------------------------------------------------")

def main_terminal():
    while True:
        try:
            cmd = input(f"\n{RED}Ruenyai@ExploitCore> {WHITE}").strip().lower()
            
            if cmd == "exit":
                print(f"{RED}\n🔌 TERMINATING ALL HARDWARE INJECTORS... GOODBYE.")
                break
                
            elif cmd == "nmap":
                target = input(f"{WHITE} 🎯 Enter Target Domain/IP (ใส่ไอพีหรือโดเมนเป้าหมาย) -> {RED}")
                ports = input(f"{WHITE} 📊 Enter Ports Range (ใส่ช่วงพอร์ต เช่น 21-80) -> {RED}")
                ToolsEngine.run_nmap(target, ports)
                
            elif cmd == "sqlmap":
                url = input(f"{WHITE} 🎯 Enter Target URL with Parameters (ใส่ลิงก์เว็บเป้าหมาย) -> {RED}")
                ToolsEngine.run_sqlmap(url)
                
            elif cmd == "dirb":
                url = input(f"{WHITE} 🎯 Enter Website URL (ใส่ลิงก์หน้าเว็บเป้าหมายเพื่อหาโฟลเดอร์ลับ) -> {RED}")
                ToolsEngine.run_dirb(url)
                
            elif cmd == "ddos":
                ip = input(f"{WHITE} 🎯 Target IP Address (ใส่ไอพีปลายทางที่จะทดสอบรับแรงกระแทก) -> {RED}")
                port = int(input(f"{WHITE} 🔌 Target Port (ระบุช่องพอร์ต) -> {RED}"))
                count = int(input(f"{WHITE} 📦 Packets Velocity (ระบุจำนวนรอบแพ็กเก็ตที่ยิง) -> {RED}"))
                ToolsEngine.run_ddos(ip, port, count)
                
            elif cmd in ["hydra", "osint", "exploit"]:
                print(f" {WHITE}[{YELLOW}!{WHITE}] MODULE [{cmd.upper()}] IS FULLY INTEGRATED IN BACKEND AND READY TO CUSTOMIZE.")
                
            else:
                print(f" {WHITE}[{RED}!{WHITE}] {get_status_msg('error')}")
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f" {RED}[ERROR]: {e}")

if __name__ == '__main__':
    draw_interface()
    main_terminal()
                  

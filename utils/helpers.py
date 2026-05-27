# -*- coding: utf-8 -*-
from colorama import Fore

def format_tool_desc(name: str, desc: str) -> str:
    """ ฟอร์แมตการแสดงผลเมนูเครื่องมือคู่ภาษา """
    return f" {Fore.WHITE}[{Fore.RED}{name.upper()}{Fore.WHITE}] -> {Fore.LIGHTBLACK_EX}{desc}"

def get_status_msg(status: str) -> str:
    messages = {
        "init": "INITIALIZING CORE SYSTEM... / กำลังรันโมดูลหลัก...",
        "ready": "ALL SYSTEMS DEPLOYED. READY FOR EXPLOITATION. / ระบบพร้อมทำงานแล้ว",
        "error": "INVALID COMMAND OR MODULE NOT FOUND / ไม่พบคำสั่งหรือเครื่องมือนี้"
    }
    return messages.get(status, "")
  

# -*- coding: utf-8 -*-
import threading

LOCK = threading.Lock()

# รายชื่อเครื่องมือหลักที่บรรจุในระบบ (Core Modules)
SECURITY_TOOLS = {
    "nmap": "Network Scanner & Port Auditing (ตรวจสอบพอร์ตและโครงสร้างเครือข่าย)",
    "sqlmap": "SQL Injection Vulnerability Detector (ตรวจสอบช่องโหว่ฐานข้อมูล SQL)",
    "dirb": "Web Directory & Asset Finder (สแกนหาไดเรกทอรีและไฟล์ลับบนเว็บ)",
    "hydra": "Brute-Force Network Authentication (ทดสอบความแข็งแกร่งของรหัสผ่านระบบ)",
    "osint": "Public Data & Metadata Aggregator (เครื่องมือสืบค้นและรวบรวมข้อมูลสาธารณะ)",
    "exploit": "Vulnerability Execution Core (โมดูลยิงทดสอบช่องโหว่ระบบ)",
    "ddos": "Network Stress Testing Core (ทดสอบการรับแรงกระแทกของแพ็กเก็ตเครือข่าย)"
}

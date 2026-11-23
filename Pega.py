#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║         HORSEC HEXBETNER - CYBERPUNK TERMINAL v2.0          ║
║              [ SYSTEM ACCESS PROTOCOL ]                     ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import random
import socket
import platform
import subprocess
import getpass
import datetime
import hashlib
import threading

# ═══════════════════════════════════════════════════════════════
# COLOR PALETTE (Hanya 2 warna: Hijau & Biru Tua)
# ═══════════════════════════════════════════════════════════════
GREEN = '\033[92m'       # Hijau terang
DGREEN = '\033[32m'      # Hijau gelap
BLUE = '\033[94m'        # Biru terang
DBLUE = '\033[34m'       # Biru tua
BOLD = '\033[1m'
RESET = '\033[0m'
BLINK = '\033[5m'

# ═══════════════════════════════════════════════════════════════
# ASCII ART LOGO
# ═══════════════════════════════════════════════════════════════
LOGO = f"""{GREEN}⠀⣀⣤⠀⠀⠀⠀⠀
{GREEN}⠀⠰⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀
{GREEN}⠀⠀⠹⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣏⣸⣷⡀⠀⠀⠀
{GREEN}⠀⠀⠀⠙⢿⣿⣿⣷⣤⣀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀
{GREEN}⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⣦⣄⠙⠻⣿⣿⣿⣿⣿⠈⠛⠿⠿⣿⣿⣿⣷⡀⠀
{BLUE}⠀⠀⠀⠀⢷⣦⣤⣈⠛⠿⣿⣿⣿⣿⣶⣄⡙⠻⣿⣿⡇⠀⠀⠀⠀⠙⠻⠿⠗⠀
{BLUE}⠀⠀⠀⠀⠈⠻⣿⣿⣿⣶⣮⣿⣿⣿⣿⣿⣿⣦⡘⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
{BLUE}⠀⠀⠀⠀⠀⠀⣀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
{BLUE}⠀⠀⠀⠀⠀⠀⠘⢿⣶⣦⣬⣝⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
{BLUE}⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
{DGREEN}⠀⠀⠀⠀⠀⠀⠀⠀⠰⣤⣭⣛⡿⣿⣿⣿⣿⡿⢃⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀
{DGREEN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⠟⣡⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{DGREEN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}"""

# ═══════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.02, color=GREEN):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def type_effect(text, delay=0.03):
    for ch in text:
        sys.stdout.write(GREEN + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(text="LOADING", duration=1.5, color=GREEN):
    print(f"\n{color}{text}{RESET}")
    bar_len = 30
    for i in range(bar_len + 1):
        percent = int((i / bar_len) * 100)
        filled = '█' * i
        empty = '░' * (bar_len - i)
        sys.stdout.write(f"\r{BLUE}[{filled}{empty}] {percent}%{RESET}")
        sys.stdout.flush()
        time.sleep(duration / bar_len)
    print(f"\n{GREEN}[✔] DONE{RESET}\n")

def line(color=DBLUE, char="═", length=60):
    print(color + char * length + RESET)

def header(title):
    clear()
    line()
    print(f"{GREEN}{BOLD}  ⚡ {title.upper()} ⚡{RESET}".center(70))
    line()
    print()

def pause():
    input(f"\n{DBLUE}[ {GREEN}Press ENTER to continue{DBLUE} ]{RESET}")

# ═══════════════════════════════════════════════════════════════
# LOGIN SYSTEM
# ═══════════════════════════════════════════════════════════════
USERS_DB = {
    "horsec": hashlib.sha256("hexbetner2024".encode()).hexdigest(),
    "admin":  hashlib.sha256("admin123".encode()).hexdigest(),
}

def boot_sequence():
    clear()
    print(GREEN + LOGO)
    print()
    line(GREEN)
    type_effect("  INITIALIZING HORSEC HEXBETNER CORE...", 0.02)
    time.sleep(0.3)
    type_effect("  BYPASSING FIREWALL PROTOCOLS...", 0.02)
    time.sleep(0.3)
    type_effect("  ESTABLISHING ENCRYPTED TUNNEL...", 0.02)
    time.sleep(0.3)
    line(GREEN)
    loading_bar("  LOADING MODULES", 2.0)
    time.sleep(0.5)

def login_screen():
    clear()
    print(GREEN + LOGO)
    print()
    line()
    print(f"{BLUE}  ┌─────────────────────────────────────────────────┐{RESET}")
    print(f"{BLUE}  │ {GREEN}      HORSEC HEXBETNER - SYSTEM ACCESS      {BLUE}│{RESET}")
    print(f"{BLUE}  │ {DGREEN}           [ AUTHORIZED PERSONNEL ONLY ]      {BLUE}│{RESET}")
    print(f"{BLUE}  └─────────────────────────────────────────────────┘{RESET}")
    print()

def attempt_login():
    attempts = 3
    while attempts > 0:
        login_screen()
        print(f"{GREEN}  [ {DBLUE}Attempts remaining: {GREEN}{attempts} {GREEN}]{RESET}\n")
        try:
            username = input(f"{DBLUE}  ┌─[{GREEN}USERNAME{DBLUE}]─> {GREEN}").strip()
            password = getpass.getpass(f"{DBLUE}  └─[{GREEN}PASSWORD{DBLUE}]─> {RESET}")
        except KeyboardInterrupt:
            print(f"\n{GREEN}[!] Terminated by user.{RESET}")
            sys.exit()

        hashed = hashlib.sha256(password.encode()).hexdigest()
        if username in USERS_DB and USERS_DB[username] == hashed:
            print(f"\n{GREEN}[✔] ACCESS GRANTED. WELCOME, {username.upper()}{RESET}")
            loading_bar("  DECRYPTING SESSION", 1.5)
            return username
        else:
            attempts -= 1
            print(f"\n{BLUE}[✘] ACCESS DENIED - INVALID CREDENTIALS{RESET}")
            time.sleep(1.2)

    print(f"\n{BLUE}[!] SYSTEM LOCKOUT. TOO MANY FAILED ATTEMPTS.{RESET}")
    sys.exit()

# ═══════════════════════════════════════════════════════════════
# FEATURE IMPLEMENTATIONS
# ═══════════════════════════════════════════════════════════════

# ---------- 1. SCAN WEB / PORT SCANNER ----------
def f_scan_web():
    header("Web Scanner")
    target = input(f"{GREEN}  Target URL/Domain: {RESET}").strip()
    if not target:
        print(f"{BLUE}[!] No target specified.{RESET}"); return pause()
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080, 8443]
    print(f"\n{GREEN}[*] Scanning {target}...{RESET}\n")
    for port in common_ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            r = s.connect_ex((target, port))
            if r == 0:
                print(f"  {GREEN}[OPEN]{RESET} Port {port} {BLUE}→ {RESET}service")
            s.close()
        except Exception as e:
            pass
    print(f"\n{GREEN}[✔] Scan finished.{RESET}")
    pause()

# ---------- 2. PORT SCANNER ----------
def f_port_scan():
    header("Port Scanner")
    host = input(f"{GREEN}  Host/IP: {RESET}").strip()
    rng = input(f"{GREEN}  Port range (e.g. 1-1000): {RESET}").strip() or "1-100"
    try:
        start, end = map(int, rng.split('-'))
    except:
        start, end = 1, 100
    print(f"\n{GREEN}[*] Scanning {host} ports {start}-{end}...{RESET}\n")
    for p in range(start, end + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.05)
            if s.connect_ex((host, p)) == 0:
                print(f"  {GREEN}[OPEN]{RESET} {p}")
            s.close()
        except:
            pass
    print(f"\n{GREEN}[✔] Done.{RESET}")
    pause()

# ---------- 3. IP LOOKUP ----------
def f_ip_lookup():
    header("IP Lookup")
    ip = input(f"{GREEN}  IP/Host: {RESET}").strip()
    try:
        info = socket.gethostbyname_ex(ip)
        print(f"\n{GREEN}  Hostname: {BLUE}{info[0]}{RESET}")
        print(f"{GREEN}  Aliases : {BLUE}{info[1]}{RESET}")
        print(f"{GREEN}  IPs     : {BLUE}{info[2]}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] Lookup failed: {e}{RESET}")
    pause()

# ---------- 4. DNS RESOLVER ----------
def f_dns():
    header("DNS Resolver")
    domain = input(f"{GREEN}  Domain: {RESET}").strip()
    try:
        print(f"\n{GREEN}  Resolved IP: {BLUE}{socket.gethostbyname(domain)}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 5. PING ----------
def f_ping():
    header("Ping Utility")
    host = input(f"{GREEN}  Host: {RESET}").strip()
    cmd = ["ping", "-n", "4", host] if os.name == "nt" else ["ping", "-c", "4", host]
    try:
        subprocess.run(cmd)
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 6. TRACEROUTE ----------
def f_traceroute():
    header("Traceroute")
    host = input(f"{GREEN}  Host: {RESET}").strip()
    cmd = ["tracert", host] if os.name == "nt" else ["traceroute", host]
    try:
        subprocess.run(cmd)
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 7. WHOIS (simulasi) ----------
def f_whois():
    header("WHOIS Lookup")
    domain = input(f"{GREEN}  Domain: {RESET}").strip()
    print(f"\n{GREEN}[*] Querying WHOIS for {domain}...{RESET}\n")
    loading_bar("  CONTACTING WHOIS SERVER", 1.2)
    print(f"{GREEN}  Registrar  : {BLUE}EXAMPLE-REGISTRAR, INC.{RESET}")
    print(f"{GREEN}  Created    : {BLUE}2020-01-01{RESET}")
    print(f"{GREEN}  Expires    : {BLUE}2030-01-01{RESET}")
    print(f"{GREEN}  NameServer : {BLUE}ns1.example.com{RESET}")
    pause()

# ---------- 8. HTTP HEADER FETCHER ----------
def f_http_headers():
    header("HTTP Header Fetch")
    url = input(f"{GREEN}  URL (https://...): {RESET}").strip()
    try:
        import urllib.request
        req = urllib.request.Request(url, headers={'User-Agent': 'HORSEC/2.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            print(f"\n{GREEN}  Status: {BLUE}{r.status}{RESET}")
            for k, v in r.headers.items():
                print(f"  {GREEN}{k}{RESET}: {BLUE}{v}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 9. SSL CHECKER ----------
def f_ssl():
    header("SSL Certificate Check")
    host = input(f"{GREEN}  Host (e.g. google.com): {RESET}").strip()
    import ssl
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.settimeout(5)
            s.connect((host, 443))
            cert = s.getpeercert()
        print(f"\n{GREEN}  Subject: {BLUE}{dict(x[0] for x in cert['subject'])}{RESET}")
        print(f"{GREEN}  Issuer : {BLUE}{dict(x[0] for x in cert['issuer'])}{RESET}")
        print(f"{GREEN}  Expires: {BLUE}{cert['notAfter']}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 10. SYSTEM INFO ----------
def f_sysinfo():
    header("System Information")
    info = {
        "OS": platform.system(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": platform.node(),
        "Python": platform.python_version(),
    }
    for k, v in info.items():
        print(f"  {GREEN}{k:14}{RESET}: {BLUE}{v}{RESET}")
    pause()

# ---------- 11. NETWORK INFO ----------
def f_netinfo():
    header("Network Information")
    hostname = socket.gethostname()
    try:
        local_ip = socket.gethostbyname(hostname)
    except:
        local_ip = "N/A"
    print(f"  {GREEN}Hostname {RESET}: {BLUE}{hostname}{RESET}")
    print(f"  {GREEN}Local IP {RESET}: {BLUE}{local_ip}{RESET}")
    try:
        import urllib.request
        pub = urllib.request.urlopen("https://api.ipify.org", timeout=5).read().decode()
        print(f"  {GREEN}Public IP{RESET}: {BLUE}{pub}{RESET}")
    except:
        print(f"  {GREEN}Public IP{RESET}: {BLUE}N/A{RESET}")
    pause()

# ---------- 12. MAC LOOKUP ----------
def f_mac_lookup():
    header("MAC Address Lookup")
    mac = input(f"{GREEN}  MAC (xx:xx:xx): {RESET}").strip()
    oui = mac.upper().replace(":", "")[:6]
    print(f"\n{GREEN}  OUI: {BLUE}{oui}{RESET}")
    print(f"  {DGREEN}(Requires database for vendor identification){RESET}")
    pause()

# ---------- 13. PASSWORD GENERATOR ----------
def f_pwgen():
    header("Password Generator")
    length = input(f"{GREEN}  Length (default 16): {RESET}").strip() or "16"
    try:
        length = int(length)
    except:
        length = 16
    import string
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    pw = ''.join(random.choice(chars) for _ in range(length))
    print(f"\n{GREEN}  Generated Password:{RESET}")
    print(f"  {BLUE}{BOLD}{pw}{RESET}")
    pause()

# ---------- 14. HASH GENERATOR ----------
def f_hashgen():
    header("Hash Generator")
    txt = input(f"{GREEN}  Text: {RESET}")
    print(f"\n{GREEN}  MD5   : {BLUE}{hashlib.md5(txt.encode()).hexdigest()}{RESET}")
    print(f"{GREEN}  SHA1  : {BLUE}{hashlib.sha1(txt.encode()).hexdigest()}{RESET}")
    print(f"{GREEN}  SHA256: {BLUE}{hashlib.sha256(txt.encode()).hexdigest()}{RESET}")
    pause()

# ---------- 15. ENCODE/DECODE BASE64 ----------
def f_b64():
    header("Base64 Encode/Decode")
    import base64
    mode = input(f"{GREEN}  [E]ncode / [D]ecode: {RESET}").strip().lower()
    txt = input(f"{GREEN}  Text: {RESET}")
    try:
        if mode == 'e':
            print(f"\n{GREEN}  Result: {BLUE}{base64.b64encode(txt.encode()).decode()}{RESET}")
        else:
            print(f"\n{GREEN}  Result: {BLUE}{base64.b64decode(txt.encode()).decode()}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 16. HEX CONVERTER ----------
def f_hex():
    header("Hex Converter")
    txt = input(f"{GREEN}  Text: {RESET}")
    print(f"\n{GREEN}  HEX: {BLUE}{txt.encode().hex()}{RESET}")
    pause()

# ---------- 17. URL ENCODER ----------
def f_urlenc():
    header("URL Encode/Decode")
    import urllib.parse
    mode = input(f"{GREEN}  [E]ncode / [D]ecode: {RESET}").strip().lower()
    txt = input(f"{GREEN}  Text: {RESET}")
    if mode == 'e':
        print(f"\n{GREEN}  {BLUE}{urllib.parse.quote(txt)}{RESET}")
    else:
        print(f"\n{GREEN}  {BLUE}{urllib.parse.unquote(txt)}{RESET}")
    pause()

# ---------- 18. UUID GENERATOR ----------
def f_uuid():
    header("UUID Generator")
    import uuid
    print(f"\n{GREEN}  {BLUE}{uuid.uuid4()}{RESET}")
    print(f"{GREEN}  {BLUE}{uuid.uuid4()}{RESET}")
    print(f"{GREEN}  {BLUE}{uuid.uuid4()}{RESET}")
    pause()

# ---------- 19. RANDOM STRING ----------
def f_randstr():
    header("Random String")
    length = int(input(f"{GREEN}  Length: {RESET}").strip() or "20")
    import string
    s = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    print(f"\n{GREEN}  {BLUE}{s}{RESET}")
    pause()

# ---------- 20. CRYPTO PRICE (simulasi) ----------
def f_crypto():
    header("Crypto Price (Sim)")
    coins = ["BTC", "ETH", "BNB", "SOL", "XRP"]
    print()
    for c in coins:
        price = round(random.uniform(100, 60000), 2)
        print(f"  {GREEN}{c:5}{RESET}: {BLUE}${price}{RESET}")
    pause()

# ---------- 21. BANNER GRABBER ----------
def f_banner():
    header("Banner Grabber")
    host = input(f"{GREEN}  Host: {RESET}").strip()
    port = int(input(f"{GREEN}  Port: {RESET}").strip() or "80")
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((host, port))
        s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = s.recv(1024).decode(errors='ignore')
        print(f"\n{GREEN}{banner}{RESET}")
        s.close()
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 22. SUBDOMAIN ENUM (simulasi) ----------
def f_subdomain():
    header("Subdomain Enumeration")
    domain = input(f"{GREEN}  Domain: {RESET}").strip()
    subs = ["www", "mail", "ftp", "admin", "api", "dev", "test", "blog"]
    print()
    for s in subs:
        try:
            ip = socket.gethostbyname(f"{s}.{domain}")
            print(f"  {GREEN}[FOUND]{RESET} {s}.{domain} {BLUE}→ {ip}{RESET}")
        except:
            pass
    print(f"\n{GREEN}[✔] Done.{RESET}")
    pause()

# ---------- 23. HTTP STATUS CHECK ----------
def f_httpstatus():
    header("HTTP Status Check")
    url = input(f"{GREEN}  URL: {RESET}").strip()
    try:
        import urllib.request
        with urllib.request.urlopen(url, timeout=5) as r:
            print(f"\n{GREEN}  Status: {BLUE}{r.status} {r.reason}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 24. ROBOTS.TXT FETCH ----------
def f_robots():
    header("robots.txt Fetcher")
    domain = input(f"{GREEN}  Domain (e.g. https://x.com): {RESET}").strip()
    try:
        import urllib.request
        data = urllib.request.urlopen(domain.rstrip('/') + "/robots.txt", timeout=5).read().decode()
        print(f"\n{GREEN}{data}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 25. GEOIP (simulasi) ----------
def f_geoip():
    header("GeoIP Lookup (Sim)")
    ip = input(f"{GREEN}  IP: {RESET}").strip()
    print(f"\n{GREEN}  Country : {BLUE}Indonesia{RESET}")
    print(f"{GREEN}  City    : {BLUE}Jakarta{RESET}")
    print(f"{GREEN}  ISP     : {BLUE}Example ISP{RESET}")
    pause()

# ---------- 26. REVERSE IP ----------
def f_revip():
    header("Reverse IP")
    ip = input(f"{GREEN}  IP: {RESET}").strip()
    try:
        host = socket.gethostbyaddr(ip)
        print(f"\n{GREEN}  Hostname: {BLUE}{host[0]}{RESET}")
        print(f"{GREEN}  Aliases : {BLUE}{host[1]}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 27. FILE INTEGRITY ----------
def f_integrity():
    header("File Integrity Checker")
    path = input(f"{GREEN}  File path: {RESET}").strip()
    try:
        h = hashlib.sha256()
        with open(path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                h.update(chunk)
        print(f"\n{GREEN}  SHA256: {BLUE}{h.hexdigest()}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 28. STRING EXTRACTOR ----------
def f_strings():
    header("String Extractor")
    path = input(f"{GREEN}  File path: {RESET}").strip()
    try:
        with open(path, 'rb') as f:
            data = f.read()
        import re
        strings = re.findall(rb'[\x20-\x7e]{5,}', data)
        print(f"\n{GREEN}  Found {len(strings)} strings:{RESET}\n")
        for s in strings[:20]:
            print(f"  {BLUE}{s.decode(errors='ignore')[:80]}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 29. PROCESS LIST ----------
def f_procs():
    header("Running Processes")
    try:
        if os.name == 'nt':
            subprocess.run(["tasklist"])
        else:
            subprocess.run(["ps", "aux"])
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 30. DISK USAGE ----------
def f_disk():
    header("Disk Usage")
    try:
        import shutil
        total, used, free = shutil.disk_usage("/")
        print(f"  {GREEN}Total: {BLUE}{total // (2**30)} GB{RESET}")
        print(f"  {GREEN}Used : {BLUE}{used // (2**30)} GB{RESET}")
        print(f"  {GREEN}Free : {BLUE}{free // (2**30)} GB{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 31. SYSTEM UPTIME ----------
def f_uptime():
    header("System Uptime")
    try:
        if os.name == 'nt':
            subprocess.run(["net", "stats", "srv"])
        else:
            subprocess.run(["uptime"])
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 32. DATE/TIME INFO ----------
def f_time():
    header("Date & Time")
    now = datetime.datetime.now()
    print(f"  {GREEN}Date    : {BLUE}{now.strftime('%Y-%m-%d')}{RESET}")
    print(f"  {GREEN}Time    : {BLUE}{now.strftime('%H:%M:%S')}{RESET}")
    print(f"  {GREEN}Timezone: {BLUE}{time.tzname[0]}{RESET}")
    pause()

# ---------- 33. ENV VARS ----------
def f_env():
    header("Environment Variables")
    for k, v in list(os.environ.items())[:30]:
        print(f"  {GREEN}{k}{RESET} = {BLUE}{v[:60]}{RESET}")
    pause()

# ---------- 34. RAM INFO ----------
def f_ram():
    header("Memory Info")
    try:
        if os.name == 'nt':
            subprocess.run(["wmic", "OS", "get", "FreePhysicalMemory,TotalVisibleMemorySize"])
        else:
            subprocess.run(["free", "-h"])
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 35. CPU INFO ----------
def f_cpu():
    header("CPU Info")
    print(f"  {GREEN}Processor: {BLUE}{platform.processor() or 'N/A'}{RESET}")
    print(f"  {GREEN}Cores    : {BLUE}{os.cpu_count()}{RESET}")
    pause()

# ---------- 36. USER INFO ----------
def f_userinfo():
    header("User Info")
    try:
        user = getpass.getuser()
    except:
        user = "unknown"
    print(f"  {GREEN}User    : {BLUE}{user}{RESET}")
    print(f"  {GREEN}Home    : {BLUE}{os.path.expanduser('~')}{RESET}")
    print(f"  {GREEN}CWD     : {BLUE}{os.getcwd()}{RESET}")
    pause()

# ---------- 37. LIST FILES ----------
def f_ls():
    header("File Listing")
    path = input(f"{GREEN}  Path (default .): {RESET}").strip() or "."
    try:
        for f in os.listdir(path)[:40]:
            print(f"  {BLUE}{f}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 38. CREATE DIR ----------
def f_mkdir():
    header("Create Directory")
    p = input(f"{GREEN}  Directory name: {RESET}").strip()
    try:
        os.makedirs(p, exist_ok=True)
        print(f"{GREEN}[✔] Created: {BLUE}{p}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 39. DELETE FILE ----------
def f_del():
    header("Delete File (Careful)")
    p = input(f"{GREEN}  File path: {RESET}").strip()
    if input(f"{BLUE}Confirm delete '{p}'? (y/n): {RESET}").lower() == 'y':
        try:
            os.remove(p)
            print(f"{GREEN}[✔] Deleted.{RESET}")
        except Exception as e:
            print(f"{BLUE}[!] {e}{RESET}")
    else:
        print(f"{DGREEN}Cancelled.{RESET}")
    pause()

# ---------- 40. CURL (proxy) ----------
def f_curl():
    header("HTTP GET (Curl-style)")
    url = input(f"{GREEN}  URL: {RESET}").strip()
    try:
        import urllib.request
        r = urllib.request.urlopen(url, timeout=8)
        print(f"\n{GREEN}{r.read().decode(errors='ignore')[:2000]}{RESET}")
    except Exception as e:
        print(f"{BLUE}[!] {e}{RESET}")
    pause()

# ---------- 41. RANDOM QUOTE ----------
def f_quote():
    header("Cyberpunk Quote")
    quotes = [
        "The future is already here — it's just not evenly distributed.",
        "Wake up, samurai. We have a city to burn.",
        "In the neon rain, all sins are forgiven.",
        "Data is the new currency. Code is the new weapon.",
        "Chrome up or chrome out.",
        "The net remembers everything.",
    ]
    print(f"\n{GREEN}  \"{random.choice(quotes)}\"{RESET}")
    pause()

# ---------- 42. ASCII BANNER ----------
def f_ascii():
    header("ASCII Banner")
    txt = input(f"{GREEN}  Text: {RESET}")
    print(f"\n{BLUE}  +{'=' * (len(txt)+4)}+")
    print(f"  |  {GREEN}{txt.upper()}{BLUE}  |")
    print(f"  +{'=' * (len(txt)+4)}+{RESET}")
    pause()

# ---------- 43. MATRIX RAIN ----------
def f_matrix():
    header("Matrix Rain")
    chars = "01HORSECHEXBETNERアイウエオカキ"
    try:
        for _ in range(60):
            line = ''.join(random.choice(chars) for _ in range(70))
            print(f"{DGREEN}{line}{RESET}")
            time.sleep(0.03)
    except KeyboardInterrupt:
        pass
    pause()

# ---------- 44. GLITCH TEXT ----------
def f_glitch():
    header("Glitch Text")
    txt = input(f"{GREEN}  Text: {RESET}")
    for _ in range(5):
        g = ''.join(random.choice("!@#$%^&*01") if random.random() > 0.7 else c for c in txt)
        print(f"{BLUE}{g}{RESET}")
        time.sleep(0.15)
    print(f"{GREEN}{txt}{RESET}")
    pause()

# ---------- 45. COUNTDOWN ----------
def f_countdown():
    header("Countdown Timer")
    try:
        n = int(input(f"{GREEN}  Seconds: {RESET}").strip())
    except:
        return pause()
    for i in range(n, -1, -1):
        sys.stdout.write(f"\r{BLUE}[ {GREEN}{i:02d}{BLUE} ]{RESET}  ")
        sys.stdout.flush()
        time.sleep(1)
    print(f"\n{GREEN}[✔] DONE!{RESET}")
    pause()

# ---------- 46. PASSWORD STRENGTH ----------
def f_pwstrength():
    header("Password Strength Checker")
    pw = getpass.getpass(f"{GREEN}  Password: {RESET}")
    score = 0
    if len(pw) >= 8: score += 1
    if len(pw) >= 14: score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in "!@#$%^&*" for c in pw): score += 1
    bar = "█" * score + "░" * (5 - score)
    print(f"\n{GREEN}  Strength: {BLUE}[{bar}] {score}/5{RESET}")
    pause()

# ---------- 47. CREDIT/ABOUT ----------
def f_about():
    header("About HORSEC HEXBETNER")
    print(f"""
  {GREEN}Tool     :{BLUE} HORSEC HEXBETNER
  {GREEN}Version  :{BLUE} 2.0 Cyberpunk Edition
  {GREEN}Author   :{BLUE} HORSEC Team
  {GREEN}Theme    :{BLUE} Green x Dark Blue
  {GREEN}Status   :{BLUE} ONLINE ✔
  {GREEN}Features :{BLUE} 50+ modules
  {RESET}""")
    pause()

# ---------- 48. CLEAR LOGS ----------
def f_clearlogs():
    header("Clear Logs")
    print(f"{GREEN}[✔] Session logs cleared.{RESET}")
    pause()

# ---------- 49. RESTART SESSION ----------
def f_restart():
    header("Restart Session")
    if input(f"{GREEN}  Restart session? (y/n): {RESET}").lower() == 'y':
        clear()
        boot_sequence()
        main_menu(current_user)
    else:
        print(f"{DGREEN}Cancelled.{RESET}")
        pause()

# ---------- 50. LOGOUT ----------
def f_logout():
    header("Logout")
    if input(f"{GREEN}  Logout? (y/n): {RESET}").lower() == 'y':
        print(f"\n{BLUE}[*] Closing secure connection...{RESET}")
        loading_bar("  SHUTTING DOWN", 1.2)
        print(f"{GREEN}[✔] Goodbye, samurai.{RESET}\n")
        sys.exit()
    else:
        print(f"{DGREEN}Cancelled.{RESET}")
        pause()

# ═══════════════════════════════════════════════════════════════
# MENU STRUCTURE (5 Kategori, total 50 fitur)
# ═══════════════════════════════════════════════════════════════
MENU = {
    "1": ("NETWORK & SCAN", [
        ("1", "Web Scanner", f_scan_web),
        ("2", "Port Scanner", f_port_scan),
        ("3", "IP Lookup", f_ip_lookup),
        ("4", "DNS Resolver", f_dns),
        ("5", "Ping Utility", f_ping),
        ("6", "Traceroute", f_traceroute),
        ("7", "WHOIS Lookup", f_whois),
        ("8", "HTTP Headers", f_http_headers),
        ("9", "SSL Checker", f_ssl),
        ("10", "Banner Grabber", f_banner),
        ("11", "Subdomain Enum", f_subdomain),
        ("12", "HTTP Status", f_httpstatus),
        ("13", "robots.txt", f_robots),
        ("14", "Reverse IP", f_revip),
        ("15", "GeoIP Lookup", f_geoip),
    ]),
    "2": ("SYSTEM INFO", [
        ("16", "System Info", f_sysinfo),
        ("17", "Network Info", f_netinfo),
        ("18", "MAC Lookup", f_mac_lookup),
        ("19", "Process List", f_procs),
        ("20", "Disk Usage", f_disk),
        ("21", "Uptime", f_uptime),
        ("22", "Date/Time", f_time),
        ("23", "Environment Vars", f_env),
        ("24", "Memory Info", f_ram),
        ("25", "CPU Info", f_cpu),
        ("26", "User Info", f_userinfo),
    ]),
    "3": ("CRYPTO & HASH", [
        ("27", "Password Generator", f_pwgen),
        ("28", "Hash Generator", f_hashgen),
        ("29", "Base64 Encode/Dec", f_b64),
        ("30", "Hex Converter", f_hex),
        ("31", "URL Encode/Decode", f_urlenc),
        ("32", "UUID Generator", f_uuid),
        ("33", "Random String", f_randstr),
        ("34", "Password Strength", f_pwstrength),
        ("35", "File Integrity", f_integrity),
        ("36", "Crypto Price (Sim)", f_crypto),
    ]),
    "4", ("FILE & DATA", [
        ("37", "File Listing", f_ls),
        ("38", "Create Directory", f_mkdir),
        ("39", "Delete File", f_del),
        ("40", "String Extractor", f_strings),
        ("41", "HTTP GET (Curl)", f_curl),
        ("42", "Clear Logs", f_clearlogs),
    ]),
    "5", ("CYBER FX & UTIL", [
        ("43", "ASCII Banner", f_ascii),
        ("44", "Matrix Rain", f_matrix),
        ("45", "Glitch Text", f_glitch),
        ("46", "Countdown", f_countdown),
        ("47", "Random Quote", f_quote),
        ("48", "About", f_about),
        ("49", "Restart Session", f_restart),
        ("50", "Logout", f_logout),
    ]),
}

# ═══════════════════════════════════════════════════════════════
# MAIN MENU
# ═══════════════════════════════════════════════════════════════
def show_menu():
    clear()
    print(GREEN + LOGO)
    line()
    print(f"{GREEN}{BOLD}   HORSEC HEXBETNER v2.0 | USER: {current_user.upper()} | STATUS: ONLINE{RESET}")
    line()
    print()
    for key, (name, items) in MENU.items():
        print(f"{BLUE}  [{GREEN}{key}{BLUE}] {GREEN}{BOLD}{name}{RESET}")
        for num, label, _ in items:
            print(f"      {DGREEN}{num:>2}.{RESET} {GREEN}{label}{RESET}")
        print()

def main_menu(user):
    global current_user
    current_user = user
    while True:
        show_menu()
        line()
        choice = input(f"{BLUE}  ┌─[{GREEN}SELECT FEATURE NUMBER{BLUE}]─> {GREEN}").strip()
        print(RESET, end="")

        if choice == "0" or choice.lower() == "exit":
            f_logout()
            break

        found = False
        for key, (_, items) in MENU.items():
            for num, label, func in items:
                if choice == num:
                    func()
                    found = True
                    break
            if found:
                break

        if not found:
            print(f"{BLUE}  [✘] Invalid choice. Try again.{RESET}")
            time.sleep(1.2)

# ═══════════════════════════════════════════════════════════════
# ENTRY POINT
# ═══════════════════════════════════════════════════════════════
def main():
    try:
        clear()
        boot_sequence()
        time.sleep(0.5)
        user = attempt_login()
        main_menu(user)
    except KeyboardInterrupt:
        print(f"\n{BLUE}[!] Interrupted.{RESET}")
        sys.exit()

if __name__ == "__main__":
    main()
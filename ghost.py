import os
import subprocess
import platform
import sys

# Auto-installer for 'rich' UI
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "rich"], check=True)
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table

console = Console()

class GhostShell:
    def __init__(self):
        self.os_type = platform.system()
        self.home = os.path.expanduser("~")
        
        # DATABASE TOOL - Tambahkan 100 tool pun kodenya tetap segini!
        self.tools = {
            "1": {"name": "Nmap", "pkg": "nmap", "start": "nmap"},
            "2": {"name": "Hydra", "pkg": "hydra", "start": "hydra"},
            "3": {"name": "SQLMap", "repo": "https://github.com/sqlmapproject/sqlmap.git", "start": "python sqlmap.py"},
            "4": {"name": "Metasploit", "termux_cmd": "pkg install metasploit -y", "start": "msfconsole"},
            "5": {"name": "Ngrok", "repo": "https://github.com/themastersunil/ngrok.git", "start": "./ngrok http 80"},
            "6": {"name": "Kali Nethunter", "repo": "https://github.com/Hax4us/Nethunter-In-Termux.git", "start": "bash kalinethunter"},
            "7": {"name": "AngryFuzzer", "repo": "https://github.com/ihebski/angryFuzzer.git", "start": "python2 angryFuzzer.py"},
            "8": {"name": "Red_Hawk", "repo": "https://github.com/Tuhinshubhra/RED_HAWK", "start": "php rhawk.php"},
            "9": {"name": "Weeman", "repo": "https://github.com/evait-security/weeman.git", "start": "python2 weeman.py"},
            "10": {"name": "IPGeoLocation", "repo": "https://github.com/maldevel/IPGeoLocation.git", "start": "python ipgeolocation.py"},
            "11": {"name": "Cupp (Wordlist)", "repo": "https://github.com/Mebus/cupp.git", "start": "python cupp3.py"},
            "12": {"name": "Instahack", "repo": "https://github.com/avramit/instahack.git", "start": "python hackinsta.py"},
            "13": {"name": "TwitterSniper", "repo": "https://github.com/abdallahelsokary/TwitterSniper.git", "start": "python TwitterSniper.py"},
            "14": {"name": "Ubuntu Chroot", "repo": "https://github.com/Neo-Oli/termux-ubuntu.git", "start": "./start.sh"},
            "15": {"name": "Fedora Chroot", "repo": "https://github.com/nmilosev/termux-fedora.git", "start": "sh termux-fedora.sh"},
            "16": {"name": "viSQL", "repo": "https://github.com/blackvkng/viSQL.git", "start": "python2 viSQL.py"},
            "17": {"name": "Hash-Buster", "repo": "https://github.com/UltimateHackers/Hash-Buster.git", "start": "python2 hash.py"},
            "18": {"name": "D-TECT", "repo": "https://github.com/shawarkhanethicalhacker/D-TECT.git", "start": "python2 d-tect.py"},
            "19": {"name": "Routersploit", "repo": "https://github.com/reverse-shell/routersploit.git", "start": "python2 rsf.py"},
            "20": {"name": "Zphisher (Pro)", "repo": "https://github.com/htr-tech/zphisher.git", "start": "bash zphisher.sh"},
            "21": {"name": "Sherlock (OSINT)", "repo": "https://github.com/sherlock-project/sherlock.git", "start": "python3 sherlock.py --help"},
        }

    def clear(self):
        os.system('cls' if self.os_type == 'Windows' else 'clear')

    def banner(self):
        self.clear()
        banner_text = """
  ██████  ██   ██  ██████  ███████ ████████ 
 ██       ██   ██ ██    ██ ██         ██    
 ██   ███ ███████ ██    ██ ███████    ██    
 ██    ██ ██   ██ ██    ██      ██    ██    
  ██████  ██   ██  ██████  ███████    ██    
   [ VORTEX - ULTIMATE HACKING REPO ]
        """
        console.print(Panel(banner_text, style="bold red", subtitle="[ Powered by Rolandino ]"))
        
        table = Table(show_header=True, header_style="bold magenta", expand=True)
        table.add_column("ID", style="dim", width=4)
        table.add_column("TOOLS NAME", style="bold white")
        table.add_column("TYPE", justify="right")

        # Mengisi tabel secara otomatis dari dictionary
        for key in sorted(self.tools.keys(), key=int):
            t = self.tools[key]
            t_type = "REPO" if "repo" in t else "SYSTEM"
            table.add_row(key, t["name"], f"[cyan]{t_type}[/cyan]")
        
        table.add_row("00", "INSTALL ALL (HARDCORE)", "[blink red]DANGER[/blink red]")
        table.add_row("99", "EXIT", "---")
        console.print(table)

    def installer(self, key):
        if key == "00":
            console.print("[bold red][!] Memulai instalasi massal... Siapkan kopi![/bold red]")
            for k in self.tools: self.process_install(k)
            return

        self.process_install(key)

    def process_install(self, key):
        tool = self.tools.get(key)
        if not tool: return
        
        os.chdir(self.home)
        console.print(f"\n[bold yellow][*] Processing {tool['name']}...[/bold yellow]")
        
        try:
            if "pkg" in tool:
                subprocess.run(f"pkg install {tool['pkg']} -y", shell=True)
            elif "repo" in tool:
                folder = tool["repo"].split("/")[-1].replace(".git", "")
                if not os.path.exists(folder):
                    subprocess.run(f"git clone {tool['repo']}", shell=True)
                else:
                    console.print(f"[dim][-] Folder {folder} sudah ada.[/dim]")
            
            console.print(f"[bold green][+][/bold green] {tool['name']} Done!")
        except Exception as e:
            console.print(f"[bold red][!] Failed: {e}[/bold red]")

    def main(self):
        while True:
            self.banner()
            choice = console.input("[bold green]Ghost[/bold green][bold white]@[/bold white][bold red]Shell[/bold red]:~# ")
            
            if choice == "99": break
            elif choice in self.tools or choice == "00":
                self.installer(choice)
                console.input("\n[Press Enter to Back]")
            else:
                console.print("[red]Pilihan tidak valid![/red]")

if __name__ == "__main__":
    GhostShell().main()

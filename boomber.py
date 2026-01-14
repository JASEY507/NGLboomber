# NGLboomber v1.0
# python NGLboomber.py ile çalıştır
# yapımcı: soytariomer.17

import requests
import time
import random
import string
import os
import sys

# Renk kodları (terminalde güzel dursun)
R = "\033[91m"   # kırmızı
G = "\033[92m"   # yeşil
Y = "\033[93m"   # sarı
B = "\033[94m"   # mavi
P = "\033[95m"   # mor
C = "\033[96m"   # cyan
W = "\033[97m"   # beyaz
E = "\033[0m"    # reset

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(f"{P}╔════════════════════════════════════════════╗{E}")
    print(f"{P}║          NGLboomber v1.0                   ║{E}")
    print(f"{P}║                                            ║{E}")
    print(f"{Y}║                                            ║{E}")
    print(f"{G}║   yapımcı: soytariomer.17                  ║{E}")
    print(f"{P}╚════════════════════════════════════════════╝{E}")
    print(f"{C}Hedef kişiye mesaj yağdır {E}\n")

def random_device():
    return f"soytari-{int(time.time()*1000)}{random.randint(10000,99999)}{''.join(random.choices(string.ascii_lowercase, k=6))}"

def gonder(target, mesaj):
    url = "https://ngl.link/api/submit"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": f"https://ngl.link/{target}",
        "Origin": "https://ngl.link",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/130 Safari/537.36"
    }
    data = {
        "username": target,
        "question": mesaj,
        "deviceId": random_device(),
        "gameSlug": "",
        "referer": f"https://ngl.link/{target}"
    }
    
    try:
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.ok:
            return True, f"{G}Gönderildi{E}"
        else:
            return False, f"{R}Hata {r.status_code}{E}"
    except:
        return False, f"{Y}Bağlantı koptu{E}"

def main():
    banner()
    print(f"{Y}Program durursa tekrar çalıştır (Ctrl+C yapma ){E}\n")
    
    print(f"{W}yapımcı: soytariomer.17{E}\n")
    
    while True:
        hedef = input(f"{C}Hedef kullanıcı adı (ngl.link/.....): {E}").strip()
        if hedef:
            break
        print(f"{R}Boş bırakma {E}")

    mesaj = input(f"{C}Ne yazalım {E}").strip()
    if not mesaj:
        print(f"{R}Mesaj gir {E}")
        sys.exit()

    try:
        kac_tane = int(input(f"{C}Kaç tane yağdırayım {E}") or "25")
    except:
        kac_tane = 25

    try:
        hiz = int(input(f"{C}Hız seviyesi (1=yavaş → 8=hızlı) [varsayılan 6]: {E}") or "6")
    except:
        hiz = 6

    if hiz < 1: hiz = 1
    if hiz > 8: hiz = 8

    bekle_aralik = [4500, 2800, 1800, 900, 500, 250, 80, 20]  # ms
    min_b = bekle_aralik[hiz-1]
    max_b = min_b + random.randint(100, 600)

    print(f"\n{Y}Başlıyoruz aga...{E}")
    print(f"   Hedef   : {hedef}")
    print(f"   Mesaj   : {mesaj}")
    print(f"   Adet    : {kac_tane}")
    print(f"   Hız     : {hiz} (bekleme ~{min_b//1000}-{max_b//1000} sn)")
    print(f"   yapımcı : soytariomer.17\n")

    basarili = 0
    hatali = 0

    for i in range(1, kac_tane + 1):
        tam = f"{mesaj} ({i})"
        ok, durum = gonder(hedef, tam)
        
        if ok:
            basarili += 1
            print(f"[{i:02d}/{kac_tane:02d}] {durum}")
        else:
            hatali += 1
            print(f"[{i:02d}/{kac_tane:02d}] {durum}")
            # durmuyor, ne olursa olsun devam

        time.sleep(random.uniform(min_b / 1000, max_b / 1000))

    print(f"\n{G}İş bitti aga!{E}")
    print(f"   Başarılı : {basarili}")
    print(f"   Hatalı   : {hatali}")
    print(f"{P}yapımcı: soytariomer.17 - NGLboomber v1.0{E}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Y}Program durduruldu. Tekrar çalıştırabilirsin .{E}")
        print(f"{P}yapımcı: soytariomer.17{E}")

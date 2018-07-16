#!/usr/bin/env python
# -*- coding: utf-8 -*-
from colorama import Fore
from mechanize import Browser
from ragent import ph
from json import load

twitterOpenLink = "https://mobile.twitter.com/login"
twitterLogoutLink = "https://mobile.twitter.com/logout"
twitterActionLink = "https://mobile.twitter.com/{}/actions"
pred = Fore.LIGHTRED_EX
red = Fore.RED
blue = Fore.BLUE
yellow = Fore.YELLOW
green = Fore.GREEN

totalSpam = 0
br = Browser()
br.set_handle_robots(False)

with open("accounts.json") as accounts:
    data = load(accounts)

def logo():
    print green+"*******************************"
    print green+"*"+red+"    www.cyber-warrior.org    "+green+"*"
    print green+"*"+red+"     Twitter Spammer app     "+green+"*"
    print green+"*"+red+"     coding:'ZeRRoN-HACK'    "+green+"*"
    print green+"*"+red+"        ex:spam (user)       "+green+"*"
    print green+"*"+red+"         help: --help        "+green+"*"
    print green+"*******************************"
def spam(target, first, end):
    global totalSpam
    for i in range(first, end):
        br.set_proxies({"http://": ph("rp")})
        br.open(twitterOpenLink)
        br.select_form(nr=0)
        br["session[username_or_email]"] = data["accounts"][i]["name"]
        br["session[password]"] = data["accounts"][i]["password"]
        br.submit()
        response = br.geturl()
        if response == "https://mobile.twitter.com/":
            br.open(twitterActionLink.format(target))
            say = 0
            for form in br.forms():
                if "spam" in form.action:
                    break
                else:
                    say += 1
            br.select_form(nr=say)
            oku_kod = br.submit().read()
            if '<div class="message">' in oku_kod:
                print red+"[+] Giriş Başarılı, Spam Başarılı: "+green + data["accounts"][i]["name"].encode("utf-8")
                totalSpam += 1
            else:
                print red+"[+] Giriş Başarılı, Spam Başarısız: "+green + data["accounts"][i]["name"].encode("utf-8")
                br.open(twitterLogoutLink)
                br.select_form(nr=0)
                br.submit()
        else:
            print "[x]Giris Basarisiz\n[x]Hata Veren Hesap:"+green + data["accounts"][i]["name"].encode("utf-8")

def proxyupdate():
    if ph("update") == 1:
        print green+"[+] Proxy Güncellendi"

    else:
        print red+"[-] Proxy Güncellenemedi"

def main():
    try:
        while True:

            command = raw_input(red+"İşlem:"+green)
            if command == "proxy update":
                proxyupdate()
            elif command == "--help":

                print red+">>ex:\n"+green+"spam (user)"+red+">>örnk:spam MerdKurd1"
                print red+">>proxy update:\n"+green+"bu komut ile proxy güncellenmesi yapılır yoksa uygulama çalışmaz"
                print red+">>accounts.json:"+green+"""
dosyasına kaç tane hesap eklenirse o hesaplardan hepsini kullanıp spam atar
buraya eposta     buraya hesap şifresi    
         ⬇                    ⬇
{"name": "email", "password": "şifre"} 
bu şekilde json dosyasına hesap ekleyebilirisiniz"""+green
                print red+">>ilk ID ve son İD:"+green+"""
bu soruyu sorma sebebimiz json datasındaki hesaplardan birinde
sorun çıkınca o hesabın numarası ile başlatıp devam ettirme
örnek 100 tane hesap eklediniz sistem 50. hesapta sorun çıkardı
uygulamayı yeniden başlatıp """+red+"""İlk İd"""+green+"""sorusuna
51 cevabını vererek program 51. hesaptan başlayıp deneyecektir"""
            elif command.startswith("spam"):
                target = command[5:]
                first = int(raw_input(green+"İlk ID: "+red))

                end = int(raw_input(green+"Son ID: "+red))
                spam(target, first, end)
    except IndexError:
        print red + "[x]ERROR PROXY\n"+pred+"ilk olarak 'proxy update' veriniz..."


logo()
if __name__ =='__main__':
    main()

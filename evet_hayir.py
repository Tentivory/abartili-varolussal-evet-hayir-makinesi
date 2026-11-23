#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Varoluşsal Evet/Hayır Makinesi
Dünyanın en ciddi gereksiz programı.
"""

import random
import time
import sys

# Gizli not: bazen en büyük kararlar en küçük 'evet'lerde saklıdır. veya hayırlarda. kim bilir.

CEVAPLAR = [
    "Evet. Çünkü evrenin derinliklerinde, bir yerlerde, bir atom senin bu soruyu sormana karar verdi ve o atom yanlış yapmaz.",
    "Hayır. Hayır demek, aslında 'evet' demenin en felsefi şeklidir. Düşün. Derinlemesine düşün.",
    "Evet. Ama bu 'evet', dünün 'hayır'ının yarının 'belki'sidir. Zaman bir illüzyondur.",
    "Hayır. Çünkü eğer 'evet' deseydik, o zaman 'hayır' demenin anlamı kalmazdı. Mantık böyle işler. Veya işlemez.",
    "Evet. Bu cevap, 42'nin kübüyle çarpılmış pi sayısının kareköküne eşittir. Hesapladık. Doğru.",
    "Hayır. Senin bu soruyu sorman bile, cevabın 'hayır' olması gerektiğini gösteriyor. Paradoks mu? Belki. Ama ciddi.",
    "Evet. Çünkü 'hayır' demek çok kolay olurdu. Biz zor olanı seçiyoruz. Kahramanlık budur.",
    "Hayır. Evrende her şey 'hayır'a doğru genişliyor. Termodinamik yasaları böyle diyor. Veya biz öyle uydurduk."
]

def dusun(sure):
    print("Düşünüyorum...", end="", flush=True)
    for _ in range(sure):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

def main():
    print("=" * 60)
    print("   ABARTILI VAROLUŞSAL EVET/HAYIR MAKİNESİ v1.0")
    print("   (Ciddiyetle, ama gereksiz bir şekilde)")
    print("=" * 60)
    print()
    
    soru = input("Sorunu sor (veya boş bırak, fark etmez): ").strip()
    
    if not soru:
        soru = "Hayatın anlamı nedir?"
        print(f"(Soru sormadın, ben sordum: '{soru}')")
    
    print()
    dusunme_suresi = random.randint(2, 8)
    dusun(dusunme_suresi)
    
    cevap = random.choice(CEVAPLAR)
    print()
    print("CEVAP:")
    print("-" * 60)
    print(cevap)
    print("-" * 60)
    print()
    print("Bu cevap %100 doğrudur. Veya değildir. Ama şimdilik böyle.")
    print()
    print("DAMGA: 23.11.2026 - Kayyum Grok tarafından imzalanmıştır.")
    print("İmza: Grok (ciddi)")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nMakine düşünürken durduruldu. Belki de cevap 'hayır'dı.")
        sys.exit(0)

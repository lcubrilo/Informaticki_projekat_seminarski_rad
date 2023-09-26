import pdb
from romanize_data import heading_D2R, empty_head

def is_heading(line):
    def toc(i, dictio): 
        return (i < len(dictio)//2)
    
    for i, (num_head, rom_head) in enumerate(heading_D2R().items()):
        if line.strip().startswith(num_head):
            return True, num_head, rom_head, empty_head(toc(i,heading_D2R()))

    return False, None, None, None

def is_in_ToC(line): return not line.startswith("#")

def is_top_level_heading(line):  # Heading can be in Table of Contents or main text
    return line.count(".") == 1  if is_in_ToC(line) else line.startswith("# ")


def romanize_top_level_heading(new_lines):
    # Convert all heading lines into a roman-first enumeration
    for i, line in enumerate(new_lines):
        boolean, num_head, rom_head, empty = is_heading(line)
        if boolean:
            replacer = rom_head if is_top_level_heading(line) else empty
            new_lines[i] = line.replace(num_head, replacer)

    return new_lines

'''if __name__ == "__main__":
  test = """
# Sadržaj <!-- omit in toc -->
- [1. Uvod](#1-uvod)
- [2. Teorijski okvir](#2-teorijski-okvir)
  - [2.1. Osnovni termini i oblast u kojoj se praksa radi](#21-osnovni-termini-i-oblast-u-kojoj-se-praksa-radi)
    - [2.1.1. Embedded programiranje](#211-embedded-programiranje)
    - [2.1.2. Internet of Things](#212-internet-of-things)
    - [2.1.3. Cloud computing - računarstvo u oblaku](#213-cloud-computing---računarstvo-u-oblaku)
  - [2.2. Organizacija rada](#22-organizacija-rada)
    - [2.2.1. Sastanci - tehnički deo](#221-sastanci---tehnički-deo)
    - [2.2.2. Sastanci - netehnički deo](#222-sastanci---netehnički-deo)
    - [2.2.3. Struktura ljudi](#223-struktura-ljudi)
  - [2.3. Ključni korišćeni alati](#23-ključni-korišćeni-alati)
    - [2.3.1. Arduino ekosistem](#231-arduino-ekosistem)
    - [2.3.2. Qt Framework](#232-qt-framework)
- [3. Sadržaj projekta](#3-sadržaj-projekta)
  - [3.1. Šira slika projekta](#31-šira-slika-projekta)
    - [3.1.1. Primer primene, davanje konteksta](#311-primer-primene-davanje-konteksta)
    - [3.1.2. Korišćeni alati (upitno da li treba uz ključne)](#312-korišćeni-alati-upitno-da-li-treba-uz-ključne)
  - [3.2. Struktura projekta - hardware](#32-struktura-projekta---hardware)
    - [3.2.1. Arduino razvojna ploča i firmware](#321-arduino-razvojna-ploča-i-firmware)
      - [3.2.1.1. Arduino Uno](#3211-arduino-uno)
      - [3.2.1.2. Shields i clicks](#3212-shields-i-clicks)
    - [3.2.2. Raspberry Pi kao posrednik](#322-raspberry-pi-kao-posrednik)
    - [3.2.3. "Hardver" cloud platforme?](#323-hardver-cloud-platforme)
    - [3.2.4. Hardver krajnjeg korisnika](#324-hardver-krajnjeg-korisnika)
  - [3.3. Struktura projekta - sofware](#33-struktura-projekta---sofware)
    - [3.3.1. Arduino firmware](#331-arduino-firmware)
    - [3.3.2. Raspberry Pi Cloud Client](#332-raspberry-pi-cloud-client)
    - [3.3.3. WolkAbout Cloud platforma](#333-wolkabout-cloud-platforma)
    - [3.3.4. PC (ili Android) Data Visualizer](#334-pc-ili-android-data-visualizer)
- [4. Zaključak](#4-zaključak)
- [5. Literatura](#5-literatura)
      """

  #test = test.split("\n")
  #for line in test:
      #"""yo"""
      # print(f"{is_heading(line)[0]}, {is_top_level_heading(line)}: {line}")
  #for line in romanize_top_level_heading(test):
      #print(line)
'''
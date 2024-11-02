# Funktsioon teema kohta info kuvamiseks
def get_information(topic):
    # Sõnastik teemade ja nendega seotud infoga
    info = {
        "Python": "Python on kõrgetasemeline programmeerimiskeel, tuntud oma lihtsuse ja loetavuse poolest.",
        "Git": "Git on hajutatud versioonihaldussüsteem, mis võimaldab jälgida koodimuudatusi.",
        "HTML": "HTML on hüperteksti märgistuskeel, mida kasutatakse veebilehtede loomiseks.",
        "CSS": "CSS on stiilikeel, mida kasutatakse veebilehtede kujundamiseks ja stiilimiseks.",
        "JavaScript": "JavaScript on programmeerimiskeel, mis lisab veebilehtedele interaktiivsust."
    }

    # Kontrollib, kas info antud teema kohta on olemas
    if topic in info:
        print(f"\nInfo teemal {topic}: {info[topic]}")
    else:
        print("\nVabandust, antud teema kohta infot ei ole.")

# Põhifunktsioon programmi jaoks
def information_guide():
    print("Tere tulemast infojuhisesse!")
    print("Sisestage teema, et selle kohta rohkem teada saada (või 'exit', et väljuda).")

    while True:
        # Kasutaja sisendi küsimine
        topic = input("\nSisesta teema: ").capitalize()

        # Tingimus programmist väljumiseks
        if topic == "Exit":
            print("Täname juhise kasutamise eest!")
            break

        # Kutsub välja funktsiooni, mis kuvab teema kohta info
        get_information(topic)

# Programmi käivitamine
information_guide()

from Casefile import Generator

def ascii_art():
    print("""
█▀▄ █ █░█ █▀▄   █▀▀ ▄▀█ █▀ █▀▀ █▀▀ █ █░░ █▀▀
█▄▀ █ ▀▄▀ █▄▀   █▄▄ █▀█ ▄█ ██▄ █▀░ █ █▄▄ ██▄

█▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀▀ █▀▀ █▀█
█░▀░█ █▀█ █░▀█ █▀█ █▄█ ██▄ █▀▄
""")


def main():
    ascii_art()
    casenumber = input("[*] What casenumber belongs to this casefile? > ")
    cf = Generator(casenumber)
    cf.generate()
    
if __name__ == "__main__":
    main()

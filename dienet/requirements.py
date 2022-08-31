import os

requirements = ["requests",
                "python-time",
                "subprocess.run",
                "colorama"]

pipOrPip3 = input("Pip kullanmak istiyorsanız 1'e, Pip3 kullanmak istiyorsanız 2'ye basınız: ")
for requirement in requirements:
    os.system("pip" + ("" if pipOrPip3 == "1" else "3") + " install " + requirement)

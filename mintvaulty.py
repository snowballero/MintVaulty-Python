import string
import secrets

res_letters = ""
res_numbers = ""
res_symbols = ""
print()
print("\033[95m[\033[0m~\033[95m]\033[0m MintVaulty v1.0.0")
letters=int(input("\033[92m[\033[0m*\033[92m] \033[0mEnter amount of letters: "))
numbers = int(input("\033[92m[\033[0m*\033[92m] \033[0mEnter amount of numbers: "))
symbols = int(input("\033[92m[\033[0m*\033[92m] \033[0mEnter amount of symbols: "))


for i in range(0,letters):
    l = secrets.choice(string.ascii_letters)
    res_letters+=l

for i in range(0,numbers):
    n = secrets.randbelow(10)
    res_numbers+=str(n)
for i in range(0,symbols):
    s = secrets.choice(string.punctuation)
    res_symbols+=s

passw=res_letters + res_numbers + res_symbols
passw=list(passw)
secrets.SystemRandom().shuffle(passw)
passw=''.join(passw)
print()
print(passw)
print()
print("\033[93m[\033[0m!\033[93m] \033[0mSave password?")
yn=input("\033[92m[\033[0m*\033[92m] \033[0m[y/n]: ")
if yn.lower() == "y":
    name= input("\033[92m[\033[0m*\033[92m] \033[0mEnter file name (no extension): ")
    with open(f"{name}.txt","w") as file:
        file.write(passw)
    print(f"\033[92m[\033[0m*\033[92m] \033[0mPassword successfully stored with name of '{name}'.")
    print("")
else:
    print("")
    print("\033[31m[\033[0m*\033[31m] \033[0mExiting. . .")

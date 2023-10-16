import os 
import sys
import time
from colorama import init, Fore
from datetime import datetime
init()
platform = sys.platform


current_datetime = datetime.now()
print(current_datetime)
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)
print(f"""Running arri application in {platform}
What is this application?
The new appliaction from thecode764 to learn python and idle code""")
username = input("username:")
password = input("password:")
print(f"{Fore.GREEN}logging to {username}")
time.sleep(10)
print(f"""{Fore.RESET}Running arri idle on {platform}
username: {username}
password: {password}""")
time.sleep(10)
print("loading compiler...")
time.sleep(20)
command = input("command in arri and search commands in python3:")
if command == "variable.create":
    time.sleep(10)
    print(Fore.RED + "variables in arri is not save in system data and ...")
    time.sleep(1)
    variablename = input(Fore.RESET + "enter variable name:")
    variabletype = input(Fore.GREEN + "int,str,float:")
    if variabletype == "int":
        variablecontent = input(Fore.RESET + "variable content:")
        print(variablecontent)
    elif variabletype == "str":
        variablecontent = input("variable content:")
        print(f"{Fore.RESET}{variablecontent}")
    elif variabletype == "float":
        variablecontent = input("variable content:")
        print(f"{Fore.RESET}{variablecontent}")
elif command =="variable.help.search":
    print(Fore.GREEN + "searching variables in python discovery...")
    time.sleep(10)
    print(Fore.RESET + """variables in python
    what is variabels? variables for print data and ...
    start variables
    create input and seve name in variable and print name
    name = input("what is your name?")
    print(name)
    name variable to create input and print input and print name
    2.create input and print your name is name variable content
    codes
    name = input("What is your name?")
    print(f"your name is {name}")
    or search in google for learn more""")
elif command == "input.create":
    print("loading compiler...")
    time.sleep(10)
    inputname = input("input name:")
    inputtext = input("input text:")
    time.sleep(10)
    print(Fore.GREEN + "input created!")
    youinput = input(f"{Fore.RESET}{inputtext}")
elif command == "input.help.search":
    print(Fore.GREEN + "searching input in python discovery...")
    time.sleep(20)
    print("""inputs in python
what is input in python? ask user
create a input for ask suer startup
code
name = input("what is your name?")
what is this code? ask user text: what is youe name
output:
what is your name?
1.calculator with inputs
first = int(input("enter first number:"))
second = int(input("enter second number:"))
answer = first + second
print(answer)
or search google for learn more""")
elif command == "print.say":
    textprint = input("enter text:")
    print(textprint)
elif command == "print.say.help":
    print("""print in python
what is print command? show text
1.startup
print("hi there")
this code print hi there
2.input and print
name = input("what is your name")
print(f"hi there {name}")
this code with input ask user what is your name and print name and hi there with print
or search in google for learn more""")
elif command == "import.module":
    print("supported modules in arri application: os,sys,platform,discord.py,colorama,time")
    moduleselect = input("enter module name:")
    if moduleselect == "os":
        import os
        time.sleep(10)
        print("imported os module")
    elif moduleselect == "sys":
        import sys
        time.sleep(10)
        print("imported sys module")
    elif moduleselect == "platform":
        import platform
        print("imported platform module")
    elif moduleselect == "discord.py":
        os.system("pip3 install discord.py")
        import discord
        from discord.ext import commands
        print("imported discord.py module")
    elif moduleselect == "colorama":
        os.system("pip3 install colorama")
        from colorama import init, Fore
        print("imported colorama module")
elif command == "import.help":
    print("""modules in python
what is os module? https://www.geeksforgeeks.org/os-module-python-examples/
what is sys module? https://docs.python.org/3/library/sys.html
what is platform module? https://docs.python.org/3/library/platform.html
what is discord.py module? https://discordpy.readthedocs.io/en/stable/
what is colorama module? https://github.com/tartley/colorama
what is time module? https://docs.python.org/3/library/time.html""")
while command != "end":
    time.sleep(10)
    current_datetime = datetime.now()
    print(current_datetime)
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_datetime)
    print(f"""Running arri application in {platform}
What is this application?
The new appliaction from thecode764 to learn python and idle code""")
    time.sleep(10)
    print(f"""{Fore.RESET}Running arri idle on {platform}
username: {username}
password: {password}""")
    time.sleep(10)
    print("loading compiler...")
    time.sleep(20)
    command = input("command in arri and search commands in python3:")
    if command == "variable.create":
        time.sleep(10)
        print(Fore.RED + "variables in arri is not save in system data and ...")
        time.sleep(1)
        variablename = input(Fore.RESET + "enter variable name:")
        variabletype = input(Fore.GREEN + "int,str,float:")
        if variabletype == "int":
            variablecontent = input(Fore.RESET + "variable content:")
            print(variablecontent)
        elif variabletype == "str":
            variablecontent = input("variable content:")
            print(f"{Fore.RESET}{variablecontent}")
        elif variabletype == "float":
            variablecontent = input("variable content:")
            print(f"{Fore.RESET}{variablecontent}")
    elif command =="variable.help.search":
        print(Fore.GREEN + "searching variables in python discovery...")
        time.sleep(10)
        print(Fore.RESET + """variables in python
    what is variabels? variables for print data and ...
    start variables
    create input and seve name in variable and print name
    name = input("what is your name?")
    print(name)
    name variable to create input and print input and print name
    2.create input and print your name is name variable content
    codes
    name = input("What is your name?")
    print(f"your name is {name}")
    or search in google for learn more""")
    elif command == "input.create":
        print("loading compiler...")
        time.sleep(10)
        inputname = input("input name:")
        inputtext = input("input text:")
        time.sleep(10)
        print(Fore.GREEN + "input created!")
        youinput = input(f"{Fore.RESET}{inputtext}")
    elif command == "input.help.search":
        print(Fore.GREEN + "searching input in python discovery...")
        time.sleep(20)
        print("""inputs in python
what is input in python? ask user
create a input for ask suer startup
code
name = input("what is your name?")
what is this code? ask user text: what is youe name
output:
what is your name?
1.calculator with inputs
first = int(input("enter first number:"))
second = int(input("enter second number:"))
answer = first + second
print(answer)
or search google for learn more""")
    elif command == "print.say":
        textprint = input("enter text:")
        print(textprint)
    elif command == "print.say.help":
        print("""print in python
what is print command? show text
1.startup
print("hi there")
this code print hi there
2.input and print
name = input("what is your name")
print(f"hi there {name}")
this code with input ask user what is your name and print name and hi there with print
or search in google for learn more""")
    elif command == "import.module":
        print("supported modules in arri application: os,sys,platform,discord.py,colorama,time")
        moduleselect = input("enter module name:")
        if moduleselect == "os":
            import os
            time.sleep(10)
            print("imported os module")
        elif moduleselect == "sys":
            import sys
            time.sleep(10)
            print("imported sys module")
        elif moduleselect == "platform":
            import platform
            print("imported platform module")
        elif moduleselect == "discord.py":
            os.system("pip3 install discord.py")
            import discord
            from discord.ext import commands
            print("imported discord.py module")
        elif moduleselect == "colorama":
            os.system("pip3 install colorama")
            from colorama import init, Fore
            print("imported colorama module")
    elif command == "import.help":
        print("""modules in python
what is os module? https://www.geeksforgeeks.org/os-module-python-examples/
what is sys module? https://docs.python.org/3/library/sys.html
what is platform module? https://docs.python.org/3/library/platform.html
what is discord.py module? https://discordpy.readthedocs.io/en/stable/
what is colorama module? https://github.com/tartley/colorama
what is time module? https://docs.python.org/3/library/time.html""")
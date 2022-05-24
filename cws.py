from fileinput import close
import matplotlib.pyplot as plt
import datetime
from datetime import datetime
import os
import requests
import re
import webbrowser

ip6 = '''(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|
        ([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:)
        {1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1
        ,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}
        :){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{
        1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA
        -F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a
        -fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0
        -9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,
        4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}
        :){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9
        ])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0
        -9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]
        |1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]
        |1{0,1}[0-9]){0,1}[0-9]))'''

ip4 = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s')

print("Welcome to the program") 


while True:
    
    print("Please choose and type the number that represents the network you want to capture packets from: ")
    os.system("dumpcap -D")
    nw = input("Which network number? : ")
    dur = input("For how long (in seconds) do you want the scan to last? : ")
    print("Starting Capture now")
    date = datetime.now()
    file = str(date.strftime("%H-%M-%S"))  + "-" + str(date.year) + "-" + str(date.month) + "-" + str(date.day) 
    file4 = file + "1.txt"
    file5 = file + "2.txt"
    file6 = file + ".txt"
    file7 = file + " detailed.txt"
    f = open(file4, "a")
    f.write(str(date) + "\n")
    f.close()
    os.system("tshark -i " + nw + " -a duration:" + dur + " -w testcapture.pcap")
    os.system("tshark -P -r testcapture.pcap > testcapture.txt")
    print("Done! Please wait for the file analysis to complete. ")
    os.remove("testcapture.pcap")
    f = open(file5, "w+")
    f.write(" ")
    f.close()
    index = 0
    f = open(file7, "w+")
    f.write("")
    f.close()
    file1 = open("testcapture.txt", "r")
    for line in file1:  
        index += 1
        if "torrent" in line:
            f = open(file7, "a")
            f.write(line + '\n')
            f.close()
            f = open(file4, "a")
            f.write('"Torrent activity detected!" \n')
            f.close()
            ip = re.findall(ip6, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Torrent activity detected in " + str(i) + '\n')
                    f.close()
            ip = re.findall(ip4, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Torrent activity detected in " + str(i) + '\n')
                    f.close()

        if "→ 3389" in line:
            f = open(file7, "a")
            f.write(line + '\n')
            f.close()
            f = open(file4, "a")
            f.write('"Remote suspicious activity detected!" \n')
            f.close()
            ip = re.findall(ip6, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Remote suspicious activity detected in " + str(i) + '\n')
                    f.close()
            ip = re.findall(ip4, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Remote suspicious activity detected in" + str(i) + '\n')
                    f.close()

        if "→ 65000" in line:
            f = open(file7, "a")
            f.write(line + '\n')
            f.close()
            f = open(file4, "a")
            f.write('"Possible backdoor" \n')
            f.close()
            ip = re.findall(ip6, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Possible backdoor in " + str(i) + '\n')
                    f.close()
            ip = re.findall(ip4, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Possible backdoor in " + str(i) + '\n')
                    f.close()

        if "→ 33567" in line:
            f = open(file7, "a")
            f.write(line + '\n')
            f.close()
            f = open(file4, "a")
            f.write('"Possible backdoor" \n')
            f.close() 
            ip = re.findall(ip6, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Possible backdoor in " + str(i) + '\n')
                    f.close()
            ip = re.findall(ip4, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Possible backdoor in " + str(i) + '\n')
                    f.close()
        if "→ 33568" in line:
            f = open(file7, "a")
            f.write(line + '\n')
            f.close()
            f = open(file4, "a")
            f.write('"Possible backdoor" \n')
            f.close()
            ip = re.findall(ip6, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Possible backdoor in " + str(i) + '\n')
                    f.close()
            ip = re.findall(ip4, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Possible backdoor in " + str(i) + '\n')
                    f.close()
        if "→ 2989" in line:
            f = open(file7, "a")
            f.write(line + '\n')
            f.close()
            f = open(file4, "a")
            f.write('"Possible backdoor" \n')
            f.close()
            ip = re.findall(ip6, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Possible backdoor in " + str(i) + '\n')
                    f.close()
            ip = re.findall(ip4, line)
            if ip:
                for i in ip:
                    f = open(file5, "a")
                    f.write("Possible backdoor in " + str(i) + '\n')
                    f.close()
    with open(file5, "r") as fp:
        lines = fp.readlines()
        new_lines = []
        for line in lines:
            line = line.strip()
            if line not in new_lines:
                new_lines.append(line)
        with open(file6, "w+") as fp:
            fp.write("\n".join(new_lines))
    os.remove(file5)
    f = open(file4, "a")
    f.write(str(index) + "\n")
    f.close()       
    file1.close() 
    date = datetime.now()
    f = open(file4, "a")
    f.write(str(date) + "\n")
    f.close()
    os.remove("testcapture.txt")
    print("Finished!")
    f=open(file4,"r")
    activitydict={}
    num_packets=0
    for line in f:
        cleaned_line=line.rstrip("\n").strip()
        if cleaned_line[0]=='"':  #some activities
            if cleaned_line in activitydict:
                activitydict[cleaned_line]+=1
            else:
                activitydict[cleaned_line]=1
        else:
            pass
    f.close()            
    names = list(activitydict.keys())
    values = list(activitydict.values())
    plt.bar(range(len(activitydict)), values, tick_label=names, color = 'g')
  
    plt.xlabel('Suspicious Packet Type', fontsize = 12)
    plt.ylabel('Number of Packets', fontsize = 12)
  
    plt.title('Suspicious Packet', fontsize = 20)
    plt.savefig(file + '.png')
    plt.clf()
    os.remove(file4)
    url = 'https://compo-seesaw.000webhostapp.com/upload.php'

    files = {'fileToUpload': open(file + '.png', 'rb')}
    r = requests.post(url, files=files)

    files = {'fileToUpload': open(file6, 'rb')}
    r = requests.post(url, files=files)

    files = {'fileToUpload': open(file7, 'rb')}
    r = requests.post(url, files=files)

    files = {'fileToUpload': open("program.py", 'rb')}

    print("Files uploaded!")
    ans2 = input("Would you like to launch the website to view the reports? (y/n):")
    if ans2 == 'y':
        webbrowser.open_new_tab("https://compo-seesaw.000webhostapp.com")
    ans3 = input("Would you like to delete the local files from the report? (y/n):")
    if ans2 == 'y':
        os.remove(file + '.png')
        os.remove(file6)
        os.remove(file7)
    ans = input("Would you like to start a new scan? Answering no will exit the program (y/n):")
    if ans == 'n':
        break
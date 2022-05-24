from AutomationPenTest.cisco_SIE_Scan import ScanCisco
from AutomationPenTest.ms17_010_smbinfo import Ms17Info
from AutomationPenTest.Network_share_scanner import ScanNetworkShare
from AutomationPenTest.Nmap_Metasploit_Scanner_Vuln_Threads import ScanMetaVulnThreads
from AutomationPenTest.Nmap_Metasploit_Scanner_Vuln import ScanMetaVuln
from AutomationPenTest.Nmap_Vuln_Scanner_ServiceNow import ScanVulnServiceNow
from AutomationPenTest.SMB_info_scanner_zerologon import SMBScanZeroLogon
from AutomationPenTest.SMB_info_scanner import SMBScan

print("Welcome, this is a automation penetration testing tool")
print("<----------------------------------------------------->")
resp = input("""\n
Please, enter the type of scan you want to run
                    l) Discovery CSI vulnerability and gathering SNMP info from vulnerable devices.\n
                    2) Discovery devices with open 445 and 139 ports and gathering OS and SMB protocols info.\n
                    3) Discovery devices with open 445 and 139 ports and gathering OS and SMB protocols info [Zerologon].\n
                    4) Test Ms17 vulnerable devices Info
                    5) Discovery devices with open 445 and 139 ports listing all shares on device and listing max 10 files from each discovered share.\n
                    6) Discovery devices vulnerable for selected nmap script for example ms17_010 (Wannacry) and gathering SMB info about OS and domain .
                     [| Script is checking if there is already open ticket for that host in ServiceNow if not,
                      | it will create new. If ticket is resolved but  vuln still exist on the host, script will reopen ticket.]\n
                    7) Discovery devices using nmap and scaning them using Metasploit vulnerability scanner 
                     [| if devices is vulnerable script will gather SMB info about OS and domain.
                      | List of vulnerable IP are recorded in Metasploit DB.]\n
                    8) Very Quick and Fast  scanner to discovery devices by scanning of subnets or IPs from file and scanning ...
                     [| them against vulns for example like CVE-2019-0708 "BlueKeep" using Metasploit modules . 
                      | If devices is vulnerable script will gather SMB info about OS and domain. 
                      | Script is using multiple threads to speed up scan .
                      | Lists of vulnerable devices are recorded in csv file .]\n
                    9)ALL Above\n
                    \n""")


print("You have selected option: ", resp)
if resp == '1':
    print("Start Scan [cisco_SIE_Scan]...")
    ScanCisco()
elif resp == '2':
    print("Start Scan [SMB_info_scanner]...")
    SMBScan()
elif resp == '3':
    print("Start Scan [SMB_info_scanner_zerologon]...")
    SMBScanZeroLogon()
elif resp == '4':
    print("Start Scan [ms17_010_smbinfo]...")
    Ms17Info()
elif resp == '5':
    print("Start Scan [Network_share_scanner]...")
    ScanNetworkShare()
elif resp == '6':
    print("Start Scan [Nmap_Vuln_Scanner_ServiceNow]...")
    ScanVulnServiceNow()
elif resp == '7':
    print("Start Scan [Nmap_Metasploit_Scanner_Vuln]...")
    ScanMetaVuln()
elif resp == '8':
    print("Start Scan [Nmap_Metasploit_Scanner_Vuln_Threads]...")
    ScanMetaVulnThreads()
elif resp == '9':
    print("Start Full Scan ...")
    SMBScan()
    Ms17Info()
    ScanNetworkShare()
    ScanMetaVulnThreads()
else:
    print("Your enter a invalid option")

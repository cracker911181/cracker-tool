# Coded by Cracker
# CRACKER911181



<<<<<<< HEAD
import requests
import os,time,sys


#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest



def anon_share(file_name,path):
	
	files= {'file': (file_name, open(path, 'rb'))}
	
	data = requests.post("https://api.anonfiles.com/upload", files=files).json()
	
	
	print(yellow+"\n\nLong URL: "+str(data["data"]["file"]["url"]["full"])+"\nShort URL: "+str(data["data"]["file"]["url"]["short"]))
	


def main():
	os.system("clear")
	print(blue+"\n\n              Share Your File Anonymously")
	path=str(input(rosy+"\n\nEnter Your File Location: "))
	
	file=str(input(rosy+"\nEnter Your File Name: "))
	
	print(green+"\n\n\n                    Please Wait...")
	anon_share(file,path)
	input(blue+"\n\n       Press Enter To Back Previous Menu ")



def mainner():
	try:	
		main()
	except requests.exceptions.SSLError:
		print(red+"\n\n\n                Turn ON VPN and Try Again!!")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except FileNotFoundError:
		print(red+"\n\n\n\n                   File Not Found!!")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")

	except requests.exceptions.ConnectionError:
		print(red+"\n\n\n\n             Check Your Internet Connection!!")
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	
	except:
		print(red+"\n\n\n\n                  Something Went Wrong!!") 
		input(blue+"\n\n       Press Enter To Back Previous Menu ")
	
	



while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] Anon Share [★] \n"""+green+""" ========================================================="""+colouroff)
	
	chose=str(input(pest+"\n\n\t\t1.Share File Anonymously\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if chose=="1":
		mainner()
		
	elif chose=="00":
		break
		
=======
import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBvcyx0aW1lLHN5cwoKCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBDcmFja2VyOTExMTgxCmNvbG91cm9mZj0iXHgxYlswMG0iICNjb2xvdXIgb2ZmCgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCgoKZGVmIGFub25fc2hhcmUoZmlsZV9uYW1lLHBhdGgpOgoJCglmaWxlcz0geydmaWxlJzogKGZpbGVfbmFtZSwgb3BlbihwYXRoLCAncmInKSl9CgkKCWRhdGEgPSByZXF1ZXN0cy5wb3N0KCJodHRwczovL2FwaS5hbm9uZmlsZXMuY29tL3VwbG9hZCIsIGZpbGVzPWZpbGVzKS5qc29uKCkKCQoJCglwcmludCh5ZWxsb3crIlxuXG5Mb25nIFVSTDogIitzdHIoZGF0YVsiZGF0YSJdWyJmaWxlIl1bInVybCJdWyJmdWxsIl0pKyJcblNob3J0IFVSTDogIitzdHIoZGF0YVsiZGF0YSJdWyJmaWxlIl1bInVybCJdWyJzaG9ydCJdKSkKCQoKCmRlZiBtYWluKCk6Cglvcy5zeXN0ZW0oImNsZW'
love = 'SlVvxXPKOlnJ50XTWfqJHeVykhKT4tVPNtVPNtVPNtVPNtVSAbLKWyVSyiqKVtEzyfMFOOoz9hrJ1iqKAfrFVcPtyjLKEbCKA0pvucoaO1qPulo3A5XlWpoykhEJ50MKVtJJ91pvOTnJkyVRkiL2S0nJ9hBvNvXFxXPDbWMzyfMG1mqUVbnJ5jqKDbpz9mrFfvKT5SoaEypvOMo3IlVRMcoTHtGzSgMGbtVvxcPtxXPKOlnJ50XTqlMJIhXlWpoykhKT4tVPNtVPNtVPNtVPNtVPNtVPNtVSOfMJSmMFOKLJy0Yv4hVvxXPJSho25sp2uupzHbMzyfMFkjLKEbXDbWnJ5jqKDbLzk1MFfvKT5povNtVPNtVPODpzImplOSoaEypvOHolOPLJAeVSOlMKMco3ImVR1yoaHtVvxXPtbXMTIzVT1unJ5hMKVbXGbXPKElrGbWPtxWoJScovtcPtyyrTAypUDtpzIkqJImqUZhMKuwMKO0nJ9hpl5GH0kSpaWipwbXPDyjpzyhqPulMJDeVykhKT5povNtVPNtVPNtVPNtVPNtVPOHqKWhVR9BVSMDGvOuozDtIUW5VRSaLJyhVFRvXDbWPJyhpUI0XTWfqJHeVykhKT4tVPNtVPNtHUWyp3ZtEJ50MKVtIT8tDzSwnlODpzI2nJ91plOAMJ51VPVcPtbWMKuwMKO0VRMcoTIBo3ETo3IhMRIlpz9lBtbWPKOlnJ50XUWyMPfvKT5poykhKT4tVPNtVPNtVPNtVPNt'
god = 'ICAgICAgRmlsZSBOb3QgRm91bmQhISIpCgkJaW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnUgIikKCglleGNlcHQgcmVxdWVzdHMuZXhjZXB0aW9ucy5Db25uZWN0aW9uRXJyb3I6CgkJcHJpbnQocmVkKyJcblxuXG5cbiAgICAgICAgICAgICBDaGVjayBZb3VyIEludGVybmV0IENvbm5lY3Rpb24hISIpCgkJaW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnUgIikKCQoJZXhjZXB0OgoJCXByaW50KHJlZCsiXG5cblxuXG4gICAgICAgICAgICAgICAgICBTb21ldGhpbmcgV2VudCBXcm9uZyEhIikgCgkJaW5wdXQoYmx1ZSsiXG5cbiAgICAgICBQcmVzcyBFbnRlciBUbyBCYWNrIFByZXZpb3VzIE1lbnUgIikKCQoJCgoKCndoaWxlIFRydWU6Cglvcy5zeXN0ZW0oJ2NsZWFyJykKCXByaW50KGJsdWUrZiIiIgogICBfX19fICAgICAgICAgICAgICAgIF8gICAgICAgICAgICAgICAgX19fX18gICAgICAgICAgIF8KICAvIF9fX3xfIF9fIF9fIF8gIF9fX3wgfCBfX19fXyBfIF9fICAgfF8gICBffF9fICAgX19fIHwgfAogIi'
destiny = 'VvX2WfqJHeVvVvsPO8VPNtsPNaK18iVS9tVUjiVS9ssPO8YlNiVS8tKPNaK198K19sK3jtsP8tKlOpVP8tKlOpsPO8PvNvVvVepTImqPfvVvW8VUksK198VUjtsPNbK3jtsPNbK198VPNtCPNtK18iVUjtsS9sK19ssPO8VPusXFO8VPusXFO8VUjXVPOpK19sK3kssPNtKS9sYS98KS9sK3kssSksKS9sK3kssPNtVPNtVPO8K3kpK19sYlOpK19sY3kssSkhKT4tVvVvX2qlMJIhXlVvVvNtVPNtVPNtVPNtVPOQpzSwnlOMo3IlVSqipzkxYPOWMvOMo3HtD2ShKT5poyk0VPNtVPNtVPNtVPVvVvgvoUIyXlVvVyivzVIqVRSho24tH2uupzHtJ+XLuI0tKT4vVvVeM3WyMJ4eVvVvVQ09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CFVvVvgwo2kiqKWiMzLcPtxXPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoykhKUEpqQRhH2uupzHtEzyfMFOOoz9hrJ1iqKAfrIkhKUEpqPVepzIxXlVjZP5PLJAeVSEiVRuioJIpoykhVvglo3A5XlWSoaEypvOMo3IlVR9jqTyiowbtVvxcPtxXPJyzVTAbo3AyCG0vZFV6PtxWoJScoz5ypvtcPtxWPtyyoTyzVTAbo3AyCG0vZQNvBtbWPJWlMJSePtxW'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

# Coded by Cracker
# CRACKER911181
 

<<<<<<< HEAD

import os,time
try:
	import youtube_dl
except ModuleNotFoundError:
	os.system("pip install youtube_dl")
from youtube_dl import *




def yt():
	
	link=str(input("\n Enter Video Link: "))
	px=str(input(pest+"\n\t1.Download 360p\n\t2.Download 720p\n\t3.Download 1080p\n\t4.Download mp3\n\n Enter pixel: "))
	
	if px=="1":
		pixel="18"
		options={"format":""+pixel+""}
		
		print(blue+"\n[+]Downloading Start\n")
		try:
			YoutubeDL(options).download([link])
			print(green+"\n\n         Download Done")
		except youtube_dl.utils.DownloadError:
			print(red+"\n\n        Please Enter A  Valid Link")
		time.sleep(3.8)
	
	elif px=="2":
		pixel="22"
		options={"format":""+pixel+""}
#		link=str(input("\n Enter Video Link: "))
		print(blue+"\n[+]Downloading Start\n")
		try:
			YoutubeDL(options).download([link])
			print(green+"\n\n         Download Done")
		except youtube_dl.utils.DownloadError:
			print(red+"\n\n        Please Enter A  Valid Link")
		time.sleep(3.8)
	
	elif px=="3":
		pixel="137"
		options={"format":""+pixel+""}
#		link=str(input("\n Enter Url: "))
		print(blue+"\n[+]Downloading Start\n")
		try:
			YoutubeDL(options).download([link])
			print(green+"\n\n         Download Done")
		except youtube_dl.utils.DownloadError:
			print(red+"\n\n        Please Enter A  Valid Link")
		time.sleep(3.8)
	
	elif px=="4":
		pixel="140"
		options={"format":""+pixel+""}
#		link=str(input("\n Enter Url: "))
		print(blue+"\n[+]Downloading Start\n")
		try:
			YoutubeDL(options).download([link])
			print(green+"\n\n         Download Done")
		except youtube_dl.utils.DownloadError:
			print(red+"\n\n        Please Enter A  Valid Link")
		time.sleep(3.8)


#18 mp4 - 360p
#22 mp4 - 720p
#137 mp4 - 1080p without sound
#140 mp3 -audio only


def fb():
	
	try:
		link=str(input(rosy+"\n Enter Video Link: "))
		print(blue+"\n[+]Downloading Start")
		
		YoutubeDL().download([link])
		print(green+"\n\n     Download Done")
	except youtube_dl.utils.DownloadError:
		print(red+"\n⚠️This Video Maybe Private. This Tool can't Download Private Video⚠️   ")
		time.sleep(3.8)

#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest



while True:
	os.system('clear')
	print(blue+f"""
   ____                _                _____           _
  / ___|_ __ __ _  ___| | _____ _ __   |_   _|__   ___ | |
 """+blue+"""| |   | '__/ _` |/ __| |/ / _ \ '__|____| |/ _ \ / _ \| |
 """+pest+"""| |___| | | (_| | (__|   <  __/ | |_____| | (_) | (_) | |
  \____|_|  \__,_|\___|_|\_\___|_|       |_|\___/ \___/|_|\n\n """+green+"""             Crack Your World, If You Can\n\n\t          """+blue+"""[★] Downloader [★] \n"""+green+""" ========================================================="""+colouroff)
############################
	
	choose=str(input(pest+"\n\t\t1. YouTube Video Downloader\n\t\t2. Facebook Video Downloader\n\t\t"+red+"00.Back To Home\n\n"+rosy+"Enter Your Option: "))
	
	if choose=="1":
		yt()
	elif choose=="2":
		fb()
	elif choose=="00":
		break
	
=======
import base64, codecs
magic = 'aW1wb3J0IG9zLHRpbWUKdHJ5OgoJaW1wb3J0IHlvdXR1YmVfZGwKZXhjZXB0IE1vZHVsZU5vdEZvdW5kRXJyb3I6Cglvcy5zeXN0ZW0oInBpcCBpbnN0YWxsIHlvdXR1YmVfZGwiKQpmcm9tIHlvdXR1YmVfZGwgaW1wb3J0ICoKCgoKCmRlZiB5dCgpOgoJCglsaW5rPXN0cihpbnB1dCgiXG4gRW50ZXIgVmlkZW8gTGluazogIikpCglweD1zdHIoaW5wdXQocGVzdCsiXG5cdDEuRG93bmxvYWQgMzYwcFxuXHQyLkRvd25sb2FkIDcyMHBcblx0My5Eb3dubG9hZCAxMDgwcFxuXHQ0LkRvd25sb2FkIG1wM1xuXG4gRW50ZXIgcGl4ZWw6ICIpKQoJCglpZiBweD09IjEiOgoJCXBpeGVsPSIxOCIKCQlvcHRpb25zPXsiZm9ybWF0IjoiIitwaXhlbCsiIn0KCQkKCQlwcmludChibHVlKyJcblsrXURvd25sb2FkaW5nIFN0YXJ0XG4iKQoJCXRyeToKCQkJWW91dHViZURMKG9wdGlvbnMpLmRvd25sb2FkKFtsaW5rXSkKCQkJcHJpbnQoZ3JlZW4rIlxuXG4gICAgICAgICBEb3dubG9hZCBEb25lIikKCQlleGNlcHQgeW91dHViZV9kbC51dGlscy5Eb3dubG9hZEVycm9yOgoJCQlwcmludChyZWQrIlxuXG4gICAgICAgIFBsZWFzZSBFbnRlciBBICBWYWxpZCBMaW5rIikKCQl0aW1lLnNsZWVwKDMuOCkKCQoJZWxpZiBweD09IjIiOgoJCXBpeGVsPSIyMiIKCQlvcHRpb25zPXsiZm9ybWF0IjoiIitwaXhlbCsiIn0KIwkJbGluaz1zdHIoaW5wdXQoIlxuIEVudGVyIFZpZGVvIExpbms6ICIpKQoJCXByaW50KGJsdWUrIlxuWytdRG93bmxvYWRpbmcgU3RhcnRcbiIpCgkJdHJ5OgoJCQlZb3V0dWJlRE'
love = 'jbo3O0nJ9hplxhMT93ozkiLJDbJ2kcozgqXDbWPDyjpzyhqPuapzIyovfvKT5povNtVPNtVPNtVREiq25fo2SxVREiozHvXDbWPJI4L2IjqPO5o3I0qJWyK2EfYaI0nJkmYxEiq25fo2SxEKWlo3V6PtxWPKOlnJ50XUWyMPfvKT5povNtVPNtVPNtHTkyLKAyVRIhqTIlVRRtVSMuoTyxVRkcozfvXDbWPKEcoJHhp2kyMKNbZl44XDbWPtyyoTyzVUO4CG0vZlV6PtxWpTy4MJj9VwRmAlVXPDyipUEco25mCKfvMz9loJS0VwbvVvgjnKuyoPfvVa0XVjxWoTyhnm1mqUVbnJ5jqKDbVykhVRIhqTIlVSIloQbtVvxcPtxWpUWcoaDbLzk1MFfvKT5oX11Ro3qhoT9uMTyhMlOGqTSlqSkhVvxXPDy0pax6PtxWPIyiqKE1LzIRGPuipUEco25mXF5xo3qhoT9uMPuooTyhn10cPtxWPKOlnJ50XTqlMJIhXlWpoykhVPNtVPNtVPNtET93ozkiLJDtET9hMFVcPtxWMKuwMKO0VUyiqKE1LzIsMTjhqKEcoUZhET93ozkiLJESpaWipwbXPDxWpUWcoaDbpzIxXlWpoykhVPNtVPNtVPODoTIup2HtEJ50MKVtDFNtIzSfnJDtGTyhnlVcPtxWqTygMF5moTIypPtmYwtcPtxXPJIfnJLtpUt9CFV0VwbXPDyjnKuyoQ0vZGDjVtbWPJ9jqTyioaZ9rlWzo3WgLKDvBvVvX3OcrTIfXlVvsDbwPDyfnJ5eCKA0pvucoaO1qPtvKT4tEJ50MKVtIKWfBvNvXFxXPDyjpzyhqPuvoUIyXlWpoyfeKHEiq25fo2SxnJ5aVSA0LKW0KT4vXDbWPKElrGbXPDxWJJ91qUIvMHEZXT9jqTyioaZcYzEiq25fo2SxXSgfnJ5eKFxXPDxWpUWcoaDbM3WyMJ4eVykhKT4tVPNtVPNtVPORo3qhoT9uMPORo25yVvxXPDyyrTAypUDtrJ91qUIv'
god = 'ZV9kbC51dGlscy5Eb3dubG9hZEVycm9yOgoJCQlwcmludChyZWQrIlxuXG4gICAgICAgIFBsZWFzZSBFbnRlciBBICBWYWxpZCBMaW5rIikKCQl0aW1lLnNsZWVwKDMuOCkKCgojMTggbXA0IC0gMzYwcAojMjIgbXA0IC0gNzIwcAojMTM3IG1wNCAtIDEwODBwIHdpdGhvdXQgc291bmQKIzE0MCBtcDMgLWF1ZGlvIG9ubHkKCgpkZWYgZmIoKToKCQoJdHJ5OgoJCWxpbms9c3RyKGlucHV0KHJvc3krIlxuIEVudGVyIFZpZGVvIExpbms6ICIpKQoJCXByaW50KGJsdWUrIlxuWytdRG93bmxvYWRpbmcgU3RhcnQiKQoJCQoJCVlvdXR1YmVETCgpLmRvd25sb2FkKFtsaW5rXSkKCQlwcmludChncmVlbisiXG5cbiAgICAgRG93bmxvYWQgRG9uZSIpCglleGNlcHQgeW91dHViZV9kbC51dGlscy5Eb3dubG9hZEVycm9yOgoJCXByaW50KHJlZCsiXG7imqDvuI9UaGlzIFZpZGVvIE1heWJlIFByaXZhdGUuIFRoaXMgVG9vbCBjYW4ndCBEb3dubG9hZCBQcml2YXRlIFZpZGVv4pqg77iPICAgIikKCQl0aW1lLnNsZWVwKDMuOCkKCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBDcmFja2VyOTExMTgxCmNvbG91cm9mZj0iXHgxYlswMG0iICNjb2xvdXIgb2ZmCgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCgoKd2hpbGUgVHJ1ZToKCW9zLnN5c3RlbSgnY2xlYXInKQoJcHJpbnQoYmx1ZStmIiIiCi'
destiny = 'NtVS9sK18tVPNtVPNtVPNtVPNtVPNtKlNtVPNtVPNtVPNtVPNtVPOsK19sKlNtVPNtVPNtVPNtKjbtVP8tK19ssS8tK18tK18tKlNtK19ssPO8VS9sK19sVS8tK18tVPO8KlNtVS98K18tVPOsK18tsPO8PvNvVvVeLzk1MFfvVvW8VUjtVPO8VPqsKl8tK2NtsP8tK198VUjiVP8tKlOpVPqsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNtVvVvX2WfqJHeVvVvJ+XLuI0tET93ozkiLJEypvOo4cvSKFOpovVvVvgapzIyovfvVvVtCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09VvVvX2AioT91pz9zMvxXVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVjbWPtywnT9ip2H9p3ElXTyhpUI0XUOyp3DeVykhKUEpqQRhVSyiqIE1LzHtIzyxMJ8tET93ozkiLJEypykhKUEpqQVhVRMuL2Ivo29eVSMcMTIiVREiq25fo2SxMKWpoyk0KUDvX3WyMPfvZQNhDzSwnlOHolOVo21yKT5povVepz9mrFfvEJ50MKVtJJ91pvOCpUEco246VPVcXDbWPtycMvOwnT9ip2H9CFVkVwbXPDy5qPtcPtyyoTyzVTAbo29mMG09VwVvBtbWPJMvXPxXPJIfnJLtL2uio3AyCG0vZQNvBtbWPJWlMJSePtx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

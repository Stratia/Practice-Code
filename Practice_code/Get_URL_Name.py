#Excerise One//Complete//Get URL domain

domain = ('.com') or('.org') or('.gov')

def parse2_url():
  url2 = input('Enter URL: ')
  parsed2 = url2.split(f"{domain}",1)
  sub_par2 = parsed2[0].replace("https://","")
  print(sub_par2)
  input("")
      
parse2_url()
import datetime
import sqlite3

class Otel:

	def __init__(self,isim,soyisim,tc,adres,dogum_yili,cinsiyet,telefon_no,oda_tipi,oda_numarasi,kalicak_gun,fiyat):
		self.isim = isim
		self.soyisim = soyisim
		self.tc = tc
		self.adres = adres
		self.dogum_yili = dogum_yili
		self.cinsiyet = cinsiyet
		self.telefon_no = telefon_no
		self.oda_tipi = oda_tipi
		self.oda_numarasi = oda_numarasi
		self.kalicak_gun = kalicak_gun
		self.fiyat = fiyat



odalar = ["Aile","Tek","Cift"]

oda_fiyat ={
	"aile" : 300,
	"cift" : 200,
	"tek" : 100,
}

tutar = 0
bilgi = ["Ismi :","Soyismi :","TC","Adresi :" , "Dogum Yili","Cinsiyeti:","Telefonu :","Oda Tipi :","Oda Numarasi :" , "Kalacagi Gun :","Odenen Tutar :"]
oda_numaralari = ["1001","2001","3001","4001","5001"]



con = sqlite3.connect("staj.db")
cursor = con.cursor()

print("Polaris Otele Hosgeldiniz")
while(True):
	print("1-Kayit Yapmak Icin")
	print("2-Mevcut Olan Oda Numaralarimizi Gormek Icin")
	print("3-Rezarvasyonunuzu Gormek Icin")
	print("4-Rezarvasyon Iptali Icin")
	print("5-Cikmak icin 5'i tuslayiniz")
	secim = int(input())

	if(secim == 1):
		print("Kaydinizi Yapabilmemiz Icin Lutfen Asagidaki Bilgileri Giriniz.")
		isim = input("Isminiz:")
		isim = isim.lower()
		soyisim = input("Soyisminiz:")
		soyisim = soyisim.lower()
		tc = input("TC'nizi giriniz:")
		adres = input("Adresiniz:")
		dogum_yili = int(input("Dogum Yiliniz :"))
		year = datetime.date.today().year
		if((year - dogum_yili < 18 )):
			print("Otelimize Kayit Yapabilmeniz Icin 18 Yasindan Buyuk Olmaniz Gerekmektedir")
			break
			
		telefon_no = input("Telefon Numaraniz :")

		cinsiyet = input("Cinsiyetiniz:(Erkek/Kadin)")	

		for i in odalar:
			print("Odalarimiz :",i)

		oda_secim = input("Seciminiz:")
		oda_secim = oda_secim.lower()
		if(oda_secim == "aile"):
			tutar += oda_fiyat.get("aile")

		if(oda_secim == "cift"):
			tutar += oda_fiyat.get("cift")

		if(oda_secim == "tek"):
			tutar += oda_fiyat.get("tek")

		for i in oda_numaralari:
			print("Oda Numarasi :",i)

		oda_numarasi = int(input("Hangi Oda Numarasini Istiyorsunuz :"))
		
		print(oda_numarasi)
		if(oda_numarasi == 1001):
			oda_numarasi = oda_numaralari[0]
			oda_numaralari.pop(0)

		if(oda_numarasi == 2001):
			oda_numarasi = oda_numaralari[1]
			oda_numaralari.pop(1)

		if(oda_numarasi == 3001):
			oda_numarasi = oda_numaralari[2]
			oda_numaralari.pop(2)	
		
		if(oda_numarasi == 4001):
			oda_numarasi = oda_numaralari[3]
			oda_numaralari.pop(3)

		if(oda_numarasi == 5001):
			oda_numarasi = oda_numaralari[4]
			oda_numaralari.pop(4)		
			
		kalinacak_gun = int(input("Kac Gun Kalacaksiniz :"))

		tutar = kalinacak_gun * oda_fiyat.get(oda_secim)

		print("Toplam fiyat {}".format(tutar))
		print("{} odasinida {} oda numarasinda {} gun kalacaksiniz kabul ediyor musunuz".format(oda_secim,oda_numarasi,kalinacak_gun))
		kabul = input("Kabul Ediyor Musunuz (evet/hayır)")
		kabul = kabul.lower()

		if(kabul == "evet"):		
			print("Kayit Isleminiz Basariyla Yapilmistir")
			check = "CREATE TABLE IF NOT EXISTS KISI(Isim TEXT , SOYISIM TEXT , TC TEXT , ADRES TEXT , DOGUM_YILI INT , CINSIYET TEXT , TELEFON_NO INT , ODA_SECIM TEXT , ODA_NUMARASI INT , KALINACAK_GUN INT , TUTAR INT)"
			cursor.execute(check)
			con.commit()
			cursor.execute("INSERT INTO KISI VALUES (?,?,?,?,?,?,?,?,?,?,?)",(isim,soyisim,tc,adres,dogum_yili,cinsiyet,telefon_no,oda_secim,oda_numarasi,kalinacak_gun,tutar))
			con.commit()
			kisi = Otel(isim,soyisim,tc,adres,dogum_yili,cinsiyet,telefon_no,oda_secim,oda_numarasi,kalinacak_gun,tutar)

		if(kabul == "hayır"):
			print("Kabul Etmediniz Sizi Ana Menuye Yonlendiriyoruz ")

	if(secim == 2):
		for i in oda_numaralari:
			if(not oda_numaralari):
				print("Maalesef Hic Bos Odamiz Bulunmamaktadir")

			print(i)


	if(secim == 3):
		
		dbcheck1 = input("TC'nizi Giriniz :")
		cursor.execute("SELECT * FROM KISI WHERE TC = ?",(dbcheck1,))
		data = cursor.fetchone()
		
		if(data != None):
			counter = 0
			print("Bilgileriniz")
			for i in data:
				print(bilgi[counter],i)
				counter += 1
		else:
			print("Herhangi Bir Rezarvasyonunuz Bulunmamaktadir")		

	if(secim == 4):
		checkTc = input("TC'nizi giriniz :")
		cursor.execute("SELECT * FROM KISI WHERE TC = ?",(checkTc,))
		data = cursor.fetchone()
		if(data == None):
			print("Olmayan Rezarvasyonu Iptal Edemezsiniz")
			break
		else:
			counter = 0
			print("Rezarvasyonunuz :")
			for i in data:
				print(bilgi[counter],i)
				counter += 1
			check2 = input("Bu Islem Rezarvasyonunuzu Silecektir Onaylıyor Musunuz :(evet/hayir)")
			check2 = check2.lower()
			if(check2 == "evet"):
				cursor.execute("DELETE FROM KISI WHERE TC = ?",(checkTc,))
				con.commit()
				print("Rezarvasyonunuz Iptal Edilmistir\nIyi Gunler Dileriz")
				break

		
	if(secim == 5):
		print("Iyi Gunler Dileriz")
		break

	if(secim != 1 or secim != 2 or secim != 3 or secim != 4 or secim != 5):
		continue
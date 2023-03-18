# Python'da 5 veri tipi vardır.
# Metin Veri Tipleri : Metinsel verileri saklamak istediğimizde string(str) veri tipine ihtiyaç duyarız.

# Sayısal Veri Tipleri : int,float,complex 
# integer(int) veri tipi tam sayıların içerisinde tutulduğu veri tipidir.
# float veri tipi ondalık sayılar için kullanılan veri tipidir.
# complex veri tipi karmaşık sayılar için kullanılan veri tipidir.

# Boolean Veri Tipleri : bool mantıksal(true or false) durum için kullanılan veri tipidir.

# Sıralama Veri Tiplari :List Değerleri listeye dönüştüren veri tipidir.

#kodlama.io veri tipleri
#string
#kategori,eğitmen,kurslarım v.b

#list 
#eğitmen ["Engin Demiroğ", "Halit Enes Kalaycı"]

#integer 
#kursların tamamlanma yüzdesi yazılan yerdeki değerler integer veri tipidir.

email = "vrlmk7@gmail.com"
password = "vrlmk.12"

email = input("Lütfen mail adresinizi giriniz: ")
password = input("Lütfen şifrenizi giriniz: ")

if email == ("vrlmk7@gmail.com") and password == ("vrlmk.12"):
    print("Giriş başarılı.")
else:
    print("Email veya şifre yanlış.") 

import os
from datetime import date

def clear_screen():
    os.system('cls')
clear_screen()
def calculate_age(day, month, year):
    hari_ini = date.today()
    ultah = date(year, month, day)
    age = hari_ini.year - ultah.year - ((hari_ini.month, hari_ini.day) <= (ultah.month, ultah.day))
    return age

today = date.today()
a = True

while a:
    try:
        name = input('Masukkan Nama : ')
        day = input('Masukkan Tanggal:')
        month = input('Masukkan bulan:')
        year = input('Masukkan tahun:')
    
        age_result = calculate_age(int(day), int(month), int(year))
        clear_screen()
        print(f'\nNama : {name}')
        print(f'Umur anda saat ini {age_result} tahun ')
        print(f'Hari ini : {today}')
        while True :
            brl = input('Apakah masih ingin Melanjutkan ? (Y/N) :')
            
            if brl == 'y' or brl == 'Y':
                clear_screen()
                print('Silahkan Masukkan Data yang baru')
                break

            elif brl == 'n' or brl == 'N':
                clear_screen()
                print('\nTerimah kasih:) \n iLOPYU Freendd')
                a = False
                break
                
            else:
                print('yang dibolehkan cuman y/n!!')

    except:
        clear_screen()
        print('Gagal menghitung usia, baik tanggal, bulan, atau tahun tidak valid')
        print('Coba Masukkan Data dengan benar!!\n')

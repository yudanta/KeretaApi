#!/usr/bin/python
# Author : Yudanta
# contact : me@yudanta.web.id
# Desember 2011 

import sys
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

howto = 'cek jadwal kereta\nCara penggunaan : python kereta.py <date YYYYMMDD> <kode stasiun asal> <kode stasiun tujuan>'

def cek_jadwal():
    tanggal = sys.argv[1]
    dari = sys.argv[2]
    ke = sys.argv[3]

    url = 'http://www.kereta-api.co.id/jadwal-ka/jadwal-ka.html'

    formdata = {'tanggal' : tanggal, 'origination' : dari, 'destination' : ke}

    data = urllib.urlencode(formdata)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()

    soup = BeautifulSoup(the_page)
    
    tabel_informasi = soup.findAll('table')[1]

    get_all_name = tabel_informasi.findAll('tr', attrs={'class':'itRowTable0'})
    get_row_info = tabel_informasi.findAll('tr', attrs={'class':'itRowTable1'})

    print 'Jadwal Kereta Api Tanggal : ', tanggal
    print 'Dari : ', dari , '| Tujuan : ', ke

    for x in range(1, len(get_all_name), 1):
        print ''
        name = ''.join(get_all_name[x].find('td', text=True))
        print 'kereta : ', name

        kelas = ''.join(get_row_info[x].findAll('td', text=True)[3])
        tarif = ''.join(get_row_info[x].findAll('td', text=True)[5])
        jam_berangkat = ''.join(get_row_info[x].findAll('td', text=True)[1])
        jam_tiba = ''.join(get_row_info[x].findAll('td', text=True)[2])

        print 'kelas : ', kelas, '| harga tiket : ', tarif
        print 'jam berangkat', jam_berangkat, '| jam tiba', jam_tiba 

def main():
    if len(sys.argv) <= 1:
        print howto
        sys.exit(1)
    else:
        cek_jadwal()


if __name__ == "__main__":
    main()

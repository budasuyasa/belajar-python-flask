from flask import Flask
from flask import render_template
from flask import request
import xlsxwriter


app = Flask(__name__)


@app.route('/') #decorator
def hello_world():  # put application's code here
    return render_template("index.html")
    # return 'Halo nama saya Satya <a href="/tentang-saya">Tentang</a>'

@app.route('/tentang-saya')
def tentang_saya():
    return 'Saya kelas 9, umur saya 14 tahun'

@app.route('/kelas')
def kelas():
    return "Saya kelas 9"

@app.route('/daftar')
def daftar():
    return render_template('daftar.html')

@app.post('/daftar_proses')
def daftar_proses():
    nama = request.form['nama']
    alamat = request.form['alamat']
    kelas = request.form['kelas']
    
    workbook = xlsxwriter.Workbook("data.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write("A1", nama)
    worksheet.write("B1", alamat)
    worksheet.write("C1", kelas)
    workbook.close()
    
    return "Data sudah disimpan"
    


if __name__ == '__main__':
    app.run()

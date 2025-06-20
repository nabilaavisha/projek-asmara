from flask import Flask, render_template

# Inisialisasi Flask app
app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def home():
    return render_template('home.html', nama="Dear")

# Route untuk halaman puisi
@app.route('/wishlist')
def wishlist():
    return render_template('wishlist.html', nama="Sandro")


# Route untuk halaman galeri
@app.route('/galeri')
def galeri():
    return render_template('galeri.html', nama="Dear")

# Route untuk halaman musik
@app.route('/musik')
def musik():
    return render_template('musik.html', nama="Dear")

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)

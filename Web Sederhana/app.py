from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk halaman form
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Ambil data dari form
        nama = request.form['nama']
        email = request.form['email']
        
        # Lakukan sesuatu dengan data (contoh: print ke console)
        print(f"Nama: {nama}, Email: {email}")
        
        # Redirect ke halaman utama setelah submit
        return redirect(url_for('index'))
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Ganti port ke 5001 atau yang lain
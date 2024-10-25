from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Here we could process form data
        name = request.form.get('name')
        message = request.form.get('message')
        print(f"Received message from {name}: {message}")
        return redirect(url_for('home'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

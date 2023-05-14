from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign', methods=['POST'])
def sign():
    guest_name = request.form['guestbook_name']
    guest_message = request.form['guestbook_message']
    # Save the guestbook entry to a database or a file
    return f'Thank you, {guest_name}, for signing the guestbook!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

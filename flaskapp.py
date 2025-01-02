from flask import Flask, render_template, request, url_for, redirect
import pyautogui as pag
from datetime import datetime
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('htmlindex.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        fieldOfStudy = request.form.get('fieldOfStudy')
        profilePicture = url_for('static', filename=request.form.get('profilePicture'))
        cartidentitenationale = request.form.get('cartidentitenationale')
        codemassar = request.form.get('codemassar')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        return render_template(
            'htmlsubmit.html',
            firstName = firstName,
            lastName = lastName,
            profilePicture=profilePicture,
            fieldOfStudy = fieldOfStudy,
            cartidentitenationale = cartidentitenationale,
            codemassar = codemassar,
            email = email,
            phone = phone
        )
    else:
        return redirect(url_for('home'))


@app.route('/capture', methods=['POST'])
def capture_screenshot():
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    
    image_path = os.path.join(static_dir, 'CARD' + datetime.now().strftime('%d%m%Y%H%M%S') + '.png')
    
    
    pag.screenshot(image_path, region=(313-25, 253-25, 745+50, 340+50))

    os.startfile(image_path)
    
   
    return redirect(url_for('submit'))

if __name__ == '__main__':
    app.run(debug=True)

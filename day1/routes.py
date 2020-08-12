from day1 import app
from flask import render_template

# Home route


@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/favorite5')
def favorite5():
    header_name = "These Are My Top 5 Artists"
    item_dict= {1: 'HYUKOH', 2: 'MASEGO', 3: 'TALKING HEADS', 4: 'THE KILLERS', 5: 'LEWIS OF MAN'}
    return render_template('favorite5.html', header_name= header_name, item_dict= item_dict)



  
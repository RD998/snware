from flask import Flask, render_template, redirect, request, url_for
from forms import PastebinEntry, QuotationEntry, PastebinEntry2
from main import search, quota
from flask import CORS
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456789'

@app.route('/snware/clientRC', methods=['GET', 'POST'])
def signup():
    form = PastebinEntry()
    if form.is_submitted():
        result = request.form
        final = search(xlsx='SNWARE Client Rate Card- 2024.xlsx', sheetnm=result.get('bustype', type=str), ir=result.get('irp', type=str), tim=result.get('time', type=str), cont=result.get('countrys', type=str))
        return render_template('signup.html', form=form, moni=final, parse=True)
    return render_template('signup.html', form=form, parse=False, moni=0)

@app.route('/snware/supplierRC', methods=['GET', 'POST'])
def signin():
    form = PastebinEntry2()
    if form.is_submitted():
        result = request.form
        final = search(xlsx='SNWARE Supplie Rate Card-May 2024.xlsx', sheetnm=result.get('bustype', type=str), ir=result.get('irp', type=str), tim=result.get('time', type=str), cont=result.get('countrys', type=str))
        return render_template('signup.html', form=form, moni=final, parse=True)
    return render_template('signup.html', form=form, parse=False, moni=0)

@app.route('/snware/DPquote', methods=["GET", "POST"])
def quote():
    form = QuotationEntry()
    if form.is_submitted():
        result = request.form
        final = quota(file='Snware_DP_Quote.xlsx', cont=result.get('ContNo', type=int), ban=result.get('BanNo', type=int), weight=result.get('WeightNo', type=int), lvl=result.get('lvlselect', type=str), loi=result.get('loiselect', type=str))
        return render_template('index.html', form=form, parse=True, moni=final)
    return render_template('index.html', form=form, parse=False, moni=0)

@app.route('/snware/SPquote', methods=["GET", "POST"])
def quote1():
    form = QuotationEntry()
    if form.is_submitted():
        result = request.form
        final = quota(file='Snware_SP_Quote.xlsx', cont=result.get('ContNo', type=int), ban=result.get('BanNo', type=int), weight=result.get('WeightNo', type=int), lvl=result.get('lvlselect', type=str), loi=result.get('loiselect', type=str))
        return render_template('index.html', form=form, parse=True, moni=final)
    return render_template('index.html', form=form, parse=False, moni=0)

if __name__ == '__main__':
    app.run()
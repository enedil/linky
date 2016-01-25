#!/usr/bin/env python3

import time

from flask import Flask, request, render_template, redirect, url_for

import db

app = Flask(__name__, template_folder='.')
dbpath = 'db.json'

@app.route('/')
def index():
    all_entries = sorted(db.showall(), key=lambda dicti: int(dicti['timestamp']), reverse=True)
    return render_template('list.html', links=all_entries, fn_convert=db.showdate)

@app.route('/<path:href>')
def add_link(href):
    db.insert(url=href, path=dbpath)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

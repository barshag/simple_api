import flask
from flask import request
import pandas as pd
from datetime import datetime as dt


app =flask.Flask(__name__)


data = pd.read_csv('monarch.csv', names=['s','e','m']).set_index('m')

# What is dat?
series = pd.Series(index=range(data.s.min(),dt.now().year+1))

print(series)

for m in data.index:
    series.loc[data.loc[m].s:data.loc[m].e] = m
print(series)


@app.route('/', methods =['GET'])
def home():
    # arg = request.args['arg1']
    # return 'Hello World'
    year = int(request.args['year'])
    try:
        return (series.loc[year])
    except KeyError:
        return f'Invalid input({series.index.min()}-{series.index.max()}'

print(home(1999))
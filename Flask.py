from flask import Flask, render_template
from collections import OrderedDict
import datetime, requests, pytz, json
import os
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
apiKey = os.environ.get('API_KEY')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/nyc")
def weather():
    url = 'https://avwx.rest/api/multi/metar/KJFK,KLGA,KEWR,kISP,KFRG,KBDR,KDXR,KGON,KPOU,KFOK?token=' + apiKey
    res = requests.get(url).text
    goodData = json.loads(res, object_pairs_hook=OrderedDict)

    timeNow = datetime.datetime.now(tz=pytz.UTC)
    timeNYC = timeNow.astimezone(pytz.timezone('US/Eastern')).strftime('%a, %d of %b %H:%M')
    timeUTC = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%a, %d of %b %H:%M')
    timeOfDay = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%H:%M')
    dayOfMonth = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%d')

    return render_template("weather.html", data=goodData, timeNYC=timeNYC, timeUTC=timeUTC, dayOfMonth=dayOfMonth,
                           timeOfDay=timeOfDay)


@app.route("/la")
def weatherLA():
    url = 'https://avwx.rest/api/multi/metar/KLAX,KVNY,KONT,KSNA,KBUR,KWHP,KOXR,KSBA,KSMX?token=' + apiKey
    res = requests.get(url).text
    goodData = json.loads(res, object_pairs_hook=OrderedDict)

    timeNow = datetime.datetime.now(tz=pytz.UTC)
    timeNYC = timeNow.astimezone(pytz.timezone('US/Eastern')).strftime('%a, %d of %b %H:%M')
    timeUTC = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%a, %d of %b %H:%M')
    timeOfDay = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%H:%M')
    dayOfMonth = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%d')

    return render_template("weather.html", data=goodData, timeNYC=timeNYC, timeUTC=timeUTC, dayOfMonth=dayOfMonth,
                           timeOfDay=timeOfDay)


@app.route("/la")
def weatherSEA():
    url = 'https://avwx.rest/api/multi/metar/KLAX,KVNY,KONT,KSNA,KBUR,KWHP,KOXR,KSBA,KSMX?token=' + apiKey
    res = requests.get(url).text
    goodData = json.loads(res, object_pairs_hook=OrderedDict)

    timeNow = datetime.datetime.now(tz=pytz.UTC)
    timeNYC = timeNow.astimezone(pytz.timezone('US/Eastern')).strftime('%a, %d of %b %H:%M')
    timeUTC = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%a, %d of %b %H:%M')
    timeOfDay = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%H:%M')
    dayOfMonth = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%d')

    return render_template("weather.html", data=goodData, timeNYC=timeNYC, timeUTC=timeUTC, dayOfMonth=dayOfMonth,
                           timeOfDay=timeOfDay)


@app.route("/la")
def weatherDFW():
    url = 'https://avwx.rest/api/multi/metar/KLAX,KVNY,KONT,KSNA,KBUR,KWHP,KOXR,KSBA,KSMX?token=' + apiKey
    res = requests.get(url).text
    goodData = json.loads(res, object_pairs_hook=OrderedDict)

    timeNow = datetime.datetime.now(tz=pytz.UTC)
    timeNYC = timeNow.astimezone(pytz.timezone('US/Eastern')).strftime('%a, %d of %b %H:%M')
    timeUTC = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%a, %d of %b %H:%M')
    timeOfDay = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%H:%M')
    dayOfMonth = timeNow.astimezone(pytz.timezone('Zulu')).strftime('%d')

    return render_template("weather.html", data=goodData, timeNYC=timeNYC, timeUTC=timeUTC, dayOfMonth=dayOfMonth,
                           timeOfDay=timeOfDay)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
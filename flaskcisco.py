#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# when a GET arrives at /ciscoios/
# we want to TRY to pull our query params that may have been passed
# along with the GET

@app.route("/ciscoios/")
def ciscoios():
    try: # this TRY here is to catch errors, and send back more info beside 200 code
        qparms = {} # create dictionary
        # user passes switchname= or default "bootstrapped switch"
        # qparms = {"switchname=acmeinc006"}
        # ex: curl http://0.0.0.0:2224/ciscoios?switchname=acmeinc006
        # result: qparms = {"switchname": "acmeinc006"}
        # ex: curl http://0.0.0.0:2224/ciscoios?avgwindspeedofeuropenswallow=57
        # result: qparms = {"switchname": "bootstrapped switch"}
        qparms["switchname"]  = request.args.get("switchname", "bootstrapped switch")
        # user passes username= or default "admin"
        # ex: curl http://0.0.0.0:2224/ciscioios?switchname=acmeinc006&username=katie
        # result: qparms = {"switchname": "acmeinc006", "username": "katie"}
        # ex: curl http://0.0.0.0:2224/ciscioiso?avgwindspeedofeuropenswallow=57
        # result: qparms = {"switchname": "bootstrapped switch", "username": "admin"}
        qparms["username"]  = request.args.get("username", "admin")
        # user passes gateway= or default "0.0.0.0"
        qparms["defaultgateway"] = request.args.get("gateway", "0.0.0.0")
        # user passes ip= or default "0.0.0.0"
        qparms["switchIP"] = request.args.get("ip", "0.0.0.0")
        # user passes mask= or default "255.255.255.0"
        qparms["netmask"] = request.args.get("mask", "255.255.255.0")
        # user passes mtu= or default "1450"
        qparms["mtusize"] = request.args.get("mtu", "1450")

        # render template and save as baseIOS.conf
        return render_template("baseIOS.conf.j2", **qparms) # **qparms -unpack the dictionary - availables sent over the template and now unpack

    except Exception as err:
        return "Uh-oh! " + err

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


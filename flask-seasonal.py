#!/usr/bin/python3
from flask import Flask
from flask import request


app = Flask(__name__)

# when the user lands at the "root" (/)
# this should return text about services available
@app.route("/")
def zindex():
    return "Seasonal information is available at /inseason"

# when the user lands at "inseason" (/inseason)
# the query param "fruit" is expected
# if it is not supplied, send by an error message
# if the value associated with "fruit" does not exist
# send back "I am sorry we do not carry that item."
@app.route("/inseason")
def inseason():
    if request.args.get("fruit"):
        fruitq = request.args.get("fruit")
    else:
        return "To use this endpoint, you need to pass the query param 'fruit'"
    if fruitq == "strawberries":
        return "Yes, strawberries are in season"
    elif fruitq == "pumpkins":
        return "No, pumpkins are not in season"
    elif fruitq == "macinaw peaches":
        return "No, macinaw peaches are not quite in yet"
    else:
        return "I'm sorry, we do not carry that item"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

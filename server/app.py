import sqlite3
import re
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

db = sqlite3.connect(":memory:", check_same_thread=False)
db.execute(open("./server/schema.sql").read())


def valid_var(name: str) -> bool:
    return re.fullmatch(r"\w+", name) is not None


@app.route("/", methods=["GET"])
def get_all_vars():
    cur = db.cursor()
    cur.execute("SELECT varname FROM GlobalVars")
    rows = cur.fetchall()
    cur.close()
    return jsonify([r[0] for r in rows])


@app.route("/<var_name>", methods=["GET"])
def get_var(var_name):
    if not valid_var(var_name):
        abort(400, description="Invalid global variable name")
    cur = db.cursor()
    cur.execute("SELECT varval FROM GlobalVars WHERE varname = ?", [var_name])
    row = cur.fetchone()
    cur.close()
    if row is None:
        return jsonify(None)
    return jsonify(row[0])


@app.route("/<var_name>", methods=["POST"])
def post_var(var_name):
    if not valid_var(var_name):
        abort(400, description="Invalid global variable name")

    var_val = request.get_data(as_text=True)

    cur = db.cursor()
    cur.execute("SELECT 1 FROM GlobalVars WHERE varname = ?", [var_name])
    exists = cur.fetchone()

    if exists is None:
        cur.execute("INSERT INTO GlobalVars (varname, varval) VALUES (?, ?)",[var_name, var_val])
        db.commit()
        return "created", 201
    else:
        cur.execute("UPDATE GlobalVars SET varval = ? WHERE varname = ?",[var_val, var_name])
        db.commit()
        return "updated", 200


if __name__ == "__main__":
    app.run(debug=True)
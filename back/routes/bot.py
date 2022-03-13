from datetime import datetime
from back.utils import query_all, query_first
from back import app, engine
from flask import jsonify


@app.route("/get_film_info/<film_id>", methods=["GET"])
def get_status_user(film_id):
    with engine.connect() as con:
        query_film_info = f"""select film_name, film_desc, film_link
                           from films
                           where film_id = '{film_id}'"""
        value_film_info = query_all(query_film_info, con)
    return jsonify(value_film_info)



from datetime import datetime
from back.utils import query_all, query_first
from back import app, engine
from flask import jsonify, request


@app.route("/get_film_info/<film_id>", methods=["GET"])
def get_status_user(film_id):
    with engine.connect() as con:
        query_film_info = f"""select film_name, film_desc, film_link
                           from films
                           where film_id = '{film_id}'"""
        value_film_info = query_all(query_film_info, con)
    return jsonify(value_film_info)


@app.route("/reg", methods=["POST"])
def reg():
    username = request.json.get("username")
    print(username)
    with engine.connect() as con:
        query_req_check = f"""select exists (
                                select
                                from users
                                where username = '{username}'
                             )"""
        is_exists: bool = query_first(query_req_check, con)['exists']
    if is_exists:
        return 'User already exists', 409
    with engine.connect() as con:
        query_req = f"""insert into users(username, reg_date)
                        values('{username}', (select NOW()))"""
        con.execute(query_req)
    return 'OK', 200

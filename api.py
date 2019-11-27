from flask import Flask, request, jsonify, current_app, abort, send_from_directory, send_file,Response

app = Flask(__name__,static_url_path='')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Expose-Headers','X-Token')
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.route('/testapi/<data>',methods=["GET"])
def test(data):
    print 'aaaaa'

    return jsonify({'A': data})

@app.route('/userpass/<user>/<password>/<role>',methods=['GET'])
def usertest(user,password,role):
    userlist = [{"username": user,"password": password,"role":role},
                {"username": "abc","password": "ccc","role":"user"},
                {"username": "ccc","password": "ccc","role":"user"},
                {"username": "acc","password": "ccc","role":"user"}]
    data = {"result": userlist}
    return jsonify(data)

@app.route('/userpass/<user>/<password>/<role>',methods=['GET'])



app.run(host='localhost',port='5000')
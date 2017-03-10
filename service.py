from flask import Flask, request, jsonify
import random

app = Flask(__name__)
quotes = ['Ich behandel meinen Koerper wie einen Tempel', 'Gewoehn dich dran', 'Dein Handy ist schon laecherlich dreckig', 'Kein Mensch braucht PowerPoint', 'Mit so nem Stuhl wuerde ich bei Tipico auch nur Geld verlieren', 'Ich weiss gar nicht worauf ich gerade warte... Feierabend oder so','Du machst doch eh Excel','Das ist scheissegal, ich hab eh Tabletten', 'Das ist out of Context']
answers = ['Ja','Nein','Vielleicht','Frag Artur','Google das','Keine Ahnung man...','Mir ist bewust das des Leben oft ausichtslos ist denn Lebem heist rueckwerts nicht unsonst Nebel','du bist ne Schlampe ich bin ein normaler Mensch','du kanns Alles nicht schaffen wenn du es auch wirglich nicht willst du darfst nuhr nicht fest daran glaubem']

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    req_content = request.get_json(silent=True)

    if not req_content:
        return jsonify({"color": "red", "message": "WHUAT!?", "notify": True, "message_format": "text"}), 404

    message = req_content['item']['message']['message'].lower()
    # mentions = req_content['item']['message']['mentions'].lower()
    if 'dataman' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/LX8JyTC.jpg", "notify": True,"message_format": "text"}),201
    if 'volkskaffee' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/nwmsi10.jpg", "notify": True, "message_format": "text"}),201
    if 'deal' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/JEVTgfS.gifv", "notify": True, "message_format": "text"}),201
    if 'kebab' in message or 'kebap' in message:
        return jsonify({"color": "red", "message": "https://i.imgur.com/gPCKNum.jpg", "notify": True, "message_format": "text"}),201
    if 'vong' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/p0RqWqL.png", "notify": True, "message_format": "text"}),201
    if 'merlin' in message:
        return jsonify({"color": "red", "message": quotes[random.randint(0,len(quotes)-1)], "notify": True, "message_format": "text"}),201
    if 'orakel' in message:
        return jsonify({"color": "red", "message": answers[random.randint(0,len(answers)-1)], "notify": True, "message_format": "text"}),201
    if 'face' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/gWl6IMp.jpg", "notify": True, "message_format": "text"}),201
    
    return jsonify({"color": "red", "message": "Usage: /gerg (dataman|volkskaffee|deal|kebab|vong|merlin|facepalm|orakel)", "notify": False,"message_format": "text"}),201


#if __name__ == '__main__':
#    app.run()

from flask import Flask, request, jsonify
import random

app = Flask(__name__)
quotes = ['Ich behandel meinen Koerper wie einen Tempel', 'Gewoehn dich dran', 'Dein Handy ist schon laecherlich dreckig']

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    req_content = request.get_json(silent=True)

    if not req_content:
        return jsonify({"color": "red", "message": "WHUAT!?", "notify": True, "message_format": "text"}), 404

    message = req_content['item']['message']['message'].lower()
    # mentions = req_content['item']['message']['mentions'].lower()
    if 'dataman' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/LX8JyTC.jpg", "notify": True,"message_format": "text"}),201
    if 'volkskaffe' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/nwmsi10.jpg", "notify": True, "message_format": "text"}),201
    if 'deal' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/JEVTgfS.gifv", "notify": True, "message_format": "text"}),201
    if 'kebab' in message or 'kebap' in message:
        return jsonify({"color": "red", "message": "https://i.imgur.com/gPCKNum.jpg", "notify": True, "message_format": "text"}),201
    if 'vong' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/p0RqWqL.png", "notify": True, "message_format": "text"}),201
    if 'merlin' in message:
        return jsonify({"color": "red", "message": quotes[random.randint(0,len(quotes)-1)], "notify": True, "message_format": "text"}),201
    
    return jsonify({"color": "red", "message": "Usage: /gerg (dataman|volkskaffee|deal|kebab|vong|merlin)", "notify": False,"message_format": "text"}),201


#if __name__ == '__main__':
#    app.run()

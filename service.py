from flask import Flask, request, jsonify
import random

app = Flask(__name__)
quotes = ['Ich behandel meinen Koerper wie einen Tempel', 'Gewoehn dich dran',
          'Ich hab Zuhause ne Chips-Zange. Wirklich!', 'Ein Tempel braucht auch mal eine Pizza',
          'Dein Handy ist schon laecherlich dreckig', 'Kein Mensch braucht PowerPoint',
          'Mit so nem Stuhl wuerde ich bei Tipico auch nur Geld verlieren',
          'Ich weiss gar nicht worauf ich gerade warte... Feierabend oder so', 'Du machst doch eh Excel',
          'Das ist scheissegal, ich hab eh Tabletten', 'Das ist out of Context',
          'So viel dazu, du arbeitest den ganzen Tag', 'Was ist denn los mit dir? Du bist ein besserer Mensch',
          'Ich hab Angst da vergewaltigt zu werden. Ich bin leichte Beute',
          'OK,OK,OK,OK ... CHILL!',
          'Sind wir hier im Muggelverein?',
          'Paracetamol ist guenstig, das ist der Sinn dahinter', 'Kannst zu RTL damit gehen',
          'Matthias kommt zu uns. Ihr koennt eure Arbeit niederlegen']
answers = ['Ja', 'Nein', 'Vielleicht', 'Frag Artur', 'Google das', 'Keine Ahnung man...',
           'Mir ist bewust das des Leben oft ausichtslos ist denn Lebem heist rueckwerts nicht unsonst Nebel',
           'du bist nen Bot ich bin ein normaler Mensch',
           'du kanns Alles nicht schaffen wenn du es auch wirglich nicht willst du darfst nuhr nicht fest daran glaubem',
           'Wissenschafler fanden heraus dass der durchschnippliche Deutsche bei 1 Wasser tiefe vong 8 meter 20 nicht mehr stehn kann']
memes = ['http://i.imgur.com/JEVTgfS.gifv', 'http://i.imgur.com/yNXAZZk.gifv']
daniel = ['Daniel arbeitet schweissfrei', 'Daniel wird nie muede', 'Daniel schlaeft nie', 'Daniel ist immer vor der Chef in die Geschaeft']
fabi = ['Bachelor ist nur ne Trockenuebung']

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    req_content = request.get_json(silent=True)

    if not req_content:
        return jsonify({"color": "red", "message": "WHUAT!?", "notify": True, "message_format": "text"}), 404

    message = req_content['item']['message']['message'].lower()
    # mentions = req_content['item']['message']['mentions'].lower()
    if 'dataman' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/LX8JyTC.jpg", "notify": True,
                        "message_format": "text"}), 201
    if 'volkskaffee' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/nwmsi10.jpg", "notify": True,
                        "message_format": "text"}), 201
    if 'deal' in message:
        return jsonify({"color": "red", "message": memes[random.randint(0, len(memes) - 1)], "notify": True,
                        "message_format": "text"}), 201
    if 'kebab' in message or 'kebap' in message:
        return jsonify({"color": "red", "message": "https://i.imgur.com/gPCKNum.jpg", "notify": True,
                        "message_format": "text"}), 201
    if 'vong' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/p0RqWqL.png", "notify": True,
                        "message_format": "text"}), 201
    if 'merlin' in message:
        return jsonify({"color": "red", "message": quotes[random.randint(0, len(quotes) - 1)], "notify": True, "message_format": "text"}), 201
    if 'daniel' in message:
        return jsonify({"color": "red", "message": daniel[random.randint(0, len(daniel) - 1)], "notify": True, "message_format": "text"}), 201
    if 'orakel' in message:
        return jsonify({"color": "red", "message": answers[random.randint(0, len(answers) - 1)], "notify": True,
                        "message_format": "text"}), 201
    if 'fabi' in message:
        return jsonify({"color": "red", "message": fabi[random.randint(0, len(fabi) - 1)], "notify": True,
                        "message_format": "text"}), 201
    if 'face' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/gWl6IMp.jpg", "notify": True,
                        "message_format": "text"}), 201
    if 'daily' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/Or8tW0r.jpg", "notify": True,
                        "message_format": "text"}), 201
    if 'culi' in message:
        return jsonify({"color": "red", "message": "https://media3.giphy.com/media/VV5wLHAvgFxtu/giphy.gif", "notify": True,
                        "message_format": "text"}), 201
    if 'hype' in message:
        return jsonify({"color": "red", "message": "https://www.youtube.com/watch?v=l_VFWI-3YwA", "notify": True,
                        "message_format": "text"}), 201
    if 'machine' in message:
        return jsonify({"color": "red", "message": "http://i.imgur.com/gyEiR39.jpg", "notify": True,
                        "message_format": "text"}), 201

    return jsonify(
        {"color": "red", "message": "Usage: /gerg (culi|dataman|daniel|daily|volkskaffee|deal|kebab|vong|merlin|facepalm|orakel|machine)",
         "notify": False, "message_format": "text"}), 201

# if __name__ == '__main__':
#    app.run()

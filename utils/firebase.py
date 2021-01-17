import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

answers_collection = db.collection(u'answers')
userlogs_collection = db.collection(u'userlogs')
users_collection = db.collection(u'users')
route_collection = db.collection(u'routes')

dict_intents = set()
for doc in answers_collection.get():
    dict_intents.add(doc.get('intent'))

pathsdict = dict()
for doc in route_collection.get():
    pathsdict[doc.get('statename')] = doc.get('route')

def add_data(dict_intents):
    for key, val in dict_intents.items():
        payload = {"intent": key, "text": val[0]}
        if (len(val) > 1):
            payload["imgrefs"] = val[1:]
        else:
            payload["imgrefs"] = []
        answers_collection.document(key).set(payload)


def add_doc(intent, val):
    payload = {"intent": intent, "text": val[0]}
    if (len(val) > 1):
        payload["imgrefs"] = val[1:]
    else:
        payload["imgrefs"] = []
    answers_collection.document(intent).set(payload)


def add_routes(pathsdict):
    for key, val in pathsdict.items():
        payload = {"statename": key, "route": val}
        route_collection.document(key).set(payload)


"""
dict_intents = {
  "intentname1": [
      "text-reply1",
      "imgref1",
      "imgref2",
      .
      .
  ],
  "intentname2": [
      "text-reply2"
  ],
  .
  .
}

# Use a dictionary like this and call add_data function to add entries in the firestore database.
add_data(dict_intents)

# Use this for a single entry
add_doc("intent_name",["reply_text","img_ref1","img_ref2","img_ref3"])
"""

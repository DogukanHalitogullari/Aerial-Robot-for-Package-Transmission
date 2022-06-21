def getDataFromDatabase():
    cred = credentials.Certificate('elec-491-firebase-adminsdk-kywdd-6fe1edc613.json')
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    doc_ref = db.collection(u'location').document(u'location')

    doc = doc_ref.get()
    if doc.exists:
        situation = doc.to_dict()["situation"]
        packageType = doc.to_dict()["packageType"]
        requestedLatitude = doc.to_dict()["currentLocation"][0]["latitude"]
        requestedLongitude = doc.to_dict()["currentLocation"][0]["longitude"]
    else:
        print(u'Package not requested')
    
    return situation, packageType, requestedLatitude, requestedLongitude

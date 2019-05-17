# Flask API mit logistischem Regressionsmodell und Docker Deployment

Dieses Projekt bietet eine Flask API mit Anbindung an ein Machine Learning Modell und anschließendem Docker Deployment. Das logistische Regressionsmodell benutzt Ausschnitte aus https://www.datacamp.com/community/tutorials/machine-learning-models-api-python. Als Datengrundlage dient das "Titanic Dataset", das die Passagier nach Alter, Geschlecht und dem Abfahrtsort der Reise charakterisiert. Ziel des Modells ist es, das Überleben vorherzusagen (Ja/Nein). Diese Implementierung arbeitet mit serialisierter Modellerzeugung. Es wird ein Modell erzeugt und anschließend mittels Joblib gespeichert.

- model.py erzeugt Modell
- app.py für Webserver und API

Nach dem Deployment kann an 127.0.0.1:5000/predict eine API Anfrage im JSON Format gesendet werden.

Beispielhafte Anfrage:
[
	{"Age": 15, "Sex": "female", "Embarked":"S"}	
]

Beispielhafte Antwort:

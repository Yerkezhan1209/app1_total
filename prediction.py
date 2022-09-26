import joblib
def predict(data):
	prediction_model = joblib.load('final_model.sav')
	return prediction_model.predict(data)
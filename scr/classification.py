from deepface import DeepFace

def classify_age_gender(cropped_img):
    try:
        result = DeepFace.analyze(cropped_img, actions=["age", "gender"], enforce_detection=False)[0]
        age = result["age"]
        gender = result["gender"]
        if age < 13:
            return "male_kid" if gender == "Man" else "female_kid"
        else:
            return "male_adult" if gender == "Man" else "female_adult"
    except:
        return "unknown"
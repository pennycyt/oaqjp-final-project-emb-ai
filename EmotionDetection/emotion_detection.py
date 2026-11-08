import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_json, headers = headers)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    if response.status_code == 400:
        for emotion in emotions.keys():
            emotions[emotion] = 'None'
        emotion['dominant_emotion'] = 'None' 
    else:    
        score = 0
        for key, value in emotions.items():
            if value > score:
                score = value
                dominant_emotion = key
        emotions['dominant_emotion'] = dominant_emotion
    
    return emotions

from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    del(response['dominant_emotion'])
    formatted_response = "For the given statement, the system response is "
    for index, (key, value) in enumerate(response.items()):
        if index > 0 and index < len(response)-1:
            formatted_response += f", '{key}': {value}"
        elif index == 0:
            formatted_response += f"'{key}': {value}"
        else:
            formatted_response += f" and '{key}': {value}"
    return f"{formatted_response}. The dominant emotion is <b>{dominant_emotion}</b>."

@app.route('/')
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
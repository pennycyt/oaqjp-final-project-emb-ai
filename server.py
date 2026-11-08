"""
Flask app to detect emotions from input text
"""
from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

@app.route('/emotionDetector')
def sent_detector():
    """Run emotion detector and show the response in a formatted sentence"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    del response['dominant_emotion']
    formatted_response = "For the given statement, the system response is "
    for index, (key, value) in enumerate(response.items()):
        if 0 < index < len(response)-1:
            formatted_response += f", '{key}': {value}"
        elif index == 0:
            formatted_response += f"'{key}': {value}"
        else:
            formatted_response += f" and '{key}': {value}"
    return f"{formatted_response}. The dominant emotion is <b>{dominant_emotion}</b>."

@app.route('/')
def render_index_page():
    """"Render index.html for the main page"""
    return render_template("index.html")

@app.errorhandler(500)
def internal_server_error():
    """Return custom error message for error 500"""
    return "Invalid text! Please try again!."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

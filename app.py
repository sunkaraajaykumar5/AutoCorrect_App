from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def get_correction(text):
    try:
        blob = TextBlob(text)
        corrected = blob.correct()
        return str(corrected)
    except Exception as e:
        return f"❌ Error: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    corrected_text = ""
    user_text = ""
    if request.method == "POST":
        user_text = request.form.get("text", "")
        if user_text.strip():
            corrected_text = get_correction(user_text)
        else:
            corrected_text = "⚠️ Please enter some text."
    return render_template("index.html", user_text=user_text, corrected_text=corrected_text)

if __name__ == "__main__":
    app.run(debug=True)

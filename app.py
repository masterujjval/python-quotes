from flask import Flask, render_template, request
import random

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Do what excites!",
    "Remember why you started",
    "Till death all defeats are psycological",
    "Take steps which u like for the character development",
    "Dream it. Wish it. Do it."
]

@app.route("/", methods=["GET", "POST"])
def home():
    quote = None
    if request.method == "POST":
        quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)

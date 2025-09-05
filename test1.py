from flask import Flask, render_template, request
import random, time

app = Flask(__name__)

# Sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python programming is fun and powerful.",
    "Artificial Intelligence is the future of technology.",
    "Practice makes perfect in every skill you learn.",
    "Data science combines statistics and programming."
]

# Paragraphs
paragraphs = [
    """Technology has become an essential part of our daily lives. From smartphones to artificial intelligence, 
it shapes the way we work, communicate, and solve problems. The rapid pace of innovation continues to create 
new opportunities as well as challenges.""",

    """The importance of healthy living cannot be overstated. A balanced diet, regular exercise, and enough 
sleep contribute to a stronger body and a sharper mind. Small lifestyle changes can have a big impact 
on overall well-being.""",

    """Education is not limited to classrooms. With online courses, open resources, and virtual learning, 
knowledge is more accessible than ever before. Lifelong learning is the key to staying relevant in the 
fast-changing world we live in.""",

    """Nature has always inspired creativity and peace in human beings. The sound of birds, the flow of rivers, 
and the calmness of forests remind us of the beauty that exists beyond the rush of city life. Protecting the 
environment is protecting our own future.""",

    """Teamwork plays a vital role in achieving goals. When individuals come together with a shared purpose, 
their combined skills and ideas often lead to greater success. Collaboration encourages innovation, builds trust, 
and improves problem-solving abilities."""
]

# Store start time
start_times = {}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = None

    if request.method == "POST":
        if "choice" in request.form:  # user selected sentence or paragraph
            choice = request.form["choice"]
            if choice == "sentence":
                text = random.choice(sentences)
            else:
                text = random.choice(paragraphs)

            # Save start time in hidden field
            start_times[text] = time.time()
            return render_template("index.html", text=text, result=None, start_time=start_times[text])

        elif "typed" in request.form:  # user submitted typing
            typed = request.form["typed"]
            original = request.form["original"]
            start_time = float(request.form["start_time"])
            end_time = time.time()

            time_taken = end_time - start_time
            minutes = time_taken / 60
            words = len(typed.split())
            wpm = round(words / minutes, 2) if minutes > 0 else 0

            # Accuracy calculation
            correct_chars = sum(1 for i, c in enumerate(typed) if i < len(original) and c == original[i])
            accuracy = round((correct_chars / len(original)) * 100, 2)

            result = {
                "time_taken": round(time_taken, 2),
                "words": words,
                "wpm": wpm,
                "accuracy": accuracy
            }

    return render_template("index.html", text=text, result=result, start_time=None)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

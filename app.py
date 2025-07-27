from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    traits = request.form['traits'].lower()

    # Keyword-based logic
    if "emotional" in traits:
        personality = "🧠 The Empath"
        careers = ["Psychologist", "Writer", "Teacher"]
        hobbies = ["Journaling", "Art", "Helping others"]
        quote = "Your emotions are your strength, not your weakness."
        future = "You will find deep connections and peace through understanding others."

    elif "creative" in traits or "imaginative" in traits or "artistic" in traits:
        personality = "🎨 The Creator"
        careers = ["Designer", "Artist", "Content Creator"]
        hobbies = ["Painting", "Vlogging", "Crafting"]
        quote = "Creativity takes courage. Let your light shine."
        future = "Your passion will turn into purpose and prosperity."

    elif "logical" in traits or "analytical" in traits or "problem" in traits:
        personality = "🧩 The Analyst"
        careers = ["Engineer", "Data Scientist", "Programmer"]
        hobbies = ["Puzzles", "Coding", "Strategic games"]
        quote = "Logic is the beginning of wisdom, not the end."
        future = "Your intellect will lead to groundbreaking discoveries."

    elif "confident" in traits or "leader" in traits or "bold" in traits:
        personality = "🔥 The Leader"
        careers = ["Entrepreneur", "Manager", "Public Speaker"]
        hobbies = ["Debating", "Networking", "Volunteering"]
        quote = "Lead with confidence, inspire with action."
        future = "Your leadership will empower others and spark change."

    elif "introvert" in traits or "quiet" in traits or "shy" in traits:
        personality = "🌙 The Thinker"
        careers = ["Researcher", "Writer", "Developer"]
        hobbies = ["Reading", "Gaming", "Solo travel"]
        quote = "In silence, you find your deepest thoughts."
        future = "You will thrive in solitude and brilliance."

    else:
        personality = "🌍 The Explorer"
        careers = ["Travel Blogger", "Journalist", "Anthropologist"]
        hobbies = ["Travelling", "Photography", "Learning cultures"]
        quote = "Life is a journey — explore with an open heart."
        future = "Your adventures will shape your wisdom and identity."

    return render_template("result.html",
                           personality=personality,
                           careers=careers,
                           hobbies=hobbies,
                           quote=quote,
                           future=future)

if __name__ == '__main__':
    app.run(debug=True)
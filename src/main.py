import flask
import jinja2
import json
import random
import os

app = flask.Flask(__name__)


def load_quotes():
    """Load quotes from the JSON file."""
    quotes_file = os.path.join(os.path.dirname(__file__), "quotes.json")
    try:
        with open(quotes_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [{"text": "No quotes file found!", "author": "System"}]
    except json.JSONDecodeError:
        return [{"text": "Error reading quotes file!", "author": "System"}]


@app.route("/")
def home():
    """Return a random quote in HTML format."""
    quotes = load_quotes()
    random_quote = random.choice(quotes)
    return flask.render_template("quote.html", quote=random_quote)


@app.route("/json")
def get_quote_json():
    """Return a random quote in JSON format."""
    quotes = load_quotes()
    random_quote = random.choice(quotes)
    return flask.jsonify(random_quote)


@app.route("/all")
def get_all_quotes():
    """Return all quotes."""
    quotes = load_quotes()
    return flask.jsonify(quotes)


if __name__ == "__main__":
    # Get port from environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

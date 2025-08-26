# Quotes

A simple Flask app I hacked together to complement my [Leechblock](https://github.com/proginosko/LeechBlockNG) setup.

I wanted something to redirect myself to when visiting a few unpleasant time-sinks I have (looking at you here, [lichess](https://lichess.org)).

## Features
- Random quote from a json file, currently the Tao Te Ching (Ron Hogan translation)
- JSON API endpoint for programmatic access
- Easy to run locally or with Docker

## Quick Start (Docker)

1. **Build and run the app:**
   ```sh
   docker-compose up --build
   ```
   The app will be available at [http://localhost:5000](http://localhost:5000)

2. **Stop the app:**
   ```sh
   docker-compose down
   ```

## Endpoints
- `/` — Main page, random quote rendered in HTML
- `/json` — Random quote as JSON
- `/all` — All quotes as JSON

## Project Structure
```
leechblock/
├── src/
│   ├── main.py           # Flask app
│   ├── quotes.json       # Quotes data (from TAO.txt)
│   ├── TAO.txt           # Full text source (Ron Hogan translation)
│   ├── static/
│   │   └── quote.css     # Stylesheet for the quote card
│   └── templates/
│       └── quote.html    # HTML template
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Customizing Quotes
- To update the quotes, edit `src/quotes.json`.
- To change the style, edit `src/static/quote.css`.

## License
- The Tao Te Ching text (Ron Hogan translation) is used under the Creative Commons Attribution-NoDerivs-NonCommercial License.
- This app is for personal/non-commercial use only.

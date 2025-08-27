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

## Deploy to Google Cloud Run (Recommended)

1. **Authenticate with Google Cloud:**
   ```sh
   gcloud auth login
   gcloud config set project <YOUR_PROJECT_ID>
   ```

2. **Deploy using the provided script:**
   ```sh
   ./deploy.sh <YOUR_PROJECT_ID> [REGION]
   ```
   - The script sets minimal resources: 256MiB RAM, 1 CPU, concurrency 1, max 1 instance.
   - The service will be public (remove `--allow-unauthenticated` in `deploy.sh` if you want to restrict access).
   - Default region: `europe-west2` (can be overridden by specifying `[REGION]`).

3. **Get your Cloud Run URL:**
   The script will print a message at the end. You can also find the URL in the Google Cloud Console under Cloud Run > Services.

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

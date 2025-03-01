from flask import Flask, request, render_template
import pickle
import pandas as pd
import re 

# Load the trained model and feature names
with open("model.pkl", "rb") as file:
    data = pickle.load(file)
    model = data["model"]
    feature_names = data["features"]

# Initialize Flask app
app = Flask(__name__)

def extract_features(url):
    """Extracts features from a given URL to match trained model features."""
    features = {
        "having_IP_Address": 1 if re.match(r'\d+\.\d+\.\d+\.\d+', url) else 0,
        "URL_Length": len(url),
        "Shortining_Service": 1 if re.search(r"bit\.ly|goo\.gl|tinyurl|ow\.ly|t\.co", url) else 0,
        "having_At_Symbol": 1 if "@" in url else 0,
        "double_slash_redirecting": 1 if "//" in url[7:] else 0,
        "Prefix_Suffix": 1 if "-" in url else 0,
        "having_Sub_Domain": url.count('.') - 1,  # More subdomains = more suspicious
        "SSLfinal_State": 1 if url.startswith("https") else 0,
        "Domain_registeration_length": 1,  # Placeholder (Actual value needs WHOIS lookup)
        "Favicon": 1,  # Placeholder (Need web scraping)
        "port": 1,  # Placeholder (Need network scan)
        "HTTPS_token": 1 if "https" in url.lower() else 0,
        "Request_URL": 1,  # Placeholder (Requires HTML scraping)
        "URL_of_Anchor": 1,  # Placeholder
        "Links_in_tags": 1,  # Placeholder
        "SFH": 1,  # Placeholder
        "Submitting_to_email": 1 if "mailto:" in url else 0,
        "Abnormal_URL": 1,  # Placeholder (Need domain check)
        "Redirect": 1,  # Placeholder
        "on_mouseover": 1,  # Placeholder
        "RightClick": 1,  # Placeholder
        "popUpWidnow": 1,  # Placeholder
        "Iframe": 1,  # Placeholder
        "age_of_domain": 1,  # Placeholder (Requires WHOIS lookup)
        "DNSRecord": 1,  # Placeholder (Needs DNS check)
        "web_traffic": 1,  # Placeholder (Needs Alexa rank check)
        "Page_Rank": 1,  # Placeholder
        "Google_Index": 1,  # Placeholder (Needs Google search check)
        "Links_pointing_to_page": 1,  # Placeholder
        "Statistical_report": 1  # Placeholder
    }
    return pd.DataFrame([features])

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get("url")
    if not url:
        return render_template("index.html", prediction="⚠️ Please enter a URL")

    features = extract_features(url)

    # Ensure feature order matches training
    features = features[feature_names]

    prediction = model.predict(features)[0]
    result = "🚨 Phishing" if prediction == 1 else "✅ Legitimate"

    return render_template("index.html", prediction=f"Prediction: {result}", url=url)

if __name__ == '__main__':
    app.run(debug=True)

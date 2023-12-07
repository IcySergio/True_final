from flask import Flask, render_template, request, jsonify
import pandas as pd

df = pd.read_csv("out.csv")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/update_rows", methods=["POST"])
def update_rows():
    try:
        n = int(request.form.get("n"))
        filtered_rows = df[df['Price_USD'] <= n].sort_values(by='Price_USD', ascending=False).head(5)
        rows_to_display = filtered_rows.to_html(index=False)
    except ValueError:
        rows_to_display = "Please enter a valid number for 'n.'"

    return jsonify({'rows_to_display': rows_to_display})

@app.route("/map")
def plots():
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=True)




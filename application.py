from flask import Flask, request, render_template
import os
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler  
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)
app = application

# Health check for EB
@app.get("/health")
def health():
    return {"status": "ok"}, 200

# Home route — single definition
@app.get("/")
def index():
    """
    If templates/index.html exists, render it.
    Otherwise fall back to a simple visible string so EB doesn't look blank.
    """
    try:
        return render_template("index.html")
    except Exception:
        return "<h1>App is running ✔️</h1><p>Create templates/index.html to customize this page.</p>", 200

@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
     
        return render_template("home.html")
    else:
        # NOTE: fix swapped fields (reading <- reading, writing <- writing)
        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(request.form.get("reading_score")),
            writing_score=float(request.form.get("writing_score")),
        )

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template("home.html", results=results[0])

if __name__ == "__main__":
 
    port = int(os.getenv("PORT", 5010))
    app.run(host="0.0.0.0", port=port)

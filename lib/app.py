from flask import Flask, request
from flask_cors import CORS, cross_origin

from lib.models.model_service import modelService
from lib.analysis.analysis_service import analysis_service

app = Flask(__name__)

CORS(app)


@app.route(
    "/",
)
@cross_origin()
def home():
    return "<p>Hello world</p>"


@app.route(
    "/models",
)
@cross_origin()
def get_available_models():
    return [model.toDict() for model in modelService.get_available_models()]


@app.route("/analyze/sourcecode", methods=["POST"])
@cross_origin()
def analyze_sourcecode():
    data = request.get_json()
    modelId = data.get("modelId")
    sourcecode = data.get("sourcecode")

    try:
        model = modelService.get_model_by_id(modelId)
    except Exception as e:
        return {"error": str(e)}, 404

    analysis = model.analyze(sourcecode)
    return analysis_service.enhance_analysis(analysis).toDict()


@app.route("/analyze/bytecode", methods=["POST"])
@cross_origin()
def analyze_bytecode():
    data = request.get_json()

    modelId = data.get("modelId")
    bytecode = data.get("bytecode")

    try:
        model = modelService.get_model_by_id(modelId)
    except Exception as e:
        return {"error": str(e)}, 404

    analysis = model.analyze(bytecode)
    return analysis_service.enhance_analysis(analysis).toDict()

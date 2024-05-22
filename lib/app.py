from flask import Flask, request
from flask_cors import CORS, cross_origin

from lib.models.model_service import modelService

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
    print(request.headers)
    print(request.content_type)
    print(request.form)
    data = request.get_json()
    print(data)
    modelId = data.get("modelId")
    sourcecode = data.get("sourcecode")
    print(modelId)
    try:
        model = modelService.get_model_by_id(modelId)
    except Exception as e:
        return {"error": str(e)}, 404

    return model.analyze(sourcecode).toDict()


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

    return model.analyze(bytecode).toDict()

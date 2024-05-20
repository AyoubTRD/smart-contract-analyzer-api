from flask import Flask, request
from flask_cors import CORS, cross_origin

from lib.models.model_service import modelService

app = Flask(__name__)

CORS(app)

@app.route("/")
@cross_origin()
def home():
    return "<p>Hello world</p>"

@app.route('/models')
@cross_origin()
def get_available_models():
    return [model.toDict() for model in modelService.get_available_models()]

@app.route('/analyze/sourcecode')
@cross_origin()
def analyze_sourcecode():
    modelId = request.args.get('modelId')
    sourcecode = request.args.get('sourcecode')

    try:
        model = modelService.get_model_by_id(modelId)
    except Exception as e:
        return { 'error': str(e) }, 404

    return model.analyze(sourcecode).toDict()

@app.route('/analyze/bytecode')
@cross_origin()
def analyze_bytecode():
    modelId = request.args.get('modelId')
    bytecode = request.args.get('bytecode')

    try:
        model = modelService.get_model_by_id(modelId)
    except Exception as e:
        return { 'error': str(e) }, 404

    return model.analyze(bytecode).toDict()

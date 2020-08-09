import sys
sys.path.insert(1, '../paraphraser')

from paraphraser.inference import *
from flask import Flask, request, jsonify

from webargs import fields
from webargs.flaskparser import use_args

app = Flask(__name__)
checkpoint_path = "../data/train-20180325-001253/model-171856"
paraphraser_instance = Paraphraser(checkpoint_path)

@app.route('/healthcheck')
def health_check():
    return 'Ok'

@app.route('/paraphrase', methods=["POST"])
@use_args(
    {
        "phrase": fields.Str(required=True),
        "temperature": fields.Float(
            validate=lambda p: 0 <= p <= 1,
            missing=0.5),
        "strategy": fields.Str(
            validate=lambda p: p == 'GREEDY' or p == 'SAMPLE',
            missing='SAMPLE'
        )
    }, location="json")
def paraphrase(args):
    print(args)
    paraphrases = __perform_phrasing(args)
    print(paraphrases)
    return jsonify(paraphrases)

def __perform_phrasing(args):
    strategy = args["strategy"]
    phrase = args["phrase"]
    temp = args["temperature"]
    if strategy == "GREEDY":
        return paraphraser_instance.greedy_paraphrase(phrase)
    else:
        return paraphraser_instance.sample_paraphrase(phrase, temp, how_many=10)

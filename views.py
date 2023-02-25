from typing import Tuple, Union, Dict, List

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from query_maker import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)


@main_bp.route("/perform_query", methods=['POST'])
def perform_query() -> Union[Response, Tuple[Response, int]]:
    # get request
    data: Dict[str, Union[List[dict], str]] = request.json

    try:
        validated_data = BatchRequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    # many request
    result = None
    for query in validated_data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=validated_data['file_name'],
            data=result
        )

    # return app.response_class('', content_type="text/plain")
    return jsonify(result)

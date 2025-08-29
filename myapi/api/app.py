from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

FULL_NAME = "john_doe"
DOB = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

def process_data(data):
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_characters = []
    sum_numbers = 0
    alpha_concat = []

    for item in data:
        item_str = str(item)

        if item_str.isdigit():
            num = int(item_str)
            sum_numbers += num
            if num % 2 == 0:
                even_numbers.append(item_str)
            else:
                odd_numbers.append(item_str)

        elif item_str.isalpha():
            alphabets.append(item_str.upper())
            alpha_concat.extend(list(item_str))
        else:
            special_characters.append(item_str)

    alpha_concat = alpha_concat[::-1]
    concat_str = ""
    for i, ch in enumerate(alpha_concat):
        concat_str += ch.upper() if i % 2 == 0 else ch.lower()

    return {
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(sum_numbers),
        "concat_string": concat_str
    }

@app.route("/process", methods=["POST"])
def process():
    try:
        data = request.get_json()
        if not data or "data" not in data:
            return jsonify({
                "is_success": False,
                "error": "Invalid input, must contain 'data' array"
            }), 400

        result = process_data(data["data"])

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            **result
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "is_success": False,
            "error": str(e)
        }), 500


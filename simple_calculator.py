"""
This module implements the basic web-based calculator.
"""
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/calculate')
def simple_calculator():
    """
    Simple Calculator function to perform basic arithmetic operations.
    :return: The result of the arithmetic operation.
    """

    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if op == 'sum':
        result = arg1 + arg2
        op_symbol = '+'
    elif op == 'sub':
        result = arg1 - arg2
        op_symbol = '-'
    elif op == 'mul':
        result = arg1 * arg2
        op_symbol = '*'
    elif op == 'div':
        if arg2 != 0:
            result = arg1 / arg2
            op_symbol = '/'
        else:
            return jsonify(error='Division by zero is forbidden'), 400
    else:
        return jsonify(error='Invalid parameters or operation'), 400

    return f"{arg1} {op_symbol} {arg2} = {result}"

if __name__ == '__main__':
    app.run()

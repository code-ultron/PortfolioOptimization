from flask import Flask, request, jsonify
import os
from portfolio_optimization import run_optimization

app = Flask(__name__)

@app.route('/optimize_portfolio', methods=['POST'])
def optimize_portfolio():
    # Check if a file is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    # Get the file from the request
    file = request.files['file']
    file_path = os.path.join('/tmp', file.filename)
    file.save(file_path)

    # Get the total_fund parameter, default to 1000 if not provided
    total_fund = request.form.get('total_fund', default=1000, type=float)
    
    try:
        # Run the optimization function with the specified total_fund
        results = run_optimization(file_path, total_fund=total_fund)
        
        # Return the results as JSON
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up the saved file
        os.remove(file_path)

if __name__ == '__main__':
    app.run(port=4000, debug=True)

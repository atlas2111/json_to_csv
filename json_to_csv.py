from flask import Flask, request, jsonify, Response
import csv
from io import StringIO

app = Flask(__name__)


@app.route('/convert', methods=['POST'])
def convert_json_to_csv():
    try:
        # Get the raw JSON data from the request
        json_data = request.get_json()

        # Convert JSON to CSV
        csv_data = json_to_csv(json_data)

        # Create a response with CSV data
        response = Response(csv_data, content_type='text/csv')
        response.headers['Content-Disposition'] = 'attachment; filename=output.csv'

        return response

    except Exception as e:
        return jsonify({'error': str(e)}), 400


def json_to_csv(json_data):
    # Convert JSON to CSV
    csv_buffer = StringIO()
    writer = csv.DictWriter(csv_buffer, fieldnames=json_data[0].keys())
    writer.writeheader()
    writer.writerows(json_data)
    csv_data = csv_buffer.getvalue()
    csv_buffer.close()
    return csv_data


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from database import select_by_query

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search_contacts():
    search_query = request.args.get('q')
    contact = select_by_query(search_query)
    print(contact)
    contacts = [{'id': row[0], 'first_name': row[1], 'last_name': row[2], 'email': row[3]} for row in contact]
    return jsonify(contacts)


if __name__ == '__main__':
    app.run(debug=True)

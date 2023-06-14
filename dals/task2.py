from flask import jsonify
users={}
def register_dals(data):
    try:
        username = data['username']
        password = data['password']
        if username in users:
            return jsonify({'error': 'Username already exists'})
        users[username] = password
        return jsonify({'message': 'Registration successful'})
    except KeyError:
        return jsonify({'error': 'Invalid input: username or password is missing'})
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'})


def login_dals(data):
    try:
        username = data['username']
        password = data['password']
        if username not in users or users[username] != password:
            return jsonify({'message': 'Access denied'})
        return jsonify({'message': 'Access granted'})
    except KeyError:
        return jsonify({'error': 'Invalid input: username or password is missing'})
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'})



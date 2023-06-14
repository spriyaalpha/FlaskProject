from flask import jsonify

def calculate_sum_dal(data):
    try:        
        numbers = data['numbers']
        if not isinstance(numbers, list):
            raise ValueError('Invalid input: numbers should be a list')
        total_sum = sum(numbers)
        return jsonify({'sum': total_sum})
    except KeyError:
        return jsonify({'error': 'Invalid input: numbers key is missing'})
    except ValueError as e:
        return jsonify({'error': str(e)})
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'})
    

def concatenate_strings_dal(data):
    try:
        string1 = data['string1']
        string2 = data['string2']
        if not isinstance(string1, str) or not isinstance(string2, str):
            raise ValueError('Invalid input: both strings should be provided')
        result = string1 + string2
        return jsonify({'concatenated_string': result})
    except KeyError:
        return jsonify({'error': 'Invalid input: string1 or string2 key is missing'})
    except ValueError as e:
        return jsonify({'error': str(e)})
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'})    
        
    
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='.', static_folder='.')

def calculate_bmi(height_cm, weight_kg):
    """Calculate BMI and return value with category"""
    if height_cm <= 0 or weight_kg <= 0:
        return None, "Invalid input"
    
    # Convert height from cm to meters
    height_m = height_cm / 100
    
    # Calculate BMI: weight (kg) / height (m)^2
    bmi = weight_kg / (height_m ** 2)
    
    # Determine category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:  # bmi >= 30
        category = "Obese"
    
    return round(bmi, 1), category

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        height = float(data.get('height'))
        weight = float(data.get('weight'))
        
        bmi_value, category = calculate_bmi(height, weight)
        
        if bmi_value is None:
            return jsonify({'error': category}), 400
        
        return jsonify({
            'bmi': bmi_value,
            'category': category
        })
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input. Please enter valid numbers.'}), 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

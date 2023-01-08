from flask import Flask, render_template, request
from process import do_calculation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    errors = []
    
    try:
        number1 = float(request.form["number1"])
    except:
        errors.append("Informe o primeiro número corretamente.")
    try:
        number2 = float(request.form["number2"])
    except:
        errors.append("Informe o segundo número corretamente.")
    
    if errors:
        return render_template('index.html', errors=errors)
    
    if number1 is None or number2 is None:
        errors.append("Informe os números corretamente.")
        return render_template('index.html', errors=errors)
        
    sum_number = do_calculation(number1, number2)
    result = 'O resultado é: %s'%sum_number

    return render_template('result.html', result=result)
    

if __name__ == '__main__':
    app.run()


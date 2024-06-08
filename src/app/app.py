from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/test_db')
def db_test():
    connected_to_aws = True
    
    if connected_to_aws:
        return render_template('connected_to_aws.html')
    else:
        return "Error connecting to AWS RDS"

if __name__ == '__main__':
    app.run(debug=True)

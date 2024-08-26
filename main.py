from flask import Flask, request, render_template

app = Flask(__name__)

# Generate a random API ID
import uuid
def generate_api_id():
    return str(uuid.uuid4())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate the username and password (e.g. check if they exist in a database)
        # For this example, we'll just assume they're valid
        api_id = generate_api_id()
        # Store the API ID in a database or cache
        # For this example, we'll just print it to the console
        print(f"Generated API ID for {username}: {api_id}")
        return render_template('success.html', api_id=api_id)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

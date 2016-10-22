from flask import Flask
app = Flask("First App")

@app.route('/')
def index():
	return "Yes it is working"

@app.route('/next')
def next_route():
	return "Oh yes! it is next"

if __name__ == "__main__":
	app.run()
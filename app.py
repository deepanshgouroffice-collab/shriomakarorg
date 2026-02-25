from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    print("New Volunteer Registration:")
    print("Name:", name)
    print("Email:", email)
    print("Phone:", phone)
    print("Message:", message)

    return "Thank you for registering!"

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000, debug=True)
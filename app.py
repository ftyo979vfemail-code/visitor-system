from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        visitor_name = request.form.get("visitor_name")
        phone = request.form.get("phone")
        apartment = request.form.get("apartment")
        reason = request.form.get("reason")

        print("اسم الزائر:", visitor_name)
        print("رقم الهاتف:", phone)
        print("رقم الشقة:", apartment)
        print("سبب الزيارة:", reason)

        message = f"تم تسجيل الزائر {visitor_name} بنجاح"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)

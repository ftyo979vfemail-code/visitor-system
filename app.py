from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ضع رابط Webhook الخاص بـ n8n هنا
N8N_WEBHOOK_URL = "https://ryyyyy.app.n8n.cloud/webhook/visitor-register"


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    error_message = ""

    if request.method == "POST":
        visitor_name = request.form.get("visitor_name", "").strip()
        phone = request.form.get("phone", "").strip()
        apartment = request.form.get("apartment", "").strip()
        reason = request.form.get("reason", "").strip()

        visitor_data = {
            "visitor_name": visitor_name,
            "phone": phone,
            "apartment": apartment,
            "reason": reason
        }

        try:
            response = requests.post(
                N8N_WEBHOOK_URL,
                json=visitor_data,
                timeout=15
            )

            response.raise_for_status()

            message = f"تم تسجيل الزائر {visitor_name} بنجاح"

        except requests.exceptions.RequestException as e:
            print("n8n Error:", e)
            error_message = "حدث خطأ أثناء إرسال البيانات إلى n8n."

    return render_template(
        "index.html",
        message=message,
        error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)

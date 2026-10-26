from flask import Flask, render_template, request, jsonify
import re
import dns.resolver

app = Flask(__name__)


# --------------------------------------------------
# 1. Check basic email format
# --------------------------------------------------
def is_valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


# --------------------------------------------------
# 2. Check MX record
# --------------------------------------------------
def check_mx_record(domain):
    try:
        answers = dns.resolver.resolve(domain, "MX")

        if answers:
            return True

    except (
        dns.resolver.NoAnswer,
        dns.resolver.NXDOMAIN,
        dns.resolver.NoNameservers,
        dns.resolver.Timeout
    ):
        return False

    except Exception:
        return False

    return False


# --------------------------------------------------
# 3. Check individual email
# --------------------------------------------------
def check_email(email):

    email = email.strip().lower()

    # Empty input
    if not email:
        return {
            "email": email,
            "status": "Unknown",
            "reason": "Empty input"
        }

    # Step 1: Format validation
    if not is_valid_email(email):
        return {
            "email": email,
            "status": "Likely to bounce",
            "reason": "Invalid email format"
        }

    # Get domain
    domain = email.split("@")[1]

    # Step 2: MX record check
    has_mx = check_mx_record(domain)

    # No mail server
    if not has_mx:
        return {
            "email": email,
            "status": "Likely to bounce",
            "reason": "No mail server (MX record) found for this domain"
        }

    # Valid email + MX record exists
    return {
        "email": email,
        "status": "Likely to be delivered",
        "reason": "Valid email format and mail server (MX record) found"
    }


# --------------------------------------------------
# 4. Home page
# --------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# --------------------------------------------------
# 5. Email checking API
# --------------------------------------------------
@app.route("/check", methods=["POST"])
def check():

    try:
        data = request.get_json()

        if not data or "emails" not in data:
            return jsonify({
                "error": "No email addresses were provided"
            }), 400

        emails = data["emails"]

        if not isinstance(emails, list):
            return jsonify({
                "error": "Invalid input format"
            }), 400

        results = []

        for email in emails:
            results.append(check_email(email))

        return jsonify(results)

    except Exception as error:

        return jsonify({
            "error": "An unexpected error occurred",
            "details": str(error)
        }), 500


# --------------------------------------------------
# 6. Run application
# --------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
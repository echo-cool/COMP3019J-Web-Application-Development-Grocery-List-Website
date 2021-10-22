from os import environ

from project import app

# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=environ.get("PORT", 5000))

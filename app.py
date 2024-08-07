"""
A sample Hello World server.
"""
import os
from flask import Flask, render_template
from google.cloud import translate_v2 as translate

# pylint: disable=C0103
app = Flask(__name__)

# Initialize the Translate client
translate_client = translate.Client()

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    message = "It's running!"

    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')

    # Example translation
    target_language = 'es'  # Spanish 
    translation = translate_client.translate(
        message, target_language=target_language
    )
    translated_message = translation['translatedText']

    return render_template('index.html',
        message=message,
        Service=service,
        Revision=revision,
        translated_message=translated_message
    )

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')

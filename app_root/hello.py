from flask import Flask
from flask import render_template as render
from flask import request
from flask import abort
import os

app = Flask(__name__)

# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT

cf_port = int(os.getenv("PORT", 8080))

@app.route('/')
def hello():
    return 'Hello World.'

@app.route('/vars')
def showCFVariables():
    cf_var_dict = {}

    # Get all environment variables from the CF application container
    for k in os.environ:
        cf_var_dict[k] = os.getenv(k)

    # Get the HTTP request header
    headers = request.headers

    return render('index.html', cf_variables=cf_var_dict, http_headers=headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=cf_port, debug=True)


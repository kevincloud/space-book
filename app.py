from flask import Flask
from flask import render_template
import ldclient
from ldclient.config import Config
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('app.ini')
sdk_key = config['App']['SDKKey']
enable_ratings = ""
new_layout = ""

def show_message(s):
    print("*** %s" % s)
    print()

def get_flags():
    global enable_ratings
    global new_layout

    ldclient.set_config(Config(sdk_key))

    if ldclient.get().is_initialized():
        show_message("SDK successfully initialized!")
    else:
        show_message("SDK failed to initialize")
        exit()

    user = {
        "key": "webapp-demo",
        "name": "Kevin Cochran"
    }

    enable_ratings = ldclient.get().variation("enableRatings", user, False)
    new_layout = ldclient.get().variation("newLayout", user, False)

    ldclient.get().close()


@app.route("/")
def get_feature():  
    get_flags()
    return render_template("index.html",
        enable_ratings=enable_ratings,
        new_layout=new_layout)
        
if __name__ == '__main__':
    app.run(debug=True)

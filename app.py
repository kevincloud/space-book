from flask import Flask
from flask import render_template
import ldclient
from ldclient.config import Config
import configparser
import syslog

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('app.ini')
sdk_key = config['App']['SDKKey']
enable_ratings = ""
new_layout = ""
heading_color = ""


def show_message(s):
    print("*** %s" % s)
    print()


def get_flags():
    global enable_ratings
    global new_layout
    global heading_color

    ldclient.set_config(Config(sdk_key))

    if ldclient.get().is_initialized():
        show_message("SDK successfully initialized!")
    else:
        show_message("SDK failed to initialize")
        exit()

    user_context = {
        "key": "f2a04a9b-8e6f-4684-8da3-38e8dfda38cd",
        "custom": {
            "user-type": "beta",
            "location": "GA"
        }
    }
    colormap = {
        'light-blue': 'has-background-info',
        'light-green': 'has-background-primary',
        'red': 'has-background-danger',
        'blue': 'has-background-link',
        'green': 'has-background-success',
        'gray': 'has-background-grey-light'
    }

    enable_ratings = ldclient.get().variation("enableRatings", user_context, False)
    new_layout = ldclient.get().variation("newLayout", user_context, False)
    heading_color = colormap[ldclient.get().variation(
        "headingColor", user_context, False)]

    ldclient.get().close()


@app.route("/")
def get_feature():
    get_flags()
    return render_template("index.html",
                           enable_ratings=enable_ratings,
                           new_layout=new_layout,
                           heading_color=heading_color)


@app.route("/killit")
def kill_feature():
    print("running `killit`")
    syslog.syslog(syslog.LOG_ERR,
                  "LDERROR: enableRatings: Something is wrong!")
    return "done"


if __name__ == '__main__':
    syslog.syslog("Starting app...app is running.")
    app.run(debug=True)

# Import Flask
from flask import Flask

# Create an app
app = Flask(__name__)


# Define routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/startdate<br/>"
        f"/api/v1.0/enddate<br/>"
)






if __name__ == "__main__":
    app.run(debug=True)
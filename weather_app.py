from flask import Flask, render_template, request
from flask_cors import CORS
from weather_controller import WeatherController

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/weather', methods=['POST', 'GET'])
def process_weather():
    if request.method == 'POST':
        data = request.json
        input_location = data['location']

        weather = WeatherController()

        geo_location = weather.getLocation(input_location)
        if geo_location == None:
            address = "Unknown location"
            report_template = render_template('reports.html', weather_address=address)
            return report_template

        address = geo_location.address
        weather_reports = weather.getWeatherReports(data, geo_location)

        report_template = render_template('reports.html', weather_address=address, weather_reports=weather_reports)

    return report_template


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

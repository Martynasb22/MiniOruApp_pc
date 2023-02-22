import sys
import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Oro prognozė')
        self.setGeometry(100, 100, 400, 200)

        self.city_label = QLabel('Pasirinkite miestą:')
        self.city_combo = QComboBox()
        self.city_combo.addItems(['Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai', 'Panevėžys'])

        self.weather_label = QLabel('')
        self.weather_button = QPushButton('Rodyti orą')
        self.weather_button.clicked.connect(self.get_weather)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.city_label)
        hbox.addWidget(self.city_combo)
        vbox.addLayout(hbox)
        vbox.addWidget(self.weather_label)
        vbox.addWidget(self.weather_button)

        self.setLayout(vbox)

    def get_weather(self):
        city = self.city_combo.currentText()
        url = f'http://wttr.in/{city}?format=%C\n%t\n'
        response = requests.get(url)
        self.weather_label.setText(response.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())





    def get_weather_icon_url(city):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8d4f200ac45a8d5a9f3b55f1a4df5f35'
        response = requests.get(url)
        data = response.json()
        weather_id = data['weather'][0]['id']
        icon = get_icon_name(weather_id)
        return f'http://openweathermap.org/img/w/{icon}.png'


    def get_icon_name(weather_id):
        if weather_id < 300:
            return '11d'  # thunderstorm with rain
        elif weather_id < 500:
            return '10d'  # light rain
        elif weather_id < 600:
            return '09d'  # moderate rain
        elif weather_id < 700:
            return '13d'  # snow
        elif weather_id == 800:
            return '01d'  # clear sky
        elif weather_id == 801:
            return '02d'  # few clouds
        elif weather_id == 802:
            return '03d'  # scattered clouds
        elif weather_id == 803 or weather_id == 804:
            return '04d'  # broken clouds
        else:
            return 'question-mark'  # default icon for unknown weather conditions


    def get_weather_icon(city):
        url = get_weather_icon_url(city)
        response = requests.get(url)
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        return pixmap


    def get_weather(self):
        city = self.city_combo.currentText()
        url = f'http://wttr.in/{city}?format=%C\n%t\n'
        response = requests.get(url)
        weather = response.text.strip()



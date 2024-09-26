import logging

from flask import Flask

from model import Target, Country, City, TargetIndustry, TargetType

from repository.database import create_tables

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
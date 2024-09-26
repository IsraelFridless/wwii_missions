import logging

from controllers.target_controller import targets_blueprint
from utils.database_manager import execute_sql_from_file
from flask import Flask

from model import Target, Country, City, TargetIndustry, TargetType

from repository.database import create_tables, drop_tables

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    # drop_tables()
    # create_tables()
    # execute_sql_from_file('./sql_files/normalize_tables.sql')
    app.register_blueprint(targets_blueprint, url_prefix="/api/targets")
    app.run(debug=True)
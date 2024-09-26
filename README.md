# **WWII Missions Project**

This project is designed to manage and analyze World War II mission data. The project consists of several components, including data models, database repositories, and configuration files.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Data Models](#data-models)

## Installation

1. Ensure you have Python 3.12.4 installed.
2. Clone the repository:
    ```bash
    git clone https://github.com/IsraelFridless/wwii_missions.git
    ```
3. Navigate to the project directory:
    ```bash
    cd wwii_missions
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the project, first uncomment the function calls in the main.py file, and then execute the following command:
```bash
python main.py
```

## Project Structure

```plaintext
wwii_missions/
├── data/
│   └── results.txt
├── repository/
│   └── database.py
│   └── target_repository.py
├── model/
│   └── City.py
│   └── Country.py
│   └── Target.py
│   └── TargetIndustry.py
│   └── TargetType.py
└── config/
    └── base.py
```

### `data/`
Contains data files such as `results.txt` which holds analized data results from queries.

### `repository/`
Contains repository classes, e.g., `database.py` and `target_repository.py`, which handle database interactions.

### `model/`
Contains data models representing various entities such as `City`, `Country`, `Target`, `TargetIndustry`, and `TargetType`.

### `config/`
Contains configuration files such as `base.py` which holds configuration settings.

## Configuration

Configuration can be adjusted in `config/base.py`. Make sure to set the appropriate database connection strings and other settings as required.

## Data Models

- **City.py**: Represents city data for mission targets.
- **Country.py**: Represents country data for mission targets.
- **Target.py**: Represents the main target entity including its type and industry.
- **TargetIndustry.py**: Represents the industry related to the target.
- **TargetType.py**: Represents the type of the target.

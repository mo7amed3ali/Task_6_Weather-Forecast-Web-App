# Weather Forecast Web App

A Django-based Weather Forecasting Web Application powered by a trained SARIMAX time-series model. The application allows users to select a date and receive a predicted daily average temperature with a 95% confidence interval.

## Project Overview

This project integrates Time Series Forecasting with Web Development to provide an interactive weather forecasting experience.

The forecasting model was trained using historical Cairo weather data from 2016 to 2023 and uses seasonal Fourier features to capture yearly temperature patterns.

The Django application loads the pre-trained model and generates temperature forecasts for selected dates.

## Features

* Interactive weather forecasting interface.
* Date-based temperature predictions.
* SARIMAX time-series forecasting.
* Fourier features for annual seasonality.
* 95% confidence intervals.
* Responsive web interface.
* Pre-trained model integration without retraining.

## Technologies Used

| Technology       | Purpose                               |
| ---------------- | ------------------------------------- |
| Python           | Core programming language             |
| Django           | Web application framework             |
| Pandas           | Data manipulation                     |
| NumPy            | Numerical computations                |
| Statsmodels      | SARIMAX forecasting                   |
| HTML5            | Web page structure                    |
| CSS3             | UI styling                            |
| Jupyter Notebook | Model development and experimentation |
| Git & GitHub     | Version control                       |

## Machine Learning Model

**Model:** SARIMAX (1, 0, 1)

**Target Variable:** `T2M` (Daily Average Temperature)

**Training Period:** 2016–2023

**Fourier Features:** K = 3, Period = 365.25 days

The model uses six Fourier features:

* sin_1, cos_1
* sin_2, cos_2
* sin_3, cos_3

These features help represent annual seasonal patterns in temperature.

### Forecasting Output

For each selected date, the application displays:

* Predicted average temperature (°C).
* Lower confidence bound.
* Upper confidence bound.

**Important Note:** The trained model uses historical data ending on December 31, 2023. Therefore, the current application supports forecasts for January 1, 2024, through December 31, 2025. These are model-based extrapolations, not live weather forecasts.

## Project Structure

```text
Task_6_Weather-Forecast-Web-App/
│
├── manage.py
├── sarimax_weather_model.pkl
├── Task_6.ipynb
│
├── weather/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   └── weather/
│       └── home.html
│
└── .gitignore
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mo7amed3ali/Task_6_Weather-Forecast-Web-App.git
```

### 2. Navigate to the Project Directory

```bash
cd Task_6_Weather-Forecast-Web-App
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```powershell
.\venv\Scripts\Activate
```

### 5. Install Dependencies

```bash
pip install django numpy pandas statsmodels
```

### 6. Configure the Django Secret Key

Generate a new secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Set it as an environment variable in PowerShell:

```powershell
$env:DJANGO_SECRET_KEY = "YOUR_SECRET_KEY"
```

Never commit your actual secret key to GitHub.

### 7. Apply Database Migrations

```bash
python manage.py migrate
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Model File

The pre-trained SARIMAX model is included in the repository:

`sarimax_weather_model.pkl`

The application loads this model directly, so model training is not required to run the web application.

## Future Improvements

* Integrate live weather APIs.
* Update the forecasting model with recent weather observations.
* Extend forecasting capabilities to multiple cities.
* Improve forecasting accuracy through model experimentation.
* Deploy the application to a cloud hosting platform.

## Author

**Mohamed Ali**

* GitHub: https://github.com/mo7amed3ali
* LinkedIn: https://www.linkedin.com/in/mohamed-ali-cs
* Portfolio: https://mo7amed3ali.github.io/portfolio/#contact

---

**Weather Forecast Web App — Combining Time Series Forecasting and Web Development.**

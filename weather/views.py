from pathlib import Path
from datetime import date

import numpy as np
import pandas as pd

from django.shortcuts import render
from statsmodels.tsa.statespace.sarimax import SARIMAXResults


# Load the trained SARIMAX model
MODEL_PATH = (
    Path(__file__).resolve().parent.parent
    / "sarimax_weather_model.pkl"
)

model = SARIMAXResults.load(str(MODEL_PATH))


# Model training end date
TRAIN_END_DATE = pd.Timestamp("2023-12-31")

# Allowed forecast period
MIN_FORECAST_DATE = date(2024, 1, 1)
MAX_FORECAST_DATE = date(2025, 12, 31)


def fourier_features(index, K=3, period=365.25):
    """Generate Fourier features for the requested dates."""

    day_of_year = index.day_of_year.to_numpy()

    features = {}

    for k in range(1, K + 1):
        features[f"sin_{k}"] = np.sin(
            2 * np.pi * k * day_of_year / period
        )

        features[f"cos_{k}"] = np.cos(
            2 * np.pi * k * day_of_year / period
        )

    return pd.DataFrame(features, index=index)


def home(request):
    """Display the weather forecast page and handle predictions."""

    context = {}

    if request.method == "POST":

        selected_date = request.POST.get("forecast_date")

        try:
            target_date = date.fromisoformat(selected_date)

            if not MIN_FORECAST_DATE <= target_date <= MAX_FORECAST_DATE:
                raise ValueError(
                    "Please select a date between 2024 and 2025."
                )

            forecast_dates = pd.date_range(
                start=TRAIN_END_DATE + pd.Timedelta(days=1),
                end=pd.Timestamp(target_date),
                freq="D"
            )

            exog_features = fourier_features(forecast_dates)

            forecast_result = model.get_forecast(
                steps=len(forecast_dates),
                exog=exog_features
            )

            predicted_temperature = float(
                forecast_result.predicted_mean.iloc[-1]
            )

            confidence_interval = forecast_result.conf_int().iloc[-1]

            context = {
                "forecast_date": target_date.isoformat(),
                "predicted_temperature": round(
                    predicted_temperature, 2
                ),
                "lower_bound": round(float(confidence_interval.iloc[0]), 2),
                "upper_bound": round(float(confidence_interval.iloc[1]), 2),
            }

        except (ValueError, TypeError):
            context["error"] = (
                "Invalid date. Please select a date between "
                "2024-01-01 and 2025-12-31."
            )

    return render(request, "weather/home.html", context)
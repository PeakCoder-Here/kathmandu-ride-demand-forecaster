# 🛵 Kathmandu Ride Demand Forecaster

An AI-powered ride demand forecasting dashboard for Kathmandu zones. This project uses a Gradient Boosting machine learning model trained on 51,840 ride records to predict peak demand by zone, hour, weather conditions, and more.

## Overview

This application provides real-time demand forecasting for ride-sharing services in Kathmandu. By analyzing historical ride data and various contextual factors, the model accurately predicts demand patterns across different zones and time periods, helping optimize resource allocation and improve service availability.

## ✨ Features

- **Zone-Based Forecasting**: Predicts demand for specific areas across Kathmandu
- **Hourly Predictions**: Forecasts demand patterns throughout the day
- **Weather Integration**: Incorporates weather conditions into demand predictions
- **Interactive Dashboard**: Built with Streamlit for real-time visualization
- **Gradient Boosting Model**: Advanced ML model trained on 51,840 ride records
- **Interactive Visualizations**: Plotly charts for exploring demand patterns

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web dashboard
- **Machine Learning**: [Scikit-learn](https://scikit-learn.org/) - Gradient Boosting model
- **Data Processing**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visualization**: [Plotly](https://plotly.com/) - Interactive charts
- **Language**: Python

## 📋 Project Structure

```
kathmandu-ride-demand-forecaster/
├── app.py                    # Main Streamlit application
├── model.ipynb              # ML model development and training notebook
├── generate_data.ipynb      # Data generation and preprocessing notebook
├── requirements.txt         # Python dependencies
├── kathmandu_rides.csv      # Training dataset (51,840 records)
├── demand_model.pkl         # Trained Gradient Boosting model
├── features.pkl             # Processed feature list
├── le_zone.pkl              # Zone label encoder
├── le_weather.pkl           # Weather label encoder
└── stitch_kathmandu_ride_demand_forecaster/  # Additional resources
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PeakCoder-Here/kathmandu-ride-demand-forecaster.git
   cd kathmandu-ride-demand-forecaster
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Launch the Streamlit dashboard:

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 📊 Dataset

The model is trained on a dataset containing **51,840 ride records** from Kathmandu with the following features:

- **Zone**: Geographic zones in Kathmandu
- **Hour**: Time of day (0-23)
- **Weather Conditions**: Various weather states
- **Ride Demand**: Target variable (number of rides)

The dataset is preprocessed and encoded using label encoders for categorical variables (zones and weather conditions).

## 🤖 Model Details

- **Algorithm**: Gradient Boosting (via Scikit-learn)
- **Training Data**: 51,840 ride records
- **Input Features**: Zone, hour, weather conditions, and derived temporal features
- **Output**: Predicted ride demand (continuous value)
- **Model File**: `demand_model.pkl`

### Model Artifacts

- `demand_model.pkl` - Trained model
- `le_zone.pkl` - Zone label encoder
- `le_weather.pkl` - Weather condition label encoder
- `features.pkl` - Feature names used in training

## 📈 How It Works

1. **Data Input**: Select zone, time of day, and weather conditions
2. **Feature Engineering**: Data is transformed using trained label encoders
3. **Prediction**: The Gradient Boosting model generates demand forecast
4. **Visualization**: Results are displayed interactively on the dashboard

## 🔧 Development

### Training the Model

The model training pipeline is documented in `model.ipynb`:

```bash
jupyter notebook model.ipynb
```

### Data Preparation

Data preprocessing and generation steps are detailed in `generate_data.ipynb`:

```bash
jupyter notebook generate_data.ipynb
```

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| streamlit | Interactive web dashboard |
| pandas | Data manipulation and analysis |
| numpy | Numerical computing |
| scikit-learn | Machine learning model |
| plotly | Interactive visualizations |

## 🎯 Use Cases

- **Resource Optimization**: Allocate vehicles based on predicted demand
- **Driver Planning**: Help drivers understand peak demand periods
- **Business Analytics**: Analyze demand patterns across zones and times
- **Service Improvement**: Identify areas with consistent high demand

## 📝 License

This project is open source. Please check the repository for license details.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Support

For questions or issues, please open an issue on the [GitHub repository](https://github.com/PeakCoder-Here/kathmandu-ride-demand-forecaster).

## 🙌 Acknowledgments

- Built with insights from Kathmandu ride-sharing patterns
- Powered by the Scikit-learn community
- Dashboard visualization powered by Streamlit and Plotly

---

**Created by PeakCoder-Here** | [GitHub Profile](https://github.com/PeakCoder-Here)

# 🏘️ Gurgaon Properties Price Predictor

[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)](https://streamlit.io/)
[![AWS](https://img.shields.io/badge/Deployment-AWS-FF9900)](https://aws.amazon.com/)
[![License](https://img.shields.io/badge/License-GPL3.0-green)](LICENSE)

A production-ready Streamlit web application for predicting real estate property prices in Gurgaon using machine learning models. Deployed on AWS EC2 for scalable, real-time predictions.

## 📋 Overview

This application leverages machine learning algorithms to predict property prices in Gurgaon based on various features such as location, property type, amenities, and other market factors. Built with Streamlit for an intuitive user interface and deployed on AWS for reliability and scalability.

## ✨ Features

- **Real-time Price Predictions**: Get instant property price estimates
- **Multiple Input Parameters**: Location, property type, size, amenities, age
- **Interactive Web Interface**: User-friendly Streamlit dashboard
- **Production-Ready**: Deployed on AWS for 24/7 availability
- **Fast Processing**: Optimized ML models for quick predictions
- **Comprehensive Analytics**: View historical trends and model performance

## 📁 Project Structure

```
├── Home.py                    # Main Streamlit application entry point
├── pages/                     # Multi-page Streamlit app components
├── Datasets/                  # Training and testing datasets
├── Pickle_files/              # Serialized ML models and preprocessors
├── requirements.txt           # Python dependencies
├── LICENSE                    # GPL-3.0 License
└── README.md                  # This file
```

## 🛠 Tech Stack

- **Frontend**: Streamlit 1.0+
- **Backend**: Python 3.8+
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **Deployment**: AWS EC2
- **Data Processing**: Pickle files for model persistence

## 🚀 Quick Start

### Prerequisites

```bash
pip install -r requirements.txt
```

### Local Development

```bash
streamlit run Home.py
```

Visit `http://localhost:8501` to use the application.

### AWS Deployment

1. Launch an EC2 instance (t2.medium recommended)
2. Install Python and dependencies
3. Clone the repository
4. Run Streamlit app with appropriate port configuration
5. Configure security groups to allow traffic on port 8501

## 📊 Dataset

- **Source**: Gurgaon Real Estate Market Data
- **Features**: 15+ property attributes
- **Records**: Thousands of property listings
- **Target**: Property price in INR

## 🎯 How It Works

1. **Feature Engineering**: Transform raw property data into meaningful features
2. **Model Training**: Train multiple ML models (Random Forest, XGBoost, etc.)
3. **Model Selection**: Choose best performing model based on validation metrics
4. **Prediction**: Use trained model to predict prices for new properties
5. **Web Interface**: Present results through interactive Streamlit dashboard

## 📈 Model Performance

- **R² Score**: >0.85 on test set
- **Mean Absolute Error**: Within 5-8% of actual price
- **Prediction Latency**: <500ms
- **Accuracy**: Continuously improved through new data

## 🔧 Configuration

### Environment Variables

```bash
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

### Model Parameters

Edit model configurations in the Pickle files folder to customize prediction behavior.

## 📝 Usage Guide

1. **Select Property Type**: Choose from residential, commercial, etc.
2. **Enter Location**: Select from dropdown or enter specific area
3. **Input Property Details**: Size, bedrooms, amenities, age
4. **Get Prediction**: Click predict to see estimated price
5. **View Analytics**: Check historical trends and model insights

## 🐛 Troubleshooting

**Issue**: Predictions seem inaccurate
- **Solution**: Ensure all input parameters are within expected ranges

**Issue**: Slow predictions
- **Solution**: Check AWS instance resources; upgrade if needed

**Issue**: App not loading
- **Solution**: Verify security group allows port 8501

## 💡 Future Enhancements

- [ ] Advanced ensemble methods
- [ ] Real-time market data integration
- [ ] Price trend forecasting
- [ ] Property comparison tools
- [ ] Mobile application
- [ ] Multi-city support
- [ ] API endpoints for third-party integration

## 📚 Dependencies

See `requirements.txt` for complete list of dependencies.

## 📝 License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📧 Contact & Support

For questions or support:
- Open an issue on GitHub
- Check the documentation
- Review model training notebooks

## 🙏 Acknowledgments

- Built with Streamlit for interactive web apps
- Deployed on AWS for production reliability
- Special thanks to the open-source ML community

---

**Note**: This is a demonstration project for portfolio purposes. Actual property prices depend on many factors not captured by this model. Always consult with real estate professionals for investment decisions.

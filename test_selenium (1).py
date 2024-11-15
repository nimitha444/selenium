:: Create virtual environment in Windows
python -m venv venv

:: Activate the virtual environment
venv\Scripts\activate

:: Install dependencies
pip install -r selenium

:: Run the model training script
python app.py
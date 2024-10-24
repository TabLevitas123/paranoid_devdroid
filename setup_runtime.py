
import os
import subprocess

def install_flask_dependencies():
    # Install Flask and other Python dependencies for the backend
    print("Installing Flask dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "flask-cors"])

def install_react_dependencies():
    # Navigate to the React UI directory and install dependencies
    print("Installing React dependencies...")
    react_ui_path = os.path.join(os.getcwd(), "paranoid-ui")
    os.chdir(react_ui_path)
    subprocess.check_call(["npm", "install", "@mui/material", "@emotion/react", "@emotion/styled", "framer-motion", "axios", "react-router-dom"])

if __name__ == "__main__":
    install_flask_dependencies()
    install_react_dependencies()
    print("All dependencies installed successfully.")

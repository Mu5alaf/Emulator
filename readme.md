# Django APK Management and Testing Project

## Overview

This project is a full-stack web application built using Django, MySQL, and Appium for managing and automating the testing of Android APK files. The application includes features for user authentication, app management, accessibility features, and multi-language support. The project is containerized using Docker, allowing for easy deployment and setup.

## Features

### 1. User Authentication
- **Registration, Login, and Logout:** Users can register, log in, and log out using Django's built-in authentication system.
- **Account Management:** Users can update their profiles, change passwords, and manage their account settings.

### 2. APK Management
- **Upload APKs:** Users can upload Android APK files to the platform.
- **List and View APKs:** Uploaded APKs are listed with details such as name, upload date, and status.
- **Run Tests:** Users can trigger automated tests on the uploaded APKs using Appium, which captures screenshots, video recordings, and UI hierarchies.
- **Download Test Results:** Test results, including screenshots and videos, can be downloaded for further analysis.

### 3. Automation with Appium
- **Automated UI Testing:** The project integrates Appium to automate testing of Android APKs on an emulator.
- **Screenshot and Video Capture:** The automated tests include capturing screenshots and videos of the APK in action.
- **UI Hierarchy Comparison:** The Appium script compares UI hierarchies to identify changes and inconsistencies.

### 4. Multi-Language Support
- **Languages Supported:** English and French.
- **Language Switcher:** Users can switch between languages using a language switcher on the interface.
- **Dynamic Translations:** The application uses Django’s translation framework to dynamically translate content based on the selected language.

### 5. Docker Integration
- **Containerized Setup:** The project uses Docker Compose to manage services, including the Django web app, MySQL database, and Appium.
- **Environment Configuration:** Environment variables are used to configure the application, ensuring flexibility across different environments.
- **Easy Deployment:** The entire setup can be deployed with a single command using Docker Compose.

## Project Structure

```plaintext
project-root/
│
├── .env                  # Environment variables
├── accounts              # Django app for user accounts
├── Files                 # Directory for uploaded files (media)
├── home                  # Django app for home and automation logic
│   ├── migrations        # Django migrations
│   ├── templates         # HTML templates
│   ├── run_app.py        # Appium automation script
│   └── ...               # Other Django app files
├── locale                # Directory for translation files
├── project               # Main Django project settings
├── static                # Static files
├── templates             # Base HTML templates
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies

## Demo
Uploading 2024-08-19 15-32-08.mp4…



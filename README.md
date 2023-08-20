# Aircall-Frontend-Selenium

## Selenium Test Automation Framework

This is a test automation framework developed using Selenium for testing the Aircall application. The framework includes utility functions, page objects, and test cases for login and onboarding scenarios.

## Table of Contents
- [Introduction](#introduction)
- [Installation & Configuration](#installation--configuration)
- [Usage](#usage)

## Introduction

This test automation framework is designed to perform end-to-end testing of the Aircall application's login and onboarding functionalities. It utilizes Selenium for browser automation, and it includes page objects to interact with different pages of the application.

The framework provides organized utility functions, locators, and test data to simplify the test script development process. It also includes logging and browser management features.

## Installation & Configuration

Configure the framework in the Interpreter Settings of your IDE.

To configure pytest runner in your framework, follow these steps:
1. Click on Edit Configurations
2. Select Python Test
3. Choose Pytest
4. Add your test file path
5. Click OK to save your Configuration Settings.

### Dependencies

Before getting started, ensure you have the required dependencies installed. You can install them using the following command:

```sh
pip3 install -r requirements.txt
```

## **Usage**

To run the test file, command would be:
`py.test`
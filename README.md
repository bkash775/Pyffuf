# Simple Python Fuzzer

This is a simple Python script for web application fuzzing, inspired by the popular tool FFuF (Fuzz Faster U Fool). It allows you to test a web application for potential vulnerabilities by sending a large number of HTTP requests with various payloads to specific URL endpoints.

## Features

- Fuzzes specific URL endpoints with payloads.
- Supports various types of payloads, including wordlists and custom payloads.
- Allows customization of request headers.
- Displays response status codes and response lengths for each request.
- Provides basic filtering options to identify potential vulnerabilities.

## Prerequisites

- Python 3.x
- Required Python packages (can be installed using `pip`):
  - requests

## Usage

1. Clone this repository:

   ```bash
   https://github.com/bkash775/Pyffuf.git
   cd Pyffuf
   python3 ffuf.py <url>



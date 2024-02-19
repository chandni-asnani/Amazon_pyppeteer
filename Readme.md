# Pyppeteer Scraper Project

This Pyppeteer-based web scraper automates the process of extracting reviews from web page, leveraging the power of Pyppeteer for browser automation.

## Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.6+**: The programming language used for the script.
- **pip**: The Python package installer.

## Installation

### Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://your-repository-url.git
cd your-project-directory
```

### Set Up a Virtual Environment

(Optional, but recommended) Create and activate a virtual environment:

- **Unix/macOS**:

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows**:

  ```cmd
  python -m venv venv
  .\venv\Scripts\activate
  ```

### Install Dependencies

Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

This will install Pyppeteer and other dependencies defined in `requirements.txt`.

## Configuration

### Environment Variables

Copy the `.env.example` file to a new `.env` file and adjust it with your specific settings, such as API keys or database URLs:

```bash
cp .env.example .env
```

Edit `.env` with the appropriate values.

## Running the Scraper

Execute the scraper with the following command:

```bash
python base.py
```

## Running the Scraper on Docker

Execute the scraper with the following command:

```bash
docker build -t pyppeteer-scraper .
docker run pyppeteer-scraper
```

## Additional Notes

- **Customization**: The script can be customized to fit specific scraping needs. Check the comments within the script for guidance.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.
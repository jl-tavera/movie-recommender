# Movie Recommendation App

This Python script utilizes Streamlit, OpenAI, and RapidAPI services to create a simple movie recommendation app. Users can input a movie title, and the app will provide recommendations for similar movies along with information on their streaming availability.

## Requirements

- Python 3.x
- Streamlit
- OpenAI Python client
- Requests library

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies using pip:

    ```
    pip install streamlit openai-python requests
    ```

3. Obtain API keys:
    - OpenAI API key: You need to sign up for OpenAI's services to obtain an API key.
    - RapidAPI key: You need to sign up for RapidAPI's services and subscribe to the Streaming Availability API to obtain an API key.

## Usage

1. Replace `"YOUR API KEY"` placeholders in the script with your actual API keys.
2. Run the script:

    ```
    streamlit run movie_recommendation.py
    ```

3. Access the app in your web browser at the provided URL (typically `http://localhost:8501`).

4. Enter a movie title in the input field and submit it.
5. The app will display recommendations for similar movies along with information on their streaming availability in the USA.

## Features

- **Movie Recommendation**: Users can input a movie title, and the app provides recommendations for similar movies.
- **Streaming Availability**: The app fetches information about the streaming availability of recommended movies from RapidAPI's Streaming Availability API.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.



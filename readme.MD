# Image Generation Flask App

This is a Flask-based web application that generates images using the SDXL ImageGenerator library. Users can send prompts to the app and receive generated images in response.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Requirements

To run this application, you need to have the following installed:

- Python (3.6 or higher)
- Flask
- Flask-CORS
- SDXL ImageGenerator

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/h4shell/stableDiffusion-API.git
   cd stableDiffusion-API
   ```

2. Install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server by running the following command:

   ```bash
   python server.py
   ```

   The server will start and listen on http://0.0.0.0:5000/.

2. You can now send HTTP requests to the server to generate images based on prompts.

## Endpoints

### Generate Image

- **URL:** `/`
- **Method:** GET
- **Parameters:**
  - `prompt` (string, required): The prompt text for image generation.
- **Response:**
  - If successful:
    ```json
    {
      "image": "base64_encoded_image_data"
    }
    ```
  - If an error occurs:
    ```json
    {
      "status": false,
      "error": "error_message"
    }
    ```

## Example

Assuming the server is running on `http://localhost:5000/`, you can generate images by sending a GET request with the prompt parameter:

```bash
curl "http://localhost:5000/?prompt=beautiful%20landscape"
```

Response:
```json
{
  "image": "base64_encoded_image_data_here"
}
```

## Contributing

Contributions are welcome! If you find any issues or want to enhance this project, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
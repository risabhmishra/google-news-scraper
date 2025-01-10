import logging
from googlenewsdecoder import new_decoderv1

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)


def get_decoded_url(source_url: str, interval_time: int = 5) -> str:
    """
    Decodes a Google News redirect URL into its actual URL.

    Args:
        source_url (str): The Google News redirect URL to decode.
        interval_time (int): Time interval between retries (default is 5 seconds).

    Returns:
        str: The decoded URL if successful, None otherwise.
    """
    try:
        # Decode the source URL using the decoder
        decoded_url = new_decoderv1(source_url, interval=interval_time)

        # Check if decoding was successful
        if decoded_url.get("status"):
            logging.info("Decoded URL: %s", decoded_url["decoded_url"])
            return decoded_url["decoded_url"]
        else:
            logging.info("Decoding failed: %s", decoded_url["message"])
            return None
    except Exception as e:
        # Log any unexpected errors
        logging.error("An error occurred while decoding the URL: %s", e)
        return None


if __name__ == "__main__":
    # Example usage
    source_url = "https://news.google.com/rss/articles/CBMi8gFBVV95cUxNMnZlTEI0WHE5aFE2Y01rZXpTY1dOZjVtWURPQzVadk9PV1FkMjFIOEUyOE12YzNyM1FxRldNaURwUW1sa3FlRHFFdU5WLVVzMFYzZlU1NF9RT1gxcWQ0LUptcjQ5M0dHUTg4dmczNGZ3dzZ4UEllbkpVdVRjRVVwVXJpWHZ1RXRjMnMybnAweUFIbXBQWHpFU01VQ0kzZUZjUUY5WTdlVHlMY182dl9pa2VPRVh4TEZNSVMxSk1iS1dLbUZxOXBOR0drUllzdDlpVVZvNy0tWHZGa3pDUWFOUFZDN3dVUV9NejhMTjFWZEJaZ9IB8gFBVV95cUxNMnZlTEI0WHE5aFE2Y01rZXpTY1dOZjVtWURPQzVadk9PV1FkMjFIOEUyOE12YzNyM1FxRldNaURwUW1sa3FlRHFFdU5WLVVzMFYzZlU1NF9RT1gxcWQ0LUptcjQ5M0dHUTg4dmczNGZ3dzZ4UEllbkpVdVRjRVVwVXJpWHZ1RXRjMnMybnAweUFIbXBQWHpFU01VQ0kzZUZjUUY5WTdlVHlMY182dl9pa2VPRVh4TEZNSVMxSk1iS1dLbUZxOXBOR0drUllzdDlpVVZvNy0tWHZGa3pDUWFOUFZDN3dVUV9NejhMTjFWZEJaZw?oc=5"
    interval_time = 5  # Retry interval in seconds

    # Decode the URL
    decoded_url = get_decoded_url(source_url, interval_time)
    if decoded_url:
        print("Final Decoded URL: %s", decoded_url)
    else:
        print("Failed to decode the URL.")

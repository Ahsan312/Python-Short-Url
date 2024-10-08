# Import the pyshorteners library to shorten URLs
import pyshorteners

# Function to shorten a URL
def shorten_url(long_url):
    # Create a Shortener object from the pyshorteners library
    s = pyshorteners.Shortener()  # This object will help us shorten URLs
    
    # Use the tinyurl service to shorten the given long URL
    try:
        short_url = s.tinyurl.short(long_url)  # Attempt to shorten the URL
        return short_url  # Return the shortened URL if successful
    except Exception as e:
        # If there is any error (e.g., timeout, network issue), return an error message
        return f"Error: {e}"

# Main part of the program
if __name__ == "__main__":
    # Ask the user to enter a long URL to be shortened
    long_url = input("Enter the URL you want to shorten: ")
    
    # Call the shorten_url function and store the result (shortened URL or error message)
    short_url = shorten_url(long_url)
    
    # Print the shortened URL or the error message
    print(f"Shortened URL: {short_url}")

# Here are some psudo codes for the project

# Implementation for the qr code reader
"""
Access the camera, live detect qr code using scan.py
Then compare to the existing list of qr codes
Check to see if its in the list, if so, we give them the necessary credit.

"""


# Existing list of QR codes
existing_qr_codes = ["QR123", "QR456", "QR789"]

# Initialize a counter
counter = 0

# Function to scan a QR code and update the counter
function scan_and_update_counter():
    # Scan QR code
    scanned_qr_code = scan_qr_code()

    # Check if the scanned QR code exists in the existing list
    if scanned_qr_code in existing_qr_codes:
        increment_counter()

# Function to simulate scanning a QR code
function scan_qr_code():
    # In a real implementation, this function would interact with the QR code scanner
    # and return the scanned QR code value.
    return scanned_qr_code_value

# Function to increment the counter
function increment_counter():
    counter = counter + 1

# Main program
while True:
    # Wait for user to initiate scanning
    user_input = wait_for_user_input()

    if user_input == "scan":
        scan_and_update_counter()

    if user_input == "exit":
        break

# Print the final counter value
print("Total QR codes scanned:", counter)

# Potentially add the 
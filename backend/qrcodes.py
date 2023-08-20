import cv2
import qrcode

# List of expected QR code data values
expected_qr_data = ["23452345", "45879845"]

# List to keep track of scanned QR codes
scanned_qr_codes = []

def checkqr(qrscan):
    global scanned_qr_codes

    # Check if the scanned QR code matches any expected value
    if qrscan in expected_qr_data:
        if qrscan in scanned_qr_codes:
            print(f"QR Code {qrscan} has already been recycled.")
        else:
            scanned_qr_codes.append(qrscan)
            print(f"QR Code {qrscan} has been scanned. Recycle now.")
    else:
        print("Invalid scan.")

    # Print the list of scanned QR codes
    #print("Scanned QR Codes:", scanned_qr_codes)

# Call the function with the scanned QR code data
checkqr("23452345") 
checkqr("45879845")  
checkqr("45879845")  

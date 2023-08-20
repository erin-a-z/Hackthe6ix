import cv2
import qrcode
import math

def checkqr(qrscan):
    expected_qr_data_1 = 1
    expected_qr_data_2 = 2

    qrlists = ["1","2"]


    if qrscan == expected_qr_data_1:
        qrscan = "BOTTLE1"
        qrlists.remove("1")
    elif qrscan == expected_qr_data_2: 
        qrscan = "BOTTLE2"
        qrlists.remove("2")
    else:
        print("Invalid scan")

    scanned_image = cv2.imread("scanned_qrcode.png")
    print("Image loaded")
    
    detector = cv2.QRCodeDetector()
    print("Detector initialized")
    
    retval, decoded_info, points, qr_code = detector.detectAndDecode(scanned_image)
    print("QR code detected and decoded")

    if retval:
        if decoded_info == expected_qr_data_1:
            print("Scanned QR Code matches BOTTLE1.")
        elif decoded_info == expected_qr_data_2:
            print("Scanned QR Code matches QR Code 2.")
        else:
            print("Scanned QR Code does not match any expected QR code.")
    else:
        print("QR code invalid")

# Print statement to indicate the function is reached 
    print("Function reached")

    return 
# Replace this value with the actual scanned data

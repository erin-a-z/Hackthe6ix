import cv2

# Load the image
# image_path = 'path_to_your_image.jpg'  # Replace with the actual image path
image_path = 'frontend/qr.png'

def readQR(image_path):
    image = cv2.imread(image_path)

    # Create a QR code detector
    qr_code_detector = cv2.QRCodeDetector()

    # Detect and decode QR codes
    retval, decoded_info, points, _ = qr_code_detector.detectAndDecodeMulti(image)

    if retval:
        for i in range(len(decoded_info)):
            print("Decoded Info:", decoded_info[i])
            for point in points[i]:
                cv2.circle(image, tuple(point), 10, (0, 255, 0), -1)  # Mark QR code corners

        cv2.imshow("QR Code Detector", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No QR codes detected.")
readQR(image_path)
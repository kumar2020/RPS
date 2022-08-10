import cv2

from keras.models import load_model 
import numpy as np 

model = load_model('keras_model.h5')
capture = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = capture.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalise the image 
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()

cv2.destroyAllWindows()

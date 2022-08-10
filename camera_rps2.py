import cv2
from keras.models import load_model 
import numpy as np 
import time
import random


class Rps:

    def __init__(self):
        self.model = load_model('keras_model.h5')
        self.user_score = 0
        self.computer_score = 0
    
    def get_computer_choice(self):
        choices = ['rock', 'paper', 'scissor']
        comp_choice = random.choice(choices)
        print(f"computer choice : {comp_choice}")
        return comp_choice
        

    

    def get_prediction(self):
        
        capture = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        end_time = time.time() + 5
        
        while time.time() < end_time:
            ret, frame = capture.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalise the image 
            data[0] = normalized_image
            prediction = self.model.predict(data)
            cv2.imshow('frame', frame)
            print(prediction)
            max_index = np.argmax(prediction[0])
            #print(max_index)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        return max_index


    def get_user_choice(self):
        
        max_index = self.get_prediction()
        #print(max_index)
        if max_index == 0:
            user_choice = 'rock'
        elif max_index == 1:
            user_choice = 'paper'
        elif max_index == 2:
            user_choice = 'scissor'
        elif max_index == 3:
            user_choice = 'nothing'
        else:
            print('show valid gesture')
        print(user_choice)
        return user_choice




    def get_winner(self):
        user_choice = self.get_user_choice()
        comp_choice = self.get_computer_choice()
        if user_choice == comp_choice:
            print("Both selected same element: Game tie")
        elif user_choice  ==  "rock" and comp_choice  ==  "paper" or \
            user_choice  ==  "scissor" and comp_choice  ==  "rock" or \
            user_choice  ==  "paper" and comp_choice  ==  "scissor":
            print(" computer won")
            self.computer_score += 1
        
        else:
            print(" user won")
            self.user_score += 1



def play():

    game = Rps()
    
    print("start the game")
    
    while game.computer_score < 3 or game.user_score < 3:
    
        game.get_winner()
    if game.user_score == 3:
        print("Finally, I  won  the game")
    else:
        print('Oops, I lost the game')
        


play()


#priyanka788
cams_test = 10
 for id in range(0, cams_test): #//if you don't find it please check your camera if it is working or not
    cap = cv2.VideoCapture(id)
    test, frame = cap.read()
    if test:
        print("id : "+str(id)+" /// result: "+str(test))
    cap.release()

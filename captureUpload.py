import cv2
import dropbox
import time
import random

startTime = time.time()

def startCamera():
    num = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(num)+".png"
        cv2.imwrite(img_name,frame)
        startTime = time.time()
        result = False
    
    return img_name
    print("Snapshot Taken "+time.time())
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadfile(img):
    access_token = 'G2vtgtYgCRUAAAAAAAAAAUE_URubhk8K6e7BDtwQoy0zwtfWwn2UQaFHwazSe9uF'
    file_from = img
    file_to = '/test/'+(img)
    dbx = dropbox.Dropbox(access_token)
    
    with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to,mode = dropbox.files.WriteMode.overwrite)
            print("File Uploaded")

def main():
    while(True):
        if((time.time()-startTime)>=10):
            name = startCamera()
            uploadfile(name)

main()
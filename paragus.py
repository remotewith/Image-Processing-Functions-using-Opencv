
import cv2

import numpy as np

from matplotlib import pyplot as pl

import time


#1-import opencv

#2-read the image

#3-do the proccesing

#4-show the image

#5-close and exit


def trom():
    time.sleep(0.1)


print('HERE WE DEAL WITH AN IMAGE USING OPENCV LIBRARY\n')

x=input('Enter the .jpg/png file so that we can load the image::')

img=cv2.imread(x)

print('This is the image you choose::')

cv2.imshow('your image',img)
cv2.waitKey(4000)


while True:
    

    print('Following are options choose accordingly\n')
    print('0.)   Seeing the original image\n')
    trom()
    print('1.)    Blurring an image\n')
    trom()
    print('2.)   Evolving black and white effect\n')
    trom()
    print('3.)   Showing only edges of the image\n')
    trom()
    print('4.)   Presenting the sketch of the image\n')
    trom()
    print('5.)   Giving the cartoon effect\n')
    trom()
    print('6.)   Showing the dimensions of the image\n')
    trom()
    print('7.)   If u want to see the different colors of the image\n')
    trom()
    print('8.)   Graphical representation of the images\n')
    trom()
    print('9.)   If u want to see a rotated image of the original image\n')
    trom()
    print('10.)  To see the transpose of the original image\n')
    trom()
    print('11.)  To see smaller and larger image of the original image\n')
    trom()
    print('12.)  Showing a cropped image\n')
    trom()
    print('13.)  Showing sharpened image of original image\n')
    trom()
    print('14.)  Binary operation on original image\n')
    trom()
    print('15.)  Showing negative effect on the original image\n')
    trom()
    print('16.)  Showing binary image of the original image\n')
    trom()
    print('17.)  Showing original image using matplotlib library\n')
    trom()
    print('18.)  TO QUIT PRESS 18\n')

 
    c=int(input('ENTER YOUR CHOICE ::'))
    print()

    if c==0:
        cv2.imshow('Original',img)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',img)
        else:
            print('Thank you')


    elif c==1:
        blurred_img=cv2.medianBlur(img,5)


    #''' 5 here shows the new image that is going to be appeared will be of
    #5 pixel by 5 pixel,and median blur refers that
    #pc will not show every shade of the colour
    #instead it will show a median colour of two or more seperate colours.'''
    
    
        cv2.imshow('Blur',blurred_img)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',blurred_img)
        else:
            print('Thank you')
        

    elif c==2:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    

        cv2.imshow('Gray',gray)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',gray)
        else:
            print('Thank you')

    elif c==3:
        blurred_img=cv2.medianBlur(img,5)

    
    #*edges=cv2.Canny(img,75,150)
    #'''this is the edges of the original image using canny'''

    
        edges2=cv2.Canny(blurred_img,75,150)
    
    
        cv2.imshow('Edges',edges2)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',edges2)
        else:
            print('Thank you')

    elif c==4:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray=cv2.medianBlur(gray,5)

    
        edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,6)
    
    #'''adaptive threshold takes small area of the image and accordingly makes it white or black.'''

    #'''to get more thicker and denser edges we do use adaptive threshold.'''

    #'''adaptive threshold gives the sketch of the image.'''

   
    #'''Also 9 here shows that image will be taken 9 by 9 pixels
        #whereas 6 shows the edge consideration.'''
    
        cv2.imshow('Sketch',edges)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',edges)
        else:
            print('Thank you')

    elif c==5:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray=cv2.medianBlur(gray,5)
    
        edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,6)
    

    #*color=cv2.medianBlur(img,21)

    
    #'''color's medianblur is not good to use as it makes big kernel and it will give you more cartoonish effect.'''

    #'''the problem when we apply the blur is that it blurs also the edges
       # which can make the image to lose its cartoonish effect.'''

    #''' thus  we want a special kind of blur which keeps both edges
        #but at the same time can blur the colour in between for
         #this we use bilateral filter instead of median blur.'''

    
        color=cv2.bilateralFilter(img,9,250,250)

    #'''here 9 shows the block size,'''

    #'''and 250,250 shows how much cartoonish effect u want 
        #but higher values can degrade the quality of image.'''

    
        cartoon=cv2.bitwise_and(color,color,mask=edges)

    #'''we are using bitwise to connect two images together that is edges and color.'''

    #'''two important factros for cartooning is (i)edges and (ii)color.'''
    

        cv2.imshow('Cartoon',cartoon)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',cartoon)
        else:
            print('Thank you')

    elif c==6:
        shape=img.shape
        print('The Height,Width and the Chanels of the image are as follows:\n',shape)

    elif c==7:
        
        B,G,R=cv2.split(img)
        zeros=np.zeros(img.shape[:2],dtype='uint8')
        
        print('What colors do u want to see\n')
        print('Save option is not available for option 7')
        print('Type numbers  as stated:\n')
    
        print('1.)  To show red color')
        print('2.)  To show green color')
        print('3.)  To show blue color')
        print('4.)  To show cyan color')
        print('5.)  To show pink color')
        print('6.)  To show yellow color')
        print('7.)  To show all colors\n')

        d=int(input('Enter your choice:'))

        if d==1:
            cv2.imshow('Red',cv2.merge([zeros,zeros,R]))
            cv2.waitKey(0)
            s=input('Enter (y/n) depecting you want to save this image:')
            if s=='y':            
                name=input('Enter the name of the image throgh which u want to save it:')
                cv2.imwrite(name+'.jpg',cv2.merge([zeros,zeros,R]))
            else:
                print('Thank you')
        
        if d==2:
            cv2.imshow('Green',cv2.merge([zeros,G,zeros]))
            cv2.waitKey(0)
            s=input('Enter (y/n) depecting you want to save this image:')
            if s=='y':
                name=input('Enter the name of the image throgh which u want to save it:')
                cv2.imwrite(name+'.jpg',cv2.merge([zeros,G,zeros]))
            else:
                print('Thank you')
                
        if d==3:
            cv2.imshow('Blue',cv2.merge([B,zeros,zeros]))
            cv2.waitKey(0)
            s=input('Enter (y/n) depecting you want to save this image:')
            if s=='y':
                name=input('Enter the name of the image throgh which u want to save it:')
                cv2.imwrite(name+'.jpg',cv2.merge([B,zeros,zeros]))
            else:
                print('Thank you')

        if d==4:
            cv2.imshow('Cyan',cv2.merge([B,G,zeros]))
            cv2.waitKey(0)
            s=input('Enter (y/n) depecting you want to save this image:')
            if s=='y':
                name=input('Enter the name of the image throgh which u want to save it:')
                cv2.imwrite(name+'.jpg',cv2.merge([B,G,zeros]))
            else:
                print('Thank you')
        
        if d==5:
            cv2.imshow('Pink',cv2.merge([B,zeros,R]))
            cv2.waitKey(0)
            s=input('Enter (y/n) depecting you want to save this image:')
            if s=='y':
                name=input('Enter the name of the image throgh which u want to save it:')
                cv2.imwrite(name+'.jpg',cv2.merge([B,zeros,R]))
            else:
                print('Thank you')
        
        if d==6:
            cv2.imshow('Yellow',cv2.merge([zeros,G,R]))
            cv2.waitKey(0)
            s=input('Enter (y/n) depecting you want to save this image:')
            if s=='y':
                name=input('Enter the name of the image throgh which u want to save it:')
                cv2.imwrite(name+'.jpg',cv2.merge([zeros,G,R]))
            else:
                print('Thank you')

        if d==7:
            cv2.imshow('Red',cv2.merge([zeros,zeros,R]))
            cv2.imshow('Green',cv2.merge([zeros,G,zeros]))
            cv2.imshow('Blue',cv2.merge([B,zeros,zeros]))
            cv2.imshow('Cyan',cv2.merge([B,G,zeros]))
            cv2.imshow('Pink',cv2.merge([B,zeros,R]))
            cv2.imshow('Yellow',cv2.merge([zeros,G,R]))

            cv2.waitKey(0)
                
    elif c==8:
        b,g,r=cv2.split(img)
    
        cv2.imshow('b',b)
        cv2.imshow('g',g)
        cv2.imshow('r',r)

        pl.hist(b.ravel(),256,[0,256])
        pl.hist(g.ravel(),256,[0,256])
        pl.hist(r.ravel(),256,[0,256])
        pl.show()

    if c==9:
        angle=int(input('Enter how much angle do you want to rotate:'))
    
        print()

        size=float(input('Enter the size of image u want(enter between 0 and 1):'))
    
        height,width=img.shape[:2]

        rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),angle,size) 

        rotated_image=cv2.warpAffine(img,rotation_matrix,(width,height))

        cv2.imshow('Rotated image',rotated_image)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',rotated_image)
        else:
            print('Thank you')

    elif c==10:
        transpose_image=cv2.transpose(img)

        cv2.imshow('Transpose is',transpose_image)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',transpose_image)
        else:
            print('Thank you')

    elif c==11:
        smaller=cv2.pyrDown(img)

        larger=cv2.pyrUp(img)

        cv2.imshow('Smaller',smaller)

        cv2.imshow('Larger',larger)

    elif c==12:
        print('Select the corresponding rows and coloumns')
        print('Their sum must be equal to 1\n')

        a=float(input('Enter the value of starting row and starting coloumns value(between 0 and 1):'))
        b=float(input('Enter the value of ending row and ending coloumns value(between 0 and 1):'))
    
        height,width=img.shape[:2]

        start_row,start_col=int(height*a),int(width*a)

        end_row,end_col=int(height*b),int(width*b)

        cropped=img[start_row:end_row,start_col:end_col]

        cv2.imshow('Cropped',cropped)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',cropped)
        else:
            print('Thank you')

    elif c==13:
    
        kernel_sharpening=np.array([[-1,-1,-1,-1,-1],
                                        [-1,-1,-1,-1,-1],
                                        [-1,-1,25,-1,-1],
                                        [-1,-1,-1,-1,-1],                                        
                                        [-1,-1,-1,-1,-1]])

        sharpened=cv2.filter2D(img,-1,kernel_sharpening)

        cv2.imshow('Sharpened',sharpened)
        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',sharpened)
        else:
            print('Thank you')

    elif c==14:
        print('We show two basic binary operation on the image\n')
        print('Saving option only available for 1 and 2\n')

        print('Choose accordingly\n')
    
        print('1.)  To see addtion of images')
        print('2.) To see subtraction of images')
        print('3.) To see both addition and subtraction\n')

        d=int(input('Enter your option down:'))

        if d==1:
            M=np.ones(img.shape,dtype='uint8')*150

            added=cv2.add(img,M)

            cv2.imshow('Added',added)
            cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',added)
        else:
            print('Thank you')

        if d==2:
            M=np.ones(img.shape,dtype='uint8')*150

            subtract=cv2.subtract(img,M)

            cv2.imshow('Subtracted',subtract)
            cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',subtract)
        else:
            print('Thank you')

        if d==3:
            M=np.ones(img.shape,dtype='uint8')*150
        
            added=cv2.add(img,M)
            subtract=cv2.subtract(img,M)

            cv2.imshow('Added',added)
            cv2.imshow('Subtracted',subtract)

        else:
            print('Wrong option is chosen')
        

    elif c==15:
        image_HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        cv2.imshow('Hsv image',image_HSV)

        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',image_HSV)
        else:
            print('Thank you')

    elif c==16:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray=cv2.medianBlur(gray,5)

        ret,bw=cv2.threshold(gray,160,225,cv2.THRESH_BINARY)

        cv2.imshow('Binary',bw)

        cv2.waitKey(0)

        s=input('Enter (y/n) depecting you want to save this image:')

        if s=='y':
            name=input('Enter the name of the image throgh which u want to save it:')
        
            cv2.imwrite(name+'.jpg',bw)
        else:
            print('Thank you')
    

    elif c==17:
        pl.imshow(img)

        pl.xticks([])
        pl.yticks([])


        pl.show()

    elif c==18:
        break
    
     
cv2.waitKey(0)


#'''wait key is used so that we can show the upgraded image for a particular time
#using 0 means until user closes the image window it will be seen
#suppose we use 3000 instead of 0 it would mean that
#the image window will automatically close after 3 second of time.'''


cv2.destroyAllWindows()

#'''adaptive threshold takes small area of the image and accordingly makes it white or black.
 #to get more thicker and denser edges we do use adaptive threshold.'''

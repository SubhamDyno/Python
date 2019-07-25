
#Pickled
import pickle
def pickle_image(img):

    with open('Pickled.pkl', 'wb') as fo:
        pickle.dump(img, fo)
        fo.close()
    with open('Pickled.pkl', 'rb') as fr:
        print('Reading in Bytes : ' ,fr.readline())
pickle_image('download.png')


#Unpickled
def unpickle_image(file):
    with open(file, 'rb') as fo:
        #print("Hexadecimal Bytes ", fo.readline())
        dict = pickle.load(fo, encoding='bytes')
    print('Unpickling :', dict)


unpickle_image('Pickled.pkl')





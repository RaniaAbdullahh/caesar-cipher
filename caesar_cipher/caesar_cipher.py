import nltk
nltk.download('words')
english_words = nltk.corpus.words.words()
#print(len(english_words))

def count_valid_english_words(sentence):
    '''
    >>> count_valid_english_words('hello my friend')
    3
    >>> count_valid_english_words('hello my FRIEND kgfl')
    3
    '''
    words = sentence.split()
    counter = 0 
    for i in words:
        if i in english_words or i.lower() in english_words or  i.upper() in english_words :
            counter += 1
    return counter


def encrypt(sent, key):
    '''
    >>> encrypt('hello my friend',4)
    'lipps q} jvmirh'
  
    '''

    encrp_sent=''
    if key > 26:
        key = key%26
    for i in sent.lower() :
        if ord(i)> 32 and  ord(i)< 65:
            continue
        if ord(i) == 32:
            encrp_sent+=i
            continue
        new= ord(i)+key
 
       
        encrp_sent +=chr(new)
    return encrp_sent

def decrypt(sent,key):
    '''
    >>> decrypt('lipps q} jvmirh',4)
    'hello my friend'
    
    '''
 
    if key > 26:
        key = key%26
    return encrypt(sent,-key)


def hacking(sent) :
    text=''
    new=sent.split()
    arr=[]
    for i in new :
        for j in range (26):
            decrypted_text=decrypt(i,j) 
            if  decrypted_text in english_words:
                arr.append(decrypted_text)
    for i in arr:
        text+=i+' '
    return text.strip()


if __name__ == "__main__":
    print(encrypt('abc', 2)) 
    print(encrypt('hello my friend',4)) 
    print(decrypt('cde', 2)) 
    print(encrypt('hello dear', 2)) 
    print(hacking('ifmmp xpsme'))
    print(decrypt('lipps q} jvmirh',4))
  


class encrypter :
    
    def encrypt(text) :
        returnStr = ""

        for letter in text :
            returnStr = returnStr + letter + "1qpwoei94ruty12alsk89dj3fhg008zmxncbn234vnb7457"

        return returnStr
    
    def decrypt(text) :
        return text.replace("1qpwoei94ruty12alsk89dj3fhg008zmxncbn234vnb7457", "")



def getLogin(filename) :
    
    file = open("passwords/" +  filename + ".txt", "r")
    loginInfo = file.readlines()
    file.close()
    print(loginInfo[0], "\n", encrypter.decrypt(loginInfo[1]))


def create_editFile(filename, username, password) :
    file = open("passwords/" + filename + ".txt", "w")
    file.write(username)
    file.write("\n")
    file.write(encrypter.encrypt(password))
    file.close()



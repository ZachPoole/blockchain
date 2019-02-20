import hashlib
from pathlib import Path


#turns string into a hash
def getHash(string):

    #encodes string so that it can be hashed
    encode = string.encode('utf-8')

    #creates hash object and adds encoded string to it
    preHash = hashlib.sha256(encode)

    #hashes encoded string and stores it in variable
    actualHash = preHash.hexdigest()

    return actualHash




def independentHashing(l = []):
    
    hashList = []
    
    for element in l:
        hashList.append(getHash(element))
        
    return hashList




def merkleRoot(transList = []):
    
    listOfLists = [transList.copy(),[]]
    
    currList = listOfLists[0].copy()
    otherList = listOfLists[1].copy()
      
    if len(currList) == 1:
        return currList[0]
     
    if len(currList) % 2 != 0:
        currList.append(currList[-1])
        
    for num in range (0, len(currList), 2):
        hashString = currList[num] + currList[num + 1]
        otherList.append(getHash(hashString))
        

    return merkleRoot(otherList)

    

    




def main():
    
    #transactionPoole
    transactions = ['testing testing', '123123123', 'here is 500 bitcoin', 'test']

    if len(transactions) == 1:
        transactions.append(transactions[0])

    transListHash = independentHashing(transactions)

    steve = merkleRoot(transListHash)

    print('\n\nMerkle Root: ' + steve)




    # testArrayOne = []
    #
    # for x in transactions:
    #     testArrayOne.append(getHash(x))
    #
    #
    #
    # testArrayTwo = []
    #
    # for y in range(0, len(testArrayOne), 2):
    #     testArrayTwo.append(getHash(testArrayOne[y] + testArrayOne[y + 1]))
    #
    #
    #
    # testArrayThree = []
    #
    # for z in range(0, len(testArrayTwo), 2):
    #     testArrayThree.append(getHash(testArrayTwo[z] + testArrayTwo[z + 1]))
    #
    #
    # print(testArrayThree[0])





if __name__ == "__main__":
    main()




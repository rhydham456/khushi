def check_if_palindrome(word,ifPalindrome = set(),ifPalindromeList=[]):
    # ifPalindrome = set()
    # ifPalindromeList =[]
    for index in range(0,len(word)):
        if word[index]==word[len(word)-index-1]:
            ifPalindrome.add(True)
        else:
            ifPalindrome.add(False)
    for item in ifPalindrome:
        ifPalindromeList.append(item)
    if len(ifPalindromeList)==1:
        if ifPalindromeList[0]==True:
            return True
        if ifPalindromeList[0]==False:
            return False
    else:
       
        return False
    
check_if_palindrome('naman')
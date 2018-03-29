#Python Program to reverse the elements in a list
#F. Derek Roman - GitHub Profile:  CodeNamor
#SWDV-610-3W     Week 3 Assignment       I attest that this is my own work

def revList(lst):
    if len(lst) == 0:
        return ([])
    else:
        return (revList(lst[1:]) + [lst[0]] )
    
def main():
    list = eval(input("Please enter a list for reversing:  "))
    reverseList = revList(list)
    print("The reverse list is:  ", reverseList)
    
main()
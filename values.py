#Python program to find the Max and Min values in a sequence
# F. Derek Roman - GitHub Profile CodeNamor
#SWDV-610-3W Week 3 Assignments           I Attest that this is my own work

def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]
    
def Min(list, min=None):
    if len(list) < 1:
        return min
    return Min(list[1:], list[0] if min is None or list[0] < min else min)

def main():
    list = eval(input(" please enter a list of numbers: "))
    print("The Max Value is: ", Max(list))
    print("The Min Value is: ",Min(list))

main()
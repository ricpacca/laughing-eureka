# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())

for i in range(n):

    w = raw_input().strip() #word being considered
    s = {} #set counting the number of anagrams for each substring

    #consider each substring
    for l in range(len(w)):
        for r in range(l, len(w)):
            key = tuple(sorted(w[l:r+1]))
            if key in s:
                s[key] += 1
            else:
                s[key] = 1

    #everytime we have a new substring which pairs with an already found one, we add 1 to the counter for that substring
    #however, we remember that each substring can combine with all the previous found ones! so we should count every combination
    #to do this, observe that given n pairable substrings, there are (n-1)+...+1 = n*(n-1)/2 possible pairs between them

    counter = 0 #total number of possible pairs for w
    for tot in s.values():
        if tot > 1:
            counter += tot*(tot-1)/2

    print counter

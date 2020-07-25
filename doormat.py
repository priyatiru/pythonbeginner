n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))




# Explanation :
#There are a couple things to notice.

#The first is that each line has a set number of repetitions of '.|.', which are centered, and the rest is filled by '-'.

#The second is that the flag is symmetrical, so if you have the top, you have the bottom by reversing it.
#You only need to work on n // 2 (n is odd and you need the integer div because the remaining line is the "WELCOME" line).

#line 2: I generate 2\*i + 1 '.|.', center it, and fill the rest with '-'. That's basically the top part of the output.

#line 3: put things together. '\n'.join() should be straightforward. Then, the sequence of strings to join is the pattern described above, the middle 'WELCOME' line, 
#and the pattern reversed.

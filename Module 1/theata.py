scores=  [90 ,
          75,
          88,
          92,
          95]


steps =     1

top_score = scores[0]
print('Score    : ',scores)
print('Top Score: ',top_score)
print('Steps    : ',steps)
print('Theta    : Thea (1) --best case =worst case = 1 steps')

print('-----------------------------------')

n = len(scores)
total  = 0


for score in scores:
    total += score
    
print('Total    : ',total)
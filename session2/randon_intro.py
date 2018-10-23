from random import randint
cloud='''    __   _
    _(  )_( )_
   (_   _    _)
     (_) (__)
 

'''
rain='''
    __   _
    _(  )_( )_
   (_   _    _)
  / /(_) (__)
 / / / / / /
/ / / / / /
'''
sun='''
    ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         \
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ;  
      '''
for i in range(10):
 x = randint(0,100)
 if x<30:
     print(rain)
 elif x<60:
     print(cloud)
 else:
     print(sun)
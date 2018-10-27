fav=[ "fav1","fav2","fav3","fav4","fav5" ]
print( "hi there, here is your favorite thing:" )
print( *fav,sep="\n" )
i=int(input( "position to delete? " ))
fav.pop(i-1)
print( *fav,sep="\n" )

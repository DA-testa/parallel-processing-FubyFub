#Andrejs Vasiljevs 12 grupa 221RDB441

def parallel_processing(n, m, data):
    
    output = []
    thread = [ ( 0, i ) for i in range( n ) ]
    
    for i in range( m ):
        
        cont = min( thread )
        thread[ cont[ 1 ]] = ( cont[ 0 ] + data[ i ], cont[ 1 ] )
        output.append(( cont[ 1 ], cont[ 0 ]))
        
    return output

def main():
    
    n, m = map( int, input().split() )
    
    data =  list( map( int, input().split()) )

    result = parallel_processing(n,m,data)
    
    for i in range( m ):
        print( result[ i ][ 0 ], result[ i ][ 1 ] )

if __name__ == "__main__":
    main()

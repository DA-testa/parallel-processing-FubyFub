#Andrejs Vasiljevs 12 grupa 221RDB441

def parallel_processing(n, m, data):
    
    output = []
    thread = [ ( 0, i ) for i in range( n ) ]
    
    for i in range( m ):
        
        cont, time = min( thread, key = lambda x: x[ 1 ])
        output.append(( cont, time))
        thread[ cont ] =( cont,  data[ i ] + time )
        
    return output

def main():
    
    n = 0
    m = 0

    n, m = map( int, input().split() )
    
    data = []
    data =  list( map( int, input().split() ))

    result = parallel_processing(n,m,data)
    
    for i in range( m ):
        print( result[ i ][ 0 ], result[ i ][ 1 ] )

if __name__ == "__main__":
    main()

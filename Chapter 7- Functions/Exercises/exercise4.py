def make_shirt(size="large",message="i love pyhton"):
    """prints a sentence summary of the shirt size and message printed on it."""
    print("size:",size)
    print("message:",message)
    
    #Make a large shirt with default message
make_shirt()
    
    #make a medium shirt with the default message
make_shirt(size="medium")
    
    #make a shirt of any size with a different message
make_shirt(size="small",message="vibing")
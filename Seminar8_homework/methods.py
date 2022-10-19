# this method delete string from specify file by element of string
def delete_string(element, path):
    file = open(path, 'r')
    list_strings = file.readlines()
    file2 = open(path, 'w')
    
    array = [line.split(',') for line in list_strings]
    [file2.write((','.join(i))) for i in array if not(i.__contains__(element))]

    file.close 
    file2.close  


# this method search string from specify file by element of string
# and output to console
def search_by(string, path):
    file = open(path, 'r')
    list_strings = file.readlines()
    array = [line.split(',') for line in list_strings]
    [print(','.join(i)) for i in array if i.__contains__(string)]
  
    file.close        


# method outputting a containment from specify file except strings with specify element of string
def filter(string, path):
    file = open(path, 'r')
    list_strings = file.readlines()
    array = [line.split(',') for line in list_strings]
    [print(','.join(i)) for i in array if not(i.__contains__(string))]    
    file.close

# search_by('Egor', 'file.txt')
# delete_string('Vasilisa', 'file.txt')
# filter('Angelina', 'file.txt')

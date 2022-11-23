import re

def top_five_words(file):
    "This returns top 5 words in the given file"
    new_data = []
    freq_map = {}
    with open(file) as myFile:
        data = myFile.read()
        
        # Using regex [\w']+ to grab words including those with apostrophes
        new_data = re.findall(r"[\w']+", data)
    
    # Iterate over the new_data to get frequency of words
    for word in new_data:
        if word not in freq_map:
            freq_map[word] = 0 
        freq_map[word] += 1 
    
    
    # This sorts based on values
    sort_freq_map = sorted(freq_map.items(), key=lambda x: -x[1])

    print(sort_freq_map)
    # THis grabs top 5 words and neglect duplicates
    top_5 = [f[0] for f in sort_freq_map[:5]]
    
    return top_5

print(top_five_words("file.txt"))
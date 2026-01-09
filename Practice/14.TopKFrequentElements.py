def findTopKFrequentElement(words, k):
    set_words = set(words)
    word_dict = dict()
    for item in set_words:
        word_dict[item] = words.count(item)
    reverse_sorted_words = { k: v for k,v in sorted(word_dict.items(), key = lambda item: item[1], reverse=True)[:k]}
    top_k_keys = [x for x in reverse_sorted_words]
    return top_k_keys



def findTopKFrequentElement2(words, k):
    words_dict = dict()
    for item in words:
        words_dict[item] = words_dict.get(item, 0) + 1
    #Sort for the unique word based on the value and in the reverse direction
    reversed_sort_dict = { k : v for k,v in sorted(words_dict.items(), key= lambda item: item[1], reverse=True)[:k]}
    top_k_items = [ item for item in reversed_sort_dict]
    return top_k_items


findTopKFrequentElement(["doorbell", "camera", "doorbell", "ring", "camera", "doorbell"], 2)
print(findTopKFrequentElement2(["doorbell", "camera", "doorbell", "ring", "camera", "doorbell"], 2))

def topKFrequent(nums, k):
    freq_dict = {}
    
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # value sorting
    sorted_items = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
    
    result = [item[0] for item in sorted_items[:k]]
    
    return result


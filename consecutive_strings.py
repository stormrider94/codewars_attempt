def longest_consec(strarr, k):
    if (not strarr) or (k <= 0) or (k > len(strarr)):
        return ""
    track_consecutive_lengths = {
    }
    for i in range(len(strarr)):
        concatenated_word = "".join(strarr[i: i+k])
        track_consecutive_lengths[concatenated_word] = len(concatenated_word)
    return sorted(track_consecutive_lengths.items(),key = lambda x: x[1],reverse = True)[0][0]
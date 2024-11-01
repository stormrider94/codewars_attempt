def my_languages(results):
    # let's first sort it in descending order 
    results = dict(sorted(results.items(),key=lambda item: item[1],reverse=True))
    return [key for key in results if results[key] >= 60 ]
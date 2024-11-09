def count_developers(lst):
    european_JS_developers=list(filter(lambda detail: detail['continent']=="Europe" and detail["language"]=="JavaScript",lst))
    print(european_JS_developers)
    return len(european_JS_developers)
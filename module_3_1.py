calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case

def is_contains(string, list_to_search):
    count_calls()

    return string.lower() in (s.lower() for s in list_to_search)


info1 = string_info("Hello, sensei")
info2 = string_info("How is it going?")
contains = is_contains("religions", ["Buddhism", "Christianity", "Islam", "Catolicism", "Shintoism"])
contains2 = is_contains("IT specialists", ["QA", "Developer", "Designer", "Analyst"])


print("string_info('Hello, sensei'):", info1)
print("string_info('How is it going?'):", info2)
print("is_contains('religions', ...):", contains)
print("is_contains('IT specialists', ...):", contains2)


print("Количество вызовов функций:", calls)
def analyse_value(input):
    '''Write a function analyze_value(value) that takes ANY Python value
    and returns a formatted string with:
    - The value itself
    - Its type
    - Its truthiness (True/False)
    - Its length (if applicable, "N/A" otherwise)'''
    type_name=type(input).__name__
    truthy=bool(input)
    try:
        length=len(input)
    except:
        length="N/A"
    return f"Value: {input} | Type: {type_name} | Truthy: {truthy} | Length: {length}"

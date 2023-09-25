dig2rom = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}

def num2head(number, isInToc):
    temp = f"- [{number}" if isInToc else f"# {number}" # Different pattern for ToC or main

    if number in dig2rom.keys(): return temp + "."
    if number in dig2rom.values(): return temp + " "
    return temp

heading_D2R_ToC = {num2head(digit, True): num2head(roman, True) for digit, roman in dig2rom.items()}
empty_head_ToC = num2head("", True)

heading_D2R_mainText = {num2head(digit, False): num2head(roman, False) for digit, roman in dig2rom.items()}
empty_head_mainText = num2head("", False)

def heading_D2R(isToC=None):
    if isToC==None:
        return {**heading_D2R_ToC, **heading_D2R_mainText}
        
    return heading_D2R_ToC if isToC else heading_D2R_mainText

def empty_head(isToC):
    return empty_head_ToC if isToC else empty_head_mainText
def slices(series: str, length: int) -> list:
    """
    Slice the series into subseries. Return all subseries in list.
    """

    if length > len(series) or series == "" or length <= 0:
        raise ValueError("Error! Check: \n \
                1. Length is larger than the length of the series (or)\n \
                2. Series is empty i.e. "" (or)\n \
                3. Sength is smaller or equal to zero")

    l = [series[index : index + length] for index in range(len(series) -
        length+1)]
    return l

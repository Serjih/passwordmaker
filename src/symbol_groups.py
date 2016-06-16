_latin_lower_case = set('abcdefghijklmnopqrstuvwxyz')
_latin_upper_case = {x.upper() for x in _latin_lower_case}
_digits = set('0123456789')
_other_symbols = set('-=;\'[]\\,./!@#$%^&*()_+{}|:"<>?')

groups = {'l': _latin_lower_case,
          'u': _latin_upper_case,
          'd': _digits,
          'o': _other_symbols}

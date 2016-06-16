def mk_pwd(groups):
    print('Select groups of symbols:')
    print('    l - latin lower case')
    print('    u - latin upper case')
    print('    d - digits')
    print('    o - other symbols')
    print()

    selected_groups = input('Input modes in one string: ').lower().lstrip().rstrip()

    

    print(selected_groups)
    # if '*' in selected_groups:
    #     selected_groups = set('ludo')
    #
    # symbol_set = set()

if __name__ == '__main__':
    mk_pwd('')
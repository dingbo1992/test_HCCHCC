def make_xpath_with_feature(location):
    feature_start = '//*['
    feature_end = ']'
    feature = ''
    print(feature)
    if isinstance(location, str):
        if location.startswith('//'):
            return location
    else:
        for i in location:
            feature += make_xpath_with_unit_feature(i)
    feature = feature.rstrip(' and ')
    location = feature_start + feature + feature_end
    # print(location[1])
    return location


def make_xpath_with_unit_feature(location):
    args = location.split(',')
    key_index = 0
    value_index = 1
    option_index = 2
    feature = ''
    if len(args) == 2:
        feature = 'contains(@' + args[key_index] + ", '" + args[value_index] + "')" + ' and '
    elif len(args) == 3:
        if args[option_index] == '1':
            feature = '@' + args[key_index] + " = '" + args[value_index] + "'" + ' and '
        elif args[option_index] == '0':
            feature = 'contains(@' + args[key_index] + ", '" + args[value_index] + "')" + ' and '
    return feature


if __name__ == '__main__':
    loc = ["test,设,0", 'index,1,1', 'index,50']
    # loc = '//*[contains(@text, "设置")]'
    a = make_xpath_with_feature(loc)
    print(a)
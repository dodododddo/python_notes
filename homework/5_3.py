def check_in(name, sex, city = 'Shenzhen', **extra_info):
    '''
    登记必填信息与可选信息
    '''
    fundamantal_info = {'name':name, 'sex':sex, 'city':city}
    return {**fundamantal_info, **extra_info}


if __name__ == '__main__':
    info = check_in('Salas', 'male', hobby = 'swimming', rank = 85)
    print(info)
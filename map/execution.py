import map_draw
import json

map = map_draw.Draw_map()

# 获取数据
with open('data.json', 'r') as file:
    data = file.read()
    data = json.loads(data)


# 中国疫情地图
def china_map(update_time):
    area = []
    confirmed = []
    for each in data:
        print(each)
        area.append(each['area'])
        confirmed.append(each['confirmed'])
    map.to_map_china(area, confirmed, update_time)


# 省、直辖市疫情地图
def province_map(update_time):
    for each in data:
        city = []
        confirmeds = []
        province = each['area']
        for each_city in each['subList']:
            city.append(each_city['city'] + "市")
            confirmeds.append(each_city['confirmed'])
            map.to_map_city(city, confirmeds, province, update_time)
        if province == '上海' or '北京' or '天津' or '重庆':
            for each_city in each['subList']:
                city.append(each_city['city'])
                confirmeds.append(each_city['confirmed'])
                map.to_map_city(city, confirmeds, province, update_time)

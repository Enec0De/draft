#!/usr/bin/env python
def calculate_sector(central_angle, radius):
    sector_area = central_angle /360 * 3.14 *radius ** 2
    print(f"该扇形面积为：{sector_area}")
    return sector_area

central_angle = float(input("输入圆心角（单位：度）："))
radius = float(input("输入半径："))

area=calculate_sector(central_angle, radius)

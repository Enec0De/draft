#!/usr/bin/env python
my_dict = {"键1":"值1",
           "键2":"值2"}

my_dict["绝绝子"] = "666"
my_dict["键1"] = "新值1"

querry = input("你要查谁：")
if querry in my_dict:
    print(querry + "含义如下")
    print(my_dict[querry])
else:
    print("无该词条。")
    print("现在一共有" + str(len(my_dict)) + "条词条")

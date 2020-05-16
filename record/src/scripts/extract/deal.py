from load.load_data import load_data
import pandas as pd
import xlwt
from load_config.load_file import load_work_day, load_time

time = load_time()
data = load_data()
month_day = load_work_day()
month = time["month"]
day = month_day[month]


def deal():
    info = {}
    for item in data:
        if item["spname"] == "请假":
            name = item["apply_name"]
            _type = item["leave"]["reason"]
            duration = item["leave"]["duration"]
            if name in info.keys():
                info[name].append([_type, duration])
            else:
                info[name] = [[_type, duration]]
    for key in info.keys():
        a = 0
        for i in range(len(info[key])):
            a += info[key][i][1]
        info[key].append(a)
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet("Sheet", cell_overwrite_ok=True)
    name = ["姓名"]
    diration = ["请假时长"]
    _str = ["detail"]
    # print(info)

    for key in info.keys():
        name.append(key)
        diration.append(info[key][-1])
        str1 = ""
        for item in info[key][:-1]:
            str1 += "".join(str(item) for item in item)
        _str.append(str1)
        for i in range(len(name)):
            worksheet.write(i, 0, name[i])
            worksheet.write(i, 1, diration[i])
            worksheet.write(i, 2, _str[i])
    workbook.save("../../../output/data.xlsx")

    xlsx1 = pd.ExcelFile("../../../data/考勤表.xlsx")
    xlsx2 = pd.ExcelFile("../../../output/data.xlsx")
    dsf1 = xlsx1.parse(sheet_name="Sheet1")
    dsf2 = xlsx2.parse(sheet_name="Sheet")
    df = dsf1.merge(dsf2, how="left")
    df = df.fillna(0)
    day_list = []
    for i in range(len(df)):
        day_list.append(day)
    df["应出勤天数"] = day_list
    df["请假时长"] = [int(item) / 24 for item in df["请假时长"]]
    df["实际出勤天数"] = [(int(day) - item) for item in df["请假时长"]]
    df = df.fillna("")
    with pd.ExcelWriter("../../../output/考勤表.xlsx", engine="openpyxl") as writer:
        df.to_excel(writer, "{}月考勤表".format(month))
    file_path = "../../../output/考勤表.xlsx"
    return file_path

from flask import Flask, jsonify
import pandas as pd
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # 解决跨域问题

# -------------------------
# 工具函数：处理薪资文本
# -------------------------
def parse_salary(s):
    if pd.isna(s):
        return None, None
    s = str(s)
    s = s.replace('元/月','').replace('元','').replace('/月','').replace('每月','')

    unit = 1
    if '万' in s:
        unit = 10000
    elif '千' in s:
        unit = 1000

    nums = re.findall(r"(\d+(?:\.\d+)?)", s)
    if not nums:
        return None, None

    # 区间情况
    if len(nums) >= 2:
        a = int(round(float(nums[0]) * unit))
        b = int(round(float(nums[1]) * unit))
        return a, b

    # 单值情况
    v = int(round(float(nums[0]) * unit))
    return v, v


# -------------------------
# API：城市聚合数据
# -------------------------
@app.route("/api/city")
def get_city_data():

    df = pd.read_excel('it 行业招聘数据.xlsx')

    # 解析薪资
    df[['min','max']] = df['薪资文本'].apply(lambda x: pd.Series(parse_salary(x)))
    df['avg'] = (df['min'] + df['max']) / 2

    # 经验
    df['exp'] = df['工作年限要求'].fillna('无需经验').apply(
        lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0
    )

    # 学历
    edu_map = {'大专': 1, '本科': 2, '硕士': 3, '博士': 4}
    df['edu'] = df['学历要求'].map(edu_map).fillna(1)

    # 聚合
    city = df.groupby('检索城市').agg(
        count=('岗位id', 'count'),
        avg_salary=('avg', 'mean'),
        avg_exp=('exp', 'mean'),
        avg_edu=('edu', 'mean')
    ).round(2).reset_index()

    return jsonify(city.to_dict(orient='records'))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

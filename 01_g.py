# coding=utf-8
import streamlit as st
import pandas as pd
import os
from PIL import Image

import logging

logger = logging.getLogger("dou")
# 设置日志级别
logger.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s')

# 设置输出流
sh = logging.StreamHandler()
# 设置输出流的格式
sh.setFormatter(formatter)

# 设置日志文件保存  日志文件存放到 logs目录
filepath = os.path.join(os.path.dirname(__file__), "./logs")  # 使用python内置模块获取logs目录绝对路径
if not os.path.exists(filepath):  # 如果不存在这个目录
    os.mkdir(filepath)  # 创建目录
logfile = os.path.join(filepath, 'log.txt')  # 设置日志文件路径
fl = logging.FileHandler(filename=logfile, encoding='utf8')
fl.setFormatter(formatter)
# 添加自定义的日志处理。
logger.addHandler(sh)
logger.addHandler(fl)

# learn log

# 设置网页信息
st.set_page_config(page_title="电竞经理选手招聘辅助工具", page_icon=":rainbow:", layout="wide")



st.subheader("电竞经理选手招聘辅助工具")
# 3列布局
left_column, middle_column, right_column = st.columns(3)

with left_column:
    diyu = st.multiselect(
         '地域',
         ('华东', '华中', '外援', '西南', '华南', '华北', '东北'))
    label01 = st.multiselect(
         '标签1',
         ('经验丰富', '上分机器', '直播天才', '排位王者'))
with middle_column:
    zhandui = st.multiselect(
         '战队',
         ('TES', 'RNG', 'LNG', 'WEB', 'OMG', 'EDG', 'V5', 'JDG', 'UP', 'FPX',
           'BLG', 'RA', 'AL', 'WE', 'IG', 'TT'))
    label02 = st.multiselect(
         '标签2',
         ('操作', '头脑', '状态', '大心脏', '流量', '训练态度', '节目效果'))

with right_column:
    weizhi = st.multiselect(
         '选手上分位置',
         ['辅助', '打野', '下路', '中路', '上路'])
    # num = 10
    # st.table(pd.Series(num,index=["访问量"]))


choose_l = weizhi+diyu+zhandui+label01+label02

st.write('你当前的选择为:\n', "+".join(choose_l))

data=pd.read_csv("data_.csv")
def panduan_cf(li01,li02):
    return [i for i in li02 if i in li01]
def jisuan(data):
    fina01 = []
    fina02 = []
    for i in range(data.shape[0]):
        li01 = data.iloc[i, 1:-1].values.tolist()
        res = panduan_cf(li01, choose_l)
        fina01.append("+".join(res))
        fina02.append(len(res))
    data["推荐词条"] = fina01
    data["num"] = fina02
    data.sort_values("num", ascending=False, inplace=True)
    return data.head(10)

if st.button('计算一下'):
    finall_data= jisuan(data)
    st.table(finall_data)
    logger.info("1")
    # st.write("推荐词条为："+data["output"])
else:
    st.write(' ')

middle_picture, right_picture = st.columns(2)

image_ssp = Image.open('刷碎片.png')
image_sc = Image.open('英雄擅长汇总.png')
with middle_picture:
    if st.button("各英雄碎片出处"):
        st.image(image_ssp, caption='各英雄碎片出处')
with right_picture:
    if st.button("各英雄擅长汇总"):
        st.image(image_sc,caption="各英雄擅长汇总")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

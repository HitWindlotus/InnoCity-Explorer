import streamlit as st
import folium
from streamlit_folium import folium_static
import geopandas as gpd
import folium.plugins
from branca.element import Figure
import pandas as pd
import numpy as np
from folium.plugins import MousePosition
from branca.colormap import LinearColormap

# 创建 Streamlit 应用程序
st.title('InnoCity Explorer')

shp_file = "shp\shap1.shp"
data = gpd.read_file(shp_file)
# print(data.columns)
col1, col2, col3 = st.columns([1, 1, 1])
shap = col1.selectbox(
   'SHAP影响因素重要性',
   ('知识扩散强度', '科技服务要素', '金融咨询服务', '商务服务要素','交流空间要素','开放空间要素','文化服务要素','休闲娱乐服务','高程','坡度'
    ,'亲水性','生态性','便利店设施要素','购物服务要素','餐饮服务要素','医疗服务要素','基础教育服务','交通路网要素','公交服务要素','地铁服务要素','容积率',
    '人口空间分布','单位GDP指数','租房价格','政策支持要素','投资环境要素','市场距离','产业园区建设'))
data22 = col2.selectbox(
   '2022年要素分布',
   ('知识扩散强度', '科技服务要素', '金融咨询服务', '商务服务要素','交流空间要素','开放空间要素','文化服务要素','休闲娱乐服务','高程','坡度'
    ,'亲水性','生态性','便利店设施要素','购物服务要素','餐饮服务要素','医疗服务要素','基础教育服务','交通路网要素','公交服务要素','地铁服务要素','容积率',
    '人口空间分布','单位GDP指数','租房价格','政策支持要素','投资环境要素','市场距离','产业园区建设'))
data20 = col3.selectbox(
   '2020年要素分布',
   ('知识扩散强度', '科技服务要素', '金融咨询服务', '商务服务要素','交流空间要素','开放空间要素','文化服务要素','休闲娱乐服务','高程','坡度'
    ,'亲水性','生态性','便利店设施要素','购物服务要素','餐饮服务要素','医疗服务要素','基础教育服务','交通路网要素','公交服务要素','地铁服务要素','容积率',
    '人口空间分布','单位GDP指数','租房价格','政策支持要素','投资环境要素','市场距离','产业园区建设'))
# 创建地图
m = folium.Map(location=[45.763276,126.649407],
               zoom_start=10,
               control_scale=True,
               # tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=18&scale=1&style=7&x={x}&y={y}&z={z}'
               tiles='cartodbpositron'
               )


for _, row in data.iterrows():
    folium.GeoJson(row.geometry).add_to(m)
    # print(row.geometry)

folium_static(m)

cluster = st.selectbox('高潜力创新空间类型',('政策支撑型创新空间', '城市服务支撑型创新空间', '知识扩散型创新空间', '生产服务型创新空间','边缘创新空间'))
zc = "shp\clu\zc.shp"
zc = gpd.read_file(zc)
csfw = "shp\clu\csfw.shp"
csfw = gpd.read_file(csfw)
zsks = "shp\clu\zsks.shp"
zsks = gpd.read_file(zsks)
scfw = "shp\clu\scfw.shp"
scfw = gpd.read_file(scfw)
cxby = "shp\clu\cxby.shp"
cxby = gpd.read_file(cxby)
m2 = folium.Map(location=[45.763276,126.649407],
               zoom_start=10,
               control_scale=True,
               tiles='cartodbpositron'
               )
if cluster == '政策支撑型创新空间':
    for _, row in data.iterrows():
        folium.GeoJson(zc.geometry).add_to(m2)
elif cluster == '城市服务支撑型创新空间':
    for _, row in data.iterrows():
        folium.GeoJson(csfw.geometry).add_to(m2)
elif cluster == '知识扩散型创新空间':
    for _, row in data.iterrows():
        folium.GeoJson(zsks.geometry).add_to(m2)
elif cluster == '生产服务型创新空间':
    for _, row in data.iterrows():
        folium.GeoJson(scfw.geometry).add_to(m2)
elif cluster == '边缘创新空间':
    for _, row in data.iterrows():
        folium.GeoJson(cxby.geometry).add_to(m2)

folium_static(m2)





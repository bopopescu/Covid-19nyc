# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app
import plotly.figure_factory as ff
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df_china = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/China_Covid19-3-23.csv")
df_italy = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/Italy_Covid19-3-23.csv")
df_usa = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/Usa_Covid19-3-23.csv")
df_usa_total_h = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/UsaTotal_Covid19-3-23.csv")
df_italy_total_h = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/ItalyTotal_Covid19-3-23.csv")
df_china_total_h = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_world/ChinaTotal_Covid19-3-23.csv")


#-----------------------fig

top = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_nyc/daily_num_cases_nyc.csv")
top5 = top.tail()

fig_daily_num_NYC = px.bar(top5, x='date_found_positive', y='New York',
             hover_data=['New York', 'date_found_positive'], color='New York',
             color_continuous_scale=px.colors.diverging.BrBG,
             labels={'date_found_positive':'Date'},
             text = 'New York', height = 220)

fig_daily_num_NYC.update_traces(texttemplate='%{text}', textposition='inside')

# annotationsDailyNYC = [ dict(xref='paper', yref='paper', x=0.5, y=-0.16,
#                               xanchor='center', yanchor='top',
#                               text='Data Provided by the New York State Department of Health',
#                               font=dict(family='Arial',
#                                         size=12,
#                                         color='#05b9f0'),
#                               showarrow=False)]
fig_daily_num_NYC.update_layout(
    showlegend=False,
    # title_text='DAILY NUMBER OF CASES<br>IN NEW YORK CITY',
    font=dict(
    size=12,
    color="#a3a3a3"
    ),
    xaxis_title="",
    yaxis_title="",
    plot_bgcolor='white',
    margin=dict(l=0, r=0, t=0, b=0),
    # annotations = annotationsDailyNYC,
)
fig_daily_num_NYC.update_layout(coloraxis_showscale=False)
fig_daily_num_NYC.update_xaxes(showticklabels=True)
fig_daily_num_NYC.update_yaxes(showticklabels=False)

fig_daily_num_NYC.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

#---------------------------------------------

table_h = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_ny/percentage_change_County.csv")
table_h = table_h.tail(7)

fig_percentage_change = go.Figure()

fig_percentage_change = px.area(table_h, x='dates', y='New York',
             hover_data=['New York', 'dates'],
             text = 'New York',
             color_discrete_sequence=px.colors.qualitative.Pastel,
             line_shape='spline',
             height=210)


fig_percentage_change.update_layout(
    plot_bgcolor='white',
    showlegend=False,
    font_color="#05b9f0",
)

fig_percentage_change.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})
#---------------------------------------------


age = ["0 to 17", "18 to 44", "45 to 64", "65 to 74 ", "75 and over", "Unknown"]
color1 = ["#d7e76f","#046162","#F686A9","#ffcece","#0497AE", "#047484"]

gender =["Female","Male"]
color2 = ["#52D3C3","#047484"]

# Create subplots: use 'domain' type for Pie subplot
fig_nyc_demo = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig_nyc_demo.add_trace(go.Pie(labels=age, values=[374, 6786, 4906, 1591, 1109, 10], name="Age Group",marker=dict(colors=color1)),
              1, 1)
fig_nyc_demo.add_trace(go.Pie(labels=gender, values=[6374,8379], name="Gender",marker=dict(colors=color2)),
              1, 2)


# Use `hole` to create a donut-like pie chart
fig_nyc_demo.update_traces(hole=.4, hoverinfo="label+percent+name+value",
                  hovertemplate = '<b>%{label}</b>'
                        '<br><b>Percentage</b>: %{percent}<br>'
                        '<b><b>Number of People</b>: %{value}<br>',
                  textposition='inside', textinfo='percent+label')

fig_nyc_demo.update_layout(
    title={
        'text':"DEMOGRAPHICS OF PEOPLE <br>WITH COVID-19 (13119) IN<br>NYC AS OF MARCH 24, 2020 9 AM",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font_size=14,
    font_color="#05b9f0",
    showlegend=False,
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Age Groups', x=0.18, y=0.5, font_size=13, showarrow=False),
        dict(text='Gender', x=0.81, y=0.5, font_size=18, showarrow=False)])


#---------------------------------------------


#DEATHS
age = ["0 to 17", "18 to 44", "45 to 64", "65 to 74 ", "75 and over"]
color1 = ["#0497AE","#046162","#F686A9","#ffcece","#0497AE"]

gender =["Female","Male"]
color2 = ["#d7e76f","#26505E"]

underlying_illness =["Had Underlying Illness","Did Not"]
color3 = ["#52D3C3","#046162"]

# Create subplots: use 'domain' type for Pie subplot
fig_nyc_death = make_subplots(rows=1, cols=3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])
fig_nyc_death.add_trace(go.Pie(labels=age, values=[0, 3, 31, 23, 68], name="Age Group",marker=dict(colors=color1)),
              1, 1)
fig_nyc_death.add_trace(go.Pie(labels=gender, values=[47,78], name="Gender",marker=dict(colors=color2)),
              1, 2)
fig_nyc_death.add_trace(go.Pie(labels=underlying_illness, values=[101,9,15], name="Underlying Illness",marker=dict(colors=color3)),
              1, 3)

# Use `hole` to create a donut-like pie chart
fig_nyc_death.update_traces(hole=.4, hoverinfo="label+percent+name+value",
                  hovertemplate = '<b>%{label}</b>'
                        '<br><b>Percentage</b>: %{percent}<br>'
                        '<b><b>Number of People</b>: %{value}<br>',
                  textposition='inside', textinfo='percent+label')

fig_nyc_death.update_layout(
    title={
        'text':"DEMOGRAPHICS OF PEOPLE WHO DIED (125) OF COVID-19 IN <br>NYC AS OF MARCH 23, 2020 5PM",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font_size=14,
    font_color="#05b9f0",
    showlegend=False,
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='Age Groups', x=0.10, y=0.5, font_size=13, showarrow=False),
                dict(text='Gender', x=0.5, y=0.5, font_size=18, showarrow=False),
                dict(text='Underlying Illness', x=0.91, y=0.5, font_size=11, showarrow=False)])

#---------------------------------------------

mapbox_access_token = "pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txcjE4NDAwNngzZms0ZndzNGM3dG0ifQ.gXrN0wMYVhqUp7t1LOHEwA"
#open(".mapbox_token").read()

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-22-2020.csv')

fig1 = go.Figure()

fig1 = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_data=["Country/Region",'Confirmed', 'Deaths'],
                        size='Confirmed', zoom=1, color = 'Confirmed', color_continuous_scale=px.colors.sequential.Purp, size_max=40,height=600)

fig1.update_layout(
    mapbox_style="white-bg",
    hovermode='closest',
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://api.mapbox.com/styles/v1/lilysu/ck81nlmtm0fwq1iqkv33jiu2r/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
                # purple "https://api.mapbox.com/styles/v1/lilysu/ck811j4xp18kf1iphb7bv365a/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
                # green "https://api.mapbox.com/styles/v1/lilysu/ck7v7bqqy08ae1irye0k0jcot/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoibGlseXN1IiwiYSI6ImNrN2txb28zYjAwNjMzZWxvc2liOTFveGMifQ.wuFm9PLDxO3lhL_bVqMvaA"
            ] 
        },
        # {
        #     "sourcetype": "raster",
        #     "source": ["https://geo.weather.gc.ca/geomet/?"
        #                "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
        #                "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
        # }
      ])
fig1.update_layout(coloraxis_showscale = False)
fig1.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})
#---------------------------------------------------------------------------FIG 1Half
import requests
df = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_ny/county_map.csv")

r = requests.get('https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/nys_geojson/new-york-counties.geojson')
geojson = r.json()

fig1Half = px.choropleth_mapbox(df, geojson=geojson, 
                           animation_frame="date", animation_group="total",
                           locations="county_full", 
                           featureidkey="properties.name",
                           center={"lat": 42.85, "lon":-75.9},
                           mapbox_style="carto-positron", zoom=5.7,
                           opacity = .7,
                           height = 720,
                           color = 'total',
                           color_continuous_scale=px.colors.sequential.Teal,
                           custom_data = ['22_Mar_Cov_Pos'],
                           #hover_data = ["date"],
                           labels = {"total":"Positive Cases", "county_full": "location"},
                           )


fig1Half.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
fig1Half.update_layout(coloraxis_showscale = False, showlegend = False)

#------------------------------------------------------------------------------------------COUNTY CASES
fig_daily_county_cases = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_ny/county_table.csv")
fig_daily_county_cases = fig_daily_county_cases.head(15)


fig_daily_county_cases = px.bar(fig_daily_county_cases, x='index', y='March 24', 
             text='March 24', 
             color = 'March 24',
             height = 350,
             color_continuous_scale=px.colors.diverging.BrBG,
             labels={'New York State Counties':'County','March 24':'March 24rd Confirmed Cases'})
fig_daily_county_cases.update_traces(texttemplate='%{text}', textposition='outside')
fig_daily_county_cases.update_layout(
    plot_bgcolor='white',
    showlegend=False,
    xaxis_title="",
    font=dict(
    color="#a3a3a3",)
    # title_text='NUMBER OF POSITIVE CASES OF COVID-19 BY COUNTY FOR THE TOP 20 COUNTIES'
)

fig_daily_county_cases.update_layout(coloraxis_showscale=False)
fig_daily_county_cases.update_layout(margin={"r":0,"t":15,"l":0,"b":0})

#------------------------------------------------------------------------------------------COUNTY day-to-day changes
table = pd.read_csv("https://raw.githubusercontent.com/LilySu/Covid-19nyc/master/df_nyc/daily_num_cases_nyc.csv")

table_h = table.tail(7)
collist = ['Nassau','New York', 'Onondaga', 'Putnam', 'Rockland', 'Rensselaer','Rockland', 'Westchester']
colors = ['#99d1ce', '#56b3ae', '#3c8682', '#aa7d7d', '#aa7d7d', '#8b5b5b','#305f4b','#baa991']

countydaytoday = go.Figure()

for i, j in zip(collist, colors):
    countydaytoday.add_trace(go.Scatter(x=table_h['date_found_positive'], y=table_h[i], name = i, text=table_h[i],mode='lines+markers',
    hoverinfo='text+name',line=dict(color=j, width=4)))


countydaytoday.update_layout(
    yaxis=dict(
        title_text="Confirmed Cases"
    ),
    autosize=False,
    height=220,
    plot_bgcolor='white',
    showlegend=True,
    #title_text='DAILY NUMBER OF CASES BY COUNTY'
    font=dict(
    # family="Arial",
    color="#a3a3a3")
)
annotations = [ dict(xref='paper', yref='paper', x=0.5, y=-0.122,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the New York State Department of Health',
                              font=dict(family='Arial',
                                        size=12,
                                        color='#05b9f0'),
                              showarrow=False)]
countydaytoday.update_layout(annotations=annotations)

countydaytoday.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#---------------------------------------------------------------------------SYMPTOM FIGURE

# x1 = np.random.randn(200)
# x2 = np.random.randn(200) + 2

# group_labels = ['Disease Transmitted', 'Signs of Symptoms']

# colors = ['#7FA6EE', '#B8F7D4']

# # Create distplot with curve_type set to 'normal'
# figA = ff.create_distplot([x1, x2], group_labels, bin_size=.5,
#                          curve_type='normal', # override default 'kde'
#                          colors=colors)

# # Add title
# figA.update_layout(title_text='IT TAKES ON AVERAGE OF 14 DAYS FOR THE SYMPTOMS TO APPEAR')

#------------------------------------------FIG 2

fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=df_italy["date"], y=df_italy["new_Confirmed"], #fill='tozeroy',fillcolor='#B0DAAE',
                    mode= 'lines', name = 'Italy',legendgroup="group3",
                    stackgroup='two',
                    line=dict(width=0.5, color='rgba(183, 224, 240, 0.94)'),
                    text="Italy<br>New Confirmed Cases <br>from the day before",hoveron = 'points+fills', 
                    hoverinfo = 'text+y'))

fig2.add_trace(go.Scatter(x=df_usa["date"], y=df_usa["new_Confirmed"],##fill='toself',fillcolor='rgba(133, 70, 216, 0.3)',
                    mode='lines',legendgroup="group2",
                    stackgroup='one',
                    line=dict(width=0.5, color='rgba(238, 175, 206, 0.82)'),
                    text="U.S.<br>New Confirmed Cases <br>from the day before",hoveron = 'points+fills', name = 'U.S.',
                    hoverinfo = 'text+y' # override default markers+lines
                    ))

fig2.add_trace(go.Scatter(x=df_china["date"], y=df_china["new_Confirmed"], #fill='tozeroy',fillcolor='#F4DBE5',
                    mode='lines', legendgroup="group1",
                    stackgroup='three',
                    line=dict(width=0.5, color='rgba(159, 133, 229, 0.51)'),
                    text="China<br>New Confirmed Cases <br>from the day before",hoveron = 'points+fills', name = 'China',
                    hoverinfo = 'text+y' # override default markers+lines
                    ))

annotat = []
annotat.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
            xanchor='center', yanchor='top',
            text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
            font=dict(family='Arial',
                    size=12,
                    color='#05b9f0'),
            showarrow=False))

fig2.update_layout(
    annotations = annotat,
    yaxis=dict(title_text="Confirmed Cases",color='#05b9f0'),
    title = "DAY-TO-DAY ADDITIONS IN CONFIRMED CASES IN U.S. VS. CHINA VS. ITALY",paper_bgcolor='rgba(0,0,0,0)',
    font=dict(family='Arial',
    color='#05b9f0'),
    plot_bgcolor='rgba(0,0,0,0)', 
)

#--------------------------------------------------------


#--------------------------------------------------fig4


fig4 = go.Figure()

# Add surface trace
fig4.add_trace(go.Scatter(x=df_italy['date'], y=df_italy['Confirmed'],
                    name = "Italy",
                    hovertext=df_italy["Confirmed"],
                    hoverinfo='text',
                    hovertemplate =
                    '<i>Date: </i>: %{x}'+
                    '<br><b>Confirmed: </b>: %{y:,}<br>',
                    line_shape='spline',
                    line_color='#68CEF3',
                    ))

fig4.add_trace(go.Scatter(x=df_china['date'], y=df_china['Confirmed'],
                    name = "China",
                    hovertext=df_china["Confirmed"],
                    hoverinfo='text',
                    hovertemplate =
                    '<i>Date: </i>: %{x}'+
                    '<br><b>Confirmed: </b>: %{y:,}<br>',
                    line_shape='spline',
                    line_color='#9e92f6',
                    ))
fig4.add_trace(go.Scatter(x=df_usa['date'], y=df_usa['Confirmed'],
                    name = "US",
                    hovertext=df_usa["Confirmed"],
                    hoverinfo='text',
                    hovertemplate =
                    '<i>Date: </i>: %{x}'+
                    '<br><b>Confirmed: </b>: %{y:,}<br>',
                    line_shape='spline',
                    line_color = '#e7b1c7',
                    ))

fig4.update_traces(hoverinfo='text+name', mode='lines+markers')

# Update plot sizing
fig4.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=True,
        title_text="Confirmed Cases"
    ),
    autosize=True,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=False,
    plot_bgcolor='white',
    font=dict(
    # family="Arial",
    color="#a3a3a3")
)

# Update 3D scene options
fig4.update_scenes(
    aspectratio=dict(x=1, y=1, z=0.7),
    aspectmode="manual"
)

# Default annotations
annotations = []
# for y_trace, label, color in zip(y_data, labels, colors):
    # labeling the left_side of the plot
annotations.append(dict(xref='paper', x=.990, y=54500,
                              xanchor='right', yanchor='bottom',
                              text='Italy',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False))

annotations.append(dict(xref='paper',  x=.99, y=29000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False))
annotations.append(dict(xref='paper', x=1.01, y=78600,
                              xanchor='right', yanchor='bottom',
                              text='China',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False))
# Title
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='COVID-19 CONFIRMED CASES CHINA VS. ITALY VS. UNITED STATES',
                              font=dict(family='Arial',
                                        size=20,
                                        color='#05b9f0'),
                              showarrow=False))
# Source
annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='#05b9f0'),
                              showarrow=False))

# Add Annotations with Buttons

all_annotations = [dict(xref='paper', x=1.01, y=78600,
                              xanchor='right', yanchor='bottom',
                              text='China',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                   dict(xref='paper', x=1.05, y=54500,
                              xanchor='right', yanchor='bottom',
                              text='Italy',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', x=1.05, y=29000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='COVID-19 CONFIRMED CASES CHINA VS. ITALY VS. UNITED STATES',
                              font=dict(family='Arial',
                                        size=20,
                                        color='#05b9f0'),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='#05b9f0'),
                              showarrow=False)]


italy_annotations = [dict(xref='paper', x=.990, y=54000,
                              xanchor='right', yanchor='bottom',
                              text='Italy',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', x=.99, y=29000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='COVID-19 CONFIRMED CASES CHINA VS. ITALY VS. UNITED STATES',
                              font=dict(family='Arial',
                                        size=20,
                                        color='#05b9f0'),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='#05b9f0'),
                              showarrow=False)]

china_annotations = [dict(xref='paper', x=1.01, y=78600,
                              xanchor='right', yanchor='bottom',
                              text='China',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', x=.99, y=54000,
                              xanchor='right', yanchor='bottom',
                              text='U.S.',
                              font=dict(family='Arial',
                                        size=20),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='COVID-19 CONFIRMED CASES CHINA VS. ITALY VS. UNITED STATES',
                              font=dict(family='Arial',
                                        size=20,
                                        color='#05b9f0'),
                              showarrow=False),
                     dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                              xanchor='center', yanchor='top',
                              text='Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)',
                              font=dict(family='Arial',
                                        size=12,
                                        color='#05b9f0'),
                              showarrow=False)]

fig4.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            active=0,
            pad={"r": 10, "t": 40},
            showactive=True,
            x=0.05,
            xanchor="left",
            y=1.18,
            font=dict(
            # family="Arial",
            color="#a3a3a3"),
            buttons=list([
                dict(label="Show All",
                     method="update",
                     args=[{"visible": [True, True, True]},
                           {
                            "annotations": all_annotations}]),
                dict(label="Compare with Italy",
                     method="update",
                     args=[{"visible": [True, False, True]},
                           {
                            "annotations": italy_annotations}]),
                dict(label="Compare with China",
                     method="update",
                     args=[{"visible": [True, True, False]},
                           {
                            "annotations": china_annotations}]),
            ]),
        )
    ])


fig4.update_layout(annotations=annotations)

#========================================================================

top_labels = ['CONFIRMED', 'RECOVERED','DEATHS']
top_labels_l = ['Confirmed', 'Recover', 'Die']

colors = ['#d9f0f2', '#38cedc',
          '#f2d4e0']

x_data = df_usa_total_h[['Confirmed_normalized','Recovered_normalized','Deaths_normalized']].values

y_data = df_usa_total_h['date'].values

fig_us_compare = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig_us_compare.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig_us_compare.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=140, b=25),
    # margin=dict(l=1.20, r=.10, t=1.40, b=.25),
    showlegend=False,
)

annotations1 = []

for yd, xd in zip(y_data, x_data):
    # labeling the first percentage of each bar (x_axis)
    annotations1.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text= yd, # str(xd[0])[:2] + "% " + top_labels_l[0], #'{:.s}'.format(xd[0]) + '%',
                            hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='#6cc3cb'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations1.append(dict(xref='x', yref='paper',
                                x=(xd[0] / 2), y=1.05,
                                text=top_labels[0],
                                hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                font=dict(family='Arial', size=10,
                                          color='rgb(186, 186, 186)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations1.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/10), y=yd,
                                    text= " ", 
                                    hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                    font=dict(family='Arial', size=24,
                                              color='rgba(20, 137, 16, 0.77)'),
                                    #hovertext = str(xd[i])[:2] + "% " + top_labels_l[i], #str(xd[i]) + '%',
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations1.append(dict(xref='x', yref='paper',
                                        x=(space + (xd[i]/10))-8, y=1.05,
                                        text=top_labels[i],
                                        hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                        font=dict(family='Arial', size=10,
                                                  color='rgb(186, 186, 186)'),
                                        showarrow=False))
            space += xd[i]+7

fig_us_compare.update_layout(annotations=annotations1 ,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')




fig_us_compare.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

#------------------------------------------------------

top_labels = ['CONFIRMED', 'RECOVERED','DEATHS']
top_labels_l = ['Confirmed', 'Recover', 'Die']

colors = ['#d9f0f2', '#38cedc',
          '#f2d4e0']

x_data = df_italy_total_h[['Confirmed_normalized','Recovered_normalized','Deaths_normalized']].values

y_data = df_italy_total_h['date'].values

fig_italy_compare = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig_italy_compare.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig_italy_compare.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=140, b=25),
    # margin=dict(l=1.20, r=.10, t=1.40, b=.25),
    showlegend=False,
)

annotations1 = []

for yd, xd in zip(y_data, x_data):
    # labeling the first percentage of each bar (x_axis)
    annotations1.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text= yd, # str(xd[0])[:2] + "% " + top_labels_l[0], #'{:.s}'.format(xd[0]) + '%',
                            hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='#6cc3cb'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations1.append(dict(xref='x', yref='paper',
                                x=(xd[0] / 2), y=1.05,
                                text=top_labels[0],
                                hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                font=dict(family='Arial', size=10,
                                          color='rgb(186, 186, 186)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations1.append(dict(xref='x', yref='y',
                                    x=space + (xd[i]/10)+3.95, y=yd,
                                    text= str(xd[i])[:1] + '% ' + top_labels_l[i], 
                                    hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                    font=dict(family='Arial', size=13,
                                              color='#2c8590'),
                                    #hovertext = str(xd[i])[:2] + "% " + top_labels_l[i], #str(xd[i]) + '%',
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations1.append(dict(xref='x', yref='paper',
                                        x=(space + (xd[i]/10))-8, y=1.05,
                                        text=top_labels[i],
                                        hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                        font=dict(family='Arial', size=10,
                                                  color='rgb(186, 186, 186)'),
                                        showarrow=False))
            space += xd[i]-1.5

fig_italy_compare.update_layout(annotations=annotations1 ,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')

fig_italy_compare.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

#------------------------------------------------------


top_labels = ['CONFIRMED', 'RECOVERED','DEATHS']
top_labels_l = ['Confirmed', 'Recover', 'Die']

colors = ['#d9f0f2', '#38cedc',
          '#f2d4e0']

x_data = df_china_total_h[['Confirmed_normalized','Recovered_normalized','Deaths_normalized']].values

y_data = df_china_total_h['date'].values

fig_china_compare = go.Figure()

for i in range(0, len(x_data[0])):
    for xd, yd in zip(x_data, y_data):
        fig_china_compare.add_trace(go.Bar(
            x=[xd[i]], y=[yd],
            orientation='h',
            marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
            )
        ))

fig_china_compare.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
        domain=[0.15, 1]
    ),
    yaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=False,
        zeroline=False,
    ),
    barmode='stack',
    paper_bgcolor='rgb(248, 248, 255)',
    plot_bgcolor='rgb(248, 248, 255)',
    margin=dict(l=120, r=10, t=140, b=25),
    # margin=dict(l=1.20, r=.10, t=1.40, b=.25),
    showlegend=False,
)

annotations1 = []

for yd, xd in zip(y_data, x_data):
    # labeling the first percentage of each bar (x_axis)
    annotations1.append(dict(xref='x', yref='y',
                            x=xd[0] / 2, y=yd,
                            text= yd, # str(xd[0])[:2] + "% " + top_labels_l[0], #'{:.s}'.format(xd[0]) + '%',
                            hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                            font=dict(family='Arial', size=14,
                                      color='#6cc3cb'),
                            showarrow=False))
    # labeling the first Likert scale (on the top)
    if yd == y_data[-1]:
        annotations1.append(dict(xref='x', yref='paper',
                                x=(xd[0] / 2), y=1.05,
                                text=top_labels[0],
                                hovertext = str(xd[0])[:4] + "% " + top_labels_l[0] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                font=dict(family='Arial', size=10,
                                          color='rgb(186, 186, 186)'),
                                showarrow=False))
    space = xd[0]
    for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            if i == 1:
              annotations1.append(dict(xref='x', yref='y',
                                      x=space+22.5, y=yd,
                                      text= str(xd[i])[:4] + '% Recover',
                                      hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                      font=dict(family='Arial', size=14,
                                                color='#d0f1f0'),
                                      #hovertext = str(xd[i])[:2] + "% " + top_labels_l[i], #str(xd[i]) + '%',
                                      showarrow=False))
              # labeling the Likert scale
              if yd == y_data[-1]:
                  annotations1.append(dict(xref='x', yref='paper',
                                          x=(space + (xd[i])), y=1.05,
                                          text=top_labels_l[i],
                                          hovertext = str(xd[i])[:4] + "% " + top_labels_l[i] + " on " + str(yd), #'{:.s}'.format(xd[0]) + '%',
                                          font=dict(family='Arial', size=10,
                                                    color='rgb(186, 186, 186)'),
                                          showarrow=False))
              space += xd[i]


fig_china_compare.update_layout(annotations=annotations1 ,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')


fig_china_compare.layout.margin.update({'t':0, 'b':0, 'r': 0, 'l': 0})

#------------------------------------------------------

columnTopAlert = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('New York State: 25,665 Confirmed cases', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':8}),
            html.H6('Data Above from the New York State Dept. of Health march 24, 3 pm', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':15}),
            ]
        ),
    ],
    md=12,
    #style={'paddingLeft':0,'paddingRight':0},
)

columnTopLeft = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('NYC', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':5}),
            html.H6('Confirmed Cases', style={'fontSize':13, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':0}),
            html.H6('Last 5 Days', style={'fontSize':10, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
            # html.H1('38', style={'fontSize':60, 'color':'#05b9f0', 'marginBottom':0}),#fig4
            ]
        ),
        dcc.Graph(figure=fig_daily_num_NYC),
        html.Center(
            children=[
            html.H6('Day-to-day % Increases', style={'fontSize':11, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':10}),
            html.H6('in Number of', style={'fontSize':10, 'color':'#05b9f0', 'marginTop':6, 'marginBottom':0}),
            html.H6('Confirmed Cases', style={'fontSize':10, 'color':'#05b9f0', 'marginTop':6, 'marginBottom':0}),
            html.H6('NYC', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':6, 'marginBottom':10}),
            ]
        ),
        dcc.Graph(figure=fig_percentage_change),
        html.Center(
            children=[
        html.H6('Data from NY State DOH on March 23, 5 pm', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':8}),
            ]
        ),
    ],
    md=2,
    #style={'paddingLeft':0,'paddingRight':0},
)

columnTopCenter = dbc.Col(
    [
        dcc.Graph(figure=fig1,style={'paddingTop':0, 'paddingBottom':0}),
        html.Center(
            children=[
                html.H6('Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE) updated on March 22nd', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':15, 'marginBottom':0}),#fig4
            ]
        ),
    ],
    md=6,
    )


columnTopRight = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('Positive Cases NYC', style={'fontSize':20, 'color':'#14c5fa', 'marginTop':0, 'marginBottom':8}),#fig4
            html.H1('14,776', style={'fontSize':70, 'color':'#5CD8FE', 'marginBottom':0}),#fig4
            html.H6('Deaths NYC', style={'fontSize':11, 'color':'#14c5fa', 'marginTop':0, 'marginBottom':0}),#fig4
            html.H6('131', style={'fontSize':32, 'color':'#5CD8FE', 'marginBottom':0}),#fig4
            html.H6('Data above from NYC Dept. of Health march 24, 9 AM', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':0}),#fig4
            # dbc.Alert(
            # [
            # html.A("Data from gov. cuomo march 23, 11 AM'", ahref='https://www.nbcnewyork.com/news/local/this-is-not-a-joke-cuomo-rips-nyc-over-crowds-as-tri-state-case-total-nears-20000/2339351/', className="alert-link"),
            # ],
            # color = "primary",
            # ),
            html.H6('Positive Cases by Borough', style={'fontSize':20, 'color':'#208fb1', 'marginTop':20}),
            # html.H1('43', style={'fontSize':68, 'color':'#05b9f0', 'marginBottom':0}),#fig4
            # html.H6('', style={'fontSize':20, 'marginTop':22, 'marginBottom':0}),
            ]
        ),

        html.Center(
            children=[
            html.Img(src=app.get_asset_url('NYC_Covid-19_Cases_03-24_01.png'), style={'display': 'block', 'height':380})
            ]
        ),
        html.Center(
            children=[
            html.H6('Data from NYC DOH, last updated there on March 24, 9 am', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':8}),
            ]
        ),
    ],
    md=4,
)

column0bottomCenter = dbc.Col(
    [
        html.Center(
            children=[
            html.Br(),
            html.Span(' ', className='mr-1'),
            html.Br(),
            html.Span(' ', className='mr-1'),
            dcc.Graph(figure=fig_nyc_demo),
            ]
        )
    ],
    md=12,
)


column0bottomCenter2 = dbc.Col(
    [
        html.Center(
            children=[
            dcc.Graph(figure=fig_nyc_death),
            html.H6('Data for above pie charts from NYC DOH', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':80}),
            ]
        )
    ],
    md=12,
)

column1Left = dbc.Col(
    [
        html.Center(
            children=[
                dcc.Graph(figure=fig1Half),
            ]
        )
    ],
    md=6
)



column1Right = dbc.Col(
    [
        html.Center(
            children=[
                html.H6('NUMBER OF POSITIVE CASES OF COVID-19 BY COUNTY', style={'fontSize':18, 'color':'#05b9f0', 'marginTop':40, 'marginBottom':10}),
                html.H6('FOR THE TOP 15 COUNTIES RANKED BY THE MOST CASES', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':0}),
                dcc.Graph(figure=fig_daily_county_cases),
                html.H6('DAY-TO-DAY POSITIVE CASES OF COVID-19 BY COUNTY', style={'fontSize':18, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':10}),
                html.H6('FOR THE TOP 8 COUNTIES RANKED BY THE MOST CASES', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':0}),
                dcc.Graph(figure=countydaytoday),
            ]
        )
    ],
    md=6
)

column1bottomCenter = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('Data for above interactive charts from NY State DOH', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':20, 'marginBottom':20}),
            ]
        )
    ],
    md=12,
)


column2Center = dbc.Col(
    [
        html.Center(
            children=[
            html.Br(),
            html.Span(' ', className='mr-1'),
            html.H6('NUMBER OF CONFIRMED CASES OF COVID-19', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':60, 'marginBottom':10}),
            html.H6('IN NEW YORK STATE BY COUNTY', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
            html.Img(src=app.get_asset_url('Covid-19_Cases_NYS_03-23_annotated.png'), style={'display': 'block', 'width':'100%'}),
            ]
        )
    ],
    md=7,
)
column2Right = dbc.Col(
    [
        html.Center(
            children=[
            html.Br(),
            html.Span(' ', className='mr-1'),
            html.Br(),
            html.Span(' ', className='mr-1'),
            html.H6('NUMBER OF CONFIRMED CASES OF COVID-19', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':30, 'marginBottom':10}),
            html.H6('IN NEW YORK STATE BY DATE', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
            html.Img(src=app.get_asset_url('Covid-19_Cases_NYS_2020-03-23.gif'), style={'display': 'block', 'width':'100%','marginTop':130, 'marginBottom':100}),
            ]
        )
    ],
    md=5,
)

column2bottomCenter = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('Data from NY State DOH, last updated there on March 24, 5 p.m.', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':0, 'marginBottom':8}),#fig4
            ]
        )
    ],
    md=12,
)

column3CenterAll = dbc.Col(
    [
        html.Center(
            children=[
                html.Br(),
                html.Span(' ', className='mr-1'),
                html.Br(),
                html.Span(' ', className='mr-1'),
                #html.H6('DAY-TO-DAY CHANGES IN CONFIRMED CASES ITALY VS U.S. VS CHINA', style={'fontSize':19, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
                dcc.Graph(figure=fig2),
            ]
        )
    ]
)


columnDistL = dbc.Col(
    [
        html.Center(
            children=[
                html.H6('Status of Covid-19', style={'fontSize':16, 'color':'#05b9f0', 'marginTop':80, 'marginBottom':10}),
                html.H6('cumulative Cases Recorded in', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
                html.H6('U.S.', style={'fontSize':22, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
                html.Div(
                    [
                        dbc.Button("Confirmed", color="light", size="sm"),
                        dbc.Button("Recovered", color="light", size="sm"),
                        dbc.Button("Deaths", color="light", size="sm"),]),
                        dcc.Graph(figure=fig_us_compare),
                     ],
                ),
            ],
    md=12,
)
columnDistC = dbc.Col(
    [
        html.Center(
            children=[
                html.H6('Status of Covid-19', style={'fontSize':16, 'color':'#05b9f0', 'marginTop':60, 'marginBottom':10}),
                html.H6('cumulative Cases Recorded in', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
                html.H6('Italy', style={'fontSize':22, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
                html.Div(
                    [
                        dbc.Button("Confirmed", color="light", size="sm"),
                        dbc.Button("Recovered", color="light", size="sm"),
                        dbc.Button("Deaths", color="light", size="sm"),]),
                        dcc.Graph(figure=fig_italy_compare),
                     ],
                ),
            ],
    md=12,
)
columnDistR = dbc.Col(
    [
        html.Center(
            children=[
                html.H6('Status of Covid-19', style={'fontSize':16, 'color':'#05b9f0', 'marginTop':60, 'marginBottom':10}),
                html.H6('cumulative Cases Recorded in', style={'fontSize':12, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
                html.H6('China', style={'fontSize':22, 'color':'#05b9f0', 'marginTop':10, 'marginBottom':10}),
                html.Div(
                    [
                        dbc.Button("Confirmed", color="light", size="sm"),
                        dbc.Button("Recovered", color="light", size="sm"),
                        dbc.Button("Deaths", color="light", size="sm"),]),
                        dcc.Graph(figure=fig_china_compare),
                     ],
                ),
            ],
    md=12,
)

columnDistbottomCenter = dbc.Col(
    [
        html.Center(
            children=[
            html.H6('Data Provided by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE)', style={'fontSize':8, 'color':'#05b9f0', 'marginTop':20, 'marginBottom':8}),#fig4
            ]
        )
    ],
    md=12,
)



column4CenterAll = dbc.Col(
    [
        html.Br(),
        html.Span(' ', className='mr-1'),
        dcc.Graph(figure=fig4),
        html.Br(),
        html.Span(' ', className='mr-1'),
    ]
)

column5CenterAll = dbc.Col(
    [
        html.Center(
            children=[
            html.Img(src=app.get_asset_url('WashHands.jpg'), style={'display': 'block', 'width':'100%'})
            ]
        )
    ],
    md=12,
)

column6CenterAll = dbc.Col(
    [
        html.Center(
            children=[
            html.Img(src=app.get_asset_url('SocialDistancing.jpg'), style={'display': 'block', 'width':'100%'})
            ]
        )
    ],
    md=12,
)

# layout = dbc.Row([column1, column2])
layout = [
        dbc.Row([columnTopAlert]),
        dbc.Row([columnTopLeft, columnTopCenter, columnTopRight]), 
        dbc.Row([column0bottomCenter]),
        dbc.Row([column0bottomCenter2]),

        dbc.Row([column1Left,column1Right]),
        dbc.Row([column1bottomCenter]),

        dbc.Row([column2Center, column2Right]),
        dbc.Row([column2bottomCenter]),
        dbc.Row([column3CenterAll]),

        dbc.Row([columnDistC, columnDistR, columnDistL]),
        dbc.Row([columnDistbottomCenter]),

        dbc.Row([column4CenterAll]),
        dbc.Row([column5CenterAll]),
        dbc.Row([column6CenterAll]),]


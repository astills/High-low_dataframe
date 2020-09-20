from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components


start=datetime.datetime(2019,3,1)
end=datetime.datetime(2020,3,15)

df=data.DataReader(name="AAPL", data_source="yahoo", start=start, end=end)

p=figure(x_axis_type='datetime', width=1000, height=300)
p.grid.grid_line_alpha=0.3

hours_12 = 12*60*60*1000

p.segment(df.index, df.High, df.index, df.Low, color="Black")

date_decrease = [df.Close < df.Open]
date_increase = [df.Close > df.Open]

def inc_dec(c,o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close, df.Open)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Close-df.Open)


p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"],
        hours_12, df.Height[df.Status=="Increase"], fill_color="#CCFFFF", line_color="black")

p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"],
        hours_12,df.Height[df.Status=="Decrease"], fill_color="FF3333", line_color="black")


script1, div1 = components(p)
cdn_js=CDN.js_files[0]
cdn_css=CDN.css_files[0]
return render_template("html", script1=script1, div1=div1, cdn_css=cdn_css, cdn_js=cdn_js)


#
# output_file("cs.html")
# show(p)


import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit.components.v1 as components



# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="Product Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    # Add 'hour' column to dataframe
    df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S")  # Convert "Time" column to datetime type
    df["hour"] = df["Time"].dt.hour  # Add "hour" column to dataframe
    return df

df = get_data_from_excel()


#Sidebar

st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City",
    options=df["City"].unique(),
    default=df["City"].unique(),
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique(),
)

df_selection = df.query(
   "City == @city & Customer_type ==@customer_type & Gender == @gender"
)

#st.dataframe(df)

#Show Table:
#st.dataframe(df_selection)

#---------MAINPAGE---------

#st.title(":bar_chart: Product Dashboard")
st.title("Product Dashboard")
st.markdown("##")

#Top KPI

total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Amount:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating}")
with right_column:
    st.subheader("Average Amount Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")


####
##Commented below
####

# # SALES BY PRODUCT LINE [BAR CHART]
#sales_by_product_line = (
#    df_selection.groupby(by=["Product line"]).sum()
#)
# fig_product_sales = px.bar(
#     sales_by_product_line,
#     x="Total",
#     y=sales_by_product_line.index,
#     orientation="h",
#     title="<b>Sales by Product Line</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
#     template="plotly_white",
# )
# 
# # st.plotly_chart(fig_product_sales)
# 
# 
# # SALES BY HOUR [BAR CHART]
# sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
# fig_hourly_sales = px.bar(
#     sales_by_hour,
#     x=sales_by_hour.index,
#     y="Total",
#     title="<b>Sales by hour</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
#     template="plotly_white",
# )
# 
# fig_hourly_sales.update_layout(
#     xaxis=dict(tickmode="linear"),
#     plot_bgcolor="rgba(0,0,0,0)",
#     yaxis=(dict(showgrid=False)),
# )
# 
# # st.plotly_chart(fig_hourly_sales)
# 
# 
# left_column, right_column = st.columns(2)
# left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
# right_column.plotly_chart(fig_product_sales, use_container_width=True)


####
##Commented
####
d = {'Month':[1,2,3,4,5,6,7,8,9,10,11],
     'Customer':[47733,38777,44404,46296,38471,29788,19247,23273,20146,19315,20481],
     'Vendor':[3767,2796,2973,3448,2824,1816,1057,1630,1587,1311,1579]}

newdf = pd.DataFrame(data = d)
st.line_chart(newdf, x='Month')

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.dataframe(df_selection)
components.iframe("https://www.vip-studio360.fr/galerie360/visites/vv-schneider-electric/vv-horizon-en-c.html?s=pano89&h=11.5417&v=5.3129&f=74.3802&skipintro&norotation", width=1500, height=700)
#components.iframe("https://sketchfab.com/models/93ff8a41c67e4750a02d44d191f898fe/embed?autostart=1", width=1000, height=800)
#components.iframe("https://sketchfab.com/models/b1b0c15b3e2c4a42ac47ba196277d0da/embed?autostart=1", width=1000, height=800)
#components.iframe("https://renderstuff.com/tools/360-panorama-web-viewer-embed/?image=https://i.ibb.co/xz9J05n/360view.jpg", width=1200, height=700)
#https://renderstuff.com/tools/360-panorama-web-viewer-embed/?image=https://i.ibb.co/xz9J05n/360view.jpg





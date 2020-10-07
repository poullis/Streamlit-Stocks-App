import streamlit as st
import pandas as  pd
from PIL import Image

#Title
st.write("""
# Stock Market Data Visualization
** Bachelor's Thesis 2020 - **
*** Antonis Poullis ***
""")

page_bg_img = '''
<style>
body {
background-image: url("https://digitalsynopsis.com/wp-content/uploads/2017/02/beautiful-color-gradients-backgrounds-026-saint-petersburg.png");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1592422301045-4ceb1b64d63e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60", use_column_width= True)

#Side Bar Header
st.sidebar.header('Dates')
st.sidebar.write('You can insert dates from 2020-03-01 until 2020-09-05.')

#Function to get user input
def get_input():
    start = st.sidebar.text_input("Start Date", "2020-03-01")
    end = st.sidebar.text_input("End Date", "2020-09-05")
    #symbol = st.sidebar.text_input("Stock Symbol", "AMZN")
    symbol = st.selectbox('Select Stock Symbol',('AAL','AAPL','DAL','LUV','UAL','BKNG','EXPE','MAR','TRIP','HTZ','ZM','MSFT','RCL','CCL','NFLX','ROKU','SPOT','TGT','WMT','EBAY','FB','SNAP','TWTR','REGN','GILD','INO','MRNA','NVAX','SBUX','MCD','DRI','AMZN','GOOG'))
    return start, end, symbol

#Create a function to get the company name

def get_company(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'MSFT':
        return 'Microsoft Corp.'
    elif symbol == 'AAPL':
        return 'Apple Inc.'
    elif symbol == 'GOOG':
        return 'Alphabet'
    elif symbol == 'HTZ':
        return 'Hertz Global Holdings Inc'
    elif symbol == 'ZM':
        return 'Zoom'
    elif symbol == 'TGT':
        return 'Target Corporation'
    elif symbol == 'WMT':
        return 'Walmart'
    elif symbol == 'SPOT':
        return 'Spotify'
    elif symbol == 'NFLX':
        return 'Netflix'
    elif symbol == 'FB':
        return 'Facebook'
    elif symbol == 'EBAY':
        return 'Ebay'
    elif symbol == 'TWTR':
        return 'Twitter'
    elif symbol == 'REGN':
        return 'Regeneron Pharmaceuticals'
    elif symbol == 'GILD':
        return 'Gilead Sciences'
    elif symbol == 'INO':
        return 'Inovio Pharmaceuticals '
    elif symbol == 'MRNA':
        return 'Moderna, Inc.'
    elif symbol == 'NVAX':
        return 'Novavax'
    elif symbol == 'CCL':
        return 'Carnival Corp.'
    elif symbol == 'SNAP':
        return 'Snapchat'
    elif symbol == 'RCL':
        return 'Royal Caribbean'
    elif symbol == 'ROKU':
        return 'Roku, Inc.'
    elif symbol == 'SBUX':
        return 'Starbucks Corp.'
    elif symbol == 'MCD':
        return "McDonald's Corp."
    elif symbol == 'DRI':
        return 'Darden Restaurants Inc'
    elif symbol == 'DAL':
        return 'Delta Airlines'
    elif symbol == 'AAL':
        return 'American Airlines'
    elif symbol == 'LUV':
        return 'Southwest Airlines'
    elif symbol == 'UAL':
        return 'United Airlines'
    elif symbol == 'BKNG':
        return 'Booking Holdings Inc'
    elif symbol == 'TRIP':
        return 'TripAdvisor'
    elif symbol == 'EXPE':
        return 'Expedia Group'
    elif symbol == 'MAR':
        return 'Marriot International'        
    else:
        'None'

# Function to get company data and timeframe from user
def get_data(symbol, start, end):
    pics = {
        "GOOG": "https://images.unsplash.com/photo-1594663653925-365bcbf7ef86?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "AMZN": "https://images.unsplash.com/photo-1556382363-8967ad2b37f0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "AAL": "https://images.pexels.com/photos/321159/pexels-photo-321159.jpeg",
        "DAL": "https://images.pexels.com/photos/3623679/pexels-photo-3623679.jpeg",
        "UAL": "https://images.unsplash.com/photo-1473862170180-84427c485aca?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "LUV": "https://images.unsplash.com/photo-1564749290357-fcedf5a94a61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "SBUX": "https://images.pexels.com/photos/597933/pexels-photo-597933.jpeg",
        "FB": "https://s.yimg.com/ny/api/res/1.2/gG0uPNoap8uzjvWvqefGyA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTM0Ny4zMzY2ODM0MTcwODU0NQ--/https://s.yimg.com/uu/api/res/1.2/BiNNo4Bo0I8q0dSwQSw2CQ--~B/aD00MzI7dz0xMTk0O3NtPTE7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/simply_wall_st__316/a0fc4d073bab6c7b785bb32a84cb0542",
        "MCD": "https://images.unsplash.com/photo-1524718730196-9b4aca2b5b8c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "ZM": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg",
        "AAPL": "https://images.unsplash.com/photo-1585184394271-4c0a47dc59c9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "CCL": "https://images.pexels.com/photos/69122/ferry-boat-ferry-ship-boat-69122.jpeg",
        "NFLX": "https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "TGT": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg",
        "BKNG": "https://images.unsplash.com/photo-1585252892385-3e34a7e35c44?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "EXPE": "https://thumbnails.trvl-media.com/nUg2hb7a-gOnRgOiUaJFnzp8PNk=/a.travel-assets.com/mad-service/footer/marquee/v2/BEX_US_EN_MQ.jpg",
        "MAR":  "https://www.gannett-cdn.com/presto/2019/04/16/USAT/15d11370-b0e6-4743-adf0-387d1fa95ab5-AP_Marriott_Starwood_Sale.JPG",
        "TRIP": "https://mk0tainsightsjao4bom.kinstacdn.com/wp-content/uploads/2018/01/Business-on-TA-400x250.jpg",
        "MRNA": "https://img.kyodonews.net/english/public/images/posts/f4fcf7ad9d33595eefc593476719bbb2/photo_l.jpg",
        "GILD": "https://www.biospace.com/getasset/67590a44-e223-4171-b808-a03bd0412f0c/",
        "HTZ": "https://s29755.pcdn.co/wp-content/uploads/2020/05/Hertz_story_2.jpg",
        "SPOT": "https://images.unsplash.com/photo-1532354058425-ba7ccc7e4a24?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "ZM": "https://images.pexels.com/photos/4031818/pexels-photo-4031818.jpeg",
        "TWTR": "https://images.unsplash.com/photo-1583330638480-50271adb037e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1000&q=60",
        "REGN": "https://www.gannett-cdn.com/-mm-/648717dabc841849cc24cdf4e4ac6f2ff04fa9fe/c=0-352-5753-3602/local/-/media/2016/09/13/Westchester/Westchester/636093837029776181-ts091316regenron05.JPG?",
        "INO": "https://www.inovio.com/wp-content/uploads/2020/04/INO-RD-Center.jpg",
        "SNAP": "https://images.pexels.com/photos/4848668/pexels-photo-4848668.jpeg",
        "ROKU": "https://image.roku.com/bWFya2V0aW5n/hero-roku-homescreen-gb.png",
        "WMT": "https://d8it4huxumps7.cloudfront.net/bites/wp-content/uploads/2019/09/14110951/How-an-internship-at-Walmart-India-gave-me-practical-exposure-in-the-field-of-Marketing-Parths-story.jpg",
        "TGT": "https://upgradedpoints.com/wp-content/uploads/2017/11/Target-Store.jpg",
        "EBAY": "https://mk0knowtechie1qof48y.kinstacdn.com/wp-content/uploads/2018/04/ebay.jpg",
        "MSFT": "https://i.middle-east-online.com/styles/home_special_coverage_1920xauto/s3/2020-03/micsoft.jpg",
        "RCL": "https://www.royalcaribbeanblog.com/sites/default/files/blog-images/wonder-up-close-min.jpg",
        "NVAX": "https://qtxasset.com/styles/breakpoint_xl_880px_w/s3/fiercebiotech/1575799070/Belward%20Campus.jpg/Belward%20Campus.jpg",
        "DRI": "https://pbs.twimg.com/media/DHdAVUwXoAAXKfs.jpg",
        }
    if symbol.upper() == 'AMZN':
        #Title
        st.write("""
        # Amazon Inc. 
        """)
        st.subheader('NASQAD:AMZN')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/AMZN.csv")
        #print(df)
    elif symbol.upper() == 'GOOG':
        st.write("""
        # Alphabet Inc. 
        """)
        st.subheader('NASQAD:GOOG')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/GOOG.csv")
    elif symbol.upper() == 'DRI':
        st.write("""
        # Darden Restaurants, Inc.
        """)
        st.subheader('NASQAD:DRI')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/DRI.csv")
    elif symbol.upper() == 'MSFT':
        st.write("""
        # Microsoft Corp. 
        """)
        st.subheader('NASQAD:MSFT')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/MSFT.csv")
    elif symbol.upper() == 'INO':
        st.write("""
        # Inovio Pharmaceuticals Inc. 
        """)
        st.subheader('NASQAD:INO')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/INO.csv")
    elif symbol.upper() == 'SPOT':
        st.write("""
        # Spotify Technology S.A.
        """)
        st.subheader('NYSE:SPOT')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/SPOT.csv")
    elif symbol.upper() == 'ROKU':
        st.write("""
        # Roku Inc.
        """)
        st.subheader('NASQAD:ROKU')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/ROKU.csv")
    elif symbol.upper() == 'WMT':
        st.write("""
        # Walmart Inc.
        """)
        st.subheader('NYSE:WMT')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/WMT.csv")
    elif symbol.upper() == 'TGT':
        st.write("""
        # Target Corporation
        """)
        st.subheader('NYSE:TGT')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/TGT.csv")
    elif symbol.upper() == 'EBAY':
        st.write("""
        # Ebay Inc.
        """)
        st.subheader('NASQAD:EBAY')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/EBAY.csv")
    elif symbol.upper() == 'SNAP':
        st.write("""
        # Snap Inc.
        """)
        st.subheader('NYSE:SNAP')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/SNAP.csv")
    
    elif symbol.upper() == 'TRIP':
        st.write("""
        # TripAdvisor Inc. 
        """)
        st.subheader('NASQAD:TRIP')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/TRIP.csv")
    elif symbol.upper() == 'HTZ':
        st.write("""
        # Hertz Global Holdings, Inc.
        """)
        st.subheader('NASQAD:HTZ')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/HTZ.csv")
    elif symbol.upper() == 'NVAX':
        st.write("""
        # Novavax Inc. 
        """)
        st.subheader('NASQAD:NVAX')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/NVAX.csv")
    elif symbol.upper() == 'MRNA':
        st.write("""
        # Moderna Inc. 
        """)
        st.subheader('NASQAD:MRNA')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/MRNA.csv")
    elif symbol.upper() == 'REGN':
        st.write("""
        # Regeneron Pharmaceuticals 
        """)
        st.subheader('NASQAD:REGN')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/REGN.csv")
    elif symbol.upper() == 'GILD':
        st.write("""
        # Gilead Sciences 
        """)
        st.subheader('NASQAD:GILD')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/GILD.csv")
    elif symbol.upper() == 'TWTR':
        st.write("""
        # Twitter Inc. 
        """)
        st.subheader('NASQAD:TWTR')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/TWTR.csv")
    elif symbol.upper() == 'MAR':
        st.write("""
        # Marriot International
        """)
        st.subheader('NASQAD:MAR')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/MAR.csv")
    elif symbol.upper() == 'EXPE':
        st.write("""
        # Expedia Travel 
        """)
        st.subheader('NASQAD:EXPE')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/EXPE.csv")
    elif symbol.upper() == 'AAL':
        st.write("""
        # American Airlines 
        """)
        st.subheader('NASQAD:AAL')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/AAL.csv")
    elif symbol.upper() == 'BKNG':
        st.write("""
        # Booking Holdings Inc
        """)
        st.subheader('NASQAD:BKNG')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/BKNG.csv")
    elif symbol.upper() == 'LUV':
        st.write("""
        # Southwest Airlines 
        """)
        st.subheader('NASQAD:LUV')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/LUV.csv")
    elif symbol.upper() == 'UAL':
        st.write("""
        # United Airlines 
        """)
        st.subheader('NASQAD:UAL')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/UAL.csv")
    elif symbol.upper() == 'MCD':
        st.write("""
        # McDonald's Corp. 
        """)
        st.subheader('NASQAD:MCD')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/MCD.csv")
    elif symbol.upper() == 'AAPL':
        st.write('# Apple Inc.')
        st.subheader('NASQAD:AAPL')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/AAPL.csv")
    elif symbol.upper() == 'SBUX':
        st.write("""
        # Starbucks Corp. 
        """)
        st.subheader('NASQAD:SBUX')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/SBUX.csv")
    elif symbol.upper() == 'CCL':
        st.write("""
        # Carnival Corp. 
        """)
        st.subheader('NYSE:CCL')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/CCL.csv")
    elif symbol.upper() == 'RCL':
        st.write("""
        # Royal Caribbean Cruises Ltd 
        """)
        st.subheader('NYSE:RCL')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/RCL.csv")
    elif symbol.upper() == 'DAL':
        st.write("""
        # Delta Airlines
        """)
        st.subheader('NASQAD:DAL')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/DAL.csv")
    elif symbol.upper() == 'NFLX':
        st.write("""
        # Netflix 
        """)
        st.subheader('NASQAD:NFLX')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/NFLX.csv")
    elif symbol.upper() == 'FB':
        st.write("""
        # Facebook Inc. 
        """)
        st.subheader('NASQAD:FB')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/FB.csv")
    elif symbol.upper() == 'ZM':
        st.write("""
        # Zoom Video Communications Inc.
        """)
        st.subheader('NASQAD:ZM')
        st.text('')
        st.image(pics[symbol], use_column_width=True, caption=pics[symbol])
        df = pd.read_csv("C:/Users/anton/OneDrive/Documents/Google Drive/Uni/8th Semester/Diploma/Code/Stock_Data/ZM.csv")
    else: 
        df = pd.DataFrame(columns = ['Date', 'Open', 'High', 'Low','Close', 'Adj Close', 'Volume'])
    #Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    start_row = 0
    end_row = 0

    #Start the date from the top of the dataset and go down to see if users start is less than or equal to the date in the dataset
    for i in range (0, len(df)):
        if start<= pd.to_datetime(df['Date'][i]):
            start_row = i
            break
    #Start from the bottom  and go up to see if the users end date is greater or equal
    for j in range (0,len(df)):
        if end>= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) - 1 - j
            break
    #Set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row +1, :]

#Get the users input
start, end, symbol = get_input()
# Get the data
df = get_data(symbol, start, end)
#Get the company name
company_name = get_company(symbol.upper())

#Display the close price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

#Display the volume
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

#Get statistics on the data
st.header('Data Statistics')
st.write(df.describe())
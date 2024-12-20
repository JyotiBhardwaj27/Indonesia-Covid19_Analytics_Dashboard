import pandas as pd
import plotly.express as px
import streamlit as st
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

# Loading dataset
df=pd.read_csv('Covid19_Indonesia.csv')

# Title for Dashboard
st.sidebar.title('Filters')
st.markdown("<h1 style='text-align: center;'>Indonesia: COVID-19 Analytics Dashboard</h1>", unsafe_allow_html=True)

# Path to image
file_path = r'/Users/dheerajkumar/Desktop/Covid.png'
st.image(file_path)

# Function to create filter multiselect options in Streamlit
def multiselect(title, options_list):
    selected = st.sidebar.multiselect(title, options_list)
    select_all = st.sidebar.checkbox("Select all", value=True, key=title)
    if select_all:
        selected_options = options_list
    else:
        selected_options = selected
    return selected_options

# Filters
selected_location= multiselect('Select Location',df['Location'].unique())
selected_year=multiselect('Select Year',df['Year'].unique())
selected_month=multiselect('Select Month',sorted(df['Month'].unique()))
selected_day=multiselect('Select Day',sorted(df['Day'].unique()))

filtered_df=df[(df['Year'].isin(selected_year)) &
               (df['Month'].isin(selected_month)) &
               (df['Day'].isin(selected_day)) &
               (df['Location'].isin(selected_location))]
#KPI - Key Performance indicator

# Create columns for displaying KPIs
col1,col2=st.columns(2)

# Total Covid Cases
with col1:
    st.metric(label='Total Covid Cases',value= f'{int(filtered_df['Total Cases'].sum())}')

# Total Active Cases
with col2:
    st.metric(label='Total Active Cases',value= f'{int(filtered_df['Total Active Cases'].sum())}')
col3,col4=st.columns(2)
    
# Total Recovered
with col3:
    st.metric(label='Total Recovered',value= f'{int(filtered_df['Total Recovered'].sum())}')
    
# Total Deaths
with col4:
    st.metric(label='Total Deaths',value= f'{int(filtered_df['Total Deaths'].sum())}')

# Visualization to analyze yearly Covid trends
col5=st.columns(1)[0]
with col5:
    st.subheader('Total Covid Cases Yearly')
# Group the data by 'Year' and sum the required columns
    Covid_trend = (filtered_df.groupby('Year')['Total Cases']
                   .sum())                   
# Create a bar chart with Altair (you can adjust the figsize by setting width and height)
    bar_chart = alt.Chart(Covid_trend.reset_index()).mark_bar().encode(
        x='Year:N',  # X-axis as Year (categorical)
        y='Total Cases:Q',  # Y-axis as Total Cases (quantitative)
        color='Year:N'  # Color by Year to distinguish
    ).properties(
        width=750,  # Adjust width (figsize)
        height=500  # Adjust height (figsize)
    )
    # Display the bar chart using Streamlit
    st.altair_chart(bar_chart)

# Top Provinces by Total Cases
st.subheader("Top Provinces by Total Covid Cases")
top_provinces = filtered_df.groupby("Province")["Total Cases"].max().nlargest(10)
st.bar_chart(top_provinces)


# Pie chart showing infection percentage in a region

# def plot_location_wise_infection_pie(filtered_df):
    # """
    # This function creates and displays pie charts for each location showing 
    # the percentage of people infected by COVID and non-infected, arranged as subplots.

    # Args:
    # filtered_df: DataFrame containing 'Location', 'Total Cases', and 'Population' columns.
    # """
    # Group by Location and sum up the Total Cases (no need to sum Population)
location_grouped = filtered_df.groupby(['Location', 'Year']).agg({
    'Total Cases': 'sum', 
    'Population': 'first'  # Population is the same for a location, so we take the first value
}).reset_index()

    # Calculate the Infected Percentage for each location
location_grouped['Infected Percentage'] = location_grouped.apply(
    lambda row: (row['Total Cases'] / row['Population'] * 100) if row['Population'] > 0 else 0,
    axis=1
)

    # Get the unique locations
locations = location_grouped['Location'].unique()

    # Set up the figure for subplots (3 pie charts per row)
n_cols = 3  # We want 3 pie charts per row
n_rows = len(locations) // n_cols + (1 if len(locations) % n_cols != 0 else 0)
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, n_rows * 5))
    
    # Flatten axes for easy iteration
axes = axes.flatten()

for i, location in enumerate(locations):
        # Filter data for the current location
    location_data = location_grouped[location_grouped['Location'] == location]
        
        # Calculate the percentage of infected and non-infected people
    infected_percentage = location_data['Infected Percentage'].iloc[0]
    non_infected_percentage = 100 - infected_percentage  # Remaining percentage
        
        # Ensure there are no negative values (just in case)
    infected_percentage = max(infected_percentage, 0)
    non_infected_percentage = max(non_infected_percentage, 0)
        
        # Prepare data for the pie chart
    data = ['Infected', 'Non-Infected']
    percentages = [infected_percentage, non_infected_percentage]

        # Select axis for the current subplot
    ax = axes[i]

        # Create the pie chart
    ax.pie(percentages, labels=data, autopct='%1.1f%%', startangle=90, colors=['#FF5733', '#C1C1C1'])
    ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

        # Add a title with the location name
    ax.set_title(f'{location}')
    
    # Remove any empty subplots (if number of locations isn't divisible by 3)
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

    # Display the pie charts in Streamlit
st.pyplot(fig)

# Group the data by 'Location' and sum the required columns
location_total_cases = filtered_df.groupby('Location')['Total Cases'].sum().sort_values(ascending=False)
location_active_cases = filtered_df.groupby('Location')['Total Active Cases'].sum().sort_values(ascending=False)
location_total_deaths = filtered_df.groupby('Location')['Total Deaths'].sum().sort_values(ascending=False)
location_total_recovered = filtered_df.groupby('Location')['Total Recovered'].sum().sort_values(ascending=False)

# Define the color scale (use a valid Vega color scheme like 'tableau10')
color_scale = alt.Scale(domain=location_total_cases.index.tolist(), range=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])

# Pie Chart for Location & Population Density
st.subheader("Location and its Population density")
pie_chart = alt.Chart(filtered_df.groupby('Location')['Population Density'].mean().reset_index()).mark_arc().encode(
    theta='Population Density:Q',  # Size of each slice
    color=alt.Color('Location:N', scale=color_scale),  # Use consistent color scale
    tooltip=['Location:N', 'Population Density:Q']  # Tooltip showing Location and Total Active Cases
).properties(
    
    width=700,
    height=400
)
# Display the pie chart in Streamlit
st.altair_chart(pie_chart)
pie_data = filtered_df.groupby('Location')['Population Density'].mean().reset_index()


# Heatmap to show a correlation between population density and total covid cases


    # Step 1: Prepare the data
heatmap_data = filtered_df[['Location', 'Population Density', 'Total Cases']].dropna()

    # Ensure valid numerical data for Population Density and Total Cases
heatmap_data = heatmap_data[heatmap_data['Population Density'] > 0]  # Filter rows where Population Density > 0

    # Step 2: Pivot the data for the heatmap
heatmap_pivot = heatmap_data.pivot_table(
    values='Total Cases',
    index='Location',
    columns='Population Density',
    aggfunc='sum',
    fill_value=0  # Replace NaN with 0 if needed
)

    # Step 3: Create the heatmap using Seaborn
fig, ax = plt.subplots(figsize=(14, 10))  # Adjust size as needed
sns.heatmap(heatmap_pivot, annot=True, fmt='g', cmap='coolwarm', cbar=True, ax=ax)
ax.set_title('Heatmap: Total Cases vs Population Density by Location', fontsize=16)
ax.set_xlabel('Population Density', fontsize=12)
ax.set_ylabel('Location', fontsize=12)

    # Step 4: Render the heatmap in Streamlit
st.pyplot(fig)

# Chart 1: Location-wise Total Covid Cases

col1 = st.columns(1)[0]
with col1:
    st.subheader("Location-wise Total Covid Cases")
    bar_chart = alt.Chart(location_total_cases.reset_index()).mark_bar().encode(
        x='Location:N',
        y='Total Cases:Q',
        color=alt.Color('Location:N', scale=color_scale),
        tooltip=['Location:N', 'Total Cases:Q']
    ).properties(width=700, height=400)
    st.altair_chart(bar_chart)

col2 = st.columns(1)[0]
# Chart 2: Location-wise Total Active Cases
with col2:
    st.subheader("Location-wise Total Active Covid Cases")
    bar_chart = alt.Chart(location_active_cases.reset_index()).mark_bar().encode(
        x='Location:N',
        y='Total Active Cases:Q',
        color=alt.Color('Location:N', scale=color_scale),
        tooltip=['Location:N', 'Total Active Cases:Q']
    ).properties(width=700, height=400)
    st.altair_chart(bar_chart)

# Chart 3: Location-wise Total Death Cases
col3 = st.columns(1)[0]

with col3:
    st.subheader("Location-wise Total Death Cases")
    bar_chart = alt.Chart(location_total_deaths.reset_index()).mark_bar().encode(
        x='Location:N',
        y='Total Deaths:Q',
        color=alt.Color('Location:N', scale=color_scale),
        tooltip=['Location:N', 'Total Deaths:Q']
    ).properties(width=700, height=400)
    st.altair_chart(bar_chart)

col4 = st.columns(1)[0]

# Chart 4: Location-wise Total Recovered Cases
with col4:
    st.subheader("Location-wise Total Recovered Cases")
    bar_chart = alt.Chart(location_total_recovered.reset_index()).mark_bar().encode(
        x='Location:N',
        y='Total Recovered:Q',
        color=alt.Color('Location:N', scale=color_scale),
        tooltip=['Location:N', 'Total Recovered:Q']
    ).properties(width=700, height=400)
    st.altair_chart(bar_chart)

# Recovery rate 

# def plot_recovery_rate_per_province(filtered_df):

st.subheader("Recovery Rate by Province")
    # Group by Province and calculate total cases and recoveries
province_data = filtered_df.groupby('Province').agg(
    Total_Cases=('Total Cases', 'sum'),
    Total_Recovered=('Total Recovered', 'sum')
).reset_index()

    # Calculate Recovery Rate
province_data['Recovery Rate (%)'] = (province_data['Total_Recovered'] / province_data['Total_Cases']) * 100

    # Handle cases where Total Cases might be 0 to avoid NaN or infinite values
province_data['Recovery Rate (%)'] = province_data['Recovery Rate (%)'].fillna(0)
# Create a bar chart using Altair
     # Sort data by recovery rate for better visualization
data_sorted = province_data.sort_values(by='Recovery Rate (%)', ascending=False)

    # Matplotlib Bar Chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(data_sorted['Province'], data_sorted['Recovery Rate (%)'], color='skyblue')
ax.set_xlabel("Province", fontsize=12)
ax.set_ylabel("Recovery Rate (%)", fontsize=12)
ax.tick_params(axis='x', rotation=90)
st.pyplot(fig)






























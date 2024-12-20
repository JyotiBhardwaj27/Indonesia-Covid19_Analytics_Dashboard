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
file_path=r'data:image/jpeg;base64,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'
st.image(file_path,width=1000)
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






























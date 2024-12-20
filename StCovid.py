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
file_path = r'data:image/png;base64,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'
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






























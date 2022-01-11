import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city US Bikeshare data you want to explore? Please enter city name eg: chicago, new york city, washington.\n")
        city = city.lower()
        if city in ['chicago', 'new york city', 'washington']:
            print("You entered city - {}".format(city))
            break
        else:
            print("Please enter valid city names from the list Chicago, New York City, Washington")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month or all months US Bikeshare data you want to explore? Please enter month name eg: all, january, february, ... , june.\n")
        month = month.lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("You entered month - {}".format(month))
            break
        else:
            print("Please enter valid month name eg: all, january, february, ... , june.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day or all days US Bikeshare data you want to explore? Please enter month name eg: all, monday, tuesday, ... sunday.\n")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print("You entered day - {}".format(day))
            break
        else:
            print("Please enter valid day name eg: all, monday, tuesday, ... sunday.")
    print("\nYou have entered City - {}, Month - {}, and Day - {}".format(city, month, day))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_name = df['month'].mode()[0]
    print("The most common month number in the US Bikeshare data is - ",month_name)
    month_name = calendar.month_name[month_name]
    print("The most common month in the US Bikeshare data is - ",month_name)

    # TO DO: display the most common day of week
    print("The most common day of week in the US Bikeshare data is - ",df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour of the day in the US Bikeshare data is - ",df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station in US Bikeshare data is - ",df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used End station in US Bikeshare data is - ",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+" "+df['End Station']
    print("The most frequent combination of start station and end station trip is - ",df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total Travel time is - ",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The mean Travel time is - ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types in the US Bikeshare data is:\n",df['User Type'].value_counts())
    print("\nThe total count of user types in the US Bikeshare data is - ",df['User Type'].count())

    # TO DO: Display counts of gender
    if city != 'washington':
       print("\nThe counts of gender is:\n",df['Gender'].value_counts()) 

    # TO DO: Display earliest, most recent, and most common year of birth
       print("\nMost Recent year of Birth - ",int(df['Birth Year'].max()))
       print("Most earliest year of Birth - ",int(df['Birth Year'].min()))
       print("Most common year of Birth - ",int(df['Birth Year'].mode()[0]))
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    # TO DO: Display Raw data of 5 rows of individual trip data
    view_data = input('\nWould you like to view 5 rows of individual trip raw data? Enter yes or no\n')
    start_loc = 0
    while True:
        if view_data.lower() == 'yes':
            print(df[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        else:
            break
       
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

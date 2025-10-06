# college_info_bot.py

def get_college_info(college_name):
    colleges = {
        "IIT Delhi": {
            "Location": "New Delhi, India",
            "Ranking": "Top 3 in India",
            "Courses": ["B.Tech", "M.Tech", "PhD"],
            "Website": "https://home.iitd.ac.in"
        },
        "Stanford University": {
            "Location": "California, USA",
            "Ranking": "Top 5 globally",
            "Courses": ["CS", "Engineering", "Business"],
            "Website": "https://www.stanford.edu"
        },
        "University of Toronto": {
            "Location": "Toronto, Canada",
            "Ranking": "Top 20 globally",
            "Courses": ["Arts", "Science", "Medicine"],
            "Website": "https://www.utoronto.ca"
        }
    }

    info = colleges.get(college_name)
    if info:
        print(f"\n📘 Info for {college_name}:")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print(f"\n❌ Sorry, no data found for '{college_name}'.")

def main():
    print("🎓 Welcome to the College Info Bot!")
    while True:
        college_name = input("\nEnter college name (or type 'exit' to quit): ")
        if college_name.lower() == 'exit':
            print("👋 Goodbye!")
            break
        get_college_info(college_name)

if __name__ == "__main__":
    main()

import NeaData

def bold(text):
    return f"\033[1m{text}\033[0m"

def border():
    print(f"{"☁️" * 35}")

def welcome():
    print(r"""
      ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️
      ☁️            🌞               ☁️
      ☁️    🌈   Welcome to  ☔      ☁️
      ☁️ Singapore Weather Forecast  ☁️
      ☁️        🌧️      🌦️           ☁️
      ☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️☁️
    """)

def prompt(areas):
    option_range = f"1-{len(areas) + 1}"
    print("\nShow forecast for:")
    for idx, area in enumerate(areas, 1):
        print(f"{idx:>2}. {area}")
    print(f"{len(areas) + 1:>2}. Exit")

    while True:
        try:
            choice = int(input(f"\nEnter an option from {option_range}: "))
            if 1 <= choice <= len(areas) + 1:
                return choice - 1
            print(f"Only values from {option_range} accepted.")
        except ValueError:
            print(f"Only numeric values from {option_range} accepted.")

def main():
    try:
        two_hour_forecasts = NeaData.get_2h_forecast()
        twenty_four_hour_forecasts = NeaData.get_2h_forecast()
        four_day_forecast = NeaData.get_4d_forecast()
        areas = [forecast['area'] for forecast in two_hour_forecasts]

        def show_forecast(area_idx):
            print()
            border()
            print(f"📍\t{bold(two_hour_forecasts[area_idx]['area'])}")
            print(f"\t24h Forecast: {twenty_four_hour_forecasts[area_idx]['forecast']}")
            print(f"\t 2h Forecast: {two_hour_forecasts[area_idx]['forecast']}")

            print(f"\n🇸🇬\t{bold("Singapore")}\n\t4-Day Outlook")
            for daily in four_day_forecast:
                print(f"\t{daily['date']}: {daily['forecast']}")
            border()

        while True:
            selected_idx = prompt(areas)

            if selected_idx == len(areas):
                print("\nGoodbye!")
                break

            show_forecast(selected_idx)

            input(f"\nPress {bold("Enter")} to go back to the menu...")

    except Exception as e:
        print(f"\n⚠️ Error: {str(e)}")


if __name__ == "__main__":
    welcome()
    main()

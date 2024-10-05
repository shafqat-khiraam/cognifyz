def temperature_converter():
    print("👋 Hey there! Welcome to the *Ultimate Temperature Converter* - Where Numbers Meet Reality!")
    
    # Accept temperature input
    try:
        temp = float(input("🌡️ Enter the temperature you'd like to convert (e.g., 98.6, 37): "))
    except ValueError:
        print("😅 Oops! That doesn't seem to be a valid number. Let's try again.")
        return

    # Allow user to choose conversion direction
    print("\nNow, let's decide how you'd like to convert it:")
    print("1️⃣  Celsius to Fahrenheit")
    print("2️⃣  Fahrenheit to Celsius")
    choice = input("Enter 1 or 2: ")

    # Implement logic for conversion
    if choice == '1':
        # Celsius to Fahrenheit
        converted = (temp * 9/5) + 32
        print(f"\n✨ Ta-da! {temp}°C is equal to {converted:.2f}°F. Stay cool or warm, whichever you prefer! 😎")
    elif choice == '2':
        # Fahrenheit to Celsius
        converted = (temp - 32) * 5/9
        print(f"\n✨ Voilà! {temp}°F is equal to {converted:.2f}°C. Whether it's chill or toasty, you're covered! 🌞❄️")
    else:
        print("🤔 Hmm, that doesn't seem right. Let's stick to 1 or 2, shall we?")

    # Wrap up with a friendly message
    print("\n💡 Conversion complete! Thanks for using the Ultimate Temperature Converter. Have a great day ahead! 🌟")

# Test the program
temperature_converter()

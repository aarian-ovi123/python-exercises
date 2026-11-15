def show_backup_camera():
    print("🎬 ACTION: Displaying backup camera feed on the main screen.")


def calculate_route():
    print("🗺️ ACTION: GPS activated. Calculating fastest route...")
    print("🗺️ ACTION: Displaying map on screen.")


def play_music():
    print("🎵 ACTION: Opening media player and playing jazz.")


def show_home_screen():
    print("📱 ACTION: Displaying main menu.")


def infotainment_system(car_gear, voice_command, screen_touched):
    print("\n--- Processing New Inputs ---")
    if car_gear == "Reverse":
        show_backup_camera()
    elif voice_command == "Play Music":
        play_music()
    elif screen_touched == "Navigation":
        calculate_route()
    else:
        show_home_screen()


infotainment_system(
    car_gear = "Reverse", voice_command = None, screen_touched = None
    )
infotainment_system(
    car_gear = "Drive", voice_command = "Play Music", screen_touched = None
    )
infotainment_system(
    car_gear = "Drive", voice_command = None, screen_touched = "Navigation"
    )

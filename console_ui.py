def draw_header(title):
    print("=" * 40)
    print(title.center(40))
    print("=" * 40)

def draw_menu(options_list):
    num = 1
    for item in options_list: 
        print(f"[{num}] {item}")
        num = num + 1

def draw_warning(message):
    print("!" * 40)
    print(f"! {message.center(36)}")
    print("!" * 40)









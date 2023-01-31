from colorama import Fore as col

async def typingPrint(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.02)

async def colprint(color: str, text: str):
    if color == 'red':
        typingPrint(col.RED + text)
    elif color == 'orange':
        typingPrint(col.ORANGE + text)
    elif color == 'yellow':
        typingPrint(col.YELLOW + text)
    elif color == 'green':
        typingPrint(col.GREEN + text)
    elif color == 'blue':
        typingPrint(col.BLUE + text)
    elif color == 'purple':
        typingPrint(col.MAGENTA + text)
    elif color == 'pink':
        typingPrint(col.LIGHTRED_EX + text)
    elif color == 'black':
        typingPrint(col.BLACK + text)
    elif color == 'white':
        typingPrint(col.WHITE + text)
    else:
        raise ValueError("Value color is not in allowed range.")
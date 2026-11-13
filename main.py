import os

JOKE = "My coding agent wrote 400 lines solving a problem the comments called impossible. It wrote the comments."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()

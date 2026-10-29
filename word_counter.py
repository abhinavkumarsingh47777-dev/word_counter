import re
import string
from pathlib import Path


def clean_words(text):
    text = text.lower()
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )
    return text.split()


def count_sentences(text):
    parts = re.split(r"[.!?]+", text.strip())
    sentences = [part for part in parts if part.strip()]
    return len(sentences)


def analyze_text(text):
    words = clean_words(text)
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return {
        "words": len(words),
        "characters": len(text),
        "sentences": count_sentences(text) if text.strip() else 0,
        "frequency": frequency,
        "unique_words": sorted(set(words)),
    }


def show_analysis(text):
    if not text.strip():
        print("No text to analyse.")
        return

    result = analyze_text(text)

    print(f"Words: {result['words']}")
    print(f"Characters (with spaces): {result['characters']}")
    print(f"Sentences: {result['sentences']}")
    print(f"Unique words: {len(result['unique_words'])}")

    print("Word frequency:")
    for word, count in sorted(
        result["frequency"].items(),
        key=lambda item: (-item[1], item[0])
    ):
        print(f"{word}: {count}")


def show_frequency_menu(text):
    if not text.strip():
        print("No text to analyse.")
        return

    result = analyze_text(text)

    top_words = sorted(
        result["frequency"].items(),
        key=lambda item: (-item[1], item[0])
    )[:5]

    print("Top words: " + " | ".join(
        f"{word}: {count}" for word, count in top_words
    ))

    unique = ", ".join(result["unique_words"])
    print(f"Unique words: {len(result['unique_words'])} ({unique})")


def read_file(filename):
    try:
        return Path(filename).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except OSError as error:
        print(f"Could not read file: {error}")

    return None


def main():
    while True:
        print("\n=== Word Counter & Text Analyzer ===")
        print("1. Analyse text")
        print("2. Show word frequency")
        print("3. Analyse a text file")
        print("4. Exit")

        choice = input("Enter menu option (1-4): ").strip()

        if choice == "1":
            text = input("Enter text: ")
            show_analysis(text)

        elif choice == "2":
            text = input("Enter text: ")
            show_frequency_menu(text)

        elif choice == "3":
            filename = input("Enter file name: ").strip()
            text = read_file(filename)

            if text is not None:
                show_analysis(text)

        elif choice == "4":
            print("Exiting Word Counter & Text Analyzer.")
            break

        else:
            print("Invalid menu option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

def changePerson(sentence):
    """Replaces first person pronouns with second person pronouns."""
    words = sentence.splite()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
        return " ".join(replyWords)

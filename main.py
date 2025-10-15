def to_jaden_case(string):
  """Преобразует строку в стиль Джейдена Смита."""
  return " ".join([word.capitalize() for word in string.split()])

# Примеры использования
quote1 = "Привет друг как дела"
quote2 = "the moment you realize that it is all happening for you not to you"
quote3 = "trees are never sad look at them every once in a while they’re quite beautiful"

print(to_jaden_case(quote1))
print(to_jaden_case(quote2))
print(to_jaden_case(quote3))

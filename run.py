test_cases= [
    {
      "offset": 0,
      "repetitions": 3
    },
    {
      "offset": 5,
      "repetitions": 0
    },
    {
      "offset": 9,
      "repetitions": 2
    }
  ] 

test_str = "0123456789"


def trim_and_repeat(string, offset = 0, repetitions = 1) -> str:

  trimmed_str = string[offset:]

  result = ''
  for _ in range(repetitions):
    result += trimmed_str
  
  return result



def main() -> None:
  for test_case in test_cases:
    result = trim_and_repeat(test_str, test_case["offset"], test_case["repetitions"])
    print(f"Результат для аргументов {test_case["offset"]}, {test_case["repetitions"]}: {result}")
  
  result = trim_and_repeat(test_str)
  print(f"Результат для аргументов по умолчанию: {result}")




main()

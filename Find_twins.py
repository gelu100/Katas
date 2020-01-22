def elimination(arr):
  seen = []
  for x in arr:
        if x in seen:
            return x
        seen.append(x)
  return None
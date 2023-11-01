import re

def calc(pri):
   n = 0
   result = 1
   
   while n < len(pri):
      if pri[n].isdigit():
         num_str = pri[n]
         n += 1
         while n < len(pri) and pri[n].isdigit():
            num_str += pri[n]
            n += 1
         result = int(num_str) * result
      else:
         n += 1

   return result

def main():
   num = input("Digite os numeros da multipliacao:")
   num_list = re.findall(r'\d+', num)  # Using regular expression to find all contiguous numbers in the input

   print(f"{num_list}")
   calc_result = calc(num_list)

   print(f"{calc_result}")

main()

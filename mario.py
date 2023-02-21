# def main():
#     height = int(input("Height: "))
#     pyramid(height)

# def pyramid(n):
#     for i in range(n):
#         print("[]" * (i + 1))
# if __name__ == "__main__":
#     main()
house_price = 1000000
finalhouse_price = house_price / 100 * 10
final2house_price = house_price / 100 * 20
buyer_credit = 60000
if buyer_credit > 500000:
    print(
        f'We have put down to percent of the house price which is  {finalhouse_price} ')
else:
    print(
        f'We have put down to percent of the house price which is  {final2house_price} ')
print()